# -*- coding: utf-8 -*-
from bigvotes import Votes

def index():
    # Define section title
    request.section_title = T('Votes')
    # Get votation members
    votes = Votes( db ).getActives()

    return {
        'votes': votes
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

