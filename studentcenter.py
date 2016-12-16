# Library imports
import webapp2
import jinja2
import os
import time
import datetime
import calendar
import unittest

from google.appengine.ext import ndb
from google.appengine.ext import testbed

# Project imports
from lecture import *
from user import *
from util import *
from question import *

class StudentCenter(webapp2.RequestHandler):
    def get(self):
        currentUser = self.request.cookies.get("CurrentUser")
        student = User.query(User.Name == currentUser).get()
        template = JINJA_ENVIRONMENT.get_template('Html/stdc.html')
        LL = student.lectures
        QL = []
        for lecName in student.lectures:
            lec = Lecture.query(Lecture.name==lecName).get()
            for QuestionKey in lec.QL:
                key = ndb.Key(urlsafe=QuestionKey)
                q = key.get()
                QL.append(q)

        template_values = {
            "CurrentUser" : currentUser,
            "QL" : QL,
            "LL" : LL,
        }
        self.response.write(template.render(template_values))

    def post(self):
        q = Question()
        m = Message()
        q.student = self.request.cookies.get("CurrentUser")
        q.topic = self.request.get("topic")
        m.name = self.request.get("CurrentUser")
        m.content = self.request.get("content")
        q.lec = self.request.get("lecture")
        q.time = datetime.datetime.now()
        q.answered = False
        q.ML.append(m)
        lec = Lecture.query(Lecture.name==q.lec).get()
        key = q.put().urlsafe()
        if lec != None:
            if lec.QL == None:
                lec.QL = []
            lec.QL.append(key)
            m.put()
            q.put()
            lec.put()
        self.redirect('/studentcenter')
