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
            print("\n────────────────────────")
            name = input("Enter your creature's name: ")
            print("────────────────────────")
            if not name.isdigit() and 3 <= len(name) <= 12:
                break
            print("\033[91mInvalid name. Must be 3-12 characters and not a number.\033[0m")
        
        valid_types = ["chaton", "chiot", "dragon", "poisson", "rhino", "singe"]
        print("────────────────────────")
        while (creature_type := input("Choose a type (chaton, chiot, dragon, poisson, rhino, singe): ")) not in valid_types:
            print("\033[91mInvalid creature type. Try again.\033[0m")
        
        self.creature = create_crature(name, creature_type)
    
    def load_creature(self, data):
        """Loads a creature from saved data."""
        self.creature = Creature(data["name"], data["type"])
        for attr in ["hungry", "energy", "happy", "heal", "age", "lvl"]:
            setattr(self.creature, attr, data[attr])
    
    def run(self):
        print("\033[H\033[J")
        print("\033[92m\nWelcome to the Virtual Creature Simulator!\nTake care of your virtual pet.\033[0m")
        if (saved_data := self.storage.load()) and input("\033[93mSave found. Load it? (y/n): \033[0m").lower() == "y":
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

           #The use of lambda here is to avoid else if or switch cases
            choices = {
                "1": lambda: self.action_manager.feed(self.creature),
                "2": lambda: self.action_manager.play(self.creature),
                "3": lambda: self.action_manager.sleep(self.creature),
                "4": lambda: self.action_manager.heal(self.creature),
                "5": lambda: show_creature_ascii(self.creature),
                "6": lambda: (self.storage.save(self.creature), print("\033[92mGame saved. Goodbye!\033[0m"), exit()),
                "7": lambda: self.action_manager.givestats(self.creature),
                "8": lambda: self.creature.say(),
                "9": lambda: print("\033[93m\nHelp Menu:\033[0m\n────────────────────────\n\033[94m1. Feed:\033[0m Feed your creature to reduce hunger.\n\033[94m2. Play:\033[0m Play with your creature to increase happiness.\n\033[94m3. Sleep:\033[0m Put your creature to sleep to restore energy.\n\033[94m4. Heal:\033[0m Heal your creature to restore health.\n\033[94m5. Show:\033[0m Display your creature's ASCII art.\n\033[94m6. Save & Quit:\033[0m Save the game and exit.\n\033[94m7. Edit Stats:\033[0m Edit your creature's stats.\n\033[94m8. Say Sound:\033[0m Make your creature say a sound.\n\033[94m9. Help:\033[0m Show this help menu.\n────────────────────────"),
            }
            
            print("\n\033[94m1. Feed\033[0m  \033[94m2. Play\033[0m  \033[94m3. Sleep\033[0m  \033[94m4. Heal\033[0m  \033[94m5. Show\033[0m  \033[94m6. Save & Quit\033[0m  \033[94m7. Edit Stats\033[0m  \033[94m8. Say Sound\033[0m  \033[94m9. Help\033[0m")
            choice = input("Your choice: ")
            print("\033[H\033[J")  # Clear the screen
            choices.get(choice, lambda: print("Invalid choice. Try again."))()

