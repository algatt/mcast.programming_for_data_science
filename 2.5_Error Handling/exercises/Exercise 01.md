# Exercise Error Handling

1. Write a function that asks the user for an integer input and prints it. `Use try/except` to catch a `ValueError` if the input is not an integer, printing an error message instead.

2. Modify the previous function to also handle a `KeyboardInterrupt` exception, which occurs when the user cancels the input, printing a different error message.

3. Extend the function from question 1 to include `else` and `finally` blocks, where `else` prints a success message and finally always prints a completion message.

4. Write a function that raises an exception with the message `Number is negative` if a user enters a negative number. If the exception is raised, print it.

5. Write a function that attempts to open a file provided by the user and print its contents. Use error handling to catch a `FileNotFoundError` and print a custom error message. Ensure the file is properly closed in a `finally` block if it was opened successfully.

6. Given a list of mixed data types, write a function that prints each item if it's an integer. Use error handling to skip any item that raises a `TypeError` when cast to an integer.

7. Write a function that takes a list of numbers and returns the sum. If the list contains a non-numeric type, catch the exception that would be raised by the sum function and return `None` instead.

8. Write a function that divides two numbers provided by the user, handling division by zero and non-numeric input exceptions. It should return the division result or an appropriate error message.

9. Write a script that iterates over a list of URLs, attempting to fetch the content of each URL using `urllib.request.urlopen`. Use error handling to print a message for each URL that cannot be fetched, continuing with the next URL in the list.

10. Write a function that takes a dictionary and a list of keys, attempting to print the value for each key. Use error handling to catch and print a message for any key that doesn't exist in the dictionary, without stopping the script.

11. Write a script that uses the `datetime` module to parse a list of date strings into `datetime` objects. Use error handling to catch and print an error message for any strings that are in an incorrect format, skipping over them.
