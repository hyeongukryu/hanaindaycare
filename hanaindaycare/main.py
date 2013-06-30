# -*- coding: utf-8 -*-

import os, datetime, base64
import webapp2, jinja2

# Jinja2 템플릿
template_dir = os.path.join(os.path.dirname(__file__), 'template')

jinja2_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir), autoescape = True)

def render_template(template_name):
    return jinja2_env.get_template(template_name + '.html').render(nav=template_name)



class HomeHandler(webapp2.RequestHandler):
    def get(self):
        self.response.out.write(render_template('home'))

class InfoHandler(webapp2.RequestHandler):
	def get(self):
		self.response.out.write(render_template('info'))

class AdmissionHandler(webapp2.RequestHandler):
	def get(self):
		self.response.out.write(render_template('admission'))

class GuideHandler(webapp2.RequestHandler):
	def get(self):
		self.response.out.write(render_template('guide'))

class MapHandler(webapp2.RequestHandler):
	def get(self):
		self.response.out.write(render_template('map'))



app = webapp2.WSGIApplication([
    ('/', HomeHandler),
    ('/info', InfoHandler),
    ('/admission', AdmissionHandler),
    ('/guide', GuideHandler),
    ('/map', MapHandler)
], debug=True)
