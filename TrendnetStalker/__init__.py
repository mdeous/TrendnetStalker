# -*- coding: utf-8 -*-

from flask import Flask, render_template

from TrendnetStalker import settings
from TrendnetStalker.models import Camera
from TrendnetStalker.views.main import main

app = Flask(__name__)
app.config.from_object(settings)

app.register_blueprint(main)
