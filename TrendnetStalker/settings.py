# -*- coding: utf-8 -*-

SECRET_KEY = 'changeme'
DEBUG = True
DATABASE = 'TrendnetStalker.db'
SHODAN_API_KEY = ''

try:
    from TrendnetStalker.prod_settings import *
except ImportError:
    pass
