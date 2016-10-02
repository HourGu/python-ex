# -*- coding: cp936 -*-
#HTML
from HTMLParser import HTMLParser
from htmlentitydefs import name2codepoint

class MyHTMLParser(HTMLParser):

    def handle_starttag(self, tag, attrs):
        print('<%s>' % tag)

    def handle_endtag(self, tag):
        print('</%s>' % tag)

    def handle_startendtag(self, tag, attrs):
        print('<%s/>' % tag)

    def handle_data(self, data):
        print('data')

    def handle_comment(self, data):
        print('<!-- -->')

    def handle_entityref(self, name):
        print('&%s;' % name)

    def handle_charref(self, name):
        print('&#%s;' % name)

parser = MyHTMLParser()
parser.feed('<html><head></head><body><p>Some <a href=\"#\">html</a> tutorial...<br>END</p></body></html>')

'''
>>> ================================ RESTART ================================
>>> 
<html>
<head>
</head>
<body>
<p>
data
<a>
data
</a>
data
<br>
data
</p>
</body>
</html>
>>> 
'''
##��ϰ
from HTMLParser import HTMLParser
import urllib

class MyHTMLParser(HTMLParser):

    def __init__(self):
        HTMLParser.__init__(self)
        self.key = {'time': None, 'event-title': None, 'event-location': None}

    def handle_starttag(self, tag, attrs):
        if tag == 'time':
            self.key['time'] = True
        elif tag == 'span' and attrs.__contains__(('class', 'event-location')):
            self.key['event-location'] = True
        elif tag == 'h3' and attrs.__contains__(('class', 'event-title')):
            self.key['event-title'] = True

    def handle_data(self, data):
        if self.key['time']:
            print 'Time:%s\t|' % data,
            self.key['time'] = None
        elif self.key['event-title']:
            print 'Title:%s\t|' % data,
            self.key['event-title'] = None
        elif self.key['event-location']:
            print 'Location:%s\t|' % data
            self.key['event-location'] = None

parser = MyHTMLParser()
html = urllib.urlopen('http://www.python.org/events/python-events/').read()
parser.feed(html)

