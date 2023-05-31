# -*- encoding: UTF-8 -*-

import schedule
import utils
import logging
import work_flow
import settings
import schedule
import time

from threading import Thread
import talib as tl

settings.init()
logging.basicConfig(format='%(asctime)s %(message)s', filename='sequoia.log')
logging.getLogger().setLevel(logging.INFO)


def job():
    if utils.is_weekday():
        work_flow.process()

if settings.config['cron']:
    EXEC_TIME = "15:15"
    schedule.every().day.at(EXEC_TIME).do(job)

    while True:
        schedule.run_pending()
        time.sleep(1)
else:
    work_flow.process()
