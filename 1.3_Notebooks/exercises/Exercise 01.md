# Notebook Exercise

1. Create a new folder named `exercise-notebook`.
2. In it, create a new environment using your Python version.
3. Activate the environment, and install the packages `pandas`, `seaborn` and `matplotlib`.
4. Create a new Jupyter notebook and name it `Iris.ipynb`.
5. Ok, now we are going to analyse a very famous dataset related to Iris flowers [Iris Data Set](https://en.wikipedia.org/wiki/Iris_flower_data_set). Create a mardown cell an in it type

```
# Data Analysis of Iris Dataset
This notebook demonstrates basic data analysis on the famous Iris dataset.
```

5. In a new code cell import the required libraries.

```
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
```

6. Now, we add some text explaining that we are going to load the dataset.

```
## Loading the Dataset
We will use pandas to load the dataset into a DataFrame.
```

7. Now, the code for actually loading the data.

```
url = "https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"
columns = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'species']
iris = pd.read_csv(url, names=columns)

```

8. Another markdown cell, explaining that we will be plotting a chart.

```
## Basic Data Visualization
Using matplotlib and seaborn for visualizing the data distribution.
```

9. Last code cell to actually display the chart.

```
plt.figure(figsize=(8, 6))
sns.scatterplot(data=iris, x='sepal_length', y='sepal_width', hue='species')
plt.title('Sepal Length vs Sepal Width')
plt.show()
```

10. Run the Notebook.
11. Now, we are going to upload it to Google Colab. Open Google Colab, and from the `Menu` choose `File` and `Upload Notebook`. Choose `Upload`, then `Browse` and find `Iris.ipynb`.
12. Run the Notebook on Google Colab as well.
13. Finally share it with your lecturer as a viewer.

<details>
<summary>Answers</summary>

```
mkdir exercise-notebook
python --version
python -m virtualenv --python=3.12 env
.\env\Scripts\activate
pip install seaborn matplotlib pandas
```

</details>
