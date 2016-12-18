import webapp2
import jinja2
import os
import time
import datetime
import calendar
import unittest
from faq import *

from google.appengine.ext import ndb

class questionAnswer(ndb.Model):
    question = ndb.StringProperty()
    answer = ndb.StringProperty()

class Topic(ndb.Model):
    heading = ndb.StringProperty()
    QAs = ndb.StructuredProperty(questionAnswer, repeated=True)


    def getQuestion(self):
        return self.question

    def getAnswer(self):
        return self.answer


    def parseQAString(string):

        subStr = string

        while subStr != "":
            heading = subStr[:subStr.find(",")].strip() # We assume that the string does not begin with a comma


            #if len(list(User.query(User.Name == userName))) != 0:
            #   return 'User name already exists.'

            #print("Loop")

            subStr = subStr[subStr.find(",") + 1:] # Move the sub string forward
            question = subStr[:subStr.find(",")].strip() # Get data

            subStr = subStr[subStr.find(",") + 1:] # Move the sub string forward
            answer = subStr[:subStr.find(",")].strip() # Get data

            topic = Topic.query(FaqTopic.heading==heading).get()
            if topic == None:
                topic = Topic()
                topic.heading = heading
                topic.QAs = []
            qa = questionAnswer()
            qa.question = question
            qa.answer = answer
            topic.QAs.append(qa)
            qa.put()
            topic.put()


            faq.put() # Put to the data store
            subStr = subStr[subStr.find("\n") + 1:] # Equivalent to readline, this just moves to the next line of text


class makeFAQ(webapp2.RequestHandler):
    def post(self):
        inputText = self.request.get("inputText")
        faqStrings = inputText.split('\n')
        print("\n\t\t in class Create far method post")

        for faq in faqStrings:
            parseQAString(faq)
            print("\n\t\tMADE User" + faq + '\n')
        self.redirect("/faq")
