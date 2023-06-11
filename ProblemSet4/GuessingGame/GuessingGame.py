import random
import sys
is_ongoing = True
while True:
    try:
        while is_ongoing:
            game_level = int(input("level: "))
            is_ongoing = False

        if game_level <= 0:
            raise ValueError 
        else:
            generate_random = random.randint(1,100)
            print(generate_random)
            guess_number = int(input("Guess: "))

            if generate_random == guess_number:
                print("Just right!")
                sys.exit()
            elif generate_random > guess_number:
                print("Too small")
            else:
                print("Too large")
                
    except ValueError:
        pass


    