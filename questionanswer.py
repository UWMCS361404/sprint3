from google.appengine.ext import ndb

class questionAnswer(ndb.Model):
    
    heading = ndb.StringProperty()
    question = ndb.StringProperty()
    answer = ndb.StringProperty()
    
    def getHeading(self):
        return self.heading
        
    def getQuestion(self):
        return self.question
        
    def getAnswer(self):
        return self.answer


    def parseUserString(string):
    
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
            
        faq = questionanswer()
    
        faq.heading = heading
        faq.question = question
        faq.answer = answer
        
        
        faq.put() # Put to the data store
        subStr = subStr[subStr.find("\n") + 1:] # Equivalent to readline, this just moves to the next line of text


class makeFAQ(webapp2.RequestHandler):
    def post(self):
        inputText = self.request.get("inputText”)
        faqs = inputText.split('/n')
        print("\n\t\t in class Create far method post")
        
        for faq in faqs:
            parseUserString(faq)
            print("\n\t\tMADE User" + faq + '\n')
        self.redirect("/faq”)



