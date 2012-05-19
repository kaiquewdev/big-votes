class Votes( object ):
	def __init__( self, db = {} ):
		output = False

		try:
			if db:
				self.db = db

		except Exception:
			return output

	def getActives( self ):
		'''
		Get actives for votes.
		'''
		import datetime

		output = []
		db = self.db

		try:
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

class Settings( Votes ):
	def __init( self ):
		Votes.__init__()