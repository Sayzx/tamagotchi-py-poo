from creature import Creature
from actions import ActionManager
from events import EventManager
from storage import Storage
from ui.display import show_creature_ascii
from creature import create_crature


class Game:
    def __init__(self):
        self.storage = Storage()
        self.creature = None
        self.action_manager = ActionManager()
        self.event_manager = EventManager()
    
    def create_creature(self):
        name = input("Entrez le nom de votre créature : ")
        while name.isdigit() or len(name) < 3 or len(name) > 12:
            print("Nom invalide. Réessayez. [Dois contenir entre 3 et 12 caractères et ne doit pas être un chiffre]")
            name = input("Entrez le nom de votre créature : ")
        
        creature_type = input("Choisissez le type (chaton,chiot,dragon,poisson,rhino,singe) : ")
        while creature_type not in ["chaton", "chiot", "dragon", "poisson", "rhino", "singe"]:
            print("Type de créature Invalide. Réessayez.")
            creature_type = input("Choisissez le type (chaton,chiot,dragon,poisson,rhino,singe) : ")
            
        self.creature = create_crature(name, creature_type)  
    def load_creature(self, data):
        self.creature = Creature(data["name"], data["type"])
        self.creature.hungry = data["hungry"]
        self.creature.energy = data["energy"]
        self.creature.happy = data["happy"]
        self.creature.heal = data["heal"]
        self.creature.age = data["age"]
        self.creature.lvl = data["lvl"]
    
    def run(self):
        print("────────────────────────")
        print("Bienvenue dans le Simulateur de créature virtuelle !")
        print("Vous allez devoir vous occuper d'une créature virtuelle.")
        print("────────────────────────")
        saved_data = self.storage.load()
        if saved_data:
            use_save = input("Une sauvegarde existe. Voulez-vous la charger ? (o/n) : ")
            if use_save.lower() == "o":
                self.load_creature(saved_data)
                print("Sauvegarde chargée.")
            else:
                self.create_creature()
        else:
            self.create_creature()
        
        while True:
            print("\nEtat de la créature:")
            print(self.creature.status())
            
            if self.creature.heal >= -40:
                self.creature.vieillir()
            elif self.creature.heal <= 0:
                self.creature.death("Santé trop faible.")
                break
            elif self.creature.hungry <= 0:
                self.creature.death("Faim trop faible.")
                break
            elif self.creature.happy <= 0:
                self.creature.death("Suicide")
            elif self.creature.energy <= 0:
                self.creature.forceSleep()
            else:
                print(f"{self.creature.name} ne vieillit pas car sa santé est trop faible.")
            
            self.event_manager.apply_random_event(self.creature)
            
            print("\nActions disponibles :")
            print("1. Nourrir")
            print("2. Jouer")
            print("3. Dormir")
            print("4. Soigner")
            print("5. Afficher la créature")
            print("6. Sauvegarder et quitter")
            
            choix = input("Votre choix : ")
            
            if choix == "1":
                self.action_manager.nourrir(self.creature)
            elif choix == "2":
                self.action_manager.jouer(self.creature)
            elif choix == "3":
                self.action_manager.dormir(self.creature)
            elif choix == "4":
                self.action_manager.soigner(self.creature)
            elif choix == "5":
                show_creature_ascii(self.creature)
            elif choix == "6":
                self.storage.save(self.creature)
                print("Jeu sauvegardé. Au revoir !")
                break
            else:
                print("Choix invalide. Réessayez.")
