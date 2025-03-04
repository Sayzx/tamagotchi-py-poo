from creature import Creature, create_crature
from actions import ActionManager
from events import EventManager
from storage import Storage
from ui.display import show_creature_ascii
import random

class Game:
    def __init__(self):
        self.storage = Storage()
        self.creature = None
        self.action_manager = ActionManager()
        self.event_manager = EventManager()
    
    def create_creature(self):
        while True:
            name = input("Enter your creature's name: ")
            if not name.isdigit() and 3 <= len(name) <= 12:
                break
            print("Invalid name. Must be 3-12 characters and not a number.")
        
        valid_types = ["chaton", "chiot", "dragon", "poisson", "rhino", "singe"]
        while (creature_type := input("Choose a type (chaton, chiot, dragon, poisson, rhino, singe): ")) not in valid_types:
            print("Invalid creature type. Try again.")
        
        self.creature = create_crature(name, creature_type)
    
    def load_creature(self, data):
        """Loads a creature from saved data."""
        self.creature = Creature(data["name"], data["type"])
        for attr in ["hungry", "energy", "happy", "heal", "age", "lvl"]:
            setattr(self.creature, attr, data[attr])
    
    def run(self):
        print("\033[H\033[J")
        print("\nWelcome to the Virtual Creature Simulator!\nTake care of your virtual pet.")
        if (saved_data := self.storage.load()) and input("Save found. Load it? (y/n): ").lower() == "y":
            self.load_creature(saved_data)
            print("Save loaded.")
        else:
            self.create_creature()
        
        while True:
            print(f"\n{self.creature.status()}")
            
            if self.creature.heal <= 0:
                self.creature.death("Health too low."); break
            if self.creature.hungry <= 0:
                self.creature.death("Starved."); break
            if self.creature.happy <= 0:
                self.creature.death("Suicide."); break
            if self.creature.energy <= 0:
                self.creature.forceSleep()
            elif self.creature.heal >= -40:
                self.creature.vieillir()
            else:
                print(f"{self.creature.name} is too weak to age.")
            if random.randint(1, 3) == 1:
                self.event_manager.apply_random_event(self.creature) # 1 / 3 
            
            choices = {
                "1": lambda: self.action_manager.feed(self.creature),
                "2": lambda: self.action_manager.play(self.creature),
                "3": lambda: self.action_manager.sleep(self.creature),
                "4": lambda: self.action_manager.heal(self.creature),
                "5": lambda: show_creature_ascii(self.creature),
                "6": lambda: (self.storage.save(self.creature), print("Game saved. Goodbye!"), exit()),
                "7": lambda: self.action_manager.givestats(self.creature),
                "8": lambda: self.creature.say()  
            }
            
            print("\n1. feed  2. Play  3. Sleep  4. Heal  5. Show  6. Save & Quit 7. Edit Stats, 8. Say Sound")
            choices.get(input("Your choice: "), lambda: print("Invalid choice. Try again."))()
