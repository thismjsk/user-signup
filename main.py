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

class MainHandler(webapp2.RequestHandler):
    def get(self):
        username_label = "<label>Username</label>"
        username = "<input name='username'/>"

        password_label = "<label>Password</label>"
        password = "<input name='password'/>"

        verify_label = "<label>Verify Password</label>"
        verify = "<input name='verify'/>"

        email_label = "<label>Email (optional)</label>"
        email = "<input name='email'/>"

        submit = "<input type='submit'/>"


        form = ("<form method='post'>" +
                username_label + username + "<br>" +
                password_label + password + "<br>" +
                verify_label + verify + "<br>" +
                email_label + email + "<br>" +
                submit + "</form>"

        )


        self.response.write(form)

    def post(self):
        self.response.write(form)



app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
