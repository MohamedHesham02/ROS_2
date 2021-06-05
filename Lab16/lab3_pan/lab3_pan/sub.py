#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from nav_msgs.msg import Path
from example_interfaces.msg import String
import math


class str_subscribe (Node):
    def __init__(self):
        super().__init__("subscribe")
        self.create_subscription(Path,"/plan",self.timer_call,10)
        self.obj_pub=self.create_publisher(String,"state",10)


    def menger_curvature(self, point_1_x, point_1_y, point_2_x, point_2_y, point_3_x, point_3_y):
        triangle_area = 0.5 * abs( (point_1_x*point_2_y) + (point_2_x*point_3_y) + (point_3_x*point_1_y) - (point_2_x*point_1_y) - (point_3_x*point_2_y) - (point_1_x*point_3_y))#Shoelace formula 
            
        curvature = (4*triangle_area) / (math.sqrt(pow(point_1_x - point_2_x,2)+pow(point_1_y - point_2_y,2)) * math.sqrt(pow(point_2_x - point_3_x,2)+pow(point_2_y - point_3_y,2)) * math.sqrt(pow(point_3_x - point_1_x,2)+pow(point_3_y - point_1_y,2)))#Menger curvature 
        return curvature


    def timer_call(self,plan):

        self.get_logger().info(str(len(plan.poses)))

        if len(plan.poses)>13:

            self.x_2=plan.poses[2].pose.position.x
            self.y_2=plan.poses[2].pose.position.y

            self.x_7=plan.poses[7].pose.position.x 
            self.y_7=plan.poses[7].pose.position.y 
            
            self.x_13=plan.poses[13].pose.position.x 
            self.y_13=plan.poses[13].pose.position.y 

            curvature=self.menger_curvature(self.x_2,self.y_2,self.x_7,self.y_7,self.x_13,self.y_13)

            msg1=String()
            msg1.data= "The path is straight"

            msg2=String()
            msg2.data="The robot is turning with a curvature: "+str(curvature)

            if curvature < 1 : 
                self.obj_pub.publish(msg1)
                self.get_logger().info(msg1.data)

            else: 
                self.obj_pub.publish(msg2)
                self.get_logger().info(msg2.data)
        
        

def main (args=None):

    rclpy.init(args=args)
    node=str_subscribe()
    rclpy.spin(node)

    rclpy.shutdown()

if __name__=="__main__":
    main()