# Exercise Data Cleaning

1. Load the two datasets `sales_data.csv` and `sales_data_extra.csv` to two separate dataframes.

2. Combine the two datasets into a dataframe `sales`.

3. Data Exploration - Show the following:

- first 6 records of the data
- data types of data frame
- and general statistics

4. Show how many nulls are there in each column.

5. For each column that has missing values fill it in with the median. Print the null count again to ensure they have been filled in.

6. The column `Date` right now has a type of `Object`. Make sure to convert it to `datetime`. Also ensure `Sales` column is `float`. Print the types again to ensure they've changed.

7. Show how many duplicate records there are (if any). If there are remove them.

8. Rename the columns so that they are all lowercase.

9. Calculate the 25% quantile `Q1` and the 75% quantile `Q3` on `sales`. Find out the IQR (inter quartile range) by subracting `Q1` from `Q3`. Only keep records that are between the range of `Q1-1.5*IQR` and `Q3+1.5*IQR`.

10. Ensure that one-hot encoding is applied to categorical columns.

11. Create two new columns, one storing the `year` and another the `month` (obtained from date).

12. Normalise `sales` and `quantity` columns using MinMaxScaler from `sklearn.preprocessing`

13. Save the modified data to `sales_cleaned.csv`.
