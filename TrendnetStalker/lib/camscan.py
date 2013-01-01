# -*- coding: utf-8 -*-

from urllib2 import urlopen, URLError
from socket import timeout

from shodan import WebAPI


class CamScanner(object):
    filter = 'netcam'

    def __init__(self, shodan_api_key):
        self.api_key = shodan_api_key
        self.api = WebAPI(self.api_key)

    def cam_available(self, url):
        try:
            resp = urlopen(url, None, 10)
        except URLError:
            print "Failed to contact cam: %s" % url
            return False
        else:
            if resp.code == 200:
                return True
            print "Bad resp code: %d" % resp.code
            return False

    def get_cams(self):
        results = self.api.search(self.filter)
        total_pages = (results['total'] / 50) + 1
        current_page = 1
        skip = False
        while current_page <= total_pages:
            if not skip:
                for result in results['matches']:
                    url = "http://%s/anony/mjpg.cgi" % result['ip']
                    if self.cam_available(url):
                        yield url, result.get('latitude'), result.get('latitude')
            current_page += 1
            try:
                results = self.api.search(self.filter, page=current_page)
            except URLError:
                print "Failed to GET page %d" % current_page
                skip = True
