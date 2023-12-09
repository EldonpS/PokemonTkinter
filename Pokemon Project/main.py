import random
import tkinter as tk
import vlc
from tkinter import ttk
from PIL import Image, ImageTk
from pathlib import Path

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / "assets"
print(f"Alamat asset: {ASSETS_PATH}")

class Pokemon:
    def __init__(self, name, element, base__hp, base__atk, base__armor):
        self.__name = name
        self.__element = element
        self.__base_hp = base__hp
        self.__base_atk = base__atk
        self.__base_armor = base__armor
        self.reset_stats()

    def reset_stats(self):
        self.__hp = self.__base_hp
        self.__max_hp = self.__base_hp
        self.__atk = self.__base_atk
        self.__armor = self.__base_armor

    def calculate_effectiveness(self, skill, opponent_element):
        effectiveness = 1.0

        if skill.get_element() == "grass":
            if self.is_super_effective(opponent_element):
                effectiveness = 2.0
            elif self.is_not_very_effective(opponent_element):
                effectiveness = 0.5

        elif skill.get_element() == "fire":
            if self.is_super_effective(opponent_element):
                effectiveness = 2.0
            elif self.is_not_very_effective(opponent_element):
                effectiveness = 0.5

        elif skill.get_element() == "water":
            if self.is_super_effective(opponent_element):
                effectiveness = 2.0
            elif self.is_not_very_effective(opponent_element):
                effectiveness = 0.5

        elif skill.get_element() == "electric":
            if self.is_super_effective(opponent_element):
                effectiveness = 2.0
            elif self.is_not_very_effective(opponent_element):
                effectiveness = 0.5

        elif skill.get_element() == "rock":
            if self.is_super_effective(opponent_element):
                effectiveness = 2.0
            elif self.is_not_very_effective(opponent_element):
                effectiveness = 0.5

        return effectiveness
    
    def calculate_damage(self, skill, opponent_element):
        damage = skill.get_damage() + self.get_atk()
        effectiveness = self.calculate_effectiveness(skill, opponent_element)

        final_damage = damage * effectiveness

        return int(final_damage)


    def is_super_effective(self, opponent__element):
        raise NotImplementedError("Subclass harus ada pada child class")

    def is_not_very_effective(self, opponent__element):
        raise NotImplementedError("Subclass harus ada pada child class")

    def get_name(self):
        return self.__name

    def get_element(self):
        return self.__element

    def get_hp(self):
        return self.__hp
    
    def set_hp(self, newhp):
        self.__hp = newhp

    def get_max_hp(self):
        return self.__max_hp

    def get_atk(self):
        return self.__atk

    def get_armor(self):
        return self.__armor
    
    def getskills_info(self):
        skills_info = []
        for skill in self.skills:
            skill_info = {
                'name': skill.get_name(),
                'damage': skill.get_damage(),
                'element': skill.get_element()
            }
            skills_info.append(skill_info)
        return skills_info

class Bulbasaur(Pokemon):
    def __init__(self):
        super().__init__("Bulbasaur", "grass", 123, 45, 50)
        self.skills = [NormalSkill("Tackle", 15), NormalSkill("Take Down", 5), GrassSkill("Razor Leaf", 20)]

    def calculate_damage(self, skill, opponent__element):
        return super().calculate_damage(skill, opponent__element)

    def is_super_effective(self, opponent__element):
        return opponent__element == "water"

    def is_not_very_effective(self, opponent__element):
        return opponent__element == "fire"

class Ivysaur(Pokemon):
    def __init__(self):
        super().__init__("Ivysaur", "grass", 134, 55, 12)
        self.skills = [GrassSkill("Sleep Powder", 10), GrassSkill("Seed Bomb", 20), GrassSkill("Solar Beam", 25)]

    def calculate_damage(self, skill, opponent__element):
        return super().calculate_damage(skill, opponent__element)

    def is_super_effective(self, opponent__element):
        return opponent__element == "water"

    def is_not_very_effective(self, opponent__element):
        return opponent__element == "fire"

class Charmander(Pokemon):
    def __init__(self):
        super().__init__("Charmander", "fire", 113, 39, 11)
        self.skills = [NormalSkill("Growl", 5), NormalSkill("Scratch", 10), FireSkill("Ember", 20)]

    def calculate_damage(self, skill, opponent__element):
        return super().calculate_damage(skill, opponent__element)

    def is_super_effective(self, opponent__element):
        return opponent__element == "grass"

    def is_not_very_effective(self, opponent__element):
        return opponent__element == "water"

class Charmeleon(Pokemon):
    def __init__(self):
        super().__init__("Charmeleon", "fire", 132, 49, 16)
        self.skills = [NormalSkill("Slash", 10), FireSkill("Fire Fang", 15), FireSkill("Fire Spin", 25)]

    def calculate_damage(self, skill, opponent__element):
        return super().calculate_damage(skill, opponent__element)

    def is_super_effective(self, opponent__element):
        return opponent__element == "grass"

    def is_not_very_effective(self, opponent__element):
        return opponent__element == "water"

class Squirtle(Pokemon):
    def __init__(self):
        super().__init__("Squirtle", "water", 90, 44, 9)
        self.skills = [NormalSkill("Tackle", 5), NormalSkill("Tail Whip", 10), WaterSkill("Water Gun", 20)]

    def calculate_damage(self, skill, opponent__element):
        return super().calculate_damage(skill, opponent__element)

    def is_super_effective(self, opponent__element):
        return opponent__element == "fire"

    def is_not_very_effective(self, opponent__element):
        return opponent__element == "grass"

class Wartortle(Pokemon):
    def __init__(self):
        super().__init__("Wartortle", "water", 121, 54, 13)
        self.skills = [NormalSkill("Bite", 10), WaterSkill("Water Pulse", 20), WaterSkill("Rain Dance", 25)]

    def calculate_damage(self, skill, opponent__element):
        return super().calculate_damage(skill, opponent__element)

    def is_super_effective(self, opponent__element):
        return opponent__element == "fire"

    def is_not_very_effective(self, opponent__element):
        return opponent__element == "grass"
    
class Sandslash(Pokemon):
    def __init__(self):
        super().__init__("Sandslash", "rock", 143, 60, 20)
        self.skills = [NormalSkill("Crush Claw", 10), rockSkill("Sand Attack", 20), rockSkill("Bulldoze", 25)]

    def calculate_damage(self, skill, opponent__element):
        return super().calculate_damage(skill, opponent__element)

    def is_super_effective(self, opponent__element):
        return opponent__element == "fire"

    def is_not_very_effective(self, opponent__element):
        return opponent__element == "grass"

class Pikachu(Pokemon):
    def __init__(self):
        super().__init__("Pikachu", "electric", 99, 35, 16)
        self.skills = [NormalSkill("Growl", 10), electricSkill("Nuzzle", 20), electricSkill("Thunder", 25)]

    def calculate_damage(self, skill, opponent__element):
        return super().calculate_damage(skill, opponent__element)

    def is_super_effective(self, opponent__element):
        return opponent__element == "water"

    def is_not_very_effective(self, opponent__element):
        return opponent__element == "grass"


class NormalSkill:
    def __init__(self, name, damage):
        self.__name = name
        self._damage = damage
        self.__element = "normal"

    def get_name(self):
        return self.__name

    def get_damage(self):
        return self._damage

    def get_element(self):
        return self.__element
    
    def set_element(self, element):
        self.__element = element
    
class GrassSkill(NormalSkill):
    def __init__(self, name, damage):
        super().__init__(name, damage)
        self.set_element("grass")

class FireSkill(NormalSkill):
    def __init__(self, name, damage):
        super().__init__(name, damage)
        self.set_element("fire")

class WaterSkill(NormalSkill):
    def __init__(self, name, damage):
        super().__init__(name, damage)
        self.set_element("water") 

class electricSkill(NormalSkill):
    def __init__(self, name, damage):
        super().__init__(name, damage)
        self.set_element("electric") 

class rockSkill(NormalSkill):
    def __init__(self, name, damage):
        super().__init__(name, damage)
        self.set_element("rock") 


class PokemonBattleUI:
    def __init__(self, master):
        self.master = master
        self.player_pokemon = None
        self.enemy_pokemon = None
        self.text_box = None
        self.player_pokemon_label = None
        self.enemy_pokemon_label = None
        self.name_label = None
        self.spin_label = None
        self.spinbox = None
        self.attack_button = None
        self.next_button = None
        self.combo_box1 = None
        self.combo_box2 = None
        self.fight_button = None
        self.run_button = None
        self.enter_button = None
        self.pokemon_images_labels = None
        self.selected_pokemon1 = None
        self.selected_pokemon2 = None
        self.pok1 = None
        self.pok2 = None
        self.chosen_skill_pokemon1 = None
        self.chosen_skill_pokemon2 = None
        self.effectiveness_pokemon1 = None
        self.effectiveness_pokemon2 = None
        self.skill_buttons = None
        self.skill_info_textbox = None
        self.playerCurr_hp_label = None
        self.enemyCurr_hp_label = None
        self.playerMaxhp_label = None
        self.enemyMaxhp_label = None
        self.appearSong = None
        self.selectSong = None
        self.battleSong = None   
        self.victorySong = None

    def get_pokemon_by_choice(self, choice):
        if isinstance(choice, str):
            choice_lower = choice.lower()
            if choice_lower == "bulbasaur":
                return Bulbasaur()
            elif choice_lower == "ivysaur":
                return Ivysaur()
            elif choice_lower == "charmander":
                return Charmander()
            elif choice_lower == "charmeleon":
                return Charmeleon()
            elif choice_lower == "squirtle":
                return Squirtle()
            elif choice_lower == "wartortle":
                return Wartortle()
            elif choice_lower == "pikachu":
                return Pikachu()
            elif choice_lower == "sandslash":
                return Sandslash()
            else:
                print("Invalid choice. Defaulting to Bulbasaur.")
                return Bulbasaur()
        else:
            return choice
    
    def load_pokemon_images(self):
        image_paths = [
            ASSETS_PATH / "bulbasaur.gif",
            ASSETS_PATH / "ivysaur.gif",
            ASSETS_PATH / "charmander.gif",
            ASSETS_PATH / "charmeleon.gif",
            ASSETS_PATH / "squirtle.gif",
            ASSETS_PATH / "wartortle.gif",
            ASSETS_PATH / "pikachu.gif",
            ASSETS_PATH / "sandslash.gif"
        ]

        pokemon_images = [Image.open(path) for path in image_paths]
        resized_images = [img.resize((100, 100)) for img in pokemon_images]
        tk_images = [ImageTk.PhotoImage(img) for img in resized_images]

        return tk_images
    
    def start_battle(self):
        startSong.stop()

        song2 = ASSETS_PATH / "rivalAppear.mp3"
        self.appearSong = vlc.MediaPlayer(song2)
        self.appearSong.play()
        
        next_background_path = ASSETS_PATH / "nextstart.png"
        next_background_image = Image.open(next_background_path)
        resized_next_background = next_background_image.resize((window_size, window_size))
        tk_next_background = ImageTk.PhotoImage(resized_next_background)

        background_label.configure(image=tk_next_background)
        background_label.image = tk_next_background

        start_button.destroy()

        self.fight_button_image_path = ASSETS_PATH / "fight.png"
        fight_image = Image.open(self.fight_button_image_path)
        resized_fight_image = fight_image.resize((100, 50))
        tk_fight_image = ImageTk.PhotoImage(resized_fight_image)

        self.fight_button = ttk.Button(square_window, image=tk_fight_image, command=self.choose)
        self.fight_button.image = tk_fight_image
        self.fight_button.place(x=400, y=457)

        self.run_button_image_path = ASSETS_PATH / "run.png"
        run_image = Image.open(self.run_button_image_path)
        resized_run_image = run_image.resize((70, 35))
        tk_run_image = ImageTk.PhotoImage(resized_run_image)

        self.run_button = ttk.Button(square_window, image=tk_run_image, command=self.run_clicked)
        self.run_button.image = tk_run_image
        self.run_button.place(x=400, y=520)

    def choose(self):
        self.appearSong.stop()

        song3 = ASSETS_PATH / "selectSong.mp3"
        self.selectSong = vlc.MediaPlayer(song3)
        self.selectSong.play()

        next_background_path = ASSETS_PATH / "choose.png"
        next_background_image = Image.open(next_background_path)
        resized_next_background = next_background_image.resize((window_size, window_size))
        tk_next_background = ImageTk.PhotoImage(resized_next_background)

        background_label.configure(image=tk_next_background)
        background_label.image = tk_next_background

        self.fight_button.destroy()
        self.run_button.destroy()

        pokemon_images = self.load_pokemon_images()
        combo_box_values = ["Bulbasaur", "Ivysaur", "Charmander", "Charmeleon", "Squirtle", "Wartortle", "Pikachu", "Sandslash"]
        self.combo_box1 = ttk.Combobox(square_window, values=combo_box_values)
        self.combo_box1.set("Choose Player")
        self.combo_box1.place(x=100, y=520)

        combo_box_values = ["Bulbasaur", "Ivysaur", "Charmander", "Charmeleon", "Squirtle", "Wartortle", "Pikachu", "Sandslash"]
        self.combo_box2 = ttk.Combobox(square_window, values=combo_box_values)
        self.combo_box2.set("Choose Enemy")
        self.combo_box2.place(x=350, y=520)

        self.enter_button = ttk.Button(square_window, text="Enter", command=self.battle_ui)
        self.enter_button.place(x=260, y=540)

        self.pokemon_images_labels = []
        for i, (img, name) in enumerate(zip(pokemon_images, combo_box_values)):
            row, col = divmod(i, 4)
            label = tk.Label(square_window, image=img, text=name, compound=tk.BOTTOM)
            label.image = img
            label.grid(row=row, column=col, padx=20, pady=40)
            self.pokemon_images_labels.append(label)

    def battle_ui(self):
        
        self.selectSong.stop()

        song4 = ASSETS_PATH / "battleSong.mp3"
        self.battleSong = vlc.MediaPlayer(song4)
        self.battleSong.play()

        self.selected_pokemon1 = self.combo_box1.get()
        self.pok1 = self.selected_pokemon1

        self.selected_pokemon2 = self.combo_box2.get()
        self.pok2 = self.selected_pokemon2
        
        player_pokemon = self.get_pokemon_by_choice(self.pok1)
        enemy_pokemon = self.get_pokemon_by_choice(self.pok2)

        next_background_path = ASSETS_PATH / "standby.png"
        next_background_image = Image.open(next_background_path)
        resized_next_background = next_background_image.resize((window_size, window_size))
        tk_next_background = ImageTk.PhotoImage(resized_next_background)

        background_label.configure(image=tk_next_background)
        background_label.image = tk_next_background

        self.combo_box1.destroy()
        self.combo_box2.destroy()
        self.enter_button.destroy()
        for label in self.pokemon_images_labels:
            label.destroy()

        self.pokemon_images_labels = []

        image_size = 200

        # Player Pokemon
        player_pokemon_image_path = ASSETS_PATH / f"{self.selected_pokemon1}.gif"
        player_pokemon_image = Image.open(player_pokemon_image_path)
        resized_player_pokemon_image = player_pokemon_image.resize((image_size, image_size))
        tk_player_pokemon_image = ImageTk.PhotoImage(resized_player_pokemon_image)

        self.player_pokemon_label = tk.Label(square_window, image=tk_player_pokemon_image, text=self.selected_pokemon1.upper(), compound=tk.BOTTOM, font=("Pokemon",12, "bold"))
        self.player_pokemon_label.image = tk_player_pokemon_image
        self.player_pokemon_label.place(x=30, y=170)

        # Enemy Pokemon
        enemy_pokemon_image_path = ASSETS_PATH / f"{self.selected_pokemon2}.gif"
        enemy_pokemon_image = Image.open(enemy_pokemon_image_path)
        resized_enemy_pokemon_image = enemy_pokemon_image.resize((image_size, image_size))
        tk_enemy_pokemon_image = ImageTk.PhotoImage(resized_enemy_pokemon_image)

        self.enemy_pokemon_label = tk.Label(square_window, image=tk_enemy_pokemon_image, text=self.selected_pokemon2.upper(), compound=tk.BOTTOM, font=("Pokemon",12, "bold"))
        self.enemy_pokemon_label.image = tk_enemy_pokemon_image
        self.enemy_pokemon_label.place(x=361, y=20)
        self.pokemon_images_labels = [self.player_pokemon_label, self.enemy_pokemon_label]

        self.playerCurr_hp_label = ttk.Label(square_window, text=f"{player_pokemon.get_hp()}", font=("Pokemon", 30))
        self.playerCurr_hp_label.place(x=358, y=325)

        self.enemyCurr_hp_label = ttk.Label(square_window, text=f"{enemy_pokemon.get_hp()}", font=("Pokemon", 30))
        self.enemyCurr_hp_label.place(x=125, y=20)

        self.playerMaxhp_label = ttk.Label(square_window, text=f"{player_pokemon.get_max_hp()}", font=("Pokemon", 30))
        self.playerMaxhp_label.place(x=470, y=325)

        self.enemyMaxhp_label = ttk.Label(square_window, text=f"{enemy_pokemon.get_max_hp()}", font=("Pokemon", 30))
        self.enemyMaxhp_label.place(x=240, y=20)
        
        self.text_box = tk.Text(square_window, height=8, width=60)
        self.text_box.place(x=30, y=430)
        self.text_box.insert(tk.END, f"Battle between {self.selected_pokemon1} and {self.selected_pokemon2}!\n\n")

        self.next_button = ttk.Button(square_window, text="Next", command=lambda: battle(player_pokemon, enemy_pokemon))
        self.next_button.place(x=260, y=550)
        
        def battle(pokemon1, pokemon2):

                self.player_pokemon_label.destroy()
                self.text_box.destroy()
                self.next_button.destroy()
                
                next_background_path = ASSETS_PATH / "skill2.png"
                next_background_image = Image.open(next_background_path)
                resized_next_background = next_background_image.resize((window_size, window_size))
                tk_next_background = ImageTk.PhotoImage(resized_next_background)

                background_label.configure(image=tk_next_background)
                background_label.image = tk_next_background

                def battle_turn():
                    next_background_path = ASSETS_PATH / "skill2.png"
                    next_background_image = Image.open(next_background_path)
                    resized_next_background = next_background_image.resize((window_size, window_size))
                    tk_next_background = ImageTk.PhotoImage(resized_next_background)

                    background_label.configure(image=tk_next_background)
                    background_label.image = tk_next_background

                    if pokemon1.get_hp() <= 0 or pokemon2.get_hp() <= 0:
                        display_winner()
                        return

                    try:
                        self.player_pokemon_label.destroy()
                        self.text_box.destroy()
                        self.next_button.destroy()
                    except:
                        pass
                    # Pilihan skill untuk pokemon1
                    self.skill_info_textbox = tk.Text(square_window, height=5, width=30)
                    self.skill_info_textbox.place(x=30, y=310)
                    self.skill_buttons = []

                    for i, skill in enumerate(pokemon1.skills, start=1):
                        button = tk.Button(square_window, text=f"{i}.{skill.get_name()}", command=lambda s=skill, p=pokemon1: show_skill_info(p, s))
                        button.place(x=25, y=425 + i * 30)
                        self.skill_buttons.append(button)

                    def show_skill_info(pokemon, skill):
                        info = f"{pokemon.get_name()}'s skills:\n\n"
                        info += f"Name: {skill.get_name()}\n"
                        info += f"Damage: {skill.get_damage()}\n"
                        info += f"Element: {skill.get_element()}"
                        self.skill_info_textbox.delete(1.0, tk.END)
                        self.skill_info_textbox.insert(tk.END, info)

                    txtskill = f"Choose a skill for {pokemon1.get_name()} (1-{len(pokemon1.skills)}):"
                    self.name_label = ttk.Label(square_window, text=txtskill, font=("Pokemon", 14))
                    self.name_label.place(x=150, y=440)

                    self.spin_label = ttk.Label(square_window, text="Pilih Skill ke- :", font=("Pokemon", 14))
                    self.spin_label.place(x=150, y=490)

                    spinbox_var = tk.IntVar()
                    self.spinbox = ttk.Spinbox(square_window, from_=1, to=len(pokemon1.skills), textvariable=spinbox_var, width=5, font=("Pokemon", 14))
                    self.spinbox.place(x=270, y=490)

                    self.attack_button = ttk.Button(square_window, text="Attack", command=lambda: use_skill())
                    self.attack_button.place(x=150, y=540)

                    def use_skill():

                        self.chosen_skill_pokemon1 = pokemon1.skills[int(spinbox_var.get()) - 1]
                        # Pilihan skill untuk pokemon2 (random)
                        self.chosen_skill_pokemon2 = random.choice(pokemon2.skills)

                        damage_pokemon1 = pokemon1.calculate_damage(self.chosen_skill_pokemon1, pokemon2.get_element())
                        damage_pokemon2 = pokemon2.calculate_damage(self.chosen_skill_pokemon2, pokemon1.get_element())

                        # Pengurangan HP berdasarkan damage dan armor
                        self.effectiveness_pokemon1 = "Normal"
                        if self.chosen_skill_pokemon1.get_element() == "water":
                            if pokemon2.get_element() == "fire":
                                self.effectiveness_pokemon1 = "Super Effective"
                            elif pokemon2.get_element() == "grass":
                                self.effectiveness_pokemon1 = "Not Very Effective"
                            elif pokemon2.get_element() == "electric":
                                self.effectiveness_pokemon1 = "Super Effective"
                            elif pokemon2.get_element() == "rock":
                                self.effectiveness_pokemon1 = "Not Very Effective"

                        elif self.chosen_skill_pokemon1.get_element() == "fire":
                            if pokemon2.get_element() == "water":
                                self.effectiveness_pokemon1 = "Not Very Effective"
                            elif pokemon2.get_element() == "grass":
                                self.effectiveness_pokemon1 = "Super Effective"
                            elif pokemon2.get_element() == "electric":
                                self.effectiveness_pokemon1 = "Super Effective"
                            elif pokemon2.get_element() == "rock":
                                self.effectiveness_pokemon1 = "Not Very Effective"

                        elif self.chosen_skill_pokemon1.get_element() == "grass":
                            if pokemon2.get_element() == "water":
                                self.effectiveness_pokemon1 = "Super Effective"
                            elif pokemon2.get_element() == "fire":
                                self.effectiveness_pokemon1 = "Not Very Effective"
                            elif pokemon2.get_element() == "electric":
                                self.effectiveness_pokemon1 = "Normal"
                            elif pokemon2.get_element() == "rock":
                                self.effectiveness_pokemon1 = "Normal"

                        elif self.chosen_skill_pokemon1.get_element() == "electric":
                            if pokemon2.get_element() == "water":
                                self.effectiveness_pokemon1 = "Super Effective"
                            elif pokemon2.get_element() == "fire":
                                self.effectiveness_pokemon1 = "Super Effective"
                            elif pokemon2.get_element() == "grass":
                                self.effectiveness_pokemon1 = "Normal"
                            elif pokemon2.get_element() == "rock":
                                self.effectiveness_pokemon1 = "Not Very Effective"

                        elif self.chosen_skill_pokemon1.get_element() == "rock":
                            if pokemon2.get_element() == "water":
                                self.effectiveness_pokemon1 = "Not Very Effective"
                            elif pokemon2.get_element() == "fire":
                                self.effectiveness_pokemon1 = "Super Effective"
                            elif pokemon2.get_element() == "grass":
                                self.effectiveness_pokemon1 = "Super Effective"
                            elif pokemon2.get_element() == "electric":
                                self.effectiveness_pokemon1 = "Not Very Effective"


                        self.effectiveness_pokemon2 = "Normal"
                        if self.chosen_skill_pokemon2.get_element() == "water":
                            if pokemon1.get_element() == "fire":
                                self.effectiveness_pokemon2 = "Super Effective"
                            elif pokemon1.get_element() == "grass":
                                self.effectiveness_pokemon2 = "Not Very Effective"
                            elif pokemon1.get_element() == "electric":
                                self.effectiveness_pokemon2 = "Super Effective"
                            elif pokemon1.get_element() == "rock":
                                self.effectiveness_pokemon2 = "Not Very Effective"

                        elif self.chosen_skill_pokemon2.get_element() == "fire":
                            if pokemon1.get_element() == "water":
                                self.effectiveness_pokemon2 = "Not Very Effective"
                            elif pokemon1.get_element() == "grass":
                                self.effectiveness_pokemon2 = "Super Effective"
                            elif pokemon1.get_element() == "electric":
                                self.effectiveness_pokemon2 = "Super Effective"
                            elif pokemon1.get_element() == "rock":
                                self.effectiveness_pokemon2 = "Not Very Effective"

                        elif self.chosen_skill_pokemon2.get_element() == "grass":
                            if pokemon1.get_element() == "water":
                                self.effectiveness_pokemon2 = "Super Effective"
                            elif pokemon1.get_element() == "fire":
                                self.effectiveness_pokemon2 = "Not Very Effective"
                            elif pokemon1.get_element() == "electric":
                                self.effectiveness_pokemon2 = "Normal"
                            elif pokemon1.get_element() == "rock":
                                self.effectiveness_pokemon2 = "Normal"

                        elif self.chosen_skill_pokemon2.get_element() == "electric":
                            if pokemon1.get_element() == "water":
                                self.effectiveness_pokemon2 = "Super Effective"
                            elif pokemon1.get_element() == "fire":
                                self.effectiveness_pokemon2 = "Super Effective"
                            elif pokemon1.get_element() == "grass":
                                self.effectiveness_pokemon2 = "Normal"
                            elif pokemon1.get_element() == "rock":
                                self.effectiveness_pokemon2 = "Not Very Effective"

                        elif self.chosen_skill_pokemon2.get_element() == "rock":
                            if pokemon1.get_element() == "water":
                                self.effectiveness_pokemon2 = "Not Very Effective"
                            elif pokemon1.get_element() == "fire":
                                self.effectiveness_pokemon2 = "Super Effective"
                            elif pokemon1.get_element() == "grass":
                                self.effectiveness_pokemon2 = "Super Effective"
                            elif pokemon1.get_element() == "electric":
                                self.effectiveness_pokemon2 = "Not Very Effective"

                        damage_taken_pokemon2 = max(0, damage_pokemon1 - pokemon2.get_armor())
                        damage_taken_pokemon1 = max(0, damage_pokemon2 - pokemon1.get_armor())

                        newhp2 = max(0, pokemon2.get_hp() - damage_taken_pokemon2)
                        newhp1 = max(0, pokemon1.get_hp() - damage_taken_pokemon1)

                        pokemon2.set_hp(newhp2)
                        pokemon1.set_hp(newhp1)

                        self.playerCurr_hp_label.destroy()
                        self.enemyCurr_hp_label.destroy()

                        self.playerCurr_hp_label = ttk.Label(square_window, text=f"{player_pokemon.get_hp()}", font=("Pokemon", 30))
                        self.playerCurr_hp_label.place(x=358, y=325)

                        self.enemyCurr_hp_label = ttk.Label(square_window, text=f"{enemy_pokemon.get_hp()}", font=("Pokemon", 30))
                        self.enemyCurr_hp_label.place(x=125, y=20)

                        log()

                    def log():
                        self.name_label.destroy()
                        self.text_box.destroy()
                        self.spinbox.destroy()
                        self.spin_label.destroy()
                        self.attack_button.destroy()
                        self.skill_info_textbox.destroy()
                        for button in self.skill_buttons:
                            button.destroy()

                        next_background_path = ASSETS_PATH / "standby.png"
                        next_background_image = Image.open(next_background_path)
                        resized_next_background = next_background_image.resize((window_size, window_size))
                        tk_next_background = ImageTk.PhotoImage(resized_next_background)

                        background_label.configure(image=tk_next_background)
                        background_label.image = tk_next_background

                        image_size = 200
                        player_pokemon_image_path = ASSETS_PATH / f"{self.selected_pokemon1}.gif"
                        player_pokemon_image = Image.open(player_pokemon_image_path)
                        resized_player_pokemon_image = player_pokemon_image.resize((image_size, image_size))
                        tk_player_pokemon_image = ImageTk.PhotoImage(resized_player_pokemon_image)

                        self.player_pokemon_label = tk.Label(square_window, image=tk_player_pokemon_image, text=self.selected_pokemon1.upper(), compound=tk.BOTTOM, font=("Pokemon",12, "bold"))
                        self.player_pokemon_label.image = tk_player_pokemon_image
                        self.player_pokemon_label.place(x=30, y=170)

                        
                        log_text = (
                            f"{pokemon1.get_name()} using {self.chosen_skill_pokemon1.get_name()}, dealing "
                            f"{(pokemon2.get_max_hp() - pokemon2.get_hp())} damage to {pokemon2.get_name()}, \n{self.effectiveness_pokemon1}\n"
                            f"{pokemon2.get_name()} using {self.chosen_skill_pokemon2.get_name()}, dealing "
                            f"{(pokemon1.get_max_hp() - pokemon1.get_hp())} damage to {pokemon1.get_name()}, \n{self.effectiveness_pokemon2}\n"
                            f"Player Pokemon ({pokemon1.get_name()}, {pokemon1.get_hp()}/{pokemon1.get_max_hp()})\n"
                            f"Enemy Pokemon ({pokemon2.get_name()},  {pokemon2.get_hp()}/{pokemon2.get_max_hp()})\n\n"
                        )

                        self.text_box = tk.Text(square_window, height=7, width=68)
                        self.text_box.place(x=20, y=450)
                        self.text_box.insert(tk.END, log_text)

                        self.next_button = ttk.Button(square_window, text="Next Turn", command=battle_turn)
                        self.next_button.place(x=260, y=550)

                def display_winner():
                    global victorySong
                    self.battleSong.stop()
                    self.text_box.destroy()
                    self.next_button.destroy()

                    song5 = ASSETS_PATH / "victorySong.mp3"
                    victorySong = vlc.MediaPlayer(song5)
                    victorySong.play()

                    self.next_button = ttk.Button(square_window, text="Home", command=self.restart)
                    self.next_button.place(x=300, y=540)

                    if pokemon1.get_hp() <= 0:
                        text = "player-defeat.png"
                        namewinner = self.selected_pokemon1
                        self.player_pokemon_label.destroy()
                        self.playerCurr_hp_label.destroy()
                        self.playerMaxhp_label.destroy()

                    elif pokemon2.get_hp() <= 0 :
                        text = "enemy-defeat.png"
                        namewinner = self.selected_pokemon2
                        self.enemy_pokemon_label.destroy()
                        self.enemyCurr_hp_label.destroy()
                        self.enemyMaxhp_label.destroy()

                    next_background_path = ASSETS_PATH / text
                    next_background_image = Image.open(next_background_path)
                    resized_next_background = next_background_image.resize((window_size, window_size))
                    tk_next_background = ImageTk.PhotoImage(resized_next_background)

                    background_label.configure(image=tk_next_background)
                    background_label.image = tk_next_background

                    enemy_pokemon_font_path = ASSETS_PATH / f"nama-{namewinner}.png"
                    enemy_pokemon_font = Image.open(enemy_pokemon_font_path)
                    resized_enemy_pokemon_font = enemy_pokemon_font.resize((150, 45))
                    tk_enemy_pokemon_font = ImageTk.PhotoImage(resized_enemy_pokemon_font)

                    self.enemy_pokemon_label = tk.Label(square_window, image=tk_enemy_pokemon_font)
                    self.enemy_pokemon_label.image = tk_enemy_pokemon_font
                    self.enemy_pokemon_label.place(x=215, y=448)


                    if pokemon1.get_hp() <= 0:
                        print(f"{pokemon1.get_name()} is KO'd, {pokemon2.get_name()} WINS")
                    else:
                        print(f"{pokemon2.get_name()} is KO'd, {pokemon1.get_name()} WINS")

                battle_turn()                  



    def run_clicked(self):
        victorySong.stop()
        square_window.destroy()

    def restart(self):
        victorySong.stop()
        square_window.destroy()
        main()

def main():
    global square_window, window_size, background_label, start_button, startSong
    square_window = tk.Tk()
    square_window.title("Pokemon Red")

    window_size = 600
    square_window.geometry(f"{window_size}x{window_size}")

    background_path = ASSETS_PATH / "start.png"
    background_image = Image.open(background_path)
    resized_background = background_image.resize((window_size, window_size))
    tk_background = ImageTk.PhotoImage(resized_background)

    background_label = tk.Label(square_window, image=tk_background)
    background_label.place(x=0, y=0, relwidth=1, relheight=1)

    pokemon_battle_ui = PokemonBattleUI(square_window)

    start_button = ttk.Button(square_window, text="Start", command=pokemon_battle_ui.start_battle)
    start_button.pack(pady=10)
    start_button.place(x=250, y=560)

    song1 = ASSETS_PATH / "startsong.mp3"
    startSong = vlc.MediaPlayer(song1)
    startSong.play()

    square_window.mainloop()

if __name__ == "__main__":
    main()