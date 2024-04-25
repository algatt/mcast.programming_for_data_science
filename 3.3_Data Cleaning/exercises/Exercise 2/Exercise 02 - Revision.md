# Exercise

- Create a folder named exercise.
- Inside this folder create a new environment called `my-env`.
- Activate the environment.
- Create a module named `myutils`
- In this module prepare the following functions:
  - `get_data` : This must accept a url, and get the response from this url. It must handle `HTTPError` and `URLError` and return their `reason`. For any other error print an appropriate message.
  - `get_users`: Calls the function `get_data` and passes the url `https://dummyjson.com/users`. From response extract `users` and return it.
  - `get_string_stats`: Accepts a `collection` and a `field`. You must iterate through the collection, and create a dictionary of values and counts for the passed field. So for example if `gender` is passed, a dictionary must be returned something similar to: `{'male': 4, 'female': 10, 'other:6'}`.
  - `get_numeric_stats`: Accepts a `collection` and a `field` and returns the `total`, `count`, and `average`. So for example if `age` is passed, a dictionary must be returned something similar to: `{'total': 300, 'count' :10, 'average': 30}`.
- Prepare a Jupyter notebook that does the following:
  - Import the module `myutils`
  - Create a list with `age`, `weight`, `gender` and `bloodGroup`.
  - Create an empty dictionary named `stats`.
  - Iterate through the fields if the field type from users is string store the result of `get_string_stats` into `stats[field]`, otherwise call `get_numeric_stats`.
  - Print `stats`
