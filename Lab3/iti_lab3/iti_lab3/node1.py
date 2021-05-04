#!/usr/bin/env python3

import rclpy 
from rclpy.node import Node
from my_msgs.msg import Custom


class num_publisher (Node):
    def __init__(self):
        super().__init__("publisher")
        self.obj_pub=self.create_publisher(Custom,"name",10)
        self.create_timer(1/2,self.timer_call)
        self.get_logger().info("Your name is published")

    def timer_call(self):
        msg=Custom()
        msg.number=5
        msg.message=("mohamed is publishing,"+str(msg.number))
        self.get_logger().info(msg.message)
        self.obj_pub.publish(msg)

def main (args=None):
        rclpy.init(args=None)
        node=num_publisher() 
        rclpy.spin(node)
        rclpy.shutdown()
        
if __name__=="__main__":
    main()