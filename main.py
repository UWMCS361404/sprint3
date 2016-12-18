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
parseUserString("es, Edward, 123, s\n") # Changed dummy names to mach their account type
parseUserString("rdsi, Bob, 321, i\n")
parseUserString("ksra, Kyle, asdf, a\n")

app = webapp2.WSGIApplication([
	('/', Login),
	('/createLecture', CreateLecture),
	('/createUsers', CreateUsers),
	('/enroll', Enroll),
	('/admin', AdminPage),
	('/logout', Logout),
    ('/studentcenter', StudentCenter),
    ('/instructorcenter', InstructorCenter),
	('/chat', Chat),
	('/faq', FAQ),
	('/response', Response),

])

# # Unit tests
# suite = unittest.TestLoader().loadTestsFromTestCase(Test)
# unittest.TextTestRunner().run(suite)
