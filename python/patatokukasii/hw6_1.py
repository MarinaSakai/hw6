#!/usr/bin/env python
# -*- coding: utf-8 -*-

import webapp2
import os
import jinja2
import cgi

JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

class BaseHandler(webapp2.RequestHandler):
    def render(self, html, values={}):
        template = JINJA_ENVIRONMENT.get_template(html)
        self.response.write(template.render(values))

class MainHandler(BaseHandler):
    def get(self):
        self.render("hw6_1.html")

class SubHandler(BaseHandler):
    def get(self):
        self.render("hw6_1_result.html")
        word1 = cgi.escape(self.request.get("word1"))
        word2 = cgi.escape(self.request.get("word2"))
        word1_list = list(word1)
        word2_list = list(word2)
        result = ""

        if len(word1_list) > len(word2_list):
            longer = len(word1_list)
            shorter = len(word2_list)
            longword = word1_list
        else:
            longer = len(word2_list)
            shorter = len(word1_list)
            longword = len(word2_list)

        for index in range(shorter):
            result +=(word1_list[index] + word2_list[index])

        for index in range(shorter, longer):
            result += longword[index]

        self.response.out.write(result)

app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/sub', SubHandler)
], debug=True)
