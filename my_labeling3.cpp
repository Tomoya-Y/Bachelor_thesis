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

using namespace std;


class MyLabeling
{
  public:
    MyLabeling();
  private:
    void scan_callback(const sensor_msgs::LaserScan::ConstPtr& scan);
    ros::NodeHandle nh;
    image_transport::Publisher image_pub;
    ros::Subscriber scan_sub;
};


//constructor
MyLabeling::MyLabeling()
{
  scan_sub = nh.subscribe("/scan", 1, &MyLabeling::scan_callback, this);
  image_transport::ImageTransport it(nh);
  image_pub = it.advertise("/imagedayo", 1);
}


void MyLabeling::scan_callback(const sensor_msgs::LaserScan::ConstPtr& scan)
{
  float theta[2][1081];
  float pol[1081];
  int rect[2][1081];
  cv::Mat image(80, 100, CV_8UC1, cv::Scalar::all(50));
  for(int i=0; i<1081; i++){
    theta[0][i] = cos(scan->angle_min + i * scan->angle_increment);
    theta[1][i] = sin(scan->angle_min + i * scan->angle_increment);
    pol[i] = scan->ranges[i];

    rect[0][i] = pol[i] * theta[0][i] * -5;
    rect[1][i] = pol[i] * theta[1][i] * 5;
    if ((0 < rect[0][i]+65) && (rect[0][i]+65 < 80) && (0 < rect[1][i]+50) && (rect[1][i]+50 < 100)){
      image.at<uchar>(rect[0][i]+65, rect[1][i]+50) = 255;
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
