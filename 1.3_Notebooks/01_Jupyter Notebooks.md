# Notebooks

## Jupyter Notebook

As previously seen, a Jupyter notebook allows you to have a combination of markdown (text) and Python code in the same 'document'.

For this part, you can create a a new folder, open it in VS Code, open a terminal and create a new environment in it.

```
python -m virtualenv --python=3.12 my-env
activate my-env
```

Now, create a new Jupyter file, press `CTRL+SHIFT+P` type `Jupyter` and select `Create: New Jupyter Notebook`.

In the top right, were you have `Select Kernel` press it, choose `Python Environments` and select the created environment.

Now for testing, we can add a markdown cell and a code cell.

In the markdown cell you can enter:

```
# Testing Notebooks
This notebook will be used for testing
```

and in the code cell you can enter:

```
a = 10
b = 20
print (a+b)
```

Now press the `Run All` button, and since the environment is new, it will ask you to install `ipykernel` package. After you install it, all the cells in the notebook should run.

For detailed information about how to use Jupyter Notebooks in VS Code please refer to https://code.visualstudio.com/docs/datascience/jupyter-notebooks.

## Google Colab

[Google Colab](https://colab.research.google.com/) is a free cloud service hosted by Google that allows you to write and execute Python code through your browser.

It is popular among data scientists and researchers for its use in machine learning and data analysis.

It also offers a collaborative environment, where multiple people can work on the same notebook at the same time, similar to Google Docs. It also offers free access to computing resources including GPUs and TPUs, which are ideal for computationally intensive tasks.

It is based on Jupyter Notebook so it's built on the same concepts although it's interface is different from Jupyter Notebooks hosted in VS Code.

## Markdown

Markdown is a markup language with plain-text formatting syntax. It is designed to be converted into HTML and is often used for writing technical content on the web.

It enables you to format text using simple, readable symbols. For instance, you can create headers with `#`, make text bold with `**`, create lists using `-` amongst others.

Markdown files typically have a .md or .markdown extension.

For more information about Markdown:

- https://www.markdownguide.org/cheat-sheet/
- https://www.datacamp.com/cheat-sheet/markdown-cheat-sheet-23
