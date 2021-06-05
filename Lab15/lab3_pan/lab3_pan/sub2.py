#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from nav_msgs.msg import Path
from example_interfaces.msg import String
import math
import numpy as np


class str_subscribe (Node):
    def __init__(self):
        super().__init__("subscribe")
        self.create_subscription(Path,"/local_plan",self.timer_call,10)
        self.obj_pub=self.create_publisher(String,"state",10)


    def menger_curvature(self, point_1_x, point_1_y, point_2_x, point_2_y, point_3_x, point_3_y):
        triangle_area = 0.5 * abs( (point_1_x*point_2_y) + (point_2_x*point_3_y) + (point_3_x*point_1_y) - (point_2_x*point_1_y) - (point_3_x*point_2_y) - (point_1_x*point_3_y))#Shoelace formula 
        
        try:

            curvature = (4*triangle_area) / (math.sqrt(pow(point_1_x - point_2_x,2)+pow(point_1_y - point_2_y,2)) * math.sqrt(pow(point_2_x - point_3_x,2)+pow(point_2_y - point_3_y,2)) * math.sqrt(pow(point_3_x - point_1_x,2)+pow(point_3_y - point_1_y,2)))
            
            return curvature
            
        except:
            
            return 0 

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



    def timer_call(self,plan):

        self.get_logger().info(str(len(plan.poses)))

        if len(plan.poses)>9:

            self.x_2=plan.poses[2].pose.position.x
            self.y_2=plan.poses[2].pose.position.y

            self.x_5=plan.poses[5].pose.position.x 
            self.y_5=plan.poses[5].pose.position.y 
            
            self.x_9=plan.poses[9].pose.position.x 
            self.y_9=plan.poses[9].pose.position.y


            new_roll_1,new_pitch_1,new_yaw_1=self.euler_from_quaternion(plan.poses[2].pose.orientation)
            new_roll_2,new_pitch_2,new_yaw_2=self.euler_from_quaternion(plan.poses[7].pose.orientation)

            orientation=new_yaw_1-new_yaw_2

            curvature=self.menger_curvature(self.x_2,self.y_2,self.x_5,self.y_5,self.x_9,self.y_9)

            msgs=String()
            msgs.data= "The path is straight"

            msgr=String()
            msgr.data="The robot is turning right with a curvature: "+str(curvature)

            msgl=String()
            msgl.data="The robot is turning left with a curvature: "+str(curvature)

            if orientation == 0 : 
                self.obj_pub.publish(msgs)
                self.get_logger().info(msgs.data)

            elif orientation > 0: 
                self.obj_pub.publish(msgr)
                self.get_logger().info("The robot is turning to the right ")

            elif orientation < 0: 
                self.obj_pub.publish(msgl)
                self.get_logger().info("The robot is turning to the left ")
        
        

def main (args=None):

    rclpy.init(args=args)
    node=str_subscribe()
    rclpy.spin(node)

    rclpy.shutdown()

if __name__=="__main__":
    main()