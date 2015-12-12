#!/bin/bash
#Start the markdown server
redis-server redis.conf
service cron start
crontab task.cron
screen python main.py

exit 0