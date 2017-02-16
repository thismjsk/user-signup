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

page_header = '''
<!DOCTYPE html>
<html>
<head>
    <title>User Signup</title>
    <style type="text/css">
        .error {
            color: red;

        }
    </style>
</head>
<body>
    <h1>Signup</h1>

</body>
</html>

'''

# # TODO 1
#     #The user does not enter a username
#     # used input type 'required'
#
# # TODO 2
#     # The user's username is not valid -- for example, contains a space character. Full spec is included in the notes underneath the video.
#
USER_RE = re.compile(r"^[a-zA-Z0-9_-]{3,20}$")
def valid_username(username):
    return username and USER_RE.match(username)

PASS_RE = re.compile(r"^.{3,20}$")
def valid_password(password):
    return password and PASS_RE.match(password)

def valid_match(password,verify):
    if password == verify:
        return True
    else:
        return False

EMAIL_RE = re.compile(r"^[\S]+@[\S]+.[\S]+$")
def valid_email(email):
    return email and EMAIL_RE.match(email)

#
# # TODO 3
#     # The user's password and password-confirmation do not match
#
# if password != verify:
#     error_match = "Passwords don't match"
#
# # TODO 4
#     # The user provides an email, but it's not a valid email.
#     # used input type 'email'




class Signup(webapp2.RequestHandler):

    def get(self):


        username_label = "<label>Username</label>"
        username = "<input name='username' type='text' required/>"

        password_label = "<label>Password</label>"
        password = "<input name='password' type='password' required/>"

        verify_label = "<label>Verify Password</label>"
        verify = "<input name='verify' type='password' required/>"

        email_label = "<label>Email (optional)</label>"
        email = "<input name='email' type='email' />"

        submit = "<input type='submit' action=/>"


        form = ("<form method='post'" +
                username_label + username + "<br>" +
                password_label + password + "<br>" +
                verify_label + verify + "<br>" +
                email_label + email + "<br>" +
                submit + "</form>"
                )


        error = self.request.get('error')
        error_element = "<p class='error'>" + error + "</p>" if error else ""

        main_content = form + error_element
        content = page_header + main_content

        self.response.write(content)

    def post(self):
        username = self.request.get("username")

        password = self.request.get("password")

        verify = self.request.get("verify")

        email = self.request.get("email")

        if not valid_username(username):
            error_username = "That's not a valid username"
            self.redirect("/?error="  + error_username)

        if not valid_password(password):
            error_password = "That's not a valid password"
            self.redirect("/?error="  + error_password)

        if not valid_match(password,verify):
            error_match = "Passwords don't match"
            self.redirect("/?error="  + error_match)

        else:
            self.redirect('/welcome?username=' + username)





class Welcome(webapp2.RequestHandler):
    def get(self):
        username = self.request.get('username')
        if valid_username(username):
            self.response.write("Welcome, " + username + "!")
        else:
            self.response.write('this is the else')





app = webapp2.WSGIApplication([
    ('/', Signup),
    ('/welcome', Welcome)
], debug=True)
