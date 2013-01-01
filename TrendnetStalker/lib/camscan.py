# -*- coding: utf-8 -*-

from urllib2 import urlopen, URLError

from shodan import WebAPI


class CamScanner(object):
    filter = 'netcam'

    def __init__(self, shodan_api_key):
        self.api_key = shodan_api_key
        self.api = WebAPI(self.api_key)

    def cam_available(self, url):
        try:
            resp = urlopen(url)
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
                        yield url, result['latitude'], result['longitude']
            current_page += 1
            try:
                results = self.api.search(self.filter, page=current_page)
            except URLError:
                print "Failed to GET page %d" % current_page
                skip = True



#def checkCam(ip):
#    try:
#        sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#        sock.settimeout(1.5)
#        sock.connect((ip,80))
#        sock.send('GET /anony/mjpg.cgi HTTP/1.0\r\n\r\n')
#        res = sock.recv(100)
#        if res.find('200 OK'):
#            return True
#        return False
#    except socket.error:
#        return False
#
#
#api = WebAPI(key)
#
##get the first page of results
#res = api.search(filter)
#
##keep track of how many results we have left
#total_pages = (res['total']/50)+1
#page = 1
#
#outfile = open('camlog_new','w')
#
#try:
#    while page <= total_pages:
#        #check the matches to see if they fit what we are looking for
#        for r in res['matches']:
#            #if(r['data'].find(filter)>0):
#            print 'Checking %s' % r['ip']
#            if checkCam(r['ip']):
#                print 'Found http://%s/anony/mjpg.cgi' % r['ip']
#                f = 'http://%s/anony/mjpg.cgi\n' % r['ip']
#                outfile.write(f)
#                outfile.flush()
#
#        page += 1
#        res = api.search(filter,page)
#except:
#    print 'fail'
#
#file.close()

