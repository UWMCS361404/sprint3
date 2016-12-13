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
from user import *
from util import *

class InstructorCenter(webapp2.RequestHandler):
    def get(self):
        CurrentUser = getAccount(self.request.cookies.get('CurrentUser'))
        print("test one")
        print(CurrentUser)
        print("test two")
        print(CurrentUser.Name)
        # idk if the next line is relevent or not. it seems I'm getting an outdated 'CurrentUser' unless I do this.
        instructor = User.query(User.Name == CurrentUser.Name).get()
        QL = []
        SL = []
        LL = instructor.lectures

        #QL.append(Question.query(Question.lec == 'cs361').fetch())
        for lecName in instructor.lectures: # this is a list of Lecture names
            lec = Lecture.query(Lecture.name==lecName).get()                         # get lecture from name
            for QuestionKey in lec.QL:
                key = ndb.Key(urlsafe=QuestionKey)       # construct key
                QL.append(key.get())                    #append QL with
            for name in lec.userNames:
                if not SL.contains(username):
                    SL.append(username)

        # for lecName in instructor.lectures:
        #     lec = Lecture.query(Lecture.name==lecName).get()                         # get lecture from name
        #     for name in lec.userNames:
        #         if not SL.contains(username):
        #             SL.append(username)

        template = JINJA_ENVIRONMENT.get_template('Html/insc.html')
        template_values = {
            "CurrentUser": CurrentUser.userName,
            'QL': QL,
            'SL': SL,
            'LL': LL
        }
        self.response.write(template.render(template_values))

    def post(self):
        q = Question()
        q.time = datetime.datetime.now()
        q.owner = self.request.get('Student')
        q.topic = self.request.get('topic')
        q.content = self.request.get('content')
        q.answered = False
        q.lec = self.request.get('')
        q.put()
        self.redirect('/instructorcenter')

    def goToChat(self):
        print('entering goToChat')
        questionKeyString = self.request.get('Quest')
        print('printing key string')
        print(questionKeyString)
        questionKey = ndb.Key(urlsafe=questionKeyString)
        question = questionKey.get()
        print('printing topic')
        print(question.topic)
        template_values = {
             'user'
        }
