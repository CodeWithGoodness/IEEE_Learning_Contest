### Home Federal Savings Bank

This code prompts the user to input a greeting and then determines the corresponding monetary value based on the provided greeting. Here's a breakdown of the code:

The user is prompted to enter a greeting using the input() function. The message "Greet the audience.." is displayed to the user.

The lower() function is used to convert the user's input to lowercase, ensuring that the code can handle different casing variations.

The strip() function is applied to remove any leading or trailing whitespace from the input, ensuring that the comparison conditions work correctly and the resulting string is stored in a variable called 'greet'.

The code checks the user's input using a series of conditional statements:

a. If the greeting starts with "hello" (e.g., "hello," "hello there"), the condition greet.startswith("hello") evaluates to True. In this case, the code executes the corresponding block and prints "$0".

b. If the greeting starts with the letter "h" but does not start with "hello", the condition greet.startswith("h") and not greet.startswith("hello") evaluates to True. This means the greeting starts with "h" but is not exactly "hello". In this case, the code executes the corresponding block and prints "$20".

c. If neither of the above conditions is met, meaning the greeting does not start with "hello" or "h", the code executes the final else block and prints "$100".


