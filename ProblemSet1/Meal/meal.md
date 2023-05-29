
### Meal Time

This code prompts the user to input the current time and determines the corresponding meal time based on the provided time. Here's a breakdown of the code:
#### main():
The main() function serves as the entry point of the program. It performs the following steps:

a. It prompts the user to input the current time using the input() function. The message "What time is it?" is displayed to the user.

b. The user's input is passed to the convert() function, which converts the time to a float value.

c. The code uses a match statement to determine the meal time based on the converted time:

If the mealTime value falls between 7.0 and 8.0 (inclusive), the code executes the corresponding block and prints "Breakfast time".

If the mealTime value falls between 12.0 and 13.0 (inclusive), the code executes the corresponding block and prints "Lunch time".

If the mealTime value falls between 18.0 and 19.0 (inclusive), the code executes the corresponding block and prints "Dinner time".
#### convert(time): 
The 'convert(time)' function takes in a string parameter, 'time' and converts it to a float value. It performs the following steps:

a. 'time' is split into hours and minutes using the split() method, assuming the time format is "HH:MM". The  colon character, ':' is the delimiter.

b. The minutes are converted to hours by dividing them by 60 and storing the result in the variable 'minutesToHour'.

c.hours, minutesToHour value are added together and stored in the variable 'total'.

d. The total value, representing the converted time, is returned.



