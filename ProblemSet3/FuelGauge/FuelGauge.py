def main():
    while True:
        try:
            fuel_gauge = input("Fraction: ")
            print(fraction_to_percent(fuel_gauge),"%", sep="")
            print(level(fraction_to_percent(fuel_gauge)))
        except ValueError:
            pass




def level(p):
    if int(p) >= 99:
        return "F"
    elif int(p) <= 1:
        return "E"
    else:
        return " "
    

def fraction_to_percent(f):
    numerator, denominator = f.split("/")
    if int(denominator) > int(numerator):

        percent_value = (int(denominator) / int(numerator))* 100
        return int(percent_value)
    else:
        return None


main()