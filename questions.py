import re
from bs4 import BeautifulSoup

def to_requete(message):
	requete=Requete(message)

	type_objet = {'python' : RequetePython, 'bash' : RequeteBash, 'info' : RequeteInfo}
	return type_objet[requete.type](message)

class Requete(object) :

	def __init__(self, requete) :

		self.requete_full = requete.content
		self.autheur = requete.author
		self.type = re.findall(r"^!([^ ]*)", self.requete_full)[0]
		self.requete = re.sub(rf'^!({self.type} )', '', self.requete_full)
		self.requete_norm = self.requete.lower().replace('é','e')

class RequetePython(Requete) :

	def __init__(self, requete) :
		Requete.__init__(self,requete)

class RequeteBash(Requete) :

	def __init__(self, requete) :
		Requete.__init__(self,requete)

class RequeteInfo(Requete) :

	def __init__(self, requete) :
		Requete.__init__(self,requete)
