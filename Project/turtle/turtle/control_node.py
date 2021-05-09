#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from turtlesim.srv import Spawn
from turtlesim.srv import Kill
import random
import time

class move (Node):
    def __init__(self):
        super().__init__("Client_node")
        self.service_client1(random.randrange(1, 10),random.randrange(1, 10),2.0,"turtlek")
        self.service_client2("turtlek")
        self.create_publisher(Twist,"goal_pose",10)
        self.create_timer(1/1,self.timer_call1)

    def service_client1(self,x,y,theta,name):
        client=self.create_client(Spawn,"spawn")
        request = Spawn.Request()
        request.x = float(x)
        request.y = float(y)
        request.theta = float(theta)
        request.name = name
        futur_obj=client.call_async(request)

        time.sleep(5)

    def timer_call(self):
        msg = Pose()
        msg.x = float(x)
        msg.y = float(y)
        self.obj_pub.publish(msg)


def main (args=None):
    rclpy.init(args=args)
    node1=move()
    rclpy.spin(node1)
    rclpy.shutdown()


if __name__ == "__main__":
    main()