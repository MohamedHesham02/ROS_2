#!/usr/bin/env python3

from geometry_msgs import msg
import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Imu
from geometry_msgs.msg import Quaternion
from math import sin, cos, pi
import numpy as np
import math
import csv

class str_subscribe (Node):
    def __init__(self):
        super().__init__("subscribe")
        self.create_subscription(Imu,"zed2_imu",self.timer_call,10)
        self.create_timer(30,self.timer_call)
        self.i=-1
        self.Veryhigh_certainty=0.00001
        self.high_certainty=0.001
        self.low_certainty=1000000000.0


    def timer_call(self):

        with open('/home/mohamed/imu_data.csv', mode='r') as Twist_file:
            reader = csv.reader(Twist_file, delimiter=',')
            data = list(reader)

        if self.i == 347:
            self.i=0
    
        self.i+=1
        row=data[self.i]

        self.accX=float(row[0])*9.8
        self.accY=float(row[1])*9.8
        self.accZ=float(row[2])*9.8
        self.angX=row[3]
        self.angY=row[4]
        self.angZ=float(row[5])
        self.yaw_deg=row[6]

        self.get_logger().info("zed2_imu_link")

        self.get_logger().info("AccelerationX is "+str(self.accX)+"with Covar.: "+ str(self.high_certainty))
        self.get_logger().info("AccelerationY is "+str(self.accY)+"with Covar.: "+ str(self.high_certainty))
        self.get_logger().info("AccelerationZ is "+str(self.accZ)+"with Covar.: "+ str(self.high_certainty))

        
        self.get_logger().info("AngX is "+str(self.angX)+"with Covar.: "+ str(self.Veryhigh_certainty))
        self.get_logger().info("AngY is "+str(self.angY)+"with Covar.: "+ str(self.Veryhigh_certainty))


        if (self.angZ < 0.3):
            self.get_logger().info("AngZ is "+str(self.angZ)+"with Covar.: "+ str(self.high_certainty))
            self.get_logger().info("Yaw is "+str(self.yaw_deg)+"with Covar.: "+ str(self.high_certainty))

        if (self.angZ > 0.3):
            self.get_logger().info("AngZ is "+str(self.angZ)+"with Covar.: "+ str(self.low_certainty))
            self.get_logger().info("Yaw is "+str(self.yaw_deg)+"with Covar.: "+ str(self.low_certainty))

    
def main (args=None):

    rclpy.init(args=args)
    node=str_subscribe()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__=="__main__":
    main()