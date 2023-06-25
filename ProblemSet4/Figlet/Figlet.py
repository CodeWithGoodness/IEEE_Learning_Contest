import sys
from pyfiglet import Figlet
import random
figlet = Figlet()
if len(sys.argv) == 1:                      #executed if the user does not input anything on the command line
    text = input("Input: ")
    figlet.setFont(font = random.choice(figlet.getFonts()))         #sets the font to a random font
    print(figlet.renderText(text))                                  #displays the text in the random font
elif len(sys.argv) == 3:                                       #executes if the user inputs 2 strings on the command line             
    font_name = sys.argv[2]                                     #sets the font name to the second string
    if sys.argv[1] == "-f" or sys.argv[1] =="--font":             #checks if the first string is "-f or font"
        if font_name not in figlet.getFonts():                  #checks if font name is valid
            sys.exit("Invalid usage")
        else:
            figlet.setFont(font = font_name )                   #if it is valid, set font name to the second string and display the input text in that font
            text = input("Input: ")
            print(figlet.renderText(text))
            sys.exit()
    else:
        sys.exit(" invalid usage")    
else:
    sys.exit("Invalid Usage")
