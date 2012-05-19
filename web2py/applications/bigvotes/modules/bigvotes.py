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

	def getAll( self ):
		output = []

		try:
			if self.db:
				db = self.db

				db.get('member')
		except Exception:
			return output


#class Settings( Votes ):
#	def __init( self ):
#		Votes.__init__()

if __name__ == '__main__':
	import doctest; doctest.testmod()