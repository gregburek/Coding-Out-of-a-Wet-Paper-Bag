import cgi
import datetime
import urllib
import wsgiref.handlers

from google.appengine.ext import db
from google.appengine.api import users
from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app

class Greeting(db.Model):
    """Models an individual Guestbook entry with an author, content, and
    date."""
    author = db.UserProperty()
    content = db.StringProperty(multiline=True)
    date = db.DateTimeProperty(auto_now_add=True)


def guestbook_key(guestbook_name=None):
    """Constructs a datastore key for a guestbook entity with
    guestbook_name."""
    return db.Key.from_path('Guestbook', guestbook_name or 'default_guestbook')



class MainPage(webapp.RequestHandler):
    def get(self):
        self.response.out.write('<html><body>')
        guestbook_name=self.request.get('guestbook_name')

        # Ancestor Queries rule
        greetings = db.GqlQuery("SELECT *"
                                "FROM Greeting "
                                "WHERE ANCESTOR IS :1 "
                                "ORDER BY date DESC LIMIT 10",
                                guestbook_key(guestbook_name))

        for greeting in greetings:
            if greeting.author:
                self.response.out.write(
                        '<b>%s</b>:' % greeting.author.nickname())
            else:
                self.response.out.write('An Anon person wrote:')
            self.response.out.write('<blockquote>%s</blockquote>' % 
                        cgi.escape(greeting.content))

        self.response.out.write("""
                    <form action="/sign?%s" method="post">
                    <div><textarea name="content" rows="3"
                    cols="60"></textarea></div>
                    <div><input type="submit" value="Sign Guestbook"></div>
                    </form>
                    <hr>
                    <form>Guestbook name: <input value="%s"
                    name="guestbook_name">
                    <input type="submit" value="switch"></form>
                    </body>
                    </html>""" % (urllib.urlencode({'guestbook_name':guestbook_name}),
                        cgi.escape(guestbook_name)))

class Guestbook(webapp.RequestHandler):
    def post(self):
        guestbook_name = self.request.get('guestbook_name')
        greeting = Greeting(parent=guestbook_key(guestbook_name))

        if users.get_current.user():
            greeting.author = users.get_current_user()

        greeting.content = self.request.get('content')
        greeting.put()
        self.redirect('/?' + urllib.encode({'guestbook_name': guestbook_name}))


application = webapp.WSGIApplication([('/', MainPage),
                                      ('/sign', Guestbook)],
                                     debug=True)

def main ():
    run_wsgi_app(application)

if __name__ == "__main__":
    main()

