# -*- coding: utf-8 -*-

from sqlite3 import IntegrityError

from TrendnetStalker.models import UnlocatedCamera, Camera
from TrendnetStalker.lib.camscan import CamScanner


def update_cams(api_key):
    scanner = CamScanner(api_key)
    for url, lat, lng in scanner.get_cams():
        model = UnlocatedCamera if (lat is None) or (lng is None) else Camera
        model_kwargs = {'url': url}
        if (lat is not None) and (lng is not None):
            model_kwargs['lat'] = lat
            model_kwargs['lng'] = lng
        try:
            model.create(**model_kwargs)
        except IntegrityError:
            print "Cam already exists: %r" % url
            continue
        else:
            print "Added new %scamera: %r" % (
                'unlocated ' if (lat is None) or (lng is None) else '',
                url
            )
