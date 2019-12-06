'''
Python Schere-Stein-Papier
Author: Ari
Youtube: 
'''
import random as r

def rpi(user_input):
    rpi = ["stein", "schere", "papier"]
    current = r.choice(rpi)

    if user_input in rpi:
        if user_input == current:
            return [0, "Unentschieden!"]

        # Stein
        elif user_input == "stein" and current == "schere":
            return [1, "Ich habe Schere! Du hast gewonnen!"]
        
        elif user_input == "stein" and current == "papier":
            return [0, "Ich habe Papier! Ich habe gewonnen!"]

        # Schere
        elif user_input == "schere" and current == "stein":
            return [0, "Ich habe Stein! Ich habe gewonnen!"]

        elif user_input == "schere" and current == "papier":
            return [1, "Ich habe Papier! Du hast gewonnen!"]

        # Papier
        elif user_input == "papier" and current == "stein":
            return [1, "Ich habe Stein! Du hast gewonnen!"]

        elif user_input == "papier" and current == "schere":
            return [0, "Ich habe Schere! Ich habe gewonnen!"]
    


def main():
    print("Wir spielen 3 Runden!")
    
    run = True
    games = 3
    points = 0

    for _ in range(games):
            user_input = input("SSP: ")

            if user_input.lower() == "exit":
                run = False

            output = rpi(user_input.lower())
            print(output[1])

            points += output[0]

    print(f"Du hast {points} Punkte!")
    


if __name__ == '__main__':
    main()
