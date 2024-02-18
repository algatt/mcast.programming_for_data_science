# Exercise DataFrames

1. Create a pandas DataFrame from the following dictionary and assign it to a variable named `students_df`. Print the dataframe.

```
data = {'Name': ['Alice', 'Bob', 'Charlie', 'Diana', 'Evan'],
        'Age': [22, 23, 24, 22, 25],
        'Major': ['Biology', 'Computer Science', 'Mathematics', 'Physics', 'Chemistry']}
```

2. Display the first `3` rows of `students_df`.

3. Select and print the `Age` and `Major` columns from `students_df`.

4. Add a new column to `students_df` named `GradYear` with values `[2022, 2023, 2023, None, 2024]`. Print the updated DataFrame.

5. Filter `students_df` to a new DataFrame `filtered_df` to keep only students majoring in `Computer Science` or `Physics`. Print the filtered DataFrame.

6. Select and print the second and fourth rows of `students_df` using their integer location.

7. Delete the `Age` column from `students_df` and print the resulting DataFrame.

8. Fill all the missing values in `GradYear` with `2023` and print the DataFrame. Also, make sure the datatype for `GradYear` is `int`.

9. Group `students_df` by `Major` and calculate the average `GradYear` for each major. Print the results.

10. Create a new DataFrame `sorted_df` storing the sorted version of `students_df` by the `GradYear` in descending order. Print the first 3 records.

11. Filter `students_df` to find students who are majoring in `Chemistry` or whose `GradYear` is before 2023. Store them in a new DataFrame `advanced_filter_df`. Print the filtered DataFrame.

12. Iterate over `students_df` rows and print the name of each student along with their major if their `GradYear` is 2023.
