def main():
    userInput = input("Write something \n")
    convertedInput = convert(userInput)
    print (convertedInput)
    
    


def convert(word):
    new = word.replace(":)", "🙂").replace(":(", "🙁")
    return new


main()    

This program has 2 major functions: main() and convert().
convert():   This function takes in a string parameter and uses the string.replace() function to convert any emoticon[:) and :(] 
within the string to emoji[🙂 and 🙁]. The converted string is now stored in a new variable called new. The return keyword returns the value of new
to the convert() function.
           
                                                                                                                                
main(): Prompts the user for input and stores it in the variable, "userInput". It then calls the convert fu
                                                                                                                           
