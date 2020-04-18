import sqlite3





"""

TABLA A USAR:

CREATE TABLE IF NOT EXISTS POKEMONS (ID INTEGER PRIMARY KEY, NAME TEXT, HP TEXT, ATTACK TEXT)


"""

class Connect:

	db_name = "pokemons.db"

	def _connect(self):
		try:
			db = sqlite3.connect(self.db_name)
			
			query = "CREATE TABLE IF NOT EXISTS POKEMONS (ID INTEGER PRIMARY KEY, NAME TEXT, HP TEXT, ATTACK TEXT)"
			db.cursor().execute(query)
			db.commit()

			return db

		except sqlite3.OperationalError as error:
			print("Error al abrir: ", error)

		finally:
			pass
			#db.close()


class PokemonModel:

	def __init__(self):
		self._db = Connect()._connect()
		self._cursor = self._db.cursor()

	def get_by(self,column,value):
		##Obten todos los pokemons que coincidan con la cadena, maximo 3
		query = "SELECT * FROM POKEMONS WHERE {column} LIKE '%{value}%' LIMIT 3;".format( column = column,value= value)
		self._cursor.execute(query)

		return self._cursor.fetchall()

	def get_by_id(self,id):
		query = "SELECT * FROM POKEMONS WHERE IDk = ? "
		self._cursor.execute(query,id)

		return self._cursor.fetchall()



	def create(self,data):

		#HAY QUE TENER EN CUENTA QUE HAY POKEMONS CON comillas simples ''
		query = """INSERT OR REPLACE INTO POKEMONS (ID,NAME, HP, ATTACK) VALUES ((SELECT ID FROM POKEMONS WHERE NAME = "{name}"),"{name}",{hp},{attack});""".format(**data)

		self._cursor.execute(query)
		self._db.commit()


	def _insert_image(self,id,data):
		##Aún no he probado scrapear las imagenes, ya luego lo actualizaré
		buff = sqlite3.Binary(data) 
		query = "UPDATE  POKEMONS SET IMAGE = ? WHERE ID = ?"
		self._cursor.execute(query,(buff,id))
		self._db.commit()


	def update(self,*args):
		#Por el momento solo serán estas estadisticas
		query = "UPDATE POKEMONS SET HP = ?,ATTACK = ? WHERE ID = ?"
		self._cursor.execute(query,args)
		self._db.commit()