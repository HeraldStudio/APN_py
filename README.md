# APN_py
> [Apple Push Notification](https://developer.apple.com/library/ios/documentation/NetworkingInternet/Conceptual/RemoteNotificationsPG/Chapters/ApplePushService.html) for Herald iOS client
> 
> 同时负责iOS客户端[APIList.plist](https://github.com/lizhuoli1126/EasyAPI)更新

[![](https://img.shields.io/hexpm/l/plug.svg)](http://www.apache.org/licenses/LICENSE-2.0)

# Build

```bash
sudo su
apt-get install redis-server
pip install Flask
pip install redis
easy_install apns
```

# Config
```python
redis_password = 'heraldapn' # redis密码
PE_URL = "http://115.28.27.150/api/pc?uuid=dbd7bb9dca167f98d0741f7067a1b7c715fe1b8c" # 跑操的API URL

identifier = 1 # APN的编号
expiry = time.time()+3600 # APN 请求最长等待秒数
priority = 10 # APN的优先级
api_version = 3.4 # APIList.plist的最新版本
```

# Run

```bash
chmod +x start.sh stop.sh
./start.sh
```

# Stop

```
./stop.sh
```