#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from turtlesim.srv import Spawn

class move (Node):
    def __init__(self):
        super().__init__("Client_node")
        self.service_client(3.0, 6.0, 1.0)

    def service_client(self,x,y,theta):
        client=self.create_client(Spawn,"spawn")
        request = Spawn.Request()
        request.x = x
        request.y = y
        request.theta = theta
        futur_obj=client.call_async(request)

def main (args=None):
    rclpy.init(args=args)
    node1=move()
    rclpy.spin(node1)
    rclpy.shutdown()

if __name__ == "__main__":
    main()