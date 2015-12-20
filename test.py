# -*- coding:utf-8 -*-

from apns import APNs, Frame, Payload

apns = APNs(use_sandbox=False, cert_file='certificate/cert-pro.pem',
	key_file='certificate/key-pro.pem')

# Send a notification
token_hex = '61f74892c732c195016de2e4fe4029bfbd09298458fc77c8ec1f507b96fb4fe0'
content = u"测试推送一下"

def send_push():
    payload = Payload(alert=content, sound="default", badge=1)
    apns.gateway_server.send_notification(token_hex, payload)

try:
	send_push()
except Exception, e:
	print(e)
	raise e