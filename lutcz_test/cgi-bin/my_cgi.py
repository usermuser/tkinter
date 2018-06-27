#!/usr/bin/python
import cgi
form = cgi.FieldStorage()
print('<!DOCTYPE html>\n')
print('<title> Reply Page </title>\n')
if not 'user' in form:
    print('<h1>Who are you?</h1>')
else:
    print('<h1>Number is <i>%s</i>! </h1>' % cgi.escape(form['user'].value))