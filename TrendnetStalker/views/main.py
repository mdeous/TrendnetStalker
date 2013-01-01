# -*- coding: utf-8 -*-

from flask import Blueprint, render_template

from TrendnetStalker.models import Camera

main = Blueprint('main', __name__)

@main.route('/')
def index():
    cameras = Camera.select()
    return render_template('index.html', cameras=cameras)
