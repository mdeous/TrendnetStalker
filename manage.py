#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask.ext.script import Command, Manager

from TrendnetStalker import app, settings


class Tornado(Command):
    """
    Starts the application using the Tornado web server.
    """
    def run(self):
        from tornado.httpserver import HTTPServer
        from tornado.ioloop import IOLoop
        from tornado.wsgi import WSGIContainer
        http_server = HTTPServer(WSGIContainer(app))
        http_server.listen(8000, address='*')
        IOLoop.instance().start()


class SyncDB(Command):
    """
    Create the database tables.
    """
    def run(self):
        from TrendnetStalker.models import Camera, Comment, Tag, CameraTag
        Camera.create_table(fail_silently=True)
        Comment.create_table(fail_silently=True)
        Tag.create_table(fail_silently=True)
        CameraTag.create_table(fail_silently=True)
#        cameras = [
#            ('http://62.31.202.38:80/anony/mjpg.cgi', 53.41669999999999, -3.0),
#            ('http://98.196.232.179:80/anony/mjpg.cgi', 29.544700000000006, -95.337),
#            ('http://187.153.107.160:80/anony/mjpg.cgi', 20.50829999999999, -86.9458)
#        ]
#        for url, lat, lng in cameras:
#            camera = Camera.create(url=url, lat=lat, lng=lng)


class UpdateDB(Command):
    def run(self):
        from TrendnetStalker.lib.updater import update_cams
        update_cams(settings.SHODAN_API_KEY)

manager = Manager(app)
manager.add_command('tornado', Tornado())
manager.add_command('syncdb', SyncDB())
manager.add_command('updatedb', UpdateDB())
manager.run()
