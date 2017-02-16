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
'''

page_footer = '''
</body>
</html>
'''

USER_RE = re.compile(r"^[a-zA-Z0-9_-]{3,20}$")
def valid_username(username):
    return username and USER_RE.match(username)

PASS_RE = re.compile(r"^.{3,20}$")
def valid_password(password):
    return password and PASS_RE.match(password)

EMAIL_RE = re.compile(r"^[\S]+@[\S]+.[\S]+$")
def valid_email(email):
    return email and EMAIL_RE.match(email)

error_messages = ["That's not a valid username",
"That's not a valid password",
"Passwords don't match",
"That's not a valid email"
]



def build_form(username_input,email_input,error_username,error_password,error_match,error_email):

    signup_header = "<h1>Signup</h1>"

    signup_form = '''
    <form method='post'>
    <table>
        <tr>
        <td><label>Username</label></td>
        <td><input name='username' type='text' value="'''+username_input+'''" required/></td>
        <td><span class='error'>'''+error_username+'''</span></td>
        </tr>

        <tr>
        <td><label>Password</label></td>
        <td><input name='password' type='password' required/></td>
        <td><span class='error'>'''+error_password+'''</span></td>
        </tr>

        <tr>
        <td><label>Verify Password</label></td>
        <td><input name='verify' type='password' required/></td>
        <td><span class='error'>'''+error_match+'''</span></td>
        </tr>

        <tr>
        <td><label>Email (optional)</label></td>
        <td><input name='email' type='email' value="'''+email_input+'''"/></td>
        <td><span class='error'>'''+error_email+'''</span></td>
        </tr>
    </table>
    <input type='submit'>

    '''

    return page_header + signup_header + signup_form + page_footer

class Signup(webapp2.RequestHandler):

    def get(self):


        error_username = ""
        error_password = ""
        error_match = ""
        error_email = ""



        # username_label = "<label>Username</label>"
        # username = "<input name='username' type='text' required/>"
        #
        # password_label = "<label>Password</label>"
        # password = "<input name='password' type='password' required/>"
        #
        # verify_label = "<label>Verify Password</label>"
        # verify = "<input name='verify' type='password' required/>"
        #
        # email_label = "<label>Email (optional)</label>"
        # email = "<input name='email' type='email' />"

        # submit = "<input type='submit' action=/>"


        # form = ("<form method='post'>" +
        #         username_label + username + "<span class='error' id='error_username'></span>" + "<br>" +
        #         password_label + password + "<span class='error' id='error_password'></span>" + "<br>" +
        #         verify_label + verify + "<span class='error' id='error_match'></span>" + "<br>" +
        #         email_label + email + "<span class='error' id='error_email'></span>" + "<br>" +
        #         submit + "</form>"
        #         )



        # error = self.request.get('error')
        # error_element = "<p class='error'>" + error + "</p>" if error else ""

        # main_content = form

        content = build_form("","","","","","")

        self.response.write(content)

    def post(self):
        username = self.request.get("username")
        password = self.request.get("password")
        verify = self.request.get("verify")
        email = self.request.get("email")

        name_err = ""
        pass_err = ""
        match_err = ""
        email_err = ""

        errors = False

        if not valid_username(username):
            name_err += error_messages[0]
            errors = True

        if not valid_password(password):
            pass_err += error_messages[1]
            errors = True

        if password != verify:
            match_err += error_messages[2]
            errors = True

        if len(email) > 0:
            if not valid_email(email):
                email_err += error_messages[3]
                errors = True

        if errors == False:
            self.redirect('/welcome?username=' + username)
        if errors == True:
            error_codes = build_form(username,email,name_err,pass_err,match_err,email_err)
            self.response.write(error_codes)




class Welcome(webapp2.RequestHandler):
    def get(self):
        username = self.request.get('username')
        greeting = "Welcome, " + username + "!"
        content = page_header + "<h1>"+greeting+"</h1>" + page_footer
        self.response.write(content)





app = webapp2.WSGIApplication([
    ('/', Signup),
    ('/welcome', Welcome)
], debug=True)
