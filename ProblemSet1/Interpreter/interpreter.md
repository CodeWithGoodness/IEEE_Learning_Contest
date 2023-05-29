### Math Interpreter

This code prompts the user to input a calculation expression and performs the corresponding calculation based on the operator provided. Here's a breakdown of the code:

The user is prompted to enter a calculation expression using the input() function. The message "Do some calculation:" is displayed to the user.

The input is split using the split() method, which separates the input into a list of substrings based on whitespace.

The first substring (operation[0]) is converted to a float and stored in the variable num_1.

The second substring (operation[1]) represents the operator and is stored in the variable operator.

The third substring (operation[2]) is converted to a float and stored in the variable num_2.

The code uses a match statement to determine the operator and perform the corresponding calculation:

a. If the operator matches "+", the code executes the corresponding block and prints the result of adding num_1 and num_2.

b. If the operator matches "-", the code executes the corresponding block and prints the result of subtracting num_2 from num_1.

c. If the operator matches "*", the code executes the corresponding block and prints the result of multiplying num_1 and num_2.

d. If the operator matches "/", the code executes the corresponding block and prints the result of dividing num_1 by num_2.

e. If none of the above conditions are met, meaning an unrecognized operator is provided, the code executes the final case _ block and prints "recheck operator".

The purpose of this code is to perform basic arithmetic calculations based on user input. It accepts two numbers and an operator, performs the corresponding calculation, and displays the result.


