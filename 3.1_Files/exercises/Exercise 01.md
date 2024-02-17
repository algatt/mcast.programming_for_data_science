# Exercise File Handling

1. Create a function that accepts a `filename` and `number_of_lines`. The function should do the following:

   - Generate a random number from 1 to 1000 or a random word (from a pre-determined list) for `number_of_lines` times.
   - To decided if it's a number or words use `random` and use a 50:50 ratio.
   - You can set a pre-determined number of words; for instance a list with 5 fruits.
   - After the number of items have been generated, store them in a file using the given `filename` making sure that every entry is on a new line.

2. Use the previous function to generate a new file `file_1.txt` with 25 lines.

3. Write a function that reads the content of a file (parameter) and prints every line to the console.

4. Write a function that takes a filename as input and returns the number of lines in the file.

5. Write a function that copies the content of a source file to a new destination file both must be passed as parameters.

6. Assuming you have a file a combination of numbers and/or strings per line. Write a function that calculates the sum of the number values only.

7. Write a function that takes a filename and prints a dashboard of information: number of lines, number of words, number of characters.

8. Write a function that takes a filename (for this example pass `ibm_log.txt`). The function must return a dictionary with every log file category, and the number of times it appeared.
   - Every line in the log file is as follows:
     `03/22 08:51:01 INFO   :.main: Using log level 511`
   - We can consider the label to be `INFO` in this case.
   - Make sure that keys are cleaned (remove `:`) before adding them to dictionary.
   - Finally, return a dictionary with all the keys and the number of times they appear.
