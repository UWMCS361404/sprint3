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

# get question from url string from request Quest
#         student = ndb.StringProperty()
#         topic = ndb.StringProperty()
#         lec = ndb.StringProperty()
#         time = ndb.DateTimeProperty()
#         answered = ndb.BooleanProperty()
#         ML = ndb.StructuredProperty(Message, repeated=True)
#
JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
autoescape=True)



class Chat(webapp2.RequestHandler):
    def get(self):
        template = JINJA_ENVIRONMENT.get_template('Html/chat.html')
        qString = self.request.get("Quest")
        print(q)
        CurrentUser = self.request.cookies.get("CurrentUser")
        qKey = ndb.Key(url_safe=qString)
        q = qKey.get()

        # student = self.request.get("student")
        # user = self.request.cookies.get("CurrentUser")
        # if student == "":
        #     student = getInstrAccount(userList).getName()
        # self.response.set_cookie("receiver", student)
        # messages = list(Message.query().order(Message.time, -Message.time))
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
            #need to get question put new message in ML
            content = self.request.get("content")
            user = self.request.cookies.get("CurrentUser")
            m = Message()
            m.content = content
            m.name = user
            message.put()
            if q.ML == None:
                q.ML = []
            q.ML.append(m)
            q.put()
            time.sleep(1)
            self.redirect("/chat")
