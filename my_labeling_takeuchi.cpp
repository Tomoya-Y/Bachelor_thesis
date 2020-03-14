#include <ros/ros.h>
#include <sensor_msgs/LaserScan.h>
#include <geometry_msgs/Twist.h>
#include <iostream>
#include <fstream>
#include <std_msgs/Float64.h>
#include <cv_bridge/cv_bridge.h>
#include <opencv2/opencv.hpp>
#include <image_transport/image_transport.h>
#include <opencv2/imgproc/imgproc.hpp>
#include <opencv2/highgui/highgui.hpp>
// #include <opencv2/opencv_lib.hpp>
#include <opencv2/highgui/highgui.hpp>
#include <sys/stat.h>
#include <typeinfo>
#include <image_transport/image_transport.h>
#include <opencv2/core.hpp>
#include <geometry_msgs/TwistStamped.h>
#include <nav_msgs/Odometry.h>
//#include <pair>
#include <vector>
#include <boost/circular_buffer.hpp>
using namespace std;


boost::circular_buffer<std::vector<std::pair<double,double> > > scan_buffer(100);



class MyLabeling
{
public:
  MyLabeling();
private:
  void scan_callback(const sensor_msgs::LaserScan::ConstPtr& scan);
  void odom_callback(const nav_msgs::Odometry::ConstPtr& odom);
  ros::NodeHandle nh;
  image_transport::Publisher image_pub;
  ros::Subscriber scan_sub;
  ros::Subscriber odom_sub;
  double g_odm_x,g_odm_y,g_odm_theta;
};


//constructor
MyLabeling::MyLabeling()
{
  scan_sub = nh.subscribe("/scan", 2, &MyLabeling::scan_callback, this);
  odom_sub = nh.subscribe("/ypspur_ros/odom", 2, &MyLabeling::odom_callback, this);

  image_transport::ImageTransport it(nh);
  image_pub = it.advertise("/imagedayo", 1);
}

void MyLabeling::odom_callback(const nav_msgs::Odometry::ConstPtr& odom){
  g_odm_x= odom->pose.pose.position.x;
  g_odm_y= odom->pose.pose.position.y;
  g_odm_theta= -2*atan2(odom->pose.pose.orientation.z,odom->pose.pose.orientation.w);
  
  //  printf("%f %f %f\n",g_odm_x,g_odm_y,g_odm_theta);
}

void MyLabeling::scan_callback(const sensor_msgs::LaserScan::ConstPtr& scan)
{
  float theta[2][1081];
  float pol[1081];
  int rect[2][1081];
  cv::Mat image(80, 100, CV_8UC1, cv::Scalar::all(50));

  //current scan->world
  std::vector<std::pair<double,double> > w_scan;
  
  printf("%f\n",g_odm_theta);
  for(int i=0; i<1081; i++){
    std::pair<double,double> point,wpoint;
    point.first  = scan->ranges[i]*cos(scan->angle_min + i * scan->angle_increment);
    point.second = scan->ranges[i]*sin(scan->angle_min + i * scan->angle_increment)+0.6;

    wpoint.first = point.first*cos(g_odm_theta) -point.second*sin(g_odm_theta) + g_odm_x;
    wpoint.second = point.first*sin(g_odm_theta) +point.second*cos(g_odm_theta) + g_odm_y;
    
    w_scan.push_back(wpoint);
  }
  scan_buffer.push_front(w_scan);
  
  for(int j=0; j<scan_buffer.size(); j++){
    for(int i=0; i<scan_buffer[j].size(); i++){
      std::pair<double,double> point;
      point.first =  (scan_buffer[j][i].first-g_odm_x)*cos(-g_odm_theta)
	-(scan_buffer[j][i].second-g_odm_y)*sin(-g_odm_theta);
      point.second =  (scan_buffer[j][i].first-g_odm_x)*sin(-g_odm_theta)
	+(scan_buffer[j][i].second-g_odm_y)*cos(-g_odm_theta);
      
      rect[0][i] = point.first * -5;
      rect[1][i] = point.second * 5;
      if ((0 < rect[0][i]+65) && (rect[0][i]+65 < 80) && (0 < rect[1][i]+50) && (rect[1][i]+50 < 100)){
	image.at<uchar>(rect[0][i]+65, rect[1][i]+50) = 255;
      }
    }
  }
  
  sensor_msgs::ImagePtr image_msg = cv_bridge::CvImage(std_msgs::Header(), "mono8", image).toImageMsg();
  image_pub.publish(image_msg);
}


int main(int argc, char** argv)
{
  ros::init(argc, argv, "my_labeling3");
  MyLabeling my_labeling;
  ros::spin();
  return 0;
}
