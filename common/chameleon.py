#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import random

class Chameleon(object):
    """docstring for Chameleon"""
    def __init__(self):
        super(Chameleon, self).__init__()

    def get_headers(self):
        return {'User-Agent': random.choice(self.ua_list)}

    def get_proxies(self):
        proxy = random.choice(self.proxy_list)
        return {'http': proxy, 'https': proxy}

    ua_list = [
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.8; rv:21.0) Gecko/20100101 Firefox/21.0',
        'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:21.0) Gecko/20130331 Firefox/21.0',
        'Mozilla/5.0 (Windows NT 6.2; WOW64; rv:21.0) Gecko/20100101 Firefox/21.0',
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.93 Safari/537.36',
        'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.11 (KHTML, like Gecko) Ubuntu/11.10 Chromium/27.0.1453.93 Chrome/27.0.1453.93 Safari/537.36',
        'Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.94 Safari/537.36',
        'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0)',
        'Mozilla/5.0 (compatible; WOW64; MSIE 10.0; Windows NT 6.2)',
        'Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; en) Presto/2.9.168 Version/11.52',
        'Opera/9.80 (Windows NT 6.1; WOW64; U; en) Presto/2.10.229 Version/11.62',
        'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_6; en-US) AppleWebKit/533.20.25 (KHTML, like Gecko) Version/5.0.4 Safari/533.20.27',
        'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/533.20.25 (KHTML, like Gecko) Version/5.0.4 Safari/533.20.27',
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.87 Safari/537.36',
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.98 Safari/537.36',
        'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36',
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.98 Safari/537.36',
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_1) AppleWebKit/602.2.14 (KHTML, like Gecko) Version/10.0.1 Safari/602.2.14',
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.63 Safari/537.36 Qiyu/2.1.0.0',
        'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.100 Safari/537.36',
        'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.87 Safari/537.36',
        'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36',
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36',
        'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36',
        'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0',
        'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36',
        'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.3 Safari/537.36',
        'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.59 Safari/537.36',
        'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36',
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.98 Safari/537.36',
        'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.63 Safari/537.36 Qiyu/2.1.0.0',
        'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36',
        'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.75 Safari/537.36',
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.95 Safari/537.36'
        'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36',
        'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36',
        'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.75 Safari/537.36'
    ]

    proxy_list = [
        '14.223.23.126:9999',
        '175.4.12.214:9999',
        '111.160.141.42:63000',
        '124.88.67.83:843',
        '120.52.73.97:8083',
        '222.87.72.105:9999',
        '124.118.237.218:9999',
        '42.84.199.115:8998',
        '123.206.93.108:8081',
        '124.88.67.10:83',
        '36.73.216.172:80',
        '14.105.168.238:9999',
        '183.71.192.189:9999',
        '58.154.33.12:8080',
        '66.65.8.172:9999',
        '60.11.35.67:8998',
        '106.46.136.64:808',
        '124.88.67.34:843',
        '94.177.248.71:8080',
        '37.59.54.189:3128',
        '113.5.234.73:9529',
        '220.166.241.51:8118',
        '92.222.106.162:9999',
        '35.157.121.224:3128',
        '120.52.73.98:8092',
        '111.85.118.25:8998',
        '119.165.11.77:8118',
        '46.105.121.118:1080',
        '114.223.87.112:9999',
        '183.71.152.206:9999',
        '182.253.161.60:8080',
        '116.199.48.245:80',
        '14.125.51.82:8888',
        '122.212.129.9:80',
        '192.99.79.159:8080',
        '120.52.73.98:8088',
        '124.88.67.31:843',
        '111.76.133.172:808',
        '14.109.132.182:9999',
        '54.153.127.129:8083',
        '35.160.136.133:8000',
        '80.240.221.38:3128',
        '52.34.230.6:8088',
        '14.105.177.85:9999',
        '110.52.183.208:9999',
        '120.52.73.98:99',
        '211.75.115.20:80',
        '119.86.68.26:9999',
        '47.89.41.164:80',
        '221.2.230.196:8998',
        '222.138.69.226:8998',
        '120.52.73.97:8084',
        '183.21.135.228:9999',
        '106.87.26.144:9999',
        '14.105.178.162:9999',
        '177.67.84.248:8080',
        '96.239.193.244:8080',
        '58.216.14.22:808',
        '115.231.175.68:8081',
        '125.88.74.122:82',
        '124.88.67.14:843',
        '111.76.133.210:808',
        '14.111.250.187:9999',
        '110.83.46.89:808',
        '121.232.145.33:9000',
        '192.99.56.104:8080',
        '203.172.223.190:8080',
        '218.109.189.16:8888',
        '110.154.92.42:8888',
        '124.88.67.7:843',
        '120.52.73.97:8094',
        '182.204.18.65:8118',
        '52.59.61.67:8083',
        '120.52.73.98:86',
        '220.250.12.19:8998',
        '115.58.16.31:9999',
        '218.86.128.62:8118',
        '106.46.136.82:808',
        '120.52.73.97:8091',
        '36.249.192.128:8118',
        '114.228.185.57:8118',
        '14.105.177.218:9999',
        '219.246.184.153:80',
        '120.52.73.97:8087',
        '14.199.124.204:80',
        '183.67.243.79:9999',
        '31.220.58.150:3128',
        '106.46.136.3:808',
        '125.81.178.86:9999',
        '120.52.73.98:84',
        '111.76.129.171:808',
        '120.52.73.98:8081',
        '120.52.73.97:98',
        '94.242.59.123:80',
        '120.52.73.98:8097',
        '112.195.72.143:8118',
        '125.112.174.36:8088',
        '120.52.73.98:90',
        '113.252.236.96:8080',
        '89.34.26.14:1080',
        '124.88.67.17:83',
        '158.69.157.32:3128',
        '121.40.139.217:80',
        '113.206.211.99:8998',
        '120.52.73.109:8090',
        '124.88.67.30:82',
        '120.52.73.97:8097',
        '52.59.66.142:8083',
        '120.52.73.98:8083',
        '163.121.187.180:8080',
        '94.177.234.145:80',
        '125.122.118.87:808',
        '120.52.73.98:97',
        '123.57.225.102:8088',
        '81.2.252.136:3128',
        '120.52.73.98:82',
        '47.91.151.193:3128',
        '122.195.181.133:8888',
        '94.177.252.80:80',
        '120.52.73.112:8090',
        '108.61.182.117:8118',
        '120.52.73.98:8093',
        '106.83.93.17:9999',
        '177.67.81.26:3128',
        '182.92.224.202:8088',
        '115.56.188.207:808',
        '111.120.117.27:9999',
        '124.88.67.81:843',
        '120.52.73.98:85',
        '124.88.67.23:843',
        '164.67.174.43:3128',
        '125.166.226.234:80',
        '115.236.226.225:8998',
        '183.68.180.241:9999',
        '117.70.96.116:9999',
        '120.52.73.98:8094',
        '120.52.73.98:8091',
        '217.33.216.114:8080',
        '140.224.76.17:808',
        '124.88.67.19:843',
        '124.88.67.32:83',
        '192.99.128.170:80',
        '119.86.11.136:9999',
        '120.52.73.98:8089',
        '192.129.221.89:9001',
        '124.88.67.31:81',
        '124.88.67.52:843',
        '31.220.54.45:80',
        '202.73.51.146:8128',
        '120.52.73.112:8080',
        '110.179.46.233:8888',
        '111.76.129.136:808',
        '106.46.136.14:808',
        '120.52.73.98:8085',
        '124.88.67.21:81',
        '125.88.74.122:83',
        '23.88.102.24:8080',
        '218.84.122.211:9999',
        '177.84.87.154:80',
        '77.73.66.227:8080',
        '182.39.153.2:8118',
        '124.88.67.17:80',
        '183.69.9.201:9999',
        '39.74.178.69:8998',
        '221.226.82.130:8998',
        '120.26.48.77:80',
        '124.88.67.32:81',
        '125.82.122.219:9999',
        '14.155.115.41:8118',
        '47.52.2.135:8080',
        '119.84.160.165:9999',
        '125.34.88.90:8118',
        '90.152.38.178:1080',
        '183.67.39.49:9999',
        '124.88.67.31:80',
        '5.160.33.92:3128',
        '14.110.119.69:9999',
        '63.150.152.151:8080',
        '14.201.122.140:80',
        '124.88.67.20:82',
        '158.69.186.112:8080',
        '124.88.67.19:82',
        '192.99.128.170:3128',
        '42.84.67.111:8888',
        '120.52.73.98:80',
        '124.88.67.10:81',
        '158.69.172.98:80',
        '124.88.67.20:843',
        '170.248.47.58:80',
        '94.177.234.145:3128',
        '117.91.185.152:9999',
        '221.215.162.218:8998',
        '138.97.241.160:80',
        '120.52.73.98:8080',
        '113.244.50.41:9999',
        '106.46.136.89:808',
        '113.69.165.251:808',
        '92.109.100.74:80',
        '106.46.136.102:808',
        '106.46.136.80:808',
        '113.141.119.212:9999',
        '125.84.218.87:9999',
        '179.185.54.114:8080',
        '124.135.154.242:9999',
        '124.88.67.34:81',
        '63.150.152.151:3128',
        '182.48.113.11:8088',
        '120.52.73.112:8091',
        '27.8.61.225:8888',
        '195.138.86.112:3128',
        '120.52.73.98:100',
        '107.170.54.215:8080',
        '94.242.59.141:80',
        '113.110.128.252:3128',
        '223.244.196.135:8118',
        '58.176.46.248:8380',
        '144.217.49.233:8080',
        '120.52.73.97:8098',
        '120.52.73.97:8081',
        '94.156.144.87:80',
        '124.88.67.39:843',
        '106.46.136.127:808',
        '185.43.210.238:8080',
        '88.159.109.104:80',
        '120.52.73.97:80',
        '120.52.73.98:8096',
        '120.52.73.98:95',
        '180.246.14.221:80',
        '124.88.67.19:80',
        '185.22.172.20:3128',
        '219.145.95.193:8998',
        '177.67.84.248:3128',
        '120.52.73.97:93',
        '175.15.183.150:9999',
        '182.88.228.251:8123',
        '120.52.73.98:98',
        '125.120.10.127:808',
        '175.7.150.232:9999',
        '222.255.236.117:3128',
        '94.46.177.99:80',
        '123.56.28.89:8080',
        '14.109.71.213:9999',
        '124.88.67.83:83',
        '114.215.29.26:80',
        '124.88.67.83:80',
        '120.52.73.97:83',
        '115.198.34.88:808',
        '106.46.136.79:808',
        '115.214.161.24:8118',
        '60.219.11.61:8998',
        '222.169.193.162:8099',
        '52.59.251.120:8083',
        '221.211.49.169:9999',
        '222.169.87.80:8998',
        '113.133.68.118:9999',
        '92.47.195.250:3128',
        '219.127.253.43:80',
        '94.23.17.132:9999',
        '120.77.223.7:28080',
        '120.52.73.97:81',
        '192.129.231.118:9001',
        '184.69.67.122:80',
        '183.71.134.87:9999',
        '192.99.128.170:8080',
        '52.59.65.26:8083',
        '119.28.12.218:8888',
        '106.88.12.198:9999',
        '120.52.73.97:8086',
        '180.251.145.175:80',
        '222.211.65.138:80',
        '124.88.67.39:80',
        '111.123.40.104:9999',
        '49.86.133.144:9999',
        '181.111.175.235:8080',
        '125.122.116.132:808',
        '183.67.28.86:9999',
        '94.156.144.87:8080',
        '124.88.67.24:843',
        '112.233.111.225:808',
        '192.129.225.194:9001',
        '14.106.15.47:9999',
        '124.234.44.219:9999',
        '58.37.57.200:8118',
        '183.68.169.171:9999',
        '5.2.64.150:1080',
        '110.189.223.201:808',
        '152.251.245.236:8080',
        '14.109.129.161:9999',
        '113.244.93.110:9999',
        '124.88.67.19:81',
        '181.59.255.227:8080',
        '219.152.196.111:9999',
        '106.46.136.20:808',
        '106.46.136.108:808',
        '123.189.56.123:9999',
        '112.249.41.57:8888',
        '117.70.184.252:9999',
        '120.52.73.112:80',
        '120.52.73.97:88',
        '120.52.73.123:100',
        '111.13.7.42:83',
        '124.88.67.10:843',
        '120.52.73.97:92',
        '120.52.73.97:97',
        '203.90.144.145:80',
        '120.52.73.97:8082',
        '125.72.106.216:808',
        '124.88.67.39:82',
        '138.97.241.160:3128',
        '124.88.67.83:82',
        '124.88.67.30:81',
        '178.206.193.107:8080',
        '183.165.93.208:8998',
        '110.187.12.138:808',
        '94.177.252.80:3128',
        '120.52.73.97:8089',
        '200.229.202.72:80',
        '212.46.215.107:8080',
        '14.105.179.167:9999',
        '85.255.11.23:3128',
        '123.4.88.196:8118',
        '124.88.67.81:81',
        '218.109.123.185:8888',
        '111.13.7.42:80',
        '153.0.163.18:8998',
        '124.88.67.18:81',
        '121.40.42.35:9999',
        '200.229.202.72:8080',
        '87.236.233.182:808',
        '186.24.7.26:8080',
        '124.88.67.30:843',
        '202.111.175.97:8080',
        '45.40.143.57:80',
        '125.46.64.91:8080',
        '124.88.67.21:83',
        '121.24.220.205:8118',
        '106.87.66.189:9999',
        '117.21.234.96:8080',
        '36.80.27.181:8080',
        '223.87.178.73:80',
        '124.88.67.17:843',
        '35.163.151.89:8083',
        '31.214.152.90:8080',
        '120.52.73.98:8100',
        '125.127.50.241:8118'
    ]

chameleon = Chameleon()
