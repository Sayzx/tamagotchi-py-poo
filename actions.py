import random
import time

class ActionManager:
    def nourrir(self, creature):
        print("────────────────────────")
        print("Vous nourrissez la créature.")
        creature.hungry = min(100, creature.hungry + 20)
        if creature.hungry > 90:
            creature.heal = max(0, creature.heal - 5)
        print("────────────────────────")

    def jouer(self, creature):
        print("────────────────────────")
        print("Veuillez choisir un jeu :")
        print("1. Jeux de calcul")
        print("2. Jeux de mémoire")
        print("3. Jeux de rapidité")

        choix = input("Votre choix : ")
        while choix not in ["1", "2", "3"]:
            print("Choix invalide.")
            choix = input("Votre choix : ")

        if choix == "1":
            self.jeu_de_calcul(creature)
        elif choix == "2":
            self.jeu_de_memoire(creature)
        else:
            self.jeu_de_rapidite(creature)
        print("────────────────────────")

    def jeu_de_calcul(self, creature):
        print("Vous jouez à un jeu de calcul.")
        score = 0
        for _ in range(3):
            a, b = random.randint(1, 10), random.randint(1, 10)
            op = random.choice(["+", "-", "*"])
            print(f"Combien font {a} {op} {b} ?")
            result = int(input("Votre réponse : "))
            correct = eval(f"{a} {op} {b}")
            if result == correct:
                score += 1
        if score >= 2:
            print("Bravo ! Vous avez gagné.\n +10 de bonheur\n +1 de niveau")
            creature.happy = min(100, creature.happy + 10)
            creature.lvl += 1
        else:
            print("Dommage, vous avez perdu.")

    def jeu_de_memoire(self, creature):
        print("Vous jouez à un jeu de mémoire.")
        numbers = [random.randint(1, 10) for _ in range(5)]
        print("Mémorisez cette suite de nombres :")
        print(numbers)
        input("Appuyez sur Entrée pour continuer.")
        print("\n" * 100) 
        print("Saisissez les nombres un par un.")
        for i, number in enumerate(numbers, 1):
            user_number = int(input(f"Nombre {i} : "))
            if user_number != number:
                print("Vous avez perdu.")
                break
        else:
            print("Bravo ! Vous avez gagné.\n +20 de bonheur\n +1 de niveau")
            creature.happy = min(100, creature.happy + 20)
            creature.lvl += 1

    def jeu_de_rapidite(self, creature):
        print("Vous jouez à un jeu de rapidité.")
        number = random.randint(1, 10)
        print("Mémorisez ce nombre :")
        print(number)
        input("Appuyez sur Entrée pour continuer.")
        start = time.time()
        print("\n" * 100) 
        user_number = int(input("Saisissez le nombre : "))
        end = time.time()
        if user_number == number and end - start < 5:
            print("────────────────────────")
            print("Bravo ! Vous avez gagné.\n +10 de bonheur\n +1 de niveau")
            creature.happy = min(100, creature.happy + 10)
            creature.lvl += 1
        else:
            print("Vous avez perdu.")
            print("────────────────────────")

    def dormir(self, creature):
        print("────────────────────────")
        print("La créature dort...\n +30 d'énergie\n -10 de faim")
        creature.energy = min(100, creature.energy + 30)
        creature.hungry = max(0, creature.hungry - 10)
        print("────────────────────────")

    def soigner(self, creature):
        print("────────────────────────")
        print("Vous soignez la créature.")
        if creature.energy < 50:
            print("Vous ne pouvez pas soigner la créature car elle n'a pas assez d'énergie.")
        else:
            print("La créature est soignée.\n +25 de santé")
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
        