#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from turtlesim.msg import Pose


class str_subscribe (Node):
    def __init__(self):
        super().__init__("subscribe")
        
        self.create_subscription(Pose,"/turtle1/custom_pose",self.timer_call,rclpy.qos.qos_profile_sensor_data)

    def timer_call(self,msg):
        print((str(msg.x),str(msg.y)))
        
    
def main (args=None):

    rclpy.init(args=args)
    node=str_subscribe()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__=="__main__":
    main()