#!/bin/bash
#Start the markdown server
redis-cli -a heraldstudio shutdown
service cron restart
crontab -r
killall python
screen -wipe

exit 0