# Library imports
import webapp2
import jinja2
import os
import time
import datetime
import calendar
import unittest

from user import *
from google.appengine.ext import ndb
from google.appengine.ext import testbed

JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
autoescape=True)

class Logout(webapp2.RequestHandler):
    def get(self):
        self.response.delete_cookie('CurrentUser')
        users = User.query().fetch()
        for user in users:
        	for lec in user.lectures:
        		print(lec)
        		print("\n")
        self.redirect("/")
