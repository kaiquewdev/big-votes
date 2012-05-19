# -*- coding: utf-8 -*-
# this file is released under public domain and you can use without limitations

#########################################################################
## Customize your APP title, subtitle and menus here
#########################################################################

response.title = 'Big Votes'
response.subtitle = 'A simple chanllenge'

## read more at http://dev.w3.org/html5/markup/meta.name.html
response.meta.author = 'Kaique da Silva <kaique.developer@gmail.com>'
response.meta.description = 'Challenge app'
response.meta.keywords = 'BBB, votes, challenge'
response.meta.generator = 'Web2py Web Framework'
response.meta.copyright = 'Copyright 2012'

## your http://google.com/analytics id
response.google_analytics_id = None

response.menu = [
    (T('Votes'), False, URL('default','index'), []),
    (T('Members'), False, URL('default','members'), []),
    (T('Members Eliminated'), False, URL('default','members', args=['eliminated']), [])
]
