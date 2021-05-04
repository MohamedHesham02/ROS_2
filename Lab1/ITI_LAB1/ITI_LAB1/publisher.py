#!/usr/bin/env python3

import rclpy 
from rclpy.node import Node
from example_interfaces.msg import String
from example_interfaces.msg import Int64
from example_interfaces.msg import Bool


class str_publisher (Node):
    def __init__(self):
        super().__init__("publisher")
        self.i=1
        self.obj_pub=self.create_publisher(String,"str_topic",10)
        self.obj_pub=self.create_publisher(String,"number",10)
        self.create_timer(1/2,self.timer_call)
        self.get_logger().info("Your name is published ") #start mesage bra l loop

    def timer_call(self):
        
        self.get_logger().info("Your name is published")  #lly hyytb3 fl loop ll publisher
        self.get_logger().info(str(self.i))
        self.i+=1
        if self.i == 6:
            self.i=1
        msg1=String()
        msg2=String()
        msg1.data="Your name is published,"+str(self.i) ##lly hyytb3 fl loop ll subscriber     
        msg2.data=str(self.i)
        self.obj_pub.publish(msg1)
        self.obj_pub.publish(msg2)


def main (args=None):
        rclpy.init(args=None) #mmkn tkon args=args
        node=str_publisher() #btnfz l func lli fl class 
        rclpy.spin(node) #bt5leeh ystna call back li order tani bl tali 3shan fi loop f hy5leeh ynfz
        

        rclpy.shutdown()
        
if __name__=="__main__":
    main()
        


