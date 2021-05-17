#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from example_interfaces.msg import String


class str_subscribe (Node):
    def __init__(self):
        super().__init__("subscribe")
        self.create_subscription(String,"str_topic",self.timer_call1,10) 
        self.create_subscription(String,"str_topic",self.timer_call2,10) 
     
    def timer_call1(self, msg):
        self.get_logger().info(msg.data)

    def timer_call2(self, msg):
        self.get_logger().info(msg.data)
    
def main (args=None):

    rclpy.init(args=args)
    node=str_subscribe()
    rclpy.spin(node)

    rclpy.shutdown()

if __name__=="__main__":
    main()