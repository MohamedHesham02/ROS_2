#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from my_msgs.srv import Ser 

class server(Node):
    def __init__(self):
        super().__init__("Client_part")
        self.service_client(True)

    def service_client(self,val):
        client=self.create_client(Ser,"First_server")
        request=Ser.Request()
        request.data=val
        futur_obj=client.call_async(request)
        futur_obj.add_done_callback(self.future_call)

    def future_call(self,future_msg):
        self.get_logger().info("mohamed")
        
def main (args=None):
    rclpy.init(args=args)
    node1=server()
    rclpy.spin(node1)
    rclpy.shutdown()

if __name__ == "__main__":
    main()