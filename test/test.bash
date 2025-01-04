#!/bin/bash
# SPDX-FileCopyrightText: 2025 Ryusei Noda
# SPDX-License-Identifier: BSD-3-Clause


dir=~
[ "$1" != "" ] && dir="$1"

cd $dir/ros2_ws

colcon build

source $dir/.bashrc

timeout 30 ros2 launch mypkg talk_listen.launch.py > /tmp/weather_publisher.log

count=$(cat /tmp/weather_publisher.log | grep -c 'weather_info_listener')

if [ "$count" -ge 2 ]; then
    echo "Test passed: Found $count entries."
    exit 0
else
    echo "Test failed: Found only $count entries."
    exit 1
fi
