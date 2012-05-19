# -*- coding: utf-8 -*-
from bigvotes import Votes

def index():
    # Define section title
    request.section_title = T('Votes')
    # Get votation members
    votes = Votes( db ).getActives().first()
    # Specifications of member
    specs = {
        'title': [member.name for member in votes.members],
        'avatar': [
            '<img src="{0}" width="40%" height="40%" />'.format( 
                    URL('default', 'download', args=[member.avatar]
                ) 
            ) for member in votes.members
        ],
    }

    return {
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

