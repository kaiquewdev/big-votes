# -*- coding: utf-8 -*-
import bigvotes.hello
from bigvotes import Votes
import datetime

def index():
    # Now time
    now = datetime.datetime.now()
    # Get votation members
    votes = Votes( db ).getActives()
    specs = {}

    if votes:
        votes = votes.first()
        # Specifications of member
        specs = {
            'id': [member.id for member in votes.members],
            'title': [member.name for member in votes.members],
            'avatar': [
                '<img src="{0}" width="40%" height="40%" />'.format( 
                        URL('default', 'download', args=[member.avatar]
                    ) 
                ) for member in votes.members
            ],
            'start': votes.start_at,
            'end': votes.end_at,
        }
    if session.vote_message:
        response.flash = session.vote_message

    return {
        'now': now,
        'votes': votes,
        'specs': specs
    }

def user():
    return dict(form=auth())


def download():
    return response.download(request,db)


def call():
    return service()


@auth.requires_signature()
def data():
    return dict(form=crud())

