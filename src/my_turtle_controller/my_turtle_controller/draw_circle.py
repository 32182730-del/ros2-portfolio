#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist

class DrawCircleNode(Node):
    def __init__(self):
        super().__init__('draw_circle')
        # Create a publisher that sends Twist messages to /turtle1/cmd_vel
        self.publisher_ = self.create_publisher(Twist, '/turtle1/cmd_vel', 10)
        # Create a timer that calls the send_command function every 0.5 seconds
        self.timer = self.create_timer(0.5, self.send_command)
        self.get_logger().info("Draw Circle Node has been started!")

    def send_command(self):
        msg = Twist()
        msg.linear.x = 2.0    # Move forward
        msg.angular.z = 1.0   # Turn left
        self.publisher_.publish(msg)
        self.get_logger().info("Publishing command...")

def main(args=None):
    rclpy.init(args=args)
    node = DrawCircleNode()
    rclpy.spin(node) # Keep the node running
    rclpy.shutdown()

if __name__ == '__main__':
    main()