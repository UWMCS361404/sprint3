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

        CurrentUser = getAccount(self.request.cookies.get("CurrentUser"))
        student = User.query(User.Name == CurrentUser.Name).get()

        template = JINJA_ENVIRONMENT.get_template('Html/stdc.html')
        #QL = list(Question.query())
        #LL = list(Lecture.query())
        LL = []
        for lecName in student.lectures:
            LL.append(Lecture.query(Lecture.name==lecName).get())                      # get lecture from name
        QL = Question.query(Question.student == student.Name).fetch()


        template_values = {
            "CurrentUser" : student,
            "QL" : QL,
            "LL": LL,
        }
        self.response.write(template.render(template_values))

    def post(self):
        question = Question()
        question.owner= self.request.cookies.get("CurrentUser")
        question.topic = self.request.get("topic")
        question.content = self.request.get("content")
        question.lec = self.request.get("class")
        question.time = datetime.datetime.now()
        question.answered = False
        question.message=[]

        lecture = self.request.get("lecture")

        question.put()
        self.redirect("/studentcenter" + "?quest" + self.request.get("Quest"))
