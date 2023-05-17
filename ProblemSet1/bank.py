#prompt the user for a greeting
greet = input("Greet the audience.. \n").lower().strip()



if greet.startswith("hello"):
    print ("$0")
elif greet.startswith("h") and not greet.startswith("hello"):
    print ("$20")
else :
  print ("$100")
