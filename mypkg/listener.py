# SPDX-FileCopyrightText: 2025 Ryusei Noda
# SPDX-License-Identifier: BSD-3-Clause

import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class WeatherInfoListener(Node):
    def __init__(self):
        super().__init__('weather_info_listener')
        self.create_subscription(String, 'weather_info', self.listener_callback, 10)

    def listener_callback(self, msg):
        self.get_logger().info(f" {msg.data}")

def main():
    rclpy.init()
    node = WeatherInfoListener()
    rclpy.spin(node)

