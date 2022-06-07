import json
import os
from pysnowball import cons
from pysnowball import api_ref
from pysnowball import utls
import time
from datetime import datetime


def _kline_with_period(symbols, period, count=-5000):
    curr_time = int(time.mktime(datetime.now().timetuple()))*1000
    url = api_ref.kline.format(symbol=symbols, begin=curr_time, period=period, type='before', count=count)

    return utls.fetch(url)


def kline_day(symbol, **kwargs):
    return _kline_with_period(symbol, 'day')

def kline_week(symbol, **kwargs):
    return _kline_with_period(symbol, 'week')
