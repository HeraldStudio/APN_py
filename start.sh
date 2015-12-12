#!/bin/bash
#Start the markdown server
redis-server redis.conf
/sbin/service crond start
python main.py

exit 0