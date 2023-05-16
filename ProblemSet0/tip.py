def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    floatValue = (f"{d:2f}").replace("$", "")
    return floatValue


def percent_to_float(p):
    percentValue = (f"{p:1f}").replace("%", "")
    return percentValue


main()