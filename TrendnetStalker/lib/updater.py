# -*- coding: utf-8 -*-

from sqlite3 import IntegrityError

from TrendnetStalker import Camera
from TrendnetStalker.lib.camscan import CamScanner


def update_cams(api_key):
    scanner = CamScanner(api_key)
    for url, lat, lng in scanner.get_cams():
        try:
            cam = Camera.create(url=url, lat=lat, lng=lng)
        except IntegrityError:
            print "Cam already exists: %r" % url
            continue
        else:
            print "Added new camera: %r" % url
