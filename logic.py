from random import randint
import requests
from datetime import datetime, timedelta

class Pokemon:
    pokemons = {}
    def __init__(self, pokemon_trainer):

        self.pokemon_trainer = pokemon_trainer   

        self.pokemon_number = randint(1,1000)
        self.img = self.get_img()
        self.name = self.get_name()
        self.ability = self.get_abilities()
        self.item = self.get_items()
        self.hp = randint(10,31)
        self.power = randint(1,9)
        self.last_feed_time = datetime.now()
        Pokemon.pokemons[pokemon_trainer] = self





    def get_img(self):
        url = f'https://pokeapi.co/api/v2/pokemon/{self.pokemon_number}'
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            return (data['sprites']['front_default'])
        else:
            return "Pikachu"
        




    def get_abilities(self):
        url = f'https://pokeapi.co/api/v2/pokemon/{self.pokemon_number}'
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            ability_list = []
            for i in data['abilities']:
                ability_list.append(i['ability']['name'])
            return ability_list
        else:
            return "Pikachu"
        



    
    def get_name(self):
        url = f'https://pokeapi.co/api/v2/pokemon/{self.pokemon_number}'
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            return (data['forms'][0]['name'])
        else:
            return "Pikachu"
        



    def get_items(self):
        url = f'https://pokeapi.co/api/v2/pokemon/{self.pokemon_number}'
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            for i in data['held_items']:
                data['held_items'].extend(i)
            data['held_items'].append('apple')
            return (data['held_items'])
        else:
            return "Pikachu"
        



    def attack(self, enemy):
        if self.hp <= 0:
            return "Вы уже проиграли!"

        enemy.hp -= self.power
        if enemy.hp <= 0:
            Pokemon.pokemons.pop(enemy.pokemon_trainer)
            return "Враг проиграл"
        else:
            return f"Враг атакован, hp врага: {enemy.hp}"
    
    def heal(self):
        if 'apple' in self.item:
            self.item.remove('apple')
            self.hp += 20
            return f'вы съели apple и восстановили здоровье на 20'
        else:
            return f'У вас уже нет apple'
    
    def feed(self, feed_interval = 20, hp_increase = 10 ):
        current_time = datetime.now()  
        delta_time = timedelta(seconds=feed_interval)  
        if (current_time - self.last_feed_time) > delta_time:
            self.hp += hp_increase
            self.last_feed_time = current_time
            return f"Здоровье покемона увеличено. Текущее здоровье: {self.hp}"
        else:
            return f"Следующее время кормления покемона: {self.last_feed_time+delta_time}"  
            





    def info(self):
        return f"Имя твоего покемона: {self.name}"

        # Метод класса для получения картинки покемона
    def show_img(self):
        return self.img
        
    def abilities(self):
        return f'способности твоего покемона: {self.ability[0]},{self.ability[1]}'
    def items(self):
        if len(self.item) == 0:
            return f'У вас нету предметов'
        else:
            return f'Предметы у твоего покемона: {self.item[0]}'





class Pokemon_fighter(Pokemon):
    def __init__(self, pokemon_trainer):
        self.pokemon_trainer = pokemon_trainer   

        self.pokemon_number = randint(1,1000)
        self.img = self.get_img()
        self.name = self.get_name()
        self.ability = self.get_abilities()
        self.item = self.get_items()
        self.hp = randint(10,21)
        self.power = randint(5,14)
        self.last_feed_time = datetime.now()
        Pokemon.pokemons[pokemon_trainer] = self


    def info(self):
        return f"Имя твоего покемона воина: {self.name}"
    

