#prompt the user for the answer and convert to lowercase
answer = input("What is the answer to the great question of life, the universe and everything? \n").lower().strip()

if answer == "42" or answer == "forty-two" or answer == "forty two":
    print("Yes")
else:
    print("No")