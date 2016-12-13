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
from login import *
from chat import *
from adminpage import *
from instructorcenter import *
from lecture import *
from logout import *
from message import *
from question import *
from studentcenter import *
from user import *
from test import *
from util import *
from faq import *
from questionanswer import *

# end touples need to be fixed so they have logout and adminpage
#userList = parseTxt("accounts.csv")
parseUserString("ed, Edward, 123, i\n")
parseUserString("al, Albert, 321, s\n")


lec = Lecture()
lec.name = "CS001"
lec.userNames = []
lec.userNames.append("ed")
lec.userNames.append("al")
lec.QL = []
lec.put()



mess = Message()
mess.content = "Q1, M1"
mess.time = datetime.datetime.now()
mess.name = "ed"


quest = Question()
quest.topic = "Q1"
quest.student = 'ed'
quest.lec = 'CS001'
quest.messageList = []
quest.time = datetime.datetime.now()


student = ndb.StringProperty()
topic = ndb.StringProperty()
lec = ndb.StringProperty()
time = datetime.datetime.now()
messageList = ndb.StructuredProperty(Message, repeated=True)



app = webapp2.WSGIApplication([
	('/', Login),
	('/admin', AdminPage),
	('/logout', Logout),
    ('/studentcenter', StudentCenter),
    ('/instructorcenter', InstructorCenter),
	('/chat', Chat),
	('/faq', FAQ)
])

# Unit tests
suite = unittest.TestLoader().loadTestsFromTestCase(Test)
unittest.TextTestRunner().run(suite)
