from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node


def generate_launch_description() -> LaunchDescription:
    return LaunchDescription(
        [
            DeclareLaunchArgument("map_dir"),
            DeclareLaunchArgument("params_file"),
            Node(
                package="fast_localization",
                executable="fast_localization",
                name="fast_localization",
                output="screen",
                parameters=[
                    LaunchConfiguration("params_file"),
                    {"map_dir": LaunchConfiguration("map_dir")},
                ],
            ),
        ]
    )
