#include "labeling_3d.h"
#include <iostream>

using namespace std;

int main(int argc, char **argv) {

    std::string rosbag_file = argv[1];
    std::string output_dir = argv[2];

    const int dir_err = mkdir(output_dir.c_str(), S_IRWXU | S_IRWXG | S_IROTH | S_IXOTH);
    const int dir_err1 = mkdir((output_dir + "/image").c_str(), S_IRWXU | S_IRWXG | S_IROTH | S_IXOTH);


    ofstream log_twist;
    log_twist.open((output_dir + "/twist.csv").c_str(), ios::trunc);

    ofstream log_force;
    log_force.open((output_dir +"/force.csv").c_str(),ios::trunc);

    ofstream log_odom;
    log_odom.open((output_dir + "/odom.csv").c_str(), ios::trunc);

    ofstream log_ndt;//ndt_poseいらないときコメントアウト
    log_ndt.open((output_dir + "/ndt.csv").c_str(), ios::trunc);

    rosbag::Bag bag;
    bag.open(rosbag_file, rosbag::bagmode::Read);

    std::vector<std::string> topics;
    topics.push_back(std::string(argv[3]));
    topics.push_back(std::string(argv[4]));
    topics.push_back(std::string(argv[5]));
    topics.push_back(std::string(argv[6]));
    topics.push_back(std::string(argv[7]));
    topics.push_back(std::string(argv[8])); //ndt_poseいらないときコメントアウト
    int pcd_num = 0;

    rosbag::View view(bag, rosbag::TopicQuery(topics));
    std_msgs::Float64::ConstPtr steer_force_tmp;
    std_msgs::Float64::ConstPtr vel_force_tmp;
    nav_msgs::Odometry::ConstPtr odom_tmp;
    sensor_msgs::Image::ConstPtr image_tmp;
    geometry_msgs::PoseStamped::ConstPtr ndt_tmp;



    foreach(rosbag::MessageInstance const m, view)
    {
      const std::string& topic_name = m.getTopic();

      sensor_msgs::Image::ConstPtr image1 = m.instantiate<sensor_msgs::Image>();
      if (image1 != NULL)
      {
        image_tmp = image1;
      }


      if (topic_name ==topics[3])
      {
        std_msgs::Float64::ConstPtr steerforce1 = m.instantiate<std_msgs::Float64>();
        if (steerforce1 != NULL)
        {
          steer_force_tmp = steerforce1;
        }
      }

      if (topic_name ==topics[4])
      {
        std_msgs::Float64::ConstPtr velforce1 = m.instantiate<std_msgs::Float64>();
        if (velforce1 != NULL)
        {
          vel_force_tmp = velforce1;
        }
      }

      nav_msgs::Odometry::ConstPtr odom1 = m.instantiate<nav_msgs::Odometry>();
      if (odom1 != NULL)
      {
        odom_tmp = odom1;
      }

      // いらないときコメントアウト
      geometry_msgs::PoseStamped::ConstPtr ndt1 = m.instantiate<geometry_msgs::PoseStamped>();
      if (ndt1 != NULL)
      {
        ndt_tmp = ndt1;
      }

      geometry_msgs::Twist::ConstPtr twist1 = m.instantiate<geometry_msgs::Twist>();
      if (twist1 != NULL)
      {
        if (image_tmp != NULL)
        {
          if (steer_force_tmp != NULL)
          {
            if (vel_force_tmp != NULL)
            {
              if (odom_tmp != NULL)
              {
                if (ndt_tmp != NULL) //ndtないとき消す
                {//ndtないとき消す
                  std::ostringstream oss;
                  oss << setfill('0') << setw(5) << pcd_num << std::endl;
                  cv_bridge::CvImagePtr cv_ptr_mono;
                  cv_ptr_mono = cv_bridge::toCvCopy(image_tmp, sensor_msgs::image_encodings::MONO8);
                  cv::Mat image_result_mono = cv_ptr_mono->image;
                  cv::imwrite(output_dir + "/image/" + oss.str() + ".png", image_result_mono);
                  log_twist << odom_tmp->header.stamp << "," << twist1->angular.z << "," << twist1->linear.x << endl;
                  log_force << odom_tmp->header.stamp << "," << steer_force_tmp->data << "," << vel_force_tmp->data << endl;
                  log_odom << odom_tmp->pose.pose.position.x << "," << odom_tmp->pose.pose.position.y << "," << odom_tmp->pose.pose.orientation.z << "," << odom_tmp->pose.pose.orientation.w << endl;
                  log_ndt << ndt_tmp->header.stamp << "," << ndt_tmp->pose.position.x << "," << ndt_tmp->pose.position.y << "," << ndt_tmp->pose.orientation.z << "," << ndt_tmp->pose.orientation.w << endl;
                  pcd_num +=1;
                }//ndtないとき消す
              }
            }
          }
        }
      }
    }

    bag.close();
    log_twist.close();
    log_force.close();
    log_odom.close();
    log_ndt.close(); //いらないときコメントアウト
    // log_twistfromodom.close();
    return (0);
}
