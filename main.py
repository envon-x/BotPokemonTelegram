
import telebot


from pokemon_model import PokemonModel
from spyder_pokemon_db import SpyderPokemon

TOKEN = "" #AQUÍ VA EL TOKEN GENERADO DEL BotFather
bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start', 'help'])
def get_all_pokemons(message):
	
	spider_pk = SpyderPokemon()
	model = PokemonModel()

	data = spider_pk.get_all()


	for name,stats in data.items():
		#pokemon = model.get_by("NAME",name) 


		#model.create(name,int(stats['hp']),int(stats['attack']))

		try:
			stats["name"] = name
			model.create(stats)			
			
		except:
			print(name,stats) 

			#id = pokemon[0] #Accediendo a la única tupla conseguida
			#model.update(name,stats['hp'],stats['attack'],id)


	bot.reply_to(message,"BASE DE DATOS ACTUALIZADA 👍")



@bot.message_handler(func=lambda message: True)
def echo_all(message):

	model = PokemonModel()
	
	data = model.get_by('NAME',message.text)	

	bot.reply_to(message, "Checa esto 😎")

	if data != []:
		for pokemon in data:
			__message = "{name} \n 🆔: {id} \n ❤️: {hp} \n ⚔️: {attack}".format(
				id = pokemon[0],
				name = pokemon[1],
				hp = pokemon[2],
				attack = pokemon[3],
				)
			bot.reply_to(message, __message)
	else:
		bot.reply_to(message,"POKEMON NO ENCONTRADO 😅")



bot.polling()

