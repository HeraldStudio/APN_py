import redis
import config

r = redis.StrictRedis(host='localhost', port=6379, db=0, password=config.redis_password)

def get_token_list():
	result = r.keys()
	return result

def set_token(token):
	result = r.set(token, 1)
	return result

def get_token(token):
	result = r.get(token)
	return result

def remove_all():
	result = r.flushall()
	return result