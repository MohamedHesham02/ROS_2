#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from example_interfaces.msg import String
from sensor_msgs.msg import LaserScan


class str_subscribe (Node):
    def __init__(self):
        super().__init__("subscribe")
        
        self.create_subscription(LaserScan,"/scan",self.timer_call1,10)
        self.create_subscription(Twist,"/key_cmd_vel",self.timer_call2,10)
        self.obj_pub=self.create_publisher(Twist,"/cmd_vel",10)
        self.create_timer(1/1,self.timer_call3)

    def timer_call1(self,scan):

        for i in scan.ranges[50:140]:
            
            self.problem=i
        
    def timer_call2(self,msg):
        
        self.linear=msg.linear.x
        self.angular=msg.angular.z

    def timer_call3(self):

        str_subscribe.timer_call1(self,scan)
        str_subscribe.timer_call2(self,msg)

        warn=Twist()
        warn.linear.x =self.linear
        warn.angular.z = self.angular

        if self.problem <= 0.5 : 
            warn.linear.x = 0
            warn.angular.z = 0

        self.obj_pub.publish(warn)

def main (args=None):

    rclpy.init(args=args)
    node=str_subscribe()
    rclpy.spin(node)

    rclpy.shutdown()

if __name__=="__main__":
    main()