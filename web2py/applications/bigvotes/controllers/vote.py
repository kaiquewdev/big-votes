# -*- coding: utf-8 -*-
from bigvotes import Votes
import datetime

def index():
	# Arguments in the uri
	args = request.args
	# Ip of client
	client_ip = request.client
	# Datetime to control votes
	now = datetime.datetime.now
	# Five minutes to other vote
	elapsed_time = datetime.timedelta( seconds = 60*5 )
	# Output of insertion of new voting
	output = False

	if args and len( args ) > 0 and client_ip:
		voting = Votes(db).getActives( int( args[0] ) ).first()
		consult = Votes(db).consult({
			'vote_id': args[0],
			'vote_ip': client_ip,
		})

		if not now() <= ( consult.vote_register + elapsed_time ):
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
			# Names of members
			members['names'] = [ member['name'] for member in members['profile'] ]
			# Id of eliminated member
			members['eliminated'] = {
				'id': members['ids'][ members['scores'].index( members['max_score'] ) ],
				'name': members['names'][ members['scores'].index( members['max_score'] ) ],
				'percentage': members['max_score'] * 100 / ( members['max_score'] + members['min_score'] ),
			} 

			if members:
				if now() > voting['start_at'] and now() < voting['end_at']:
					output = Votes(db).newVote( { 'vote': args[0], 'member': args[1] } )
					
					if output:
						session.vote_message = T('Voted in %(name)s' % ( members['profile'].get( int( args[1] ) ) ) )
			if now() > voting['start_at'] and now() > voting['end_at']:
					# Update status to eliminated after voting
					Votes(db).updateStatus({
						'id': int( members['eliminated']['id'] ),
						'status': 'eliminated',
					})

					session.vote_message = T('Voting complete, %(name)s was eliminated!' % ( members['eliminated'] ) )

	return redirect( URL('default', 'index', args=['result']) )	

def result():
	pass