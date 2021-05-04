#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from std_srvs.srv import Empty

class move (Node):
    def __init__(self):
        super().__init__("Client_node")
        self.service_client()

    def service_client(self):
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



