# -*- coding: utf-8 -*-
from bigvotes import Members

def index():
	members = Members(db).getBy()

	return {
		'members': members
	}

def eliminated():
	members = Members(db).getBy(status = 'deactive')

	return {
		'members': members
	}