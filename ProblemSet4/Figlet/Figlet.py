import sys
from pyfiglet import Figlet
import random
figlet = Figlet()
figlet.getFonts()

try:
    if len(sys.argv) == 1:
        text = input("Input: ")
        figlet.setFont(font = random.choice(figlet.getFonts()))
        print(figlet.renderText(text))
    elif len(sys.argv) == 3:
        font_name = sys.argv[2]
        figlet.setFont(font = font_name )
        for font_name in figlet.getFonts():
            if font_name in figlet.getFonts():
                text = input("Input: ")
                print(figlet.renderText(text))
                sys.exit()
            else:
                raise ValueError
            
    else:
        print ("Invalid Usage")
except ValueError:
    print("Invalid font")