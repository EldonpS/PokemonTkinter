class Pokemon:
   def __init__(self, name, element, base_hp, base_atk, base_armor):
       self.__name = name
       self.__element = element
       self.__base_hp = base_hp
       self.__base_atk = base_atk
       self.__base_armor = base_armor
       self.reset_stats()

   def get_name(self):
       return self.__name

   def get_element(self):
       return self.__element

   def get_base_hp(self):
       return self.__base_hp

   def get_base_atk(self):
       return self.__base_atk

   def get_base_armor(self):
       return self.__base_armor

   def reset_stats(self):
       self.__hp = self.__base_hp
       self.__atk = self.__base_atk
       self.__armor = self.__base_armor

   def get_hp(self):
       return self.__hp

   def get_atk(self):
       return self.__atk

   def get_armor(self):
       return self.__armor

   def attack(self, other):
       other.take_damage(self.get_atk() * 1.0)

   def take_damage(self, dmg):
       dmg_after_armor = max(0, dmg - self.get_armor())
       self.__hp = max(0, self.get_hp() - dmg_after_armor)

   def is_alive(self):
       return self.get_hp() > 0

class Skill:
   def __init__(self, name, dmg, cost):
       self.__name = name
       self.__dmg = dmg
       self.__cost = cost

   def get_name(self):
       return self.__name

   def get_dmg(self):
       return self.__dmg

   def get_cost(self):
       return self.__cost

   def use(self, user, target):
       user.take_damage(self.get_cost() * 1.0)
       target.take_damage(self.get_dmg() * 1.0)

class PokemonGUI:
   def __init__(self, pokemon):
       self.__pokemon = pokemon

   def get_pokemon(self):
       return self.__pokemon

   def attack(self, other):
       self.get_pokemon().attack(other)

   def use_skill(self, skill, other):
       skill.use(self.get_pokemon(), other)

   def take_damage(self, dmg):
       self.get_pokemon().take_damage(dmg)

   def is_alive(self):
       return self.get_pokemon().is_alive()

def battle(pokemon1, pokemon2):
   while pokemon1.is_alive() and pokemon2.is_alive():
       pokemon1.attack(pokemon2)
       if pokemon2.is_alive():
           pokemon2.attack(pokemon1)

   if pokemon1.is_alive():
       print(pokemon1.get_name() + " wins!")
   else:
       print(pokemon2.get_name() + " wins!")

pokemon1 = Pokemon("Pikachu", "Electric", 100, 50, 50)
pokemon2 = Pokemon("Charizard", "Fire", 100, 80, 60)

pokemon1_gui = PokemonGUI(pokemon1)
pokemon2_gui = PokemonGUI(pokemon2)

battle(pokemon1_gui, pokemon2_gui)
