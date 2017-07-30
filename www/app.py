#! /usr/bin/env python3
#-*- coding: utf-8 -*-

#/Users/liyongyao/work/python/blog_env/bin/python3.6.exe
# import sys
# import os


# print(sys.version)
# print(sys.version_info)

# print(os.path.abspath(__file__)) # 绝对路径， 加文件名
# print(os.path.split(os.path.realpath(__file__))[0])
# print('info...')

import logging; logging.basicConfig(level=logging.INFO)

import asyncio, os, json, time
from datetime import datetime

from aiohttp import web

def index(request):
    return web.Response(body=b'<h1>Awesome</h1>', content_type='text/html')
# web.Response(body=b'<h1>Awesome</h1>') 未被识别为html, 会下载； 加上 content_type='text/html' 可解决此问题

@asyncio.coroutine
def init(loop):
    app = web.Application(loop=loop)
    app.router.add_route('GET','/', index)
    srv = yield from loop.create_server(app.make_handler(), '127.0.0.1', 9000)
    logging.info('server started at http://127.0.0.1:9000...')
    return srv

loop = asyncio.get_event_loop()
loop.run_until_complete(init(loop))
loop.run_forever()