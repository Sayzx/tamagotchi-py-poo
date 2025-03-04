import time
import sys
import os
import pygame
import threading
class Creature:
    def __init__(self, name, type_creature):
        self.name = name
        self.type = type_creature
        self.hungry = 50  
        self.energy = 50  
        self.happy = 50  
        self.heal = 50    
        self.age = 1       
        self.lvl = 1

    def status(self):
        age_ranges = [(5, "Baby"), (13, "Enfant"), (18, "Ado"), (40, "Jeune")]
        status_age = "Vieux"  

        for limit, label in age_ranges:
            if self.age < limit:
                status_age = label
                break  

        return (
            f"\033[1;34m{self.name} ({self.type})\033[0m\n"
            f"\033[1;31mHungry: {self.hungry}/100\033[0m\n"
            f"\033[1;32mEnergy: {self.energy}/100\033[0m\n"
            f"\033[1;33mHappy: {self.happy}/100\033[0m\n"
            f"\033[1;36mHeal: {self.heal}/100\033[0m\n"
            f"\033[1;35mAge: {self.age} ({status_age})\033[0m\n"
            f"\033[1;37mLevel: {self.lvl}\033[0m"
        )



    def vieillir(self):
        if self.heal >= -40:
            self.age += 1
            self.energy = max(0, self.energy - 2)
            self.heal = max(-100, self.heal - 1)
        else:
            print(f"{self.name} does not age because its health is too low.")
    
    def death(self, cause):
        print("\033[1;31m──────────୨ৎDeath Certificate୨ৎ──────────\033[0m")
        print(f"\033[1;31m{self.name} died at the age of {self.age} years.\033[0m")
        print(f"\033[1;31mDeath cause: {cause}\033[0m")
        print("\033[1;31m────────────────────────\033[0m")

    def forceSleep(self):
        print("────────────────────────")
        print("Your creature is sleeping...")

        duration = 20 
        steps = 20  

        for i in range(steps + 1):
            percent = int((i / steps) * 100)
            bar = "█" * i + "-" * (steps - i)  
            sys.stdout.write(f"\r\033[1;32m[{bar}] {percent}%\033[0m")
            sys.stdout.flush()
            time.sleep(duration / steps)

        print("\n+25 Energy | -10 Hungry")



""" Subclasses for different types of creatures"""
def send_sound(nameaudio):
    sound_path = os.path.join(os.path.dirname(__file__), "ui", "sound", nameaudio)

    if not os.path.exists(sound_path):
        print("⚠️ Fichier audio non trouvé :", sound_path)
        return
    
    def play_sound():
        pygame.init()
        pygame.mixer.init()
        pygame.mixer.music.load(sound_path)
        pygame.mixer.music.set_volume(1.0)  
        pygame.mixer.music.play()
    
    threading.Thread(target=play_sound, daemon=True).start()
    time.sleep(2)
    pygame.mixer.music.stop()


class Chaton(Creature):
    def __init__(self, name):
        super().__init__(name, "chaton")
        self.happy += 10  
    def say(self):
        send_sound("miow.mp3")

class Chiot(Creature):
    def __init__(self, name):
        super().__init__(name, "chiot")
        self.energy += 10  
    def say(self):
        send_sound("woof.mp3")
     
class Dragon(Creature):
    def __init__(self, name):
        super().__init__(name, "dragon")
        self.heal += 20  
    def say(self):
        send_sound("grr.mp3")
    

class Poisson(Creature):
    def __init__(self, name):
        super().__init__(name, "poisson")
        self.energy -= 10  
    def say(self):
        print("The fish is silent.")

class Rhino(Creature):
    def __init__(self, name):
        super().__init__(name, "rhino")
        self.heal += 30  
    def say(self):
        send_sound("roar.mp3")

class Singe(Creature):
    def __init__(self, name):
        super().__init__(name, "singe")
        self.happy += 15
    def say(self):
        send_sound("monkey.mp3")

# Factory function to create a creature
def create_crature(name, type_creature):
    types = {
        "chaton": Chaton,
        "chiot": Chiot,
        "dragon": Dragon,
        "poisson": Poisson,
        "rhino": Rhino,
        "singe": Singe
    }
    return types[type_creature](name)
