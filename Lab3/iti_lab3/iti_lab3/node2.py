#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from my_msgs.msg import Custom
from my_msgs.srv import Ser 

class num_subscribe (Node):
    def __init__(self):
        super().__init__("subscribe")
        self.create_subscription(Custom,"name",self.timer_call,10)
        self.create_service(Ser,"First_server",self.srv_call)
        self.get_logger().info("Your no. is accumlated ")
        self.counter=5
        
    def timer_call(self, msg):
        self.get_logger().info(msg.message)
        self.counter+=msg.number
        self.get_logger().info(str(self.counter))

    def srv_call(self,req,rsp):
        request=req.data
        if request == True:
            self.counter=0
            self.counter+=5
            rsp.success = True
            rsp.message="OK call"
        self.get_logger().info(rsp.message)

        return rsp
    
def main (args=None):

    rclpy.init(args=args)
    node=num_subscribe()
    rclpy.spin(node)

    rclpy.shutdown()

if __name__=="__main__":
    main()