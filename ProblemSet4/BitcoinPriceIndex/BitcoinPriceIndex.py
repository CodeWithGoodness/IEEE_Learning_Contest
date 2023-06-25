import sys
import requests
try:
    float_value = float(sys.argv[2])
    price = input("Price:" )
except:
    sys.exit("Invalid input")