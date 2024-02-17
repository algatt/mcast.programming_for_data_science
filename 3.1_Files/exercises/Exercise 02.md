# Exercise Pandas File Management

1. Write a script using `pandas` to read a CSV file named `sales.csv` and print the first 5 rows.

2. Modify the script from Question 1 to write the read DataFrame to a new CSV file named `sales_copy.csv`, excluding the index.

3. Write a script to read an Excel file named `inventory.xlsx` from the sheet named `stock` and print the first 5 rows.

4. Modify the script from Question 3 to write the DataFrame to a new Excel file named `inventory_copy.xlsx` with the sheet name as "Inventory".

5. Add error handling to the script from Question 1 to catch a `FileNotFoundError` when the `sales.csv` file does not exist, printing a user-friendly error message.

6. Modify the script from the previous question to read only the columns `date`, `product` and `quantity` from the `sales.csv` file.

7. Write a script to read a JSON file named `customers.json` and print the first 5 rows.

8. Change the previous script to write the DataFrame to a new JSON file named `customers_copy`.json. Make sure to save them as individual records and every record in a new line (without array notation).

9. Write a script that shows all the sheet names available in an Excel file named `data.xlsx`.

10. Combine two CSVs, `sales_jan.csv` and `sales_feb.csv`, into a new CSV named `sales_janfeb.csv`.

11. Write a script that reads the `sales.csv` file. After loading it filter out records where the quantity is more than `50`. Print the result of the filtered data.

12. Read the first three chunks from a file `big_file.csv`.
