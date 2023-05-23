#prompt the user for input
userInput = input("Say something \n")

#split the input
splitInput = userInput.split(" ")

#join the splitted words with dots inbetween
print("...".join(splitInput))
