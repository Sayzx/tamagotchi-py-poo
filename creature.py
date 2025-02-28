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
        return (f"{self.name} ({self.type})\n"
                f"Faim: {self.hungry}/100\n"
                f"Energie: {self.energy}/100\n"
                f"Bonheur: {self.happy}/100\n"
                f"Santé: {self.heal}/100\n"
                f"Âge: {self.age}\n"
                f"Niveau: {self.lvl}"
                )

    def vieillir(self):
        if self.heal >= -40:
            self.age += 1
            self.energy = max(0, self.energy - 2)
            self.heal = max(-100, self.heal - 1)
        else:
            print(f"{self.name} ne vieillit pas car sa santé est trop faible.")
    
    def death(self, cause):
        print("──────────୨ৎCertificat de MORT୨ৎ──────────")
        print(f"{self.name} est morte à l'âge de {self.age} ans.")
        print("Cause du décès : ", cause)
        print("────────────────────────")

    def forceSleep(self):
        print("────────────────────────")
        print("La créature dort...")

        duration = 20 
        steps = 20  

        for i in range(steps + 1):
            percent = int((i / steps) * 100)
            bar = "█" * i + "-" * (steps - i)  
            sys.stdout.write(f"\r[{bar}] {percent}%")
            sys.stdout.flush()
            time.sleep(duration / steps)

        print("\n+25 d'énergie\n-10 de faim")




# Sous-classes pour les différents types de créatures


class Chaton(Creature):
    def __init__(self, name):
        super().__init__(name, "chaton")
        self.happy += 10  

    def say(self):
        sound_path = os.path.join(os.path.dirname(__file__), "ui", "sound", "miow.mp3")

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

class Chiot(Creature):
    def __init__(self, name):
        super().__init__(name, "chiot")
        self.energy += 10  

class Dragon(Creature):
    def __init__(self, name):
        super().__init__(name, "dragon")
        self.heal += 20  

class Poisson(Creature):
    def __init__(self, name):
        super().__init__(name, "poisson")
        self.energy -= 10  

class Rhino(Creature):
    def __init__(self, name):
        super().__init__(name, "rhino")
        self.heal += 30  

class Singe(Creature):
    def __init__(self, name):
        super().__init__(name, "singe")
        self.happy += 15

# Fonction pour instancier la bonne créature
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
