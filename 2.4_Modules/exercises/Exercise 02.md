# Exercise Custom Module

This worksheet is designed around creating a custom Python module tailored for basic data science applications.

Create a new file named `DataScienceBasics.py` that will contain all the required functions. Ensure you include proper docstrings for each function, explaining its purpose, parameters, and return value.

1.  Start by creating a function named `calculate_mean` in your module that takes a list of numbers as an argument and returns the mean of those numbers.

2.  Add a function named `calculate_median` to your module. This function should take a list of numbers and return the median value.

3.  Write a function named `load_data` that takes a filename (a string) as its argument. This function should read a file containing JSON data, parse it, and return the data as a list of dictionaries. Assume each line in the file is a separate JSON encoded dictionary.

    - You can manually create a file named `data.txt` and in it place this content:

      ```
        { "id": 1, "name": "Alice", "age": 30, "score": 88 }
        { "id": 2, "name": "Bob", "age": 25, "score": 92 }
        { "id": 3, "name": "Charlie", "age": 25, "score": 95 }
        { "id": 4, "name": "Diana", "age": 30, "score": 100 }
        { "id": 5, "name": "Wallace", "age": 31, "score": 50 }
      ```

4.  Create a function named `filter_data` that takes two arguments: the dataset (a list of dictionaries) and a lambda function. The function should return a new list containing all the items for which the lamba function returns `True`.

5.  Add a function called `get_unique_values` that takes the dataset and a key (string) as arguments. This function should return a set of unique values for the specified key in the dataset.

6.  Implement a function named `transform_data` that takes the dataset, a key, and a transform function. The function should apply the transform function to each value of the specified key in the dataset and return the modified dataset.

7.  Create a function named `describe_data` that takes the dataset and a key, then calculates and prints the mean, and median for the numerical data associated with the key.

8.  Write a function named `aggregate_data` that takes the dataset and a keys. This function should return a dictionary with the unique values of the first key as the keys and the sum of the corresponding values the same key.

9.  Create a new script and inpirt `DataScienceBasics.py` as `dsb`. Then perform the following tasks:

- Define a `main` function and in it do the following:
  - Create a variable `data` and load the data from the txt file.
  - Create a new variable `new_data` that contains the filtered data of all records that do not have a score of `100`.
  - In the same variable `new_data` deduct 5 points to all players.
  - Create a new variable `stats` that stores the mean and median of the `score`.
  - Print the unique player names (use `new_data`).
  - Print the mean and median (calculated previously).
  - Print the total number of players by their age (use `new_data`)
- Make sure that `main` is called if the file is run directly.
