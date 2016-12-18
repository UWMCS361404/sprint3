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
from util import *
from message import *

class Chat(webapp2.RequestHandler):
    def get(self):
        template = JINJA_ENVIRONMENT.get_template('Html/chat.html')
        
        user = getAccount(self.request.cookies.get("CurrentUser"))
        messages = list(Message.query().order(Message.time, -Message.time))
        chatKey = "/chat?Quest=" + self.request.get("Quest")
                
        question = ndb.Key(urlsafe=self.request.get("Quest")).get()
        messages = list(question.ML)

        accounts = []
        
        for i in range(len(messages)):
            accounts.append(getAccount(messages[i].name))

        template_values = {
            "user": user,
            "messages": messages,
            "chatKey": chatKey,
            "size": len(messages),
            "accounts": accounts
        }

        self.response.write(template.render(template_values))
        
    def post(self):
        if self.request.get("message").strip() == "":
            user = self.request.cookies.get("CurrentUser")
            self.redirect("/chat")
        else:
            content = self.request.get("message")
            user = self.request.cookies.get("CurrentUser")
            
            message = Message()
            message.content = content
            message.name = user
            message.time = datetime.datetime.now()
            
            question = ndb.Key(urlsafe=self.request.get("Quest"))
            question = question.get()
            question.ML.append(message)
            question.put()
            
            self.redirect("/chat?Quest=" + self.request.get("Quest"))
