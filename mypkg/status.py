#!/usr/bin/python3
# SPDX-FileCopyrightText: 2024 Ryusei Noda
# SPDX-License-Identifier: BSD-3-Clause

import rclpy
from rclpy.node import Node
import psutil
from datetime import datetime

def main(args=None):
    rclpy.init(args=args)

    node = Node('system_status')

    node.get_logger().info('System Status Node has started.')

    try:
        while rclpy.ok():
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
            node.get_logger().info(log_message)

            node.get_clock().sleep_for(rclpy.time.Duration(seconds=1))
    except KeyboardInterrupt:
        node.get_logger().info('Node is shutting down.')
    finally:

        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()

