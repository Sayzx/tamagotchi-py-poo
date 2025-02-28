import json
import os

class Storage:
    def __init__(self, filepath="data/savegame.json"):
        self.filepath = filepath

    def save(self, creature):
        data = {
            "name": creature.name,
            "type": creature.type,
            "hungry": creature.hungry,
            "energy": creature.energy,
            "happy": creature.happy,
            "heal": creature.heal,
            "age": creature.age,
            "lvl": creature.lvl
        }

        with open(self.filepath, "w") as f:
            json.dump(data, f)
        print("Sauvegarde effectuée.")

    def load(self):
        if not os.path.exists(self.filepath):
            print("Aucune sauvegarde trouvée.")
            return None

        if os.path.getsize(self.filepath) == 0:
            print("Le fichier de sauvegarde est vide.")
            return None

        with open(self.filepath, "r") as f:
            try:
                data = json.load(f)
            except json.JSONDecodeError:
                print("Erreur lors du décodage du fichier de sauvegarde.")
                return None
        return data
