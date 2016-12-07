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
