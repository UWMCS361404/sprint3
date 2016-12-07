import webapp2
import jinja2
import os
import time
import datetime
import calendar
import unittest

from google.appengine.ext import ndb
from google.appengine.ext import testbed

#JINJA_ENVIRONMENT = jinja2.Environment(
#    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
#    extensions=['jinja2.ext.autoescape'],
#autoescape=True)

class FAQ(webapp2.RequestHandler):
    def get(self):
        template = JINJA_ENVIRONMENT.get_template('faq.html')
        user = self.request.cookies.get("CurrentUser")

        faqs = list(questionAnswer.query().order(questionAnswer.heading, -questionAnswer.heading))

        template_values = {
            "user": getAccount(user, userList),
            "faqs": faqs
        }

        self.response.write(template.render(template_values))

    def post(self):

        if self.request.get("heading") == "" or self.request.get("question") == "" or self.request.get("answer") == "":
            user = self.request.cookies.get("CurrentUser")
            self.redirect("/messcenter?user=" + user)

        else:

            qa = questionAnswer(heading=self.request.get("heading"), question=self.request.get("question"), answer=self.request.get("answer"))
            qa.put()

            user = self.request.cookies.get("CurrentUser")
            self.redirect("/messcenter?user=" + user)
