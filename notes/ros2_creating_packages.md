# Creating a ROS 2 Python Package

## 1. Create the Package
Run this command in the `~/ros2_ws` directory to create the toolbox for our Python code:

```bash
ros2 pkg create --build-type ament_python my_turtle_controller --dependencies rclpy geometry_msgs