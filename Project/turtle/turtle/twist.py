#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from turtlesim.srv import Spawn
from turtlesim.srv import Kill
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose
import random
import time
import math

class catch (Node):
    def __init__(self):
        super().__init__("subscribe")
        self.service_client(random.randrange(1, 10),random.randrange(1, 10),2.0,"turtlek")
        self.create_subscription(Pose,"turtle1/pose",self.timer_call,10)
        self.obj_pub=self.create_publisher(Twist,"turtle1/cmd_vel",10)
        self.dx=0.0
        self.dy=0.0
        self.x=0.0
        self.y=0.0
        self.name="m"

    def service_client(self,x,y,theta,name):
        client=self.create_client(Spawn,"spawn")
        request = Spawn.Request()
        request.x = float(x)
        request.y = float(y)
        request.theta = float(theta)
        request.name = name
        futur_obj = client.call_async(request)
        self.x = request.x
        self.y = request.y
        self.name = request.name
        print(self.x)
        
    def timer_call(self,msg1):
      
        self.dx= (self.x-msg1.x)
        self.dxs = pow(self.dx, 2)
        self.dy= (self.y-msg1.y)
        self.dys=pow(self.dy, 2)
        self.tani=math.atan2(self.dy, self.dx)
        msg = Twist()
        msg.linear.x = (math.sqrt(self.dxs+self.dys))*2
        msg.angular.z = (self.tani-2)*2
        self.obj_pub.publish(msg)

        print(msg1.x)
        print(self.x)

        if (self.dx<=3)&(self.dy<=3):

            def service_client1(self,name):
                client=self.create_client(Kill,"kill")
                request = Kill.Request()
                request.name = name
                futur_obj=client.call_async(request)

            def service_client(self,x,y,theta,name):
                client=self.create_client(Spawn,"spawn")
                request = Spawn.Request()
                request.x = float(x)
                request.y = float(y)
                request.theta = float(theta)
                request.name = name
                futur_obj=client.call_async(request)


def main (args=None):

    rclpy.init(args=args)
    node=catch()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__=="__main__":
    main()