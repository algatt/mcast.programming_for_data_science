# Wine Quality Prediction

1. Import the data from `winequality-red.csv` to `wine_red` and `winequality-white.csv` to `wine-white`.
2. Add a column named `type` to each dataframe with the type of wine (whether it's red or white).
3. Combine the two datasets to a dataframe named `wine`.
4. Show this message `Dataset has 6497 rows and 13 columns.` (not hard-coded).
5. Rename the columns `residual sugar` to `sugar`, and `quality` to `target`.
6. Display each column, and the number of null values it contains.
7. Fill any missing values in `fixed acidity` with the mean of it.
8. Drop any observations that have missing values.
9. Display the number of records per `target`.
10. Keep observations which have a target of `4` to `7`.
11. Display these messages (not hard-coded):
    - Dataset has 6264 rows and 13 columns.
    - Dataset has 233 less rows.
12. Create a dictionary named `sugar`, and in it you must have a key for each target. Each target must have the `min` and `max` for `sugar` for each `target`.
13. Save the dataframe without an index to `wine_combined.csv`.
14. Create a variable `features` that is a list of the the wine dataframe columns. Then remove the `target` entry from it.
16. Create a variable `X` with the columns stored in `features` from dataframe `wine`. Create a variable `y` to store the values of `target` from dataframe `wine`.
17. If there are any categorical values, make sure to convert them to dummies, as integers, and add the prefix `type`.
18. Use `StandardScaler` to transform the data found in `X` to `X_scaled`.
19. Create a loop that ranges from 1 up to the number of columns found in `X_scaled`. For every loop:
    - Create a `pca` variable using `PCA` and setting the number of components to the current index in the loop.
    - Create a `principal_components` variable that stores the fitted transformed data from pca on `X_scaled`.
    - Create a `df_pca` variable which is the `principal_components` converted as a pandas DataFrame.
    - Create a variable `total` with the sum of the `explained_variance_ratio_` obtained from the `pca`.
    - Print a message for each loop as follows: `Components 1 has ratio of 0.3628718699478484`.
    - If the `total` is more than `0.9` print this message `Using 8 components for PCA` and stop the loop.
20. Create a train/test split on `X` and `y` with a test size of `0.3`.
21. Create another train/test split on `df_pca` and `y` with the same properties.
22. Create a function `train` that accepts `X_train` and `y_train` as parameters. The function must:
    - Store the transposed result of `X_train` to `X_T`.
    - Calculate the `beta` using `np.linalg.inv`.
    - Return the `beta`
23. Create a variable `model_without_pca` that stores the result of the training done on `X_train` and `y_train`.
24. Create another variable `model_with_pca` that stores the result of the training done on `X_train_pca` and `y_train_pca`.
25. Create a function `calculate_rmse` that accepts the `beta`, `X_test`, and `y_test`. The function must:
    - Calculate `y_pred` by multplying `X_test` with `beta`.
    - Calculate `rmse` and return it.
26. Create a variable `rmse_without_pca` and store the result of `calculate_rmse` based on the `model_without_pca`.
27. Create another variable `rmse_with_pca` that stores the result of `calculate_rmse` based on the `model_with_pca`.
28. Print both RMSEs, and discuss which model is the best.