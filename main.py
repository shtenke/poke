import telebot 
from config import token
import random
from logic import Pokemon, Pokemon_fighter
from datetime import datetime, timedelta

bot = telebot.TeleBot(token) 

@bot.message_handler(commands=['go'])
def go(message):
    if message.from_user.username not in Pokemon.pokemons.keys():
        num = random.randint(1,2)
        if num == 1:
            pokemon = Pokemon_fighter(message.from_user.username)
        else:
            pokemon = Pokemon(message.from_user.username)
        bot.send_message(message.chat.id, pokemon.info())
        bot.send_photo(message.chat.id, pokemon.show_img())
        bot.send_message(message.chat.id, pokemon.abilities())
        bot.send_message(message.chat.id, pokemon.items())
    else:
        bot.reply_to(message, "Ты уже создал себе покемона")

@bot.message_handler(commands=['attack'])
def attack(message):
    if message.reply_to_message:
        my_username = message.from_user.username
        enemy_username = message.reply_to_message.from_user.username
        
        if my_username not in Pokemon.pokemons:
            bot.send_message(message.chat.id, "У вас нет покемона. Создайте его с помощью команды /go")
            return
        if enemy_username not in Pokemon.pokemons:
            bot.send_message(message.chat.id, "У врага нет покемона. Создайте его с помощью команды /go")
            return

        my_pokemon = Pokemon.pokemons[my_username]
        enemy_pokemon = Pokemon.pokemons[enemy_username]

        bot.send_message(message.chat.id, my_pokemon.attack(enemy_pokemon))
    else:
        bot.send_message(message.chat.id, "Команду /attack нужно писать в ответ на сообщение человека, которого вы хотите атаковать")
@bot.message_handler(commands=['feed'])
def feed(message):
    my_username = message.from_user.username
    my_pokemon = Pokemon.pokemons[my_username]
    bot.send_message(message.chat.id, my_pokemon.feed())
@bot.message_handler(commands=['heal'])
def heal(message):
    my_username = message.from_user.username
    my_pokemon = Pokemon.pokemons[my_username]
    bot.send_message(message.chat.id, my_pokemon.heal())
@bot.message_handler(commands=['info'])
def info(message):
    if message.from_user.username in Pokemon.pokemons.keys():
        pok = Pokemon.pokemons[message.from_user.username]
        bot.send_message(message.chat.id, pok.info())
        bot.send_photo(message.chat.id, pok.show_img())
        bot.send_message(message.chat.id, pok.abilities())
        bot.send_message(message.chat.id, pok.items())
    else:
        bot.send_message(message.chat.id, 'у вас нету покемона')



bot.infinity_polling(none_stop=True)

