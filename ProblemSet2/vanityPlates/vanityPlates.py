
def main ():
    plate = input("Plate: ")
    is_valid(plate)
    if is_valid(plate):
        print("Valid")
    else:
       print("Invalid")














def is_valid(plate_number):
    l = len(plate_number)
    
    for i in plate_number:
        if l >= 2 and l <= 6:
            if plate_number[0:2].isalpha():
                if all (i.isalnum() for i in plate_number):
                    print (plate_number[:-1])
                    if plate_number[-1].isdigit() and int (plate_number[-1]) != 0:
                       return "Valid"
                   


main()