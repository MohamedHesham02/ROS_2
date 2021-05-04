#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from example_interfaces.msg import String
from example_interfaces.msg import Int64
from example_interfaces.srv import SetBool


class num_subscribe (Node):
    def __init__(self):
        super().__init__("subscribe")
        self.i=0
        self.create_subscription(String,"number",self.timer_call,10) 
        self.obj_pub2=self.create_publisher(String,"number",10)
        self.get_logger().info("Your no. is accumlated ")
        self.create_service(SetBool,"First_server",self.srv_call)
  

    def timer_call(self, msg):
        msg=String()
        self.get_logger().info(msg.data)
        self.i+=3
        self.get_logger().info(str(self.i))
        

    def srv_call(self,req,rsp):
        request=req.data
        if request == True:
            self.i=0
            self.i+=3
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