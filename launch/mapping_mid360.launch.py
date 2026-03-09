import os

from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, IncludeLaunchDescription
from launch.conditions import IfCondition
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import LaunchConfiguration, PathJoinSubstitution
from launch_ros.actions import Node
from launch_ros.substitutions import FindPackageShare


def generate_launch_description():
    package_share = get_package_share_directory('fast_lio')
    mid360_config = os.path.join(package_share, 'config', 'mid360.yaml')
    rviz_config = os.path.join(package_share, 'rviz_cfg', 'loam_livox.rviz')

    livox_driver = LaunchConfiguration('livox_driver')
    rviz = LaunchConfiguration('rviz')

    return LaunchDescription([
        DeclareLaunchArgument('livox_driver', default_value='false'),
        DeclareLaunchArgument('rviz', default_value='true'),
        Node(
            package='fast_lio',
            executable='fastlio_mapping',
            name='laserMapping',
            output='screen',
            parameters=[
                mid360_config,
                {
                    'feature_extract_enable': False,
                    'point_filter_num': 3,
                    'max_iteration': 3,
                    'filter_size_surf': 0.5,
                    'filter_size_map': 0.5,
                    'cube_side_length': 1000.0,
                    'runtime_pos_log_enable': False,
                },
            ],
        ),
        Node(
            package='rviz2',
            executable='rviz2',
            name='rviz2',
            arguments=['-d', rviz_config],
            output='screen',
            condition=IfCondition(rviz),
        ),
        Node(
            package='tf2_ros',
            executable='static_transform_publisher',
            name='livox_frame_body_broadcaster',
            arguments=['0', '0', '0', '0', '0', '0', '1', 'body', 'livox_frame'],
            output='screen',
        ),
        IncludeLaunchDescription(
            PythonLaunchDescriptionSource(
                PathJoinSubstitution([
                    FindPackageShare('livox_ros_driver2'),
                    'launch_ROS2',
                    'msg_MID360_launch.py',
                ])
            ),
            condition=IfCondition(livox_driver),
        ),
    ])