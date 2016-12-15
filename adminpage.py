# Library imports
import webapp2
import jinja2
import os
import time
import datetime
import calendar
import unittest

from util import *
from user import *

from google.appengine.ext import ndb
from google.appengine.ext import testbed

JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
autoescape=True)


class AdminPage(webapp2.RequestHandler):
    def get(self):
        users = User.query().fetch()
        lectures = Lecture.query().fetch()
        template = JINJA_ENVIRONMENT.get_template('/Html/admin.html')

        template_values = {
            "users": users,
            "lectures": lectures,
        }
        self.response.write(template.render(template_values))

class CreateLecture(webapp2.RequestHandler):
    def post(self):
        lec = Lecture()
        lec.name = self.request.get('lecName')
        lec.userNames = []
        lec.QL = []
        lec.put()
        self.redirect("/admin")

class CreateUsers(webapp2.RequestHandler):
    def post(self):
        userText = self.request.get("userText")
        users = userText.split('/n')
        print("\n\t\t in class CreateUsers method post")

        for user in users:
            parseUserString(user)
            print("\n\t\tMADE User" + user + '\n')
        self.redirect("/admin")

class Enroll(webapp2.RequestHandler):
    def post(self):
        print("in enroll post")
        users = self.request.get_all("users")
        lectures = self.request.get_all("lectures")
        print(users)
        for lec in lectures:
            print("lec = ")
            print(lec)
            currentLec = Lecture.query(Lecture.name==lec).get()
            print("currentLec =")
            print(currentLec)
            for user in users:
                print("user=")
                print(user)
                currentUser = User.query(User.Name==user).get()
                print("currentuser = ")
                print(currentUser)
                currentLec.userNames.append(currentUser.Name)
                currentUser.lectures.append(currentLec.name)
                print("final currentLec =")
                print(currentLec)
                print("final currentuser = ")
                print(currentUser)
                currentLec.put()
                currentUser.put()
        self.redirect("/admin")
