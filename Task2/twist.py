#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
import time

class move (Node):
    def __init__(self):
        super().__init__("Client_node")
        self.obj_pub=self.create_publisher(Twist,"turtle1/cmd_vel",10)
        self.create_timer(1/1,self.timer_call)
        self.create_timer(1/1,self.timer_call1)
        self.create_timer(1/1,self.timer_call2)
        
    def timer_call(self):
        msg = Twist()
        msg.linear.x = 1.0
        self.obj_pub.publish(msg)
        
        time.sleep(3)

    
    def timer_call1(self):
        msg = Twist()
        msg.linear.x = 1.0
        msg.angular.z = 0.5
        self.obj_pub.publish(msg)

        time.sleep(3)

    def timer_call2(self):
        msg = Twist()
        msg.angular.z = 1.0
        self.obj_pub.publish(msg)

        time.sleep(3)

    



    

def main (args=None):
    rclpy.init(args=args)
    node1=move()
    rclpy.spin(node1)
    rclpy.shutdown()

if __name__ == "__main__":
    main()