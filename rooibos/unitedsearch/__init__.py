class Result:
	""" Holds the image-metadata pairs found by a search of a database. """
	
	def __init__(self, total, nextoffset):
		""" total is how many images were found by the search. Note,
		the actual Result object doesn't store all of them, only some"""
		self.nextoffset = nextoffset
		self.total = total
		self.images = []

	def addImage(self, image):
		self.images += [image]

class ResultImage:
	def __init__(self, infourl, thumb, name, identifier):
		""" infourl is the url gone to when the result is clicked
		thumb is the thumbnail url
		identifier is passed to the seracher's .getImage to get the corresponding Image object """
		self.infourl = infourl
		self.thumb = thumb
		self.name = name
		self.identifier = identifier
	
	def withIdentifier(self, newIdent):
		return ResultImage(self.infourl, self.thumb, self.name, self.identifier and newIdent)

class ResultRecord:
	def __init__(self, record, identifier):
		""" can be returned instead of both Result and ResultImage
		the identifier is still up to the search implementation---records and non-records could
		potentially be mixed """
		self.record = record
		self.identifier = identifier
	
	def withIdentifier(self, newIdent):
		return ResultRecord(self.record, self.identifier and newIdent)

class Image:
	""" A single image-metadata pair"""
	
	def __init__(self, url, thumb, name, meta, identifier):
		""" url is path to just the image
		thumb is url to the thumbnail
		meta is a dictionary of any useful info about this image
		identifier is sufficient info to find this image again """
		self.url = url
		self.thumb = thumb
		self.name = name
		self.meta = meta
		self.identifier = identifier
	
	def withIdentifier(self, newIdent):
		return Image(self.url, self.thumb, self.name, self.meta, self.identifier and newIdent)


class ScalarParameter:
	""" Essentially a nameless (that will probably come from a MapParameter) search filter applicable to the given database"""
	
	def __init__(self, type, label=None):
		""" eg type = boolean """
		self.type = type
		self.label = label

class OptionalParameter:
	def __init__(self, subparam, label=None):
		self.subparam = subparam
		self.label = label

class MapParameter:
	""" MapParameter({ "category": ScalarParameter(str), "year": OptionalParameter(ScalarParameter("year")) }) """
	def __init__(self, parammap, label=None):
		self.parammap = parammap
		self.label = label
