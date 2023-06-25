def main():
    greet = input("Greet the audience.. \n")
    print (f"${value(greet)}")
   

def value(greeting):
    if greeting.lower().strip().startswith("hello"):
        return 0
    elif greeting.lower().strip().startswith("h") and not greeting.startswith("hello"):
        return 20
    else :
        return 100
   
if __name__ == "__main__":
   main()