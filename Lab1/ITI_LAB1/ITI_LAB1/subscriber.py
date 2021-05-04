#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from example_interfaces.msg import String
from example_interfaces.msg import Int64


class str_subscribe (Node):
    def __init__(self):
        super().__init__("subscribe")
        self.create_subscription(String,"str_topic",self.timer_call,10) #kda h3ml subsribe mn l str_topic w no3 l data string
        self.create_subscription(String,"number",self.timer_call,10) #kda h3ml subsribe gdeed mn l number lli hwa topic gdeed w no3 l data string

        self.get_logger().info("Your name is published ") # awl msg bttb3t 

        #tool ma l publisher bytb3 l subscriber byfdl yfollow l order lli m3mol bl timercall w yfdl yb3t l msg lli msglha ttb3 fl msg data 
     

    def timer_call(self, msg):
        self.get_logger().info(msg.data)
        


def main (args=None):

    rclpy.init(args=args)
    node=str_subscribe()
    rclpy.spin(node)

    rclpy.shutdown()

if __name__=="__main__":
    main()