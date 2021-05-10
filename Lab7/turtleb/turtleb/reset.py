#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from std_srvs.srv import Empty
from turtlesim.msg import Pose

class move (Node):
    def __init__(self):
        super().__init__("Client_node")

        self.create_subscription(Pose,"turtle1/pose",self.timer_call,10)

    def timer_call(self,msg):

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
    node1=move()
    rclpy.spin(node1)
    rclpy.shutdown()

if __name__ == "__main__":
    main()
