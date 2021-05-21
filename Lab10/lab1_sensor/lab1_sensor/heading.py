#!/usr/bin/env python3

from geometry_msgs import msg
import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Imu
from geometry_msgs.msg import Quaternion
from math import sin, cos, pi
import numpy as np
import math

class str_subscribe (Node):
    def __init__(self):
        super().__init__("subscribe")
        self.create_subscription(Imu,"imu",self.timer_call,10)
        self.d=0

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


    def timer_call(self, imu):

        if (abs(imu.linear_acceleration.x) >=0.3):
            self.get_logger().info("Warning !! .. linear acceleration x exceeded the limit . Current acceleration is"+str(imu.linear_acceleration.x)+" m2/s")
        
        if (abs(imu.angular_velocity.z) >=0.3):
            self.get_logger().info("Warning !! .. angular velocity z exceeded the limit . Current Angular velocity is"+ str(imu.angular_velocity.z)+" rad/sec")
        
    
        msg_roll,msg_pitch,msg_yaw=self.euler_from_quaternion(imu.orientation)

        self.d= (msg_yaw*180)/math.pi

        if (self.d>=-2) & (self.d>=2):
            self.get_logger().info("The robot is nearly heading north .. Heading is:"+ str(self.d)+" degrees")

    
def main (args=None):

    rclpy.init(args=args)
    node=str_subscribe()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__=="__main__":
    main()