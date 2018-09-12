#!/usr/bin/env python3

from flask import Flask, session

from .controllers.general import controller as general_controller

omnibus = Flask(__name__)
omnibus.secret_key = "super secret"

omnibus.register_blueprint(general_controller)
