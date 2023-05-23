def main():
    userInput = input("Write something \n")
    convertedInput = convert(userInput)
    print (convertedInput)
    
    


def convert(word):
    new = word.replace(":)", "🙂").replace(":(", "🙁")
    return new


main()    
