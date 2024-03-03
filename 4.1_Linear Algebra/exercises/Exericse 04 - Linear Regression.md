# Exercise Linear Regression

In this exercise we are going to try and predict the age of abalone using various measurements. For this exercise you need to install the library `ucimlrepo`. 

1. Import `fetch_ucirepo` from `ucimlrepo` and use it to load the dataset with label `abalone` to a variable.

2. Extract `data.features` to a variable `X` and `data.targets` (selecting `Rings` only) to `y`.

3. Print the variables in `abalone` using `abalone.variables`. This will explain what each column is showing.

4. You can notice that `Sex` is `Categorical` and we cannot work with this. So use `pandas` function `get_dummies` to convert `Sex` to one-hot encoding. Make sure you convert to `int` not Boolean.

5. Use dataset `X` and run correlation with `y`, making sure to sort result in descending order. Which variable/s has the strongest relationship with th age?

6. Import `train_test_split` from `sklearn.model_selection` and split the dataset into 60% training and 40% test.

7. Create a variable `X_transpose` that will contain the `X_train` transposed.

8. Create a variable `beta` that stores the regression result you can calculate it as follows $beta = np.linalg.inv(X_transpose.dot(X_train)).dot(X_transpose).dot(y_train)$.

9. Create a function `calculate_rmse` that needs 3 parameters `beta`, `X_test`, and `y_test`. The function must do the following:
- Set `total_error` to zero
- Loop for the number of rows there are in `X_test`
    - predict the values for the current row using `np.dot` and passing `beta` and the current row
    - Calculate the difference of the prediction from the actual value
    - Add the squared difference to `total_error`
- Return the `total_error` divided by the number of observations, square rooted.

10. Call the previous function and take not of the result.

11. Next we are going to test PCA using components 1 to how many columns there are in the dataset, and return the cumulative variance ratio for all attempts. Follow these steps:
- From `sklearn.decomposition` import `PCA`. 
- Set `cumulative` to an empty list
- Set a loop that iterates on how much columns `X` has
    - apply PCA based on the current iteration
    - `fit_transform` the PCA
    - add the sum of the `explained_variance_ratio_` to `cumulative`
- Convert `cumulative` to a numpy array.

12. Using `np.where` find the first index where the cumulative ratio exceeds or is equal to 0.95. Then using this create a new PCA based on this result's number of components, and create a `pandas` DataFrame on the transformed fit of the PCA.

13. Create train / test split again, this time making sure that for X you're using the PCA result.

14. Transpose `X_train` again, and calculate `beta` again.

15. Calculate the RMSE again using the PCA data. Take note of the result, and compare with previous one.