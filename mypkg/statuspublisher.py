#!/usr/bin/python3
# SPDX-FileCopyrightText: 2024 Ryusei Noda
# SPDX-License-Identifier: BSD-3-Clause

import rclpy
from rclpy.node import Node
import psutil
from datetime import datetime
from std_msgs.msg import String

class SystemStatusPublisher(Node):
    def __init__(self):
        super().__init__('system_status_publisher')
        self.publisher_ = self.create_publisher(String, 'system_status', 10)  # トピック名 'system_status'
        self.timer = self.create_timer(1.0, self.publish_system_status)  # 1秒ごとに情報をパブリッシュ
        self.get_logger().info('System Status Publisher Node has started.')

    def publish_system_status(self):
        now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        cpu_usage = psutil.cpu_percent(interval=None)
        memory = psutil.virtual_memory()
        battery = psutil.sensors_battery()

        memory_usage = f'{memory.percent}%'
        battery_status = 'Charging' if battery.power_plugged else 'Discharging'
        battery_percent = f'{battery.percent}%'

        log_message = (
            f"Time: {now}\n"
            f"CPU Usage: {cpu_usage}%\n"
            f"Memory Usage: {memory_usage}\n"
            f"Battery: {battery_percent} ({battery_status})"
        )

        msg = String()
        msg.data = log_message
        self.publisher_.publish(msg)
        self.get_logger().info(f"Published: {log_message}")

def main(args=None):
    rclpy.init(args=args)
    node = SystemStatusPublisher()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        node.get_logger().info('Node is shutting down.')
    finally:
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()

