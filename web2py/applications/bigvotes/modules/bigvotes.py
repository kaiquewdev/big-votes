class Votes( object ):
	def __init__( self, db = {} ):
		output = {}

		try:
			if db:
				self.db = db

		except Exception:
			return output

	def getActives( self, vote_id = 0 ):
		'''
		Get actives for votes.
		>>> Votes().getActives()
		[]
		'''
		import datetime

		output = []

		try:
			if self.db:
				db = self.db
				now = datetime.datetime.now()
				
				query = ( db.vote.active == True )

				if vote_id:
					query &= ( db.vote.id == vote_id )

				votes = db( query ).select()

				if votes:
					output = votes

			return output
		except Exception:
			return output

	def newVote( self, ids = {} ):
		'''
		Insert new vote to the system.
		'''
		output = False
		voting = ''

		try:
			if self.db:
				db = self.db

				if ids:
					voting = db.voting.insert(
						vote_id = ids['vote'],
						member_id = ids['member'],
					)

					if voting:
						output = voting
			return output
		except Exception:
			return output

	def getScore( self, voting_id = 0 ):
		'''
		Get score of voting.
		'''
		output = {}
		selection = {}

		try:
			if self.db:
				db = self.db

				if voting_id:
					# Ge votes by id
					selection = db( 
						( db.voting.vote_id == voting_id ) 
					).select()

					if selection:
						for vote in selection:
							verify_key = output.has_key( vote['member_id'] )
							if verify_key:
								output[ vote['member_id'] ]['score'] += 1
							elif not verify_key:
								output[ vote['member_id'] ] = {
									'name': vote['member_id']['name'],
									'score': 1
								}
				return output
			return output
		except Exception:
			return output

	def updateStatus( self, info = {} ):
		'''
		Change status to a new.
		'''
		output = {}

		try:
			if self.db:
				db = self.db

				if info:
					output = db( db.member.id == info['id'] ).update( status = info['status'] )
			return output
		except Exception:
			return output

	def consult( self, info = {} ):
		'''
		Consult if has ip in voting.
		'''
		output = {}

		try:
			if self.db:
				db = self.db

				if info:
					output = db(
						( db.voting.vote_id == info['vote_id'] ) &
						( db.voting.vote_ip == info['vote_ip'] )
					).select().first()
			return output
		except Exception:
			return output

class Members( Votes ):
	def __init__( self, db ):
		Votes.__init__(self, db)

	def getActiveMember( self, id = 0 ):
		'''
		Get members by id
		'''
		output = []

		try:
			if self.db and id:
				db = self.db

				output = db( 
					( db.member.id == int( id ) ) & 
					( db.member.status == 'active' ) 
				).select().first()

			return output
		except Exception:
			return output

	def getBy( self, status = 'active' ):
		'''
		Get members by status
		'''
		output = []

		try:
			if self.db and status:
				db = self.db

				output = db( db.member.status == status ).select()

			return output
		except Exception:
			return output

def hello():
			print 'Testing decorator'
			return

if __name__ == '__main__':
	import doctest; doctest.testmod()