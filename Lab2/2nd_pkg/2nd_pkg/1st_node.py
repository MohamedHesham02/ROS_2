#!/usr/bin/env python3

import rclpy 
from rclpy.node import Node
from example_interfaces.msg import String
from example_interfaces.msg import Int64
from example_interfaces.msg import Bool


class num_publisher (Node):
    def __init__(self):
        super().__init__("publisher")
        self.i=3
        self.obj_pub=self.create_publisher(String,"number",10)
        self.create_timer(1/2,self.timer_call)
        self.get_logger().info("no. is published ") 

    def timer_call(self):
        
        self.get_logger().info("no. is fixed")  
        self.get_logger().info(str(self.i))
        msg=String()
        msg.data=(str(self.i))
        self.obj_pub.publish(msg)

def main (args=None):
        rclpy.init(args=None)
        node=num_publisher() 
        rclpy.spin(node) 
    
        rclpy.shutdown()
        
if __name__=="__main__":
    main()
