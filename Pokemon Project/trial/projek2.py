import random

class Pokemon:
    def __init__(self, name, element, base_hp, base_atk, base_armor):
        self._name = name
        self._element = element
        self._base_hp = base_hp
        self._base_atk = base_atk
        self._base_armor = base_armor
        self.reset_stats()

    def reset_stats(self):
        self._hp = self._base_hp
        self._max_hp = self._base_hp
        self._atk = self._base_atk
        self._armor = self._base_armor

    def calculate_damage(self, skill):
        raise NotImplementedError("Subclasses should implement this method")

    def is_super_effective(self, opponent_element):
        raise NotImplementedError("Subclasses should implement this method")

    def is_not_very_effective(self, opponent_element):
        raise NotImplementedError("Subclasses should implement this method")

    def display_stats(self):
        print(f"{self._name} - Element: {self._element}")
        print(f"HP: {self._hp}/{self._max_hp} | ATK: {self._atk} | Armor: {self._armor}")

    def get_name(self):
        return self._name

    def get_element(self):
        return self._element

    def get_hp(self):
        return self._hp

    def get_max_hp(self):
        return self._max_hp

    def get_atk(self):
        return self._atk

    def get_armor(self):
        return self._armor

class NormalSkill:
    def __init__(self, name, damage):
        self._name = name
        self._damage = damage
        self._element = "normal"

    def get_name(self):
        return self._name

    def get_damage(self):
        return self._damage

    def get_element(self):
        return self._element

class GrassSkill(NormalSkill):
    def __init__(self, name, damage):
        super().__init__(name, damage)
        self._element = "grass"

class FireSkill(NormalSkill):
    def __init__(self, name, damage):
        super().__init__(name, damage)
        self._element = "fire"

class WaterSkill(NormalSkill):
    def __init__(self, name, damage):
        super().__init__(name, damage)
        self._element = "water"

class Bulbasaur(Pokemon):
    def __init__(self):
        super().__init__("Bulbasaur", "grass", 45, 49, 49)
        self._skills = [NormalSkill("Tackle", 15), NormalSkill("Take Down", 5), GrassSkill("Razor Leaf", 20)]

    def calculate_damage(self, skill):
        return skill.get_damage() + self.get_atk()

    def is_super_effective(self, opponent_element):
        return opponent_element == "water"

    def is_not_very_effective(self, opponent_element):
        return opponent_element == "fire"

class Ivysaur(Pokemon):
    def __init__(self):
        super().__init__("Ivysaur", "grass", 55, 59, 59)
        self._skills = [GrassSkill("Sleep Powder", 10), GrassSkill("Seed Bomb", 20), GrassSkill("Solar Beam", 25)]

    def calculate_damage(self, skill):
        return skill.get_damage() + self.get_atk()

    def is_super_effective(self, opponent_element):
        return opponent_element == "water"

    def is_not_very_effective(self, opponent_element):
        return opponent_element == "fire"

class Charmander(Pokemon):
    def __init__(self):
        super().__init__("Charmander", "fire", 39, 52, 43)
        self._skills = [NormalSkill("Growl", 5), NormalSkill("Scratch", 10), FireSkill("Ember", 20)]

    def calculate_damage(self, skill):
        return skill.get_damage() + self.get_atk()

    def is_super_effective(self, opponent_element):
        return opponent_element == "grass"

    def is_not_very_effective(self, opponent_element):
        return opponent_element == "water"

class Charmeleon(Pokemon):
    def __init__(self):
        super().__init__("Charmeleon", "fire", 49, 62, 53)
        self._skills = [NormalSkill("Slash", 10), FireSkill("Fire Fang", 15), FireSkill("Fire Spin", 25)]

    def calculate_damage(self, skill):
        return skill.get_damage() + self.get_atk()

    def is_super_effective(self, opponent_element):
        return opponent_element == "grass"

    def is_not_very_effective(self, opponent_element):
        return opponent_element == "water"

class Squirtle(Pokemon):
    def __init__(self):
        super().__init__("Squirtle", "water", 44, 48, 65)
        self._skills = [NormalSkill("Tackle", 5), NormalSkill("Tail Whip", 10), WaterSkill("Water Gun", 20)]

    def calculate_damage(self, skill):
        return skill.get_damage() + self.get_atk()

    def is_super_effective(self, opponent_element):
        return opponent_element == "fire"

    def is_not_very_effective(self, opponent_element):
        return opponent_element == "grass"

class Wartortle(Pokemon):
    def __init__(self):
        super().__init__("Wartortle", "water", 54, 58, 75)
        self._skills = [NormalSkill("Bite", 10), WaterSkill("Water Pulse", 20), WaterSkill("Rain Dance", 25)]

    def calculate_damage(self, skill):
        return skill.get_damage() + self.get_atk()

    def is_super_effective(self, opponent_element):
        return opponent_element == "fire"

    def is_not_very_effective(self, opponent_element):
        return opponent_element == "grass"

def battle(pokemon1, pokemon2):

    while pokemon1.get_hp() > 0 and pokemon2.get_hp() > 0:
        # Pilihan skill untuk pokemon1
        print(f"\n{pokemon1.get_name()}'s Skills:")
        for i, skill in enumerate(pokemon1._skills, start=1):
            print(f"{i}. {skill.get_name()}")

        chosen_skill_index = int(input(f"Choose a skill for {pokemon1.get_name()} (1-{len(pokemon1._skills)}): ")) - 1
        chosen_skill_pokemon1 = pokemon1._skills[chosen_skill_index]

        damage_pokemon1 = pokemon1.calculate_damage(chosen_skill_pokemon1)

        # Pilihan skill untuk pokemon2 (random)
        chosen_skill_pokemon2 = random.choice(pokemon2._skills)
        damage_pokemon2 = pokemon2.calculate_damage(chosen_skill_pokemon2)

        # Menentukan efektivitas serangan berdasarkan elemen skill
        effectiveness_pokemon1 = "Normal"
        if chosen_skill_pokemon1.get_element() == "water" and pokemon2.get_element() == "fire":
            effectiveness_pokemon1 = "Super Effective"
        elif chosen_skill_pokemon1.get_element() == "fire" and pokemon2.get_element() == "grass":
            effectiveness_pokemon1 = "Super Effective"
        elif chosen_skill_pokemon1.get_element() == "grass" and pokemon2.get_element() == "water":
            effectiveness_pokemon1 = "Super Effective"
        elif chosen_skill_pokemon1.get_element() == "water" and pokemon2.get_element() == "grass":
            effectiveness_pokemon1 = "Not Very Effective"
        elif chosen_skill_pokemon1.get_element() == "fire" and pokemon2.get_element() == "water":
            effectiveness_pokemon1 = "Not Very Effective"
        elif chosen_skill_pokemon1.get_element() == "grass" and pokemon2.get_element() == "fire":
            effectiveness_pokemon1 = "Not Very Effective"

        effectiveness_pokemon2 = "Normal"
        if chosen_skill_pokemon2.get_element() == "water" and pokemon1.get_element() == "fire":
            effectiveness_pokemon2 = "Super Effective"
        elif chosen_skill_pokemon2.get_element() == "fire" and pokemon1.get_element() == "grass":
            effectiveness_pokemon2 = "Super Effective"
        elif chosen_skill_pokemon2.get_element() == "grass" and pokemon1.get_element() == "water":
            effectiveness_pokemon2 = "Super Effective"
        elif chosen_skill_pokemon2.get_element() == "water" and pokemon1.get_element() == "grass":
            effectiveness_pokemon2 = "Not Very Effective"
        elif chosen_skill_pokemon2.get_element() == "fire" and pokemon1.get_element() == "water":
            effectiveness_pokemon2 = "Not Very Effective"
        elif chosen_skill_pokemon2.get_element() == "grass" and pokemon1.get_element() == "fire":
            effectiveness_pokemon2 = "Not Very Effective"

        # Pengurangan HP berdasarkan damage dan armor
        damage_taken_pokemon2 = max(0, damage_pokemon1 - pokemon2.get_armor())
        damage_taken_pokemon1 = max(0, damage_pokemon2 - pokemon1.get_armor())

        pokemon2._hp = max(0, pokemon2.get_hp() - damage_taken_pokemon2)
        pokemon1._hp = max(0, pokemon1.get_hp() - damage_taken_pokemon1)

        # Menampilkan log pertarungan
        print(f"{pokemon1.get_name()} using {chosen_skill_pokemon1.get_name()}, dealing "
              f"{(pokemon2.get_max_hp() - pokemon2.get_hp())} damage to {pokemon2.get_name()}, ", end="")
        print(effectiveness_pokemon1)

        if pokemon2.get_hp() <= 0:
            print(f"{pokemon2.get_name()} is KO'd, {pokemon1.get_name()} WINS")
            break

        print(f"{pokemon2.get_name()} using {chosen_skill_pokemon2.get_name()}, dealing "
              f"{(pokemon1.get_max_hp() - pokemon1.get_hp())} damage to {pokemon1.get_name()}, ", end="")
        print(effectiveness_pokemon2)

        # Menampilkan status HP setiap Pokemon setiap giliran
        print(f"Player Pokemon ({pokemon1.get_name()}, {pokemon1.get_hp()}/{pokemon1.get_max_hp()})")
        print(f"Enemy Pokemon ({pokemon2.get_name()}, {pokemon2.get_hp()}/{pokemon2.get_max_hp()})")

        if pokemon1.get_hp() <= 0:
            print(f"{pokemon1.get_name()} is KO'd, {pokemon2.get_name()} WINS")
            break

def main():
    print("Welcome to Pokemon Battle Simulator!")

    # Pilihan Pokemon untuk player
    print("\nChoose your Pokemon:")
    print("1. Bulbasaur\n2. Ivysaur\n3. Charmander\n4. Charmeleon\n5. Squirtle\n6. Wartortle")

    player_choice = int(input("Enter the number of your chosen Player Pokemon: "))
    player_pokemon = get_pokemon_by_choice(player_choice)

    # Pilihan Pokemon untuk enemy (random)
    enemy_choice = int(input("Enter the number of your chosen Enemy Pokemon: "))
    enemy_pokemon = get_pokemon_by_choice(enemy_choice)

    print(f"\nPlayer sends out {player_pokemon.get_name()}")
    print(f"Enemy sends out {enemy_pokemon.get_name()}")

    # Memulai pertarungan
    battle(player_pokemon, enemy_pokemon)

def get_pokemon_by_choice(choice):
    if choice == 1:
        return Bulbasaur()
    elif choice == 2:
        return Ivysaur()
    elif choice == 3:
        return Charmander()
    elif choice == 4:
        return Charmeleon()
    elif choice == 5:
        return Squirtle()
    elif choice == 6:
        return Wartortle()
    else:
        print("Invalid choice. Defaulting to Bulbasaur.")
        return Bulbasaur()

if __name__ == "__main__":
    main()
