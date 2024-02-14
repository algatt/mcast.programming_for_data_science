# Exercise Standard Modules

1. Date and Time Difference - Using the `datetime` library, write a function that takes two strings representing dates (in the format "YYYY-MM-DD") and returns the number of days between them.

2. Fetch Web Page Content - Use the `urllib` library to write a function that takes a URL as input and returns the HTML content of the page as a string.

3. Parse JSON from a String - Use the `json` library, write a function that takes a JSON formatted string representing a dictionary and returns a dictionary with the given data. You can use the string `'{"name": "Alex", "age": 30, "city": "Valletta"}'` for testing.

4. Generate Random User IDs - Use the `random` library and create a function that generates a list of `n` unique user IDs, where each ID is a random integer between `1000` and `9999`. Ensure no ID is repeated.

5. Calculate Circle Area - Use the math library to write a function that calculates and returns the area of a circle given its radius. Use `math.pi` for the `π`value.

6. Combine `datetime` and `random` - Write a script that generates a list of `n` random dates within a given year. Each date should be unique. Use `datetime` for date handling and `random` for the generation.

7. Fetch and Parse JSON from an API - Use `urllib` to fetch data from a free-to-use API (e.g., http://jsonplaceholder.typicode.com/todos/1) and then parse this data from JSON to a Python dictionary using `json`.

8. Filter Data - Add a new function makes use of the function created in question 7, so that it filters the fetched data to only include todos that are completed. Make sure to retrieve all todos by using the url `https://jsonplaceholder.typicode.com/todos/`.

9. Statistical Analysis of Random Data - Generate a list of 100 random numbers between 1 and 100 using `random`. Then, write a function to calculate and print the mean, median, and mode of these numbers without using any external libraries. Use math for any mathematical operations required.
