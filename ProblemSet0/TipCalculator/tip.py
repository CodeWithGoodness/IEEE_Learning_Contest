def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    
    floatValue = float(d.replace("$", ""))
    to_1_dp = f"{floatValue:.1f}"
    return (float(to_1_dp))


def percent_to_float(p):
    toFloat = float(p.replace("%", ""))/100
    return (float(toFloat))


main()