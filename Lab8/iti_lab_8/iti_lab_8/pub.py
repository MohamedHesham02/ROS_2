#!/usr/bin/env python3
import rclpy 
from rclpy.node import Node
from example_interfaces.msg import String
import time

class str_publisher (Node):
    def __init__(self):
        super().__init__("publisher")
        self.i=1
        self.obj_pub=self.create_publisher(String,"str_topic",10)
        self.create_timer(0.5,self.timer_call)

    def timer_call(self):
        
        self.i+=1

        if (self.i % 2 != 0):
            self.get_logger().info("Hello")
        if (self.i % 2 == 0):
            self.get_logger().info("Hi!")
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
 
    
    
     

