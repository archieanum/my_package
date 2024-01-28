from launch import LaunchDescription
from launch_ros.actions import Node
import launch_ros.descriptions

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='demo_nodes_py',
            executable='listener'
        )
    ])