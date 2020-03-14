#include "ros/ros.h"
#include "dynamixel_msgs/JointState.h"
#include "dynamixel_controllers/SetTorqueLimit.h"
#include "std_msgs/Float64.h"
#include "geometry_msgs/TwistStamped.h"
#include "geometry_msgs/Twist.h"
#include <sensor_msgs/Joy.h>

#define ORIGIN_STEER M_PI
#define ORIGIN_VEL (0.4-0.2)
#define SENSITIVITY_STEER 1.5  /*rad/(rad/m)*/ //default:0.4
#define SENSITIVITY_VEL 1.5    /*rad/(m/s)*/ //default:0.4

ros::Publisher m_cmd_pub;
ros::Publisher m_steer_force_pub;
ros::Publisher m_vel_force_pub;

double g_target_steer;
double g_target_vel;

double g_current_steer;
double g_current_vel;

double g_steer_force;
double g_vel_force;


void steer_stateCallback(const dynamixel_msgs::JointState::ConstPtr& msg)
{
  if(msg->load <-0.4 ||msg->load > 0.4){
    dynamixel_controllers::SetTorqueLimit torque;
    torque.request.torque_limit=0.3;//0.2
    ros::service::call("/steer_controller/set_torque_limit",torque);
  }else if(msg->load >-0.1 && msg->load < 0.1){
    dynamixel_controllers::SetTorqueLimit torque;
    torque.request.torque_limit=0.3;//0.5
    ros::service::call("/steer_controller/set_torque_limit",torque);
  }
  //  printf("get steer  %f %f %f\n",msg->goal_pos,msg->current_pos,msg->load);
  g_steer_force=msg->load;
  g_current_steer=msg->current_pos;
}

void vel_stateCallback(const dynamixel_msgs::JointState::ConstPtr& msg)
{

  if(msg->load <-0.2 || msg->load >0.2){
    dynamixel_controllers::SetTorqueLimit torque;
    torque.request.torque_limit=0.15;
    ros::service::call("/vel_controller/set_torque_limit",torque);
  }else if(msg->load >-0.05&&msg->load<0.05){
    dynamixel_controllers::SetTorqueLimit torque;
    torque.request.torque_limit=0.15;
    ros::service::call("/vel_controller/set_torque_limit",torque);
  }
  //printf("get vel  %f %f %f\n",msg->goal_pos,msg->current_pos,msg->load);
  g_vel_force=msg->load;
  g_current_vel=msg->current_pos;
}


void cmd_callback(const geometry_msgs::Twist& msg){
  g_target_vel = msg.linear.x;
  g_target_steer = msg.angular.z/msg.linear.x;
}


int main(int argc, char **argv)
{
  ros::init(argc, argv, "dx_controller");
  ros::NodeHandle n;
  ros::Subscriber sub = n.subscribe("/steer_controller/state",
				    10, steer_stateCallback);
  ros::Subscriber sub2 = n.subscribe("/vel_controller/state",
				    10, vel_stateCallback);

  ros::Publisher pub = n.advertise<std_msgs::Float64>("/steer_controller/command", 10);
  ros::Publisher pub2 = n.advertise<std_msgs::Float64>("/vel_controller/command", 10);

  // m_cmd_pub = n.advertise<geometry_msgs::Twist>("ypspur_ros/cmd_vel", 10);
  m_cmd_pub = n.advertise<geometry_msgs::Twist>("/steering_and_velocity", 10);
  m_steer_force_pub = n.advertise<std_msgs::Float64>("dx/steer_force", 10);
  m_vel_force_pub = n.advertise<std_msgs::Float64>("dx/vel_force", 10);

  ros::Subscriber m_motion_sub = n.subscribe("/tomoyakun", 10, cmd_callback);

  ros::Rate loop_rate(30);

  std_msgs::Float64 angle1,angle2;
  //angle.data =0;
  dynamixel_controllers::SetTorqueLimit torque;
  dynamixel_controllers::SetTorqueLimit torque2;
  torque.request.torque_limit=0.35;
  ros::service::call("/steer_controller/set_torque_limit",torque);
  torque2.request.torque_limit=0.15;
  ros::service::call("/vel_controller/set_torque_limit",torque2);

  g_target_steer=0;
  g_target_vel=0;

  while(ros::ok()){
    //set target angle
    angle1.data = ORIGIN_STEER + g_target_steer*SENSITIVITY_STEER;
    if(g_target_vel>0)
      angle2.data = ORIGIN_VEL  + g_target_vel*SENSITIVITY_VEL;
    else
      angle2.data = ORIGIN_VEL  + g_target_vel*SENSITIVITY_VEL-0.;

    pub.publish(angle1);
    pub2.publish(angle2);


    //output twist information
    geometry_msgs::Twist cmdf;
    if(g_current_vel>ORIGIN_VEL)
      cmdf.linear.x =(g_current_vel-ORIGIN_VEL)/SENSITIVITY_VEL;
    else if(g_current_vel<ORIGIN_VEL-0.)
      cmdf.linear.x =(g_current_vel-ORIGIN_VEL+0.)/SENSITIVITY_VEL;
    else
      cmdf.linear.x=0;
    if(cmdf.linear.x > 1.0)
      cmdf.linear.x = 0;
    // if(cmdf.linear.x > 0.3)
    //   cmdf.linear.x = 0.3;

    if(cmdf.linear.x <0.02){
      if(cmdf.linear.x <-0.2)
	cmdf.linear.x +=0.2;
      else
	cmdf.linear.x =0;
    }

    cmdf.angular.z=cmdf.linear.x*((g_current_steer-ORIGIN_STEER)/SENSITIVITY_STEER);
    m_cmd_pub.publish(cmdf);

    //output force information
    std_msgs::Float64 steer_force,vel_force;
    steer_force.data=g_steer_force;
    vel_force.data  =g_vel_force;

    m_steer_force_pub.publish(steer_force);
    m_vel_force_pub.publish(vel_force);


    printf("%f %f %f %f %f %f %f %f\n",
	   cmdf.linear.x,
	   cmdf.angular.z,
	   g_target_steer,
	   g_steer_force,
	   g_current_steer,
	   g_target_vel,
	   g_vel_force,
	   g_current_vel);


    ros::spinOnce();
    loop_rate.sleep();
  }

  return 0;
}
// %EndTag(FULLTEXT)%
