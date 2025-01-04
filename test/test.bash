#!/bin/bash
# SPDX-FileCopyrightText: 2025 Ryusei Noda
# SPDX-License-Identifier: BSD-3-Clause

dir=~
[ "$1" != "" ] && dir="$1"

cd $dir/ros2_ws
colcon build

source $dir/.bashrc

timeout 30 ros2 launch mypkg weather_publisher.launch.py > /tmp/weather_publisher.log

cat /tmp/weather_publisher.log | grep 'temperature'
cat /tmp/weather_publisher.log | grep 'windspeed'
cat /tmp/weather_publisher.log | grep 'precipitation'

