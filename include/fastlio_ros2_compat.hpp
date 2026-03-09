#ifndef FASTLIO_ROS2_COMPAT_HPP
#define FASTLIO_ROS2_COMPAT_HPP

#include <cassert>

#include <rclcpp/rclcpp.hpp>
#include <sensor_msgs/msg/imu.hpp>
#include <sensor_msgs/msg/point_cloud2.hpp>
#include <nav_msgs/msg/odometry.hpp>
#include <nav_msgs/msg/path.hpp>
#include <geometry_msgs/msg/pose_stamped.hpp>
#include <geometry_msgs/msg/quaternion.hpp>
#include <geometry_msgs/msg/vector3.hpp>
#include <visualization_msgs/msg/marker.hpp>
#include <livox_ros_driver2/msg/custom_msg.hpp>
#include <fast_lio/msg/pose6_d.hpp>

namespace sensor_msgs {
using Imu = msg::Imu;
using PointCloud2 = msg::PointCloud2;
using ImuConstPtr = msg::Imu::ConstSharedPtr;
}

namespace nav_msgs {
using Odometry = msg::Odometry;
using Path = msg::Path;
}

namespace geometry_msgs {
using PoseStamped = msg::PoseStamped;
using Quaternion = msg::Quaternion;
using Vector3 = msg::Vector3;
}

namespace visualization_msgs {
using Marker = msg::Marker;
}

namespace livox_ros_driver2 {
using CustomMsg = msg::CustomMsg;
}

namespace fast_lio {
using Pose6D = msg::Pose6D;
}

namespace fastlio_ros2 {

inline rclcpp::Logger logger()
{
  return rclcpp::get_logger("fastlio_mapping");
}

}  // namespace fastlio_ros2

#define ROS_WARN(...) RCLCPP_WARN(fastlio_ros2::logger(), __VA_ARGS__)
#define ROS_ERROR(...) RCLCPP_ERROR(fastlio_ros2::logger(), __VA_ARGS__)
#define ROS_INFO(...) RCLCPP_INFO(fastlio_ros2::logger(), __VA_ARGS__)
#define ROS_ASSERT(...) assert(__VA_ARGS__)

#endif