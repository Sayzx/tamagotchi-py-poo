import random

class EventManager:
    EVENTS = {
        "sickness": {
            "message": "Oh no! Your creature has fallen ill. (Health -20)",
            "effects": {"heal": -15},
            "random_choice": False
        },
        "meet": {
            "message": ["Your creature met another creature, which improved its happiness. (+10 happiness)",
                        "The meeting didn't go well. They had a fight. (-5 happiness)"],
            "effects": [{"happy": 10}, {"happy": -5}],
            "random_choice": True
        },
        "date": {
            "message": ["Your creature has a romantic date. The date was a success! (+20 happiness)",
                        "Your creature has a romantic date. The date failed. (-10 happiness)"],
            "effects": [{"happy": 20}, {"happy": -10}],
            "random_choice": True
        },
        "party": {
            "message": ["Your creature is invited to a party. The party went well. (+10 happiness)",
                        "Your creature is invited to a party. The party was a bit too wild... (-10 happiness, -10 health)"],
            "effects": [{"happy": 10}, {"happy": -10, "heal": -10}],
            "random_choice": True
        },
        "rain": {
            "message": "It's raining, your creature got sick and lost happiness. (-10 happiness, -10 health)",
            "effects": {"heal": -10, "happy": -10},
            "random_choice": False
        },
        "nothing": {
            "message": "Nothing happens.",
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
            print("[NEW EVENT DETECTED]")
            print(event_data["message"][index])
            print("────────────────────────")
            for key, value in event_data["effects"][index].items():
                setattr(creature, key, max(0, getattr(creature, key) + value))
        else:
            print(event_data["message"])
            for key, value in event_data["effects"].items():
                setattr(creature, key, max(0, getattr(creature, key) + value))
