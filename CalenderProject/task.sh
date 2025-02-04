#!/bin/bash
export DISPLAY=:0
export DBUS_SESSION_BUS_ADDRESS="unix:path=/run/user/1000/bus"
message=$1
echo "$message" >> /home/muhamed/ODC/project/output.log
notify-send -t 2000 "Notification" "$message"