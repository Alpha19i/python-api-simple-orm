# -*- coding: utf-8 -*-
import os
from flask import Flask, request, jsonify, make_response
from flask_restful import Resource, Api
from json import dumps
from flask_cors import CORS, cross_origin
from modal import db, User, app, users_schema, user_schema
from flask_marshmallow import Marshmallow
