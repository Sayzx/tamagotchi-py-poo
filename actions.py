import random
import time

class ActionManager:
    def nourrir(self, creature):
        print("────────────────────────")
        print("You feed your creature")
        creature.hungry = min(100, creature.hungry + 20)
        if creature.hungry > 90:
            creature.heal = max(0, creature.heal - 5)
        print("────────────────────────")

    def jouer(self, creature):
        print("────────────────────────")
        print("Choose a game to play with your creature:")
        print("1. Math game")
        print("2. Memory game")
        print("3. Speed game")

        choix = input("Your choice: ")
        while choix not in ["1", "2", "3"]:
            print("Invalid choice. Try again.")
            choix = input("Your choice: ")

        if choix == "1":
            self.mathgame(creature)
        elif choix == "2":
            self.memorygame(creature)
        else:
            self.jeu_de_rapidite(creature)
        print("────────────────────────")

    def mathgame(self, creature):
        print("Vous jouez à un jeu de calcul.")
        score = 0
        for _ in range(3):
            a, b = random.randint(1, 10), random.randint(1, 10)
            op = random.choice(["+", "-", "*"])
            print(f"Calcul: {a} {op} {b} ?")
            result = int(input("Answer: "))
            correct = eval(f"{a} {op} {b}")
            if result == correct:
                score += 1
        if score >= 2:
            print("Nice ! You Win.\n +10 Happy \n +1 LvL")
            creature.happy = min(100, creature.happy + 10)
            creature.lvl += 1
        else:
            print("You lose.")

    def memorygame(self, creature):
        print("You play a memory game.")
        numbers = [random.randint(1, 10) for _ in range(5)]
        print("Memorize these numbers:")
        print(numbers)
        input("Press Enter to continue.")
        print("\n" * 100) 
        print("Enter the numbers you remember.")
        for i, number in enumerate(numbers, 1):
            user_number = int(input(f"Number {i} : "))
            if user_number != number:
                print("You lose.")
                break
        else:
            print("Well done ! You Win.\n +20 Happy \n +1 LvL")
            creature.happy = min(100, creature.happy + 20)
            creature.lvl += 1

    def fastgame(self, creature):
        print("You play a speed game.")
        number = random.randint(1, 10)
        print("Memorize this number:")
        print(number)
        input("Press Enter to continue.")
        start = time.time()
        print("\n" * 100) 
        user_number = int(input("Enter the number: "))
        end = time.time()
        if user_number == number and end - start < 5:
            print("────────────────────────")
            print("Well done ! You Win.\n +10 Happy \n +1 LvL")
            creature.happy = min(100, creature.happy + 10)
            creature.lvl += 1
        else:
            print("You lose.")
            print("────────────────────────")

    def dormir(self, creature):
        print("────────────────────────")
        print("You put your creature to sleep.")
        creature.energy = min(100, creature.energy + 30)
        creature.hungry = max(0, creature.hungry - 10)
        print("────────────────────────")

    def soigner(self, creature):
        print("────────────────────────")
        print("You heal your creature.")
        if creature.energy < 50:
            print("The creature is too weak to be healed.")
        else:
            print("The creature is healed.")
            creature.heal = min(100, creature.heal + 25)
            print("────────────────────────")
        
    def check_value(self, creature, attribut):
        """Check if the value of the attribute is too high or too low."""
        if getattr(creature, attribut) > 100:
            setattr(creature, attribut, 100)
        elif getattr(creature, attribut) < 0:
            setattr(creature, attribut, 0)
        print("Value checked.")
        

    def givestats(self, creature):
        """Modify a specific attribute of the creature."""
        print("────────────────────────")
        print(creature.status())
        print("────────────────────────")

        valid_attributes = ["heal", "hungry", "energy", "happy"]
        attribut = input("Choose an attribute to modify (heal, hungry, energy, happy): ")

        while attribut not in valid_attributes:
            print("Invalid attribute. Try again.")
            attribut = input("Choose an attribute to modify (heal, hungry, energy, happy): ")

        try:
            new_value = int(input("New value: "))
            setattr(creature, attribut, new_value)
            self.check_value(creature, attribut)
        except ValueError:
            print("Invalid input. Please enter a number.")
        