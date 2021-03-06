# -*- coding: utf-8 -*-
from bigvotes import Members

def index():
	members = Members(db).getBy()

	return {
		'members': members
	}

def profile():
	args = request.args
	member = Members(db)

	if len( args ) > 0:
		member = member.getActiveMember( args[0] )
	else:
		redirect( URL( 'index' ) )

	return {
		'member': member
	}

def eliminated():
	members = Members(db).getBy(status = 'eliminated')

	return {
		'members': members
	}