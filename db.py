# -*- coding: utf-8 -*-
import redis
import config

r = redis.StrictRedis(host=config.host, port=config.port, db=config.db, password=config.password)

def get_token_list():
	result = r.keys()
	return result

def set_token(token):
	result = r.set(token, 1)
	return result

def get_token(token):
	result = r.get(token)
	return result
def remove_token(token):
	result = r.delete(token)
	return result

def remove_all():
	result = r.flushall()
	return result