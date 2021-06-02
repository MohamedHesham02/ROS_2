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

        if len(plan.poses)>9:

            self.x_2=plan.poses[2].pose.position.x
            self.y_2=plan.poses[2].pose.position.y
            self.coordinate_2=(self.x_2,self.y_2)
            self.x_6=plan.poses[6].pose.position.x 
            self.y_6=plan.poses[6].pose.position.y 
            self.coordinate_6=(self.x_6,self.y_6)
            self.x_9=plan.poses[9].pose.position.x 
            self.y_9=plan.poses[9].pose.position.y 
            self.coordinate_9=(self.x_9,self.y_9)

            curvature=self.menger_curvature(self.x_2,self.y_2,self.x_6,self.y_6,self.x_9,self.y_9)

            msg1=String()
            msg1.data="The path is straight"

            msg2=String()
            msg2.data="The robot is turning with a curvature: "+str(curvature)
            
            if curvature < 0.5 : 
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