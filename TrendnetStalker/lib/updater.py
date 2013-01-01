# -*- coding: utf-8 -*-

from TrendnetStalker import Camera
from TrendnetStalker.lib.camscan import CamScanner


def update_cams(api_key):
    scanner = CamScanner(api_key)
    for url, lat, lng in scanner.get_cams():
        cam = Camera.create(url=url, lat=lat, lng=lng)
        print "Added new camera: %r" % url
