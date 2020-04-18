
from bs4 import BeautifulSoup
from pokemon_model import PokemonModel 
import requests



class SpyderPokemon:

	url = 'https://pokemondb.net/pokedex/all'

	def __init__(self):
		self.page_response = requests.get(self.url)
		self.page_content = ""
		#self.num_pokemons = 0
		self._data = {}

	def get_all(self):

		if self.page_response.status_code == 200:
			self.page_content = BeautifulSoup(self.page_response.text,"html.parser")

			entrys = self.page_content.find_all('tr')

			for entry in entrys:
				number = entry.find('span',{'class':'infocard-cell-data'})
				name = entry.find('a',{'class':'ent-name'})
				stats = entry.find_all('td',{'class':'cell-num'})
				#_type = entry.find('a',{'class':'type-icon'})


				if name != None:
					t_name = name.text
					if t_name not in self._data:
						self._data[t_name]= {
							'hp': stats[1].text,
							'attack':stats[2].text,
							} #'type': _type,  #'number': number.text,
							

						#self.num_pokemons +=1


		return self._data

	def _save(self):
		pass




