import random
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
from pathlib import Path

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / "assets"

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

    def calculate_damage(self, skill, opponent_element):
        damage = skill.get_damage() + self.get_atk()

        if skill.get_element() == "normal":
            effectiveness = 1.0
        elif skill.get_element() == "grass" and self.is_super_effective(opponent_element):
            effectiveness = 2.0
        elif skill.get_element() == "grass" and self.is_not_very_effective(opponent_element):
            effectiveness = 0.5
        elif skill.get_element() == "fire" and self.is_super_effective(opponent_element):
            effectiveness = 2.0
        elif skill.get_element() == "fire" and self.is_not_very_effective(opponent_element):
            effectiveness = 0.5
        elif skill.get_element() == "water" and self.is_super_effective(opponent_element):
            effectiveness = 2.0
        elif skill.get_element() == "water" and self.is_not_very_effective(opponent_element):
            effectiveness = 0.5
        else:
            effectiveness = 1.0

        final_damage = damage * effectiveness

        return int(final_damage)

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
    
    def get_skills(self):
        return self._skills
    
    def get_skills_info(self):
        skills_info = []
        for skill in self._skills:
            skill_info = {
                'name': skill.get_name(),
                'damage': skill.get_damage(),
                'element': skill.get_element()
            }
            skills_info.append(skill_info)
        return skills_info

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

    def calculate_damage(self, skill, opponent_element):
        return super().calculate_damage(skill, opponent_element)

    def is_super_effective(self, opponent_element):
        return opponent_element == "water"

    def is_not_very_effective(self, opponent_element):
        return opponent_element == "fire"

class Ivysaur(Pokemon):
    def __init__(self):
        super().__init__("Ivysaur", "grass", 55, 59, 59)
        self._skills = [GrassSkill("Sleep Powder", 10), GrassSkill("Seed Bomb", 20), GrassSkill("Solar Beam", 25)]

    def calculate_damage(self, skill, opponent_element):
        return super().calculate_damage(skill, opponent_element)

    def is_super_effective(self, opponent_element):
        return opponent_element == "water"

    def is_not_very_effective(self, opponent_element):
        return opponent_element == "fire"

class Charmander(Pokemon):
    def __init__(self):
        super().__init__("Charmander", "fire", 39, 52, 43)
        self._skills = [NormalSkill("Growl", 5), NormalSkill("Scratch", 10), FireSkill("Ember", 20)]

    def calculate_damage(self, skill, opponent_element):
        return super().calculate_damage(skill, opponent_element)

    def is_super_effective(self, opponent_element):
        return opponent_element == "grass"

    def is_not_very_effective(self, opponent_element):
        return opponent_element == "water"

class Charmeleon(Pokemon):
    def __init__(self):
        super().__init__("Charmeleon", "fire", 49, 62, 53)
        self._skills = [NormalSkill("Slash", 10), FireSkill("Fire Fang", 15), FireSkill("Fire Spin", 25)]

    def calculate_damage(self, skill, opponent_element):
        return super().calculate_damage(skill, opponent_element)

    def is_super_effective(self, opponent_element):
        return opponent_element == "grass"

    def is_not_very_effective(self, opponent_element):
        return opponent_element == "water"

class Squirtle(Pokemon):
    def __init__(self):
        super().__init__("Squirtle", "water", 44, 48, 65)
        self._skills = [NormalSkill("Tackle", 5), NormalSkill("Tail Whip", 10), WaterSkill("Water Gun", 20)]

    def calculate_damage(self, skill, opponent_element):
        return super().calculate_damage(skill, opponent_element)

    def is_super_effective(self, opponent_element):
        return opponent_element == "fire"

    def is_not_very_effective(self, opponent_element):
        return opponent_element == "grass"

class Wartortle(Pokemon):
    def __init__(self):
        super().__init__("Wartortle", "water", 54, 58, 75)
        self._skills = [NormalSkill("Bite", 10), WaterSkill("Water Pulse", 20), WaterSkill("Rain Dance", 25)]

    def calculate_damage(self, skill, opponent_element):
        return super().calculate_damage(skill, opponent_element)

    def is_super_effective(self, opponent_element):
        return opponent_element == "fire"

    def is_not_very_effective(self, opponent_element):
        return opponent_element == "grass"

class PokemonBattleUI:
    def __init__(self, master):
        self.master = master
        self.player_pokemon = None
        self.enemy_pokemon = None
        self.text_box = None
        self.player_pokemon_label = None
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
            ASSETS_PATH / "wartortle.gif"
        ]

        pokemon_images = [Image.open(path) for path in image_paths]
        resized_images = [img.resize((100, 100), Image.ANTIALIAS) for img in pokemon_images]
        tk_images = [ImageTk.PhotoImage(img) for img in resized_images]

        return tk_images
    
    def start_battle(self):
        next_background_path = ASSETS_PATH / "nextstart.png"
        next_background_image = Image.open(next_background_path)
        resized_next_background = next_background_image.resize((window_size, window_size), Image.ANTIALIAS)
        tk_next_background = ImageTk.PhotoImage(resized_next_background)

        background_label.configure(image=tk_next_background)
        background_label.image = tk_next_background

        start_button.destroy()

        self.fight_button_image_path = ASSETS_PATH / "fight.png"
        fight_image = Image.open(self.fight_button_image_path)
        resized_fight_image = fight_image.resize((100, 50), Image.ANTIALIAS)
        tk_fight_image = ImageTk.PhotoImage(resized_fight_image)

        self.fight_button = ttk.Button(square_window, image=tk_fight_image, command=self.choose)
        self.fight_button.image = tk_fight_image
        self.fight_button.place(x=400, y=430)

        self.run_button_image_path = ASSETS_PATH / "run.png"
        run_image = Image.open(self.run_button_image_path)
        resized_run_image = run_image.resize((70, 50), Image.ANTIALIAS)
        tk_run_image = ImageTk.PhotoImage(resized_run_image)

        self.run_button = ttk.Button(square_window, image=tk_run_image, command=self.run_clicked)
        self.run_button.image = tk_run_image
        self.run_button.place(x=400, y=510)

    def choose(self):

        next_background_path = ASSETS_PATH / "choose.png"
        next_background_image = Image.open(next_background_path)
        resized_next_background = next_background_image.resize((window_size, window_size), Image.ANTIALIAS)
        tk_next_background = ImageTk.PhotoImage(resized_next_background)

        background_label.configure(image=tk_next_background)
        background_label.image = tk_next_background

        self.fight_button.destroy()
        self.run_button.destroy()

        pokemon_images = self.load_pokemon_images()
        combo_box_values = ["Bulbasaur", "Ivysaur", "Charmander", "Charmeleon", "Squirtle", "Wartortle"]
        self.combo_box1 = ttk.Combobox(square_window, values=combo_box_values)
        self.combo_box1.set("Choose Player")
        self.combo_box1.place(x=100, y=520)

        combo_box_values = ["Bulbasaur", "Ivysaur", "Charmander", "Charmeleon", "Squirtle", "Wartortle"]
        self.combo_box2 = ttk.Combobox(square_window, values=combo_box_values)
        self.combo_box2.set("Choose Enemy")
        self.combo_box2.place(x=350, y=520)

        self.enter_button = ttk.Button(square_window, text="Enter", command=self.battle_ui)
        self.enter_button.place(x=260, y=540)

        self.pokemon_images_labels = []
        for i, (img, name) in enumerate(zip(pokemon_images, combo_box_values)):
            row, col = divmod(i, 3)
            label = tk.Label(square_window, image=img, text=name, compound=tk.BOTTOM)
            label.image = img
            label.grid(row=row, column=col, padx=40, pady=40)
            self.pokemon_images_labels.append(label)

    def battle_ui(self):
        
        self.selected_pokemon1 = self.combo_box1.get()
        self.pok1 = self.selected_pokemon1

        self.selected_pokemon2 = self.combo_box2.get()
        self.pok2 = self.selected_pokemon2
        
        player_pokemon = self.get_pokemon_by_choice(self.pok1)
        enemy_pokemon = self.get_pokemon_by_choice(self.pok2)

        next_background_path = ASSETS_PATH / "standby.png"
        next_background_image = Image.open(next_background_path)
        resized_next_background = next_background_image.resize((window_size, window_size), Image.ANTIALIAS)
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
        resized_player_pokemon_image = player_pokemon_image.resize((image_size, image_size), Image.ANTIALIAS)
        tk_player_pokemon_image = ImageTk.PhotoImage(resized_player_pokemon_image)

        self.player_pokemon_label = tk.Label(square_window, image=tk_player_pokemon_image, text=self.selected_pokemon1.upper(), compound=tk.BOTTOM, font=("Pokemon",12, "bold"))
        self.player_pokemon_label.image = tk_player_pokemon_image
        self.player_pokemon_label.place(x=30, y=170)

        # Enemy Pokemon
        enemy_pokemon_image_path = ASSETS_PATH / f"{self.selected_pokemon2}.gif"
        enemy_pokemon_image = Image.open(enemy_pokemon_image_path)
        resized_enemy_pokemon_image = enemy_pokemon_image.resize((image_size, image_size), Image.ANTIALIAS)
        tk_enemy_pokemon_image = ImageTk.PhotoImage(resized_enemy_pokemon_image)

        enemy_pokemon_label = tk.Label(square_window, image=tk_enemy_pokemon_image, text=self.selected_pokemon2.upper(), compound=tk.BOTTOM, font=("Pokemon",12, "bold"))
        enemy_pokemon_label.image = tk_enemy_pokemon_image
        enemy_pokemon_label.place(x=360, y=20)
        self.pokemon_images_labels = [self.player_pokemon_label, enemy_pokemon_label]
        
        self.text_box = tk.Text(square_window, height=8, width=60)
        self.text_box.place(x=30, y=425)
        self.text_box.insert(tk.END, f"Battle between {self.selected_pokemon1} and {self.selected_pokemon2}!\n\n")

        self.next_button = ttk.Button(square_window, text="Next", command=lambda: battle(player_pokemon, enemy_pokemon))
        self.next_button.place(x=260, y=550)
        
        def battle(pokemon1, pokemon2):

                self.player_pokemon_label.destroy()
                self.text_box.destroy()
                self.next_button.destroy()
                
                next_background_path = ASSETS_PATH / "skill2.png"
                next_background_image = Image.open(next_background_path)
                resized_next_background = next_background_image.resize((window_size, window_size), Image.ANTIALIAS)
                tk_next_background = ImageTk.PhotoImage(resized_next_background)

                background_label.configure(image=tk_next_background)
                background_label.image = tk_next_background

                def battle_turn():

                    if pokemon1.get_hp() <= 0 or pokemon2.get_hp() <= 0:
                        display_winner()
                        return

                    try:
                        self.player_pokemon_label1.destroy()
                        self.text_box.destroy()
                        self.next_button.destroy()
                    except:
                        pass
                    # Pilihan skill untuk pokemon1
                    self.skill_info_textbox = tk.Text(square_window, height=5, width=30)
                    self.skill_info_textbox.place(x=30, y=310)
                    self.skill_buttons = []

                    for i, skill in enumerate(pokemon1._skills, start=1):
                        button = tk.Button(square_window, text=f"{i}.{skill.get_name()}", command=lambda s=skill, p=pokemon1: show_skill_info(p, s))
                        button.place(x=25, y=425 + i * 30)
                        self.skill_buttons.append(button)

                    def show_skill_info(pokemon, skill):
                        info = f"{pokemon.get_name()}'s skills:\n\n"
                        info += f"Name: {skill.get_name()}\n"
                        info += f"Damage: {skill.get_damage()}\n"
                        info += f"Element: {skill.get_element()}"
                        self.skill_info_textbox.delete(1.0, tk.END)  # Clear previous content
                        self.skill_info_textbox.insert(tk.END, info)

                    txtskill = f"Choose a skill for {pokemon1.get_name()} (1-{len(pokemon1._skills)}):"
                    self.name_label = ttk.Label(square_window, text=txtskill, font=("Pokemon", 14))
                    self.name_label.place(x=150, y=440)

                    self.spin_label = ttk.Label(square_window, text="Pilih Skill ke- :", font=("Pokemon", 14))
                    self.spin_label.place(x=150, y=490)

                    spinbox_var = tk.IntVar()
                    self.spinbox = ttk.Spinbox(square_window, from_=1, to=len(pokemon1._skills), textvariable=spinbox_var, width=5, font=("Pokemon", 14))
                    self.spinbox.place(x=270, y=490)

                    self.attack_button = ttk.Button(square_window, text="Attack", command=lambda: use_skill())
                    self.attack_button.place(x=150, y=540)

                    def use_skill():


                        self.chosen_skill_pokemon1 = pokemon1._skills[int(spinbox_var.get()) - 1]

                        # Pilihan skill untuk pokemon2 (random)
                        self.chosen_skill_pokemon2 = random.choice(pokemon2._skills)

                        damage_pokemon1 = pokemon1.calculate_damage(self.chosen_skill_pokemon1, pokemon2.get_element())
                        damage_pokemon2 = pokemon2.calculate_damage(self.chosen_skill_pokemon2, pokemon1.get_element())

                        # Pengurangan HP berdasarkan damage dan armor
                        self.effectiveness_pokemon1 = "Normal"
                        if self.chosen_skill_pokemon1.get_element() == "water" and pokemon2.get_element() == "fire":
                            self.effectiveness_pokemon1 = "Super Effective"
                        elif self.chosen_skill_pokemon1.get_element() == "fire" and pokemon2.get_element() == "grass":
                            self.effectiveness_pokemon1 = "Super Effective"
                        elif self.chosen_skill_pokemon1.get_element() == "grass" and pokemon2.get_element() == "water":
                            self.effectiveness_pokemon1 = "Super Effective"
                        elif self.chosen_skill_pokemon1.get_element() == "water" and pokemon2.get_element() == "grass":
                            self.effectiveness_pokemon1 = "Not Very Effective"
                        elif self.chosen_skill_pokemon1.get_element() == "fire" and pokemon2.get_element() == "water":
                            self.effectiveness_pokemon1 = "Not Very Effective"
                        elif self.chosen_skill_pokemon1.get_element() == "grass" and pokemon2.get_element() == "fire":
                            self.effectiveness_pokemon1 = "Not Very Effective"

                        self.effectiveness_pokemon2 = "Normal"
                        if self.chosen_skill_pokemon2.get_element() == "water" and pokemon1.get_element() == "fire":
                            self.effectiveness_pokemon2 = "Super Effective"
                        elif self.chosen_skill_pokemon2.get_element() == "fire" and pokemon1.get_element() == "grass":
                            self.effectiveness_pokemon2 = "Super Effective"
                        elif self.chosen_skill_pokemon2.get_element() == "grass" and pokemon1.get_element() == "water":
                            self.effectiveness_pokemon2 = "Super Effective"
                        elif self.chosen_skill_pokemon2.get_element() == "water" and pokemon1.get_element() == "grass":
                            self.effectiveness_pokemon2 = "Not Very Effective"
                        elif self.chosen_skill_pokemon2.get_element() == "fire" and pokemon1.get_element() == "water":
                            self.effectiveness_pokemon2 = "Not Very Effective"
                        elif self.chosen_skill_pokemon2.get_element() == "grass" and pokemon1.get_element() == "fire":
                            self.effectiveness_pokemon2 = "Not Very Effective"

                        damage_taken_pokemon2 = max(0, damage_pokemon1 - pokemon2.get_armor())
                        damage_taken_pokemon1 = max(0, damage_pokemon2 - pokemon1.get_armor())

                        pokemon2._hp = max(0, pokemon2.get_hp() - damage_taken_pokemon2)
                        pokemon1._hp = max(0, pokemon1.get_hp() - damage_taken_pokemon1)

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
                        resized_next_background = next_background_image.resize((window_size, window_size), Image.ANTIALIAS)
                        tk_next_background = ImageTk.PhotoImage(resized_next_background)

                        background_label.configure(image=tk_next_background)
                        background_label.image = tk_next_background

                        image_size = 200
                        player_pokemon_image_path = ASSETS_PATH / f"{self.selected_pokemon1}.gif"
                        player_pokemon_image = Image.open(player_pokemon_image_path)
                        resized_player_pokemon_image = player_pokemon_image.resize((image_size, image_size), Image.ANTIALIAS)
                        tk_player_pokemon_image = ImageTk.PhotoImage(resized_player_pokemon_image)

                        enemy_pokemon_image_path = ASSETS_PATH / f"{self.selected_pokemon2}.gif"
                        enemy_pokemon_image = Image.open(enemy_pokemon_image_path)
                        resized_enemy_pokemon_image = enemy_pokemon_image.resize((image_size, image_size), Image.ANTIALIAS)
                        tk_enemy_pokemon_image = ImageTk.PhotoImage(resized_enemy_pokemon_image)

                        self.player_pokemon_label1 = tk.Label(square_window, image=tk_player_pokemon_image)
                        self.player_pokemon_label1.image = tk_player_pokemon_image
                        self.player_pokemon_label1.place(x=30, y=170)

                        enemy_pokemon_label = tk.Label(square_window, image=tk_enemy_pokemon_image)
                        enemy_pokemon_label.image = tk_enemy_pokemon_image
                        enemy_pokemon_label.place(x=360, y=20)

                        self.pokemon_images_labels = [self.player_pokemon_label1, enemy_pokemon_label]

                        
                        log_text = (
                            f"{pokemon1.get_name()} using {self.chosen_skill_pokemon1.get_name()}, dealing "
                            f"{(pokemon2.get_max_hp() - pokemon2.get_hp())} damage to {pokemon2.get_name()}, {self.effectiveness_pokemon1}\n"
                            f"{pokemon2.get_name()} using {self.chosen_skill_pokemon2.get_name()}, dealing "
                            f"{(pokemon1.get_max_hp() - pokemon1.get_hp())} damage to {pokemon1.get_name()}, {self.effectiveness_pokemon2}\n"
                            f"Player Pokemon ({pokemon1.get_name()}, {pokemon1.get_hp()}/{pokemon1.get_max_hp()})\n"
                            f"Enemy Pokemon ({pokemon2.get_name()},  {pokemon2.get_hp()}/{pokemon2.get_max_hp()})\n\n"
                        )

                        self.text_box = tk.Text(square_window, height=4, width=65)
                        self.text_box.place(x=20, y=460)
                        self.text_box.insert(tk.END, log_text)

                        self.next_button = ttk.Button(square_window, text="Next Turn", command=battle_turn)
                        self.next_button.place(x=260, y=550)

                def display_winner():
                    enemy_pokemon_label.destroy()
                    next_background_path = ASSETS_PATH / "defeat.png"
                    next_background_image = Image.open(next_background_path)
                    resized_next_background = next_background_image.resize((window_size, window_size), Image.ANTIALIAS)
                    tk_next_background = ImageTk.PhotoImage(resized_next_background)

                    background_label.configure(image=tk_next_background)
                    background_label.image = tk_next_background

                    if pokemon1.get_hp() <= 0:
                        print(f"{pokemon1.get_name()} is KO'd, {pokemon2.get_name()} WINS")
                    else:
                        print(f"{pokemon2.get_name()} is KO'd, {pokemon1.get_name()} WINS")

                # Start the battle by initiating the first turn
                battle_turn()                  



    def run_clicked(self):
        square_window.destroy()

# Create the Tkinter window
square_window = tk.Tk()
square_window.title("Pokemon Red")

# Set the window size
window_size = 600
square_window.geometry(f"{window_size}x{window_size}")

# Load the background image
background_path = ASSETS_PATH / "start.png"
background_image = Image.open(background_path)
resized_background = background_image.resize((window_size, window_size), Image.ANTIALIAS)
tk_background = ImageTk.PhotoImage(resized_background)

# Display the background image in the label
background_label = tk.Label(square_window, image=tk_background)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

# Create an instance of the PokemonBattleUI class
pokemon_battle_ui = PokemonBattleUI(square_window)

start_button = ttk.Button(square_window, text="Start", command=pokemon_battle_ui.start_battle)
start_button.pack(pady=10)
start_button.place(x=250, y=560)
# Create the "Start" button
# Run the Tkinter main loop
square_window.mainloop()