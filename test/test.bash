#!/bin/bash
# SPDX-FileCopyrightText: 2025 Ryusei Noda
# SPDX-License-Identifier: BSD-3-Clause

dir=~
[ "$1" != "" ] && dir="$1"

cd $dir/ros2_ws

colcon build

source $dir/.bashrc

timeout 60 ros2 launch mypkg talk_listen.launch.py > /tmp/weather_publisher.log

if grep -q 'weather_info_listener' /tmp/weather_publisher.log; then
    echo "Test passed: Listener found in the log."
    exit 0
else
    echo "Test failed: Listener not found in the log."
    exit 1
fi

