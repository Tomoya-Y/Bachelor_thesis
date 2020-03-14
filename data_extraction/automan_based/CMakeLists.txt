cmake_minimum_required(VERSION 2.8.3)
project(labeling_3d)

find_package(
  catkin REQUIRED COMPONENTS
  cv_bridge
  message_filters
  rosbag
  sensor_msgs
  std_msgs
)

set(OpenCV_STATIC ON)
set(OpenCV_CUDA OFF)
set(OpenCV_DIR "${CMAKE_SOURCE_DIR}/../install")

find_package(OpenCV REQUIRED)

include_directories(${OpenCV_INCLUDE_DIRS})
link_directories(${OpenCV_LIB_DIR})

find_package(PCL 1.1 REQUIRED)
include_directories(${PCL_INCLUDE_DIRS})
link_directories(${PCL_LIBRARY_DIRS})
add_definitions(${PCL_DEFINITIONS})

include_directories(/usr/local/include /opt/ros/melodic/include ${OpenCV_INCLUDE_DIRS} /home/tomoya/catkin_ws/)

add_executable(labeling_3d labeling_3d.cpp labeling_3d.h)
target_link_libraries(labeling_3d ${catkin_LIBRARIES} ${PCL_LIBRARIES} gflags ${OpenCV_LIBS})
