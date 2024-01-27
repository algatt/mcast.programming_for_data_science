# Cloning an Existing Repository

Sometimes its useful to clone an existing repository, and continue working on it and push it to your own repository.

Consider this repository https://github.com/awesomedata/awesome-public-datasets. Our aim is to clone this repository and push it to one of our own.

## Create Empty Repository

First task is to create an empty repository on Github. For this purpose you can call it `test_dataset`.

## Clone Existing Repository

Go to our usual folder `git-training` and open a terminal prompt.

Clone the remote repository using

```
git clone https://github.com/awesomedata/awesome-public-datasets.git test_dataset
```

> Note: The last part `test_dataset` was added so that the repository is cloned to a folder with that name. If you leave it out, it will be cloned to the original name.

## Pushing to Our Repository

The last step is to go inside the repository and change the origin url to our own repository.

```
cd test_dataset
git remote set-url origin https://github.com/algatt/test_dataset.git
git push -u origin master
```

From now on, any changes that you do to this repo will be uploaded to your repository.

## Final Steps

You can delete this repository since it will not be used anymore.
