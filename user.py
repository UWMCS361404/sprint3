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

# User
#     Name is a unique name. On creation it cannot be in store
#     userName is Displayed to user on page
#     password is a string password
#     atype is a 1 character string "a", "i", or "s" for admin, instructor, or student
#     lecture is a list of unique lecture names

class User(ndb.Model):
    Name = ndb.StringProperty()
    userName = ndb.StringProperty()
    password = ndb.StringProperty()
    aType = ndb.StringProperty()
    lectures = ndb.StringProperty(repeated=True)
    #lectures = ndb.StructuredProperty(Lecture, repeated=True)

    def toString(self):
        s= ("("+self.name + (",") + self.userName + (",") + self.password + (",") + self.aType + (",") + ("{") )

        # Old version
        #for i in self.Lectures.length():
        #    s.append(i.Name)
        #    s.append(";")

        # To be tested
        #s.append(str(Lectures))
        s.append("}")
        s.append(")")
        return s
