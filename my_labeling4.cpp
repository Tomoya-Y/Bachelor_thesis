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
#include <opencv2/highgui/highgui.hpp>
#include <sys/stat.h>
#include <typeinfo>
#include <image_transport/image_transport.h>
#include <opencv2/core.hpp>
#include <geometry_msgs/TwistStamped.h>
#include <nav_msgs/Odometry.h>

using namespace std;


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
    int count = 0;
    struct Factor{
      float scan_list[2][1081];
      float odom_list[3];
    };
    struct FactorStack{
      Factor element[40];
      int top;
      int tail;
    };
    FactorStack fstack;
    FactorStack fstack_tmp;
    FactorStack fstack_odom;
    FactorStack fstack_odom_tmp;
    float position_x;
    float position_y;
    float orientation_z;
    float orientation_w;
};


//constructor
MyLabeling::MyLabeling()
{
  scan_sub = nh.subscribe("/scan", 10, &MyLabeling::scan_callback, this);
  odom_sub = nh.subscribe("/ypsppur_ros/odom", 10, &MyLabeling::odom_callback, this);
  image_transport::ImageTransport it(nh);
  image_pub = it.advertise("/image_move", 1);
}


void MyLabeling::scan_callback(const sensor_msgs::LaserScan::ConstPtr& scan)
{
  if (count < 40)
  {
    float theta[2][1081];
    float pol[1081];
    int rect[2][1081];
    cv::Mat image(80, 100, CV_8UC1, cv::Scalar::all(50));
    for(int j=0; j<1081; j++){
      theta[0][j] = cos(scan->angle_min + j * scan->angle_increment);
      theta[1][j] = sin(scan->angle_min + j * scan->angle_increment);
      pol[j] = scan->ranges[j];
      fstack.element[fstack.top].scan_list[0][j]=pol[j] * theta[0][j];
      fstack.element[fstack.top].scan_list[1][j]=pol[j] * theta[1][j];
    }
    fstack.top++;
    fstack_odom.element[fstack_odom.top].odom_list[0]=position_x;
    fstack_odom.element[fstack_odom.top].odom_list[1]=position_y;
    fstack_odom.element[fstack_odom.top].odom_list[2]=2.0*atan(orientation_z/orientation_w);
    fstack_odom.top++;
  }

  else
  {
    //スタックを１つずつずらす
    for (int i=1;i<40;i++){
      fstack_tmp.element[i-1]=fstack.element[i];
      fstack_odom_tmp.element[i-1]=fstack_odom.element[i];
    }
    //新しく入ってきたscanをスタックの4番目につっこむ
    float theta[2][1081];
    float pol[1081];
    for(int j=0; j<1081; j++){
      theta[0][j] = cos(scan->angle_min + j * scan->angle_increment);
      theta[1][j] = sin(scan->angle_min + j * scan->angle_increment);
      pol[j] = scan->ranges[j];
      fstack_tmp.element[39].scan_list[0][j]=pol[j] * theta[0][j];
      fstack_tmp.element[39].scan_list[1][j]=pol[j] * theta[1][j];
    }
    fstack=fstack_tmp;
    fstack_odom_tmp.element[39].odom_list[0] = position_x;
    fstack_odom_tmp.element[39].odom_list[1] = position_y;
    fstack_odom_tmp.element[39].odom_list[2] = 2.0 * atan(orientation_z/orientation_w);
    fstack_odom=fstack_odom_tmp;
    //画像を重ねる
    //新しく入ってきたものを基準に過去のものを回転、平行移動をする
    cv::Mat image(80, 100, CV_8UC1, cv::Scalar::all(50));
    float theta_odom;
    float lotation[2][2];
    theta_odom = fstack_odom.element[9].odom_list[2];
    lotation[0][0] = cos(theta_odom);
    lotation[0][1] = -1*sin(theta_odom);
    lotation[1][0] = sin(theta_odom);
    lotation[1][1] = cos(theta_odom);
    for(int i=0; i<40; i++)
    {
      float after_lotation[2][1081];
      int matrix[2][1081];
      int color = (i*6) + 15;
      for (int l = 0; l < 2; l++)
      {
        for(int j = 0; j < 1081; j++)
        {
          after_lotation[l][j]=0;
          for(int k = 0; k < 2; k++)
          {
            after_lotation[l][j] += lotation[l][k] * fstack.element[i].scan_list[k][j];
          }
        }
      }
      for(int k = 0; k < 1081; k++)
      {
        matrix[0][k] = (after_lotation[0][k] + fstack_odom.element[39].odom_list[0])*5;
        matrix[1][k] = (after_lotation[1][k] + fstack_odom.element[39].odom_list[1])*5;
      }
      for(int j=0; j<1081; j++)
      {
        if ((0 < (1*matrix[0][j])+65) && ((1*matrix[0][j])+65 < 80) && (0 < (-1*matrix[1][j])+50) && ((-1*matrix[1][j])+50 < 100))
        {
          image.at<uchar>((1*matrix[0][j])+65, (-1*matrix[1][j])+50) = color;
        }
      }
    }
    sensor_msgs::ImagePtr image_msg = cv_bridge::CvImage(std_msgs::Header(), "mono8", image).toImageMsg();
    image_pub.publish(image_msg);
  }
  count += 1;
}

void MyLabeling::odom_callback(const nav_msgs::Odometry::ConstPtr& odom)
{
  position_x = odom->pose.pose.position.x;
  position_y = odom->pose.pose.position.y;
  orientation_z = odom->pose.pose.orientation.z;
  orientation_w = odom->pose.pose.orientation.w;
}


int main(int argc, char** argv)
{
  ros::init(argc, argv, "my_labeling4");
  MyLabeling my_labeling;
  ros::spin();
  return 0;
}
