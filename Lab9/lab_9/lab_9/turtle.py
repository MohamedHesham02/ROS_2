#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from std_srvs.srv import Empty
from turtlesim.msg import Pose
import csv

class turtle_execute (Node):
    def __init__(self):
        super().__init__("turtle")
        self.obj_pub=self.create_publisher(Twist,"turtle1/cmd_vel",10)
        self.create_subscription(Pose,"turtle1/pose",self.timer_call1,10)
        self.create_timer(1/1,self.timer_call)
        self.i=0
        
            
    def timer_call(self):
        msg = Twist()
        with open('/home/mohamed/turtle_commands.csv', mode='r') as Twist_file:
            reader = csv.reader(Twist_file, delimiter=',')
            data = list(reader)
        
        if self.i == 12:
            self.i=0
        self.i+=1
        row=data[self.i]
        self.x=row[0]
        self.z=row[1]
        msg.linear.x = float(self.x)
        msg.angular.z = float(self.z)
        self.obj_pub.publish(msg)


    def timer_call1(self,msg):
        
        if (msg.x>8) or (2>msg.x):

            client=self.create_client(Empty,"reset")
            request = Empty.Request()
            futur_obj=client.call_async(request)

        elif (msg.y>8) or (2>msg.y):

            client=self.create_client(Empty,"reset")
            request = Empty.Request()
            futur_obj=client.call_async(request)




def main (args=None):
    rclpy.init(args=args)
    node1=turtle_execute()
    rclpy.spin(node1)
    rclpy.shutdown()


if __name__ == "__main__":
    main()
