# Library imports
import webapp2
import jinja2
import os
import time
import datetime
import calendar
import unittest

from message import *
from question import *
from user import *
from util import *

from google.appengine.ext import ndb
from google.appengine.ext import testbed

# get question from url string from request Quest
#         student = ndb.StringProperty()
#         topic = ndb.StringProperty()
#         lec = ndb.StringProperty()
#         time = ndb.DateTimeProperty()
#         answered = ndb.BooleanProperty()
#         ML = ndb.StructuredProperty(Message, repeated=True)


class Chat(webapp2.RequestHandler):
    def get(self):
        template = JINJA_ENVIRONMENT.get_template('Html/chat.html')
        qString = self.request.get("Quest")
        CurrentUser = self.request.cookies.get("CurrentUser")
        qKey = ndb.Key(urlsafe=qString)
        q = qKey.get()
        template_values = {
            "q": q,
            "CurrentUser": CurrentUser,
        }
        self.response.write(template.render(template_values))




    # content = ndb.StringProperty()
    # name = ndb.StringProperty()
    # time = ndb.DateTimeProperty(auto_now_add=True)

    def post(self):
        if self.request.get("message").strip() == "":
            user = self.request.cookies.get("CurrentUser")
            self.redirect("/chat")
        else:
            print("\n\n in else statement")
            key_str = self.request.get("quest")
            print(key_str)
            print("in else statement after requesting \"quest\" \n\n")
            my_key = ndb.Key(urlsafe=key_str)
            q = ndb.Key(urlsafe=my_key).get()
            #q = qKey.get()
            #need to get question put new message in ML
            content = self.request.get("content")
            user = self.request.cookies.get("CurrentUser")
            m = Message()
            m.content = content
            m.name = user
            m.put()
            q.ML.append(m)
            q.put()
            time.sleep(1)
            self.redirect("/chat")
