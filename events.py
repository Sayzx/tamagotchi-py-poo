import random

class EventManager:
    EVENTS = {
        "maladie": {
            "message": "Oh non ! Votre créature est tombée malade.(Santé -20)",
            "effects": {"heal": -15},
            "random_choice": False
        },
        "meet": {
            "message": ["Votre créature a rencontré une autre créature, cela a amélioré son bonheur.(+10 bonheur)",
                        "La rencontre n'a pas été très bonne. Elle s'est embrouillée.(-5 bonheur)"],
            "effects": [{"happy": 10}, {"happy": -5}],
            "random_choice": True
        },
        "date": {
            "message": ["Votre créature a un rendez-vous romantique.\nLe rendez-vous a été un succès ! (+20 bonheur)",
                        "Votre créature a un rendez-vous romantique.\nLe rendez-vous a échoué.(-10 bonheur)"],
            "effects": [{"happy": 20}, {"happy": -10}],
            "random_choice": True
        },
        "party": {
            "message": ["Votre créature est invitée à une soirée.\nLa soirée s'est bien passée.(+10 bonheur)",
                        "Votre créature est invitée à une soirée.\nLa soirée a été un peu trop arrosée... (-10 bonheur, -10 santé)"],
            "effects": [{"happy": 10}, {"happy": -10, "heal": -10}],
            "random_choice": True
        },
        "rain": {
            "message": "Il pleut, votre créature est tombée malade et a perdu du bonheur.(-10 bonheur, -10 santé)",
            "effects": {"heal": -10, "happy": -10},
            "random_choice": False
        },
        "rien": {
            "message": "Rien ne se passe.",
            "effects": {},
            "random_choice": False
        },
    }

    def apply_random_event(self, creature):
        event = random.choice(list(self.EVENTS.keys()))
        event_data = self.EVENTS[event]

        if event_data["random_choice"]:
            index = random.choice([0, 1])
            print("────────────────────────")
            print("[NOUVELLE ÉVÈNEMENT DETECTÉ]")
            print(event_data["message"][index])
            print("────────────────────────")
            for key, value in event_data["effects"][index].items():
                setattr(creature, key, max(0, getattr(creature, key) + value))
        else:
            print(event_data["message"])
            for key, value in event_data["effects"].items():
                setattr(creature, key, max(0, getattr(creature, key) + value))
