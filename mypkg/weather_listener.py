import rclpy
from rclpy.node import Node
from std_msgs.msg import String


class ISSPositionListener(Node):
    def __init__(self):
        super().__init__("iss_position_listener")
        self.create_subscription(String,"now_position",self.listener_callback,10)

    def listener_callback(self,msg):
        self.get_logger().info(f"{msg.data}")

def main():
    rclpy.init()
    node = ISSPositionListener()
    rclpy.spin(node)
