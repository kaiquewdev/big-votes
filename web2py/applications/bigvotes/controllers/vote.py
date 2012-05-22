# -*- coding: utf-8 -*-
from bigvotes import Votes
import datetime

def index():
	args = request.args
	client_ip = request.client
	now = datetime.datetime.now
	elapsed_time = datetime.timedelta( seconds = 60*5 )
	output = False

	if args and len( args ) > 0 and client_ip:
		consult = Votes(db).consult({
			'vote_id': args[0],
			'vote_ip': client_ip,
		})

		if now() > ( consult.vote_register + elapsed_time ):
			output = Votes(db).newVote( { 'vote': args[0], 'member': args[1] } )

			if output:
				members = {}
				# Profile of members in the score
				members['profile'] = Votes(db).getScore( args[0] )
				# Score of members
				members['scores'] = [ members['profile'][member]['score'] for member in members['profile'] ]
				# Max score to eliminate
				members['max_score'] = max( members['scores'] )
				# Min score
				members['min_score'] = min( members['scores'] )
				# Members is tied
				members['tied'] = ( members['max_score'] == members['min_score'] )
				# Id of members in the profile score
				members['ids'] = [ int( member ) for member in members['profile'] ]
				# Id of eliminated member
				members['eliminated'] = {
					'id': members['ids'][ members['scores'].index( members['max_score'] ) ],
					'name': members['names'][ members['scores'].index( members['max_score'] ) ],
				} 

				if members:
					response.flash = T('Voted in ')
		else:
			redirect( URL('default', 'index') )
	else:
		redirect( URL('default', 'index') )

	return {
		'vote': args[1],
		'members': members
	}

def result():
	pass