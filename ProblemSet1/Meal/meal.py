def main():
    mealTime =  convert(input("What time is it? "))

    match mealTime:
        case mealTime if mealTime >= 7.0 and mealTime <= 8.0:
            print("Breakfast time")
        case mealTime if mealTime >= 12.0 and mealTime <= 13.0:
            print("Lunch time")
        case mealTime if mealTime >= 18.0 and mealTime <= 19.0:
            print("Dinner time")


def convert(time):
    hours, minutes = time.split(":")
    minutesToHour = float(minutes)/60
    total = float(hours) + minutesToHour
    return  (total)


if __name__ == "__main__":
    main()

