# Exerscise Basic NLP

The data for this exercise was obtained from [Poem Classification NLP - Kaggle](https://www.kaggle.com/datasets/ramjasmaurya/poem-classification-nlp).

1. Prepare a code cell to include all required imports.
2. Read the file `poems.csv` into a dataframe.
3. Extract the column `Poem` into a list named `documents`.
4. Apply a lambda function to lower case all text in `documents`.
5. Create a set with all the unique characters in all words found in all documents.
6. Create a loop that iterates through the character set previously created and if it's not a letter from `a` to `z` remove it from the `documents`. Hint: you can use `string.ascii_lowercase` to check if it's from `a` to `z`.
7. Create a list `tokenized_docs` that contains all the words in the documents. This will serve as our tokenization.
8. Create a set `unique_words` with all the unqiue words in all documents.
9. Create an `embeddings` dictionary that assigns a 12-point vector to each unique word.
10. Prepare a matrix `dtm` filled with zeros suitable to our setup.
11. Create a dictionary `word_to_index` that maps each unique word to a number.
12. Populate the document term matrix `dtm`. Iterate through every `tokenized_docs`. Convert each word in the each document to an index using the previously generate dictionary `word_to_index`. Increase the document term matrix value by `1` as appropriate.
13. Create a `cosine_similarity` function that accepts two vectors. Calculate the `dot` product of vector 1 and vector 2. Calculate normalisation of vector 1, and that of vector 2. Divide the dot product by the product of the normalisations of vector 1 and vector 2.
14. Test the `cosine_similarity` function on document 1 and document 2.
15. Create a `similarity_matrix` that calculates the similarity for all documents.
16. Create a list that has the `similarity_matrix` of document 1 sorted in descending order. We need the indexes though.
17. Pick the most similar document.
18. Print them both.
