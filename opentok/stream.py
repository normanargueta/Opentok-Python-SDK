class Stream(object):
	"""
	Represents an OpenTok stream
	"""

	def __init__(self, kwargs):
		for key, value in kwargs.items():
			setattr(self, key, value)