#!/usr/bin/env python3
import rclpy 
from rclpy.node import Node
from example_interfaces.msg import String


class str_publisher (Node):
    def __init__(self):
        super().__init__("publisher")
        self.i=1
        self.obj_pub=self.create_publisher(String,"str_topic",10)
        self.create_timer(1/1,self.timer_call1)
        self.create_timer(1/1,self.timer_call2)

    def timer_call1(self):
        self.get_logger().info("Hi")
        msg=String()
        msg.data="I've heard msg"
        self.obj_pub.publish(msg)
    
    def timer_call2(self):
        self.get_logger().info("Hello")
        msg=String()
        msg.data="I've heard msg"
        self.obj_pub.publish(msg)

def main (args=None):

        rclpy.init(args=None) 
        node=str_publisher() 
        rclpy.spin(node) 

        rclpy.shutdown()
        
if __name__=="__main__":
    main()

