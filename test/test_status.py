import pytest
from unittest.mock import patch
from rclpy.node import Node
import psutil
from status import main

@pytest.fixture
def node():
    node = Node('test_node')
    yield node
    node.destroy_node()

def test_system_status_log(node):
    with patch('psutil.cpu_percent') as mock_cpu_percent, \
         patch('psutil.virtual_memory') as mock_virtual_memory, \
         patch('psutil.sensors_battery') as mock_battery:
        
        mock_cpu_percent.return_value = 50
        mock_virtual_memory.return_value = psutil._psvm.svmem(virtual_memory=0, available=0, percent=60, total=0, used=0, free=0)
        mock_battery.return_value = psutil._psbattery.sensors_battery(percent=80, power_plugged=True)

        with patch.object(node.get_logger(), 'info') as mock_logger:

            main()
         
            log_message = (
                "Time: 2024-01-01 12:00:00\n"
                "CPU Usage: 50%\n"
                "Memory Usage: 60%\n"
                "Battery: 80% (Charging)"
            )
            mock_logger.assert_any_call(log_message)

