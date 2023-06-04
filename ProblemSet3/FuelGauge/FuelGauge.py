def main():
    while True:
        try:
            fuel_gauge = input("Fraction: ")
            if fraction_to_percent(fuel_gauge) != "0":
                level(fraction_to_percent(fuel_gauge))
        except ValueError:
            pass
        except ZeroDivisionError:
            pass
        




def level(p):
    if int(p) >= 99:
        print ("F")
    elif int(p) <= 1:
        print ("E")
    else:
        print (p, "%", sep="")
    

def fraction_to_percent(f):
    numerator, denominator = f.split("/")
    if int(denominator) >= int(numerator):

        percent_value = (int(numerator) / int(denominator))* 100
        return int(percent_value)
    else:
        return "0"


main()