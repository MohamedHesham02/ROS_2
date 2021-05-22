#!/usr/bin/env python3

from geometry_msgs import msg
import rclpy
from rclpy.node import Node
from nav_msgs.msg import Odometry
from geometry_msgs.msg import Quaternion
from math import sin, cos, pi
import numpy as np
import math
import csv

class str_subscribe (Node):
    def __init__(self):
        super().__init__("subscribe")
        self.create_subscription(Odometry,"odom",self.timer_call,10) 
        self.i=0

    def euler_from_quaternion(self, quaternion):
        x = quaternion.x
        y = quaternion.y
        z = quaternion.z
        w = quaternion.w

        sinr_cosp = 2 * (w * x + y * z)
        cosr_cosp = 1 - 2 * (x * x + y * y)
        roll = np.arctan2(sinr_cosp, cosr_cosp)
        sinp = 2 * (w * y - z * x)
        pitch = np.arcsin(sinp)

        siny_cosp = 2 * (w * z + x * y)
        cosy_cosp = 1 - 2 * (y * y + z * z)
        yaw = np.arctan2(siny_cosp, cosy_cosp)

        return roll, pitch, yaw 


    def timer_call(self,msg):

        with open('/home/mohamed/imu_data.csv', mode='r') as Twist_file:
            reader = csv.reader(Twist_file, delimiter=',')
            data = list(reader)
    
        
        row=data[self.i]

        self.currX=float(row[0])
        self.currY=float(row[1])
        self.yawdeg=float(row[2])

        self.yawrad=(self.yawdeg*math.pi)/180

        if (float(msg.pose.pose.position.x)>=float(self.currX)-0.5) & (float(msg.pose.pose.position.x)<=float(self.currX)+0.5):
            self.get_logger().info("i execute all positionx and last one is: "+str(msg.pose.pose.position.x))
            self.i+=1
        
        if (float(msg.pose.pose.position.y)>=float(self.currY)-0.5) & (float(msg.pose.pose.position.y)<=float(self.currY)+0.5):
            self.get_logger().info("i execute all positiony and last one is: "+str(msg.pose.pose.position.y))
            self.i+=1

        new_roll,new_pitch,new_yaw=self.euler_from_quaternion(msg.pose.pose.orientation)

        self.yawdegr=(new_yaw*180)/math.pi

        if (float(self.yawdegr)>=float(self.yawdeg)-5) & (self.yawdegr<=float(self.yawdeg)+5):
            self.get_logger().info("i execute all positionyaw and last one is"+str(new_yaw))
            self.i+=1


def main (args=None):

    rclpy.init(args=args)
    node=str_subscribe()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__=="__main__":
    main()