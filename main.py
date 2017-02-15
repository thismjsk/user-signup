#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import webapp2
import re

contents = '''<!DOCTYPE html>
<html>
<head>
    <title>User Signup</title>
    <style type="text/css">
    .error {color: red}
    </style>
</head>

<body>

</body>
</html>

'''

USER_RE = re.compile(r"^[a-zA-Z0-9_-]{3,20}$")
def valid_username(username):
    return username and USER_RE.match(username)



class MainHandler(webapp2.RequestHandler):
    def get(self):

        username_label = "<label>Username</label>"
        username = "<input name='username' type='text' required/>"

        password_label = "<label>Password</label>"
        password = "<input name='password' type='password' required/>"

        verify_label = "<label>Verify Password</label>"
        verify = "<input name='verify' type='password' required/>"

        email_label = "<label>Email (optional)</label>"
        email = "<input name='email' type='email'/>"

        submit = "<input type='submit' action=/>"


        form = ("<form method='post'" +
                username_label + username + "<br>" +
                password_label + password + "<br>" +
                verify_label + verify + "<br>" +
                email_label + email + "<br>" +
                submit + "</form>"
                )


        header = "<h1>Signup</h1>"

        self.response.write(header + form)

    def post(self):
        username = self.request.get("username")
        password = self.request.get("password")
        verify = self.request.get("verify")
        email = self.request.get("email")

        if valid_username(username):
            self.redirect('/welcome?username=' + username)




class Welcome(webapp2.RequestHandler):
    def get(self):
        username = self.request.get('username')
        if valid_username(username):
            self.response.write("Welcome, " + username + "!")
        else:
            self.response.write('this is the else')





app = webapp2.WSGIApplication([
    ('/', MainHandler), ('/welcome', Welcome)
], debug=True)
