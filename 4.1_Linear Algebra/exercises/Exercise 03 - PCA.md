# Exercise PCA with scikit-learn

In this exercise, we're going to perform PCA on a wine dataset. We will determine how many minimum dimensions are required.

1. Import `datasets` from `sklearn`. Then from this `dataset` load the dataset related to wine using the function `load_wine`, make sure to load as a frame. Extract the data part from this wine data and store it in `df`. Display the first 5 records.

2. Display the shape of `df`.

3. Display information about all the columns found in `df`.

4. From `sklearn.preprocessing` import `StandardScaler`, then initialise it. Use `fit_transform` on the dataset `df` and store it into a new variable `df_scaled`. Print the first 3 rows.

5. From `sklearn.decomposition` import `PCA`. Initiliase `PCA` using 3 components. Apply `fit_transform` to `df_scaled`.

6. Print the `components_` found in the pca.

7. Print the `explained_variance_ratio_` found in the pca.

8. Print the total of  `explained_variance_ratio_`.

9. Create a variable `nums` having a sequence of numbers from `0` upto the number of dimensions there are in the dataset.

10. Create an empty list `var_ratio`. Iterate through the `nums` list, and for every iteration initialise `PCA` having the number of components with the current number in the loop, then apply it to `df_scaled`. Append the total of the `explained_variance_ratio_` to it.

11. Print the `var_ratio` list.

12. Import `matplotlib.pyplot` as `plt`. Create a plot having x-axis `nums`, and y-axis `var_ratio`; making sure the marker is `o`. Add a horizontal line at `0.95` making it dashed and red. Add appropriate axis labels, and a title.

13. From the chart what is the suitable number of components that we can use.

14. Using `numpy` functions find the number of components required for a PCA > 0.95.
