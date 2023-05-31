import requests
import json
import logging
from requests.auth import HTTPBasicAuth
import settings
import time
import Constants

def push(msg):
    if settings.config['push']['enable']:
        payload = json.dumps({
            "type": "headline",
            "from": settings.config['push']['admin'],
            "to": settings.config['push']['user'],
            "subject": "investing",
            "body": msg
        })
        response = requests.post(settings.config['push']['url'], auth=HTTPBasicAuth(settings.config['push']['admin'],
                                                settings.config['push']['admin_pass']), data=payload)
        print(response.text)
    logging.info(msg)


def statistics(msg=None):
    push(msg)


def strategy(msg=None):
    if msg is None or not msg:
        msg = '今日没有符合条件的股票'
    push(msg)


def saveStrategyRes(strategy, res):
    if settings.config['save']['enable']:
        today = time.strftime("%Y-%m-%d", time.localtime()) 
        try:
            with open(f'{strategy}:{today}.csv','a+', encoding='utf-8') as file:
                for stock in res:
                    file.write(f'{stock[0]}, {stock[1]}\n')
        except FileNotFoundError:
            print('无法打开指定的文件!')
        except LookupError:
            print('指定了未知的编码!')
        except UnicodeDecodeError:
            print('读取文件时解码错误!')

def saveSampleRes(msg):
    if settings.config['save']['enable']:
        today = time.strftime("%Y-%m-%d", time.localtime()) 
        try:
            with open(f'{Constants.SAMPLE_PREFIX}:{today}.csv','a+', encoding='utf-8') as file:
                file.write(msg)
        except FileNotFoundError:
            print('无法打开指定的文件!')
        except LookupError:
            print('指定了未知的编码!')
        except UnicodeDecodeError:
            print('读取文件时解码错误!')





'''
保存文件

合法的mode
r、rb、r+、rb+、w、wb、w+、wb+、a、ab、a+、ab+
'''
