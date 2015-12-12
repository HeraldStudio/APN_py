#!/bin/bash
#Start the markdown server
redis-cli -a shutdown
/sbin/service crond stop

exit 0