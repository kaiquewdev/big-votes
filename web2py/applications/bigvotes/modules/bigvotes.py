class Votes( object ):
	def __init__( self, db = {} ):
		output = {}

		try:
			if db:
				self.db = db

		except Exception:
			return output

	def getActives( self ):
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
				
				votes = db( 
					db.vote.active == True
				).select( 
					orderby =~ db.vote.start_at 
				)

				if votes:
					output = votes

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


#class Settings( Votes ):
#	def __init( self ):
#		Votes.__init__()

if __name__ == '__main__':
	import doctest; doctest.testmod()