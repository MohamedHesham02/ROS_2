#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from example_interfaces.msg import String
from example_interfaces.msg import Int64
from rclpy.qos import qos_profile_sensor_data
from rclpy.qos import QoSProfile
from rclpy.qos import QoSReliabilityPolicy


class str_subscribe (Node):
    def __init__(self):
        super().__init__("subscribe")
        
        self.create_subscription(String,"my_topic",self.timer_call,rclpy.qos.qos_profile_sensor_data) 
        self.counter=0

    def timer_call(self, msg):
        self.get_logger().info(msg.data)
        self.counter+=1
        print("mohamed heard "+msg.data+ str(self.counter)+" times")

    
def main (args=None):

    rclpy.init(args=args)
    node=str_subscribe()
    rclpy.spin(node)

    rclpy.shutdown()

if __name__=="__main__":
    main()