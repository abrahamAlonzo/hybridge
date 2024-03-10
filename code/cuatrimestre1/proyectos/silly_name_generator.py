# Generar un nombre tonto
import random

first_names = ["Bumpy", "Crazy", "Funky", "Goofy", "Happy", "Jumpy", "Lucky", "Puffy", "Silly", "Zippy"]
last_names = ["Banana", "Bear", "Chicken", "Duck", "Elephant", "Fish", "Giraffe", "Hippo", "Iguana", "Jellyfish"]


#generate menu for pick a name
def generate_name():
    first = random.choice(first_names)
    last = random.choice(last_names)
    return first + " " + last

def main():
    print("Bienvenido a Silly Name Generator!")
    while True:
        print("Tu nombre tonto es: " + generate_name())
        print("Generar otro? (y/n)")
        response = input()
        if response.lower() != "y":
            break
    print("Bye!")

if __name__ == "__main__":
    main()