import json

def calculate_mean(nums):
    """
    Calculate the mean of a list of numbers.
    
    Parameters:
    nums (list): A list of numbers.
    
    Returns:
    float: The mean of the numbers.
    """
    return sum(nums) / len(nums)

def calculate_median(nums):
    """
    Calculate the median of a list of numbers.
    
    Parameters:
    nums (list): A list of numbers.
    
    Returns:
    float: The median of the numbers.
    """
    return sorted(nums)[len(nums)//2]

def load_data(filename):
    """
    Load data from a JSON file where each line is a JSON object.
    
    Parameters:
    filename (str): The path to the file.
    
    Returns:
    list: A list of dictionaries loaded from the file.
    """
    with open(filename, 'r') as file:
        data = [json.loads(line) for line in file]
    return data

def filter_data(dataset, fun):
    """
    Filter a dataset based on a function.
    
    Parameters:
    dataset (list): A list of dictionaries representing the dataset.
    fun (function): A function that takes a dictionary and returns True or False.
    
    Returns:
    list: A list of dictionaries that satisfy the filtering function.
    """
    return [item for item in dataset if fun(item)]

def get_uniques(dataset, key):
    """
    Get unique values from a dataset for a specific key.
    
    Parameters:
    dataset (list): A list of dictionaries representing the dataset.
    key (str): The key for which unique values are sought.
    
    Returns:
    set: A set of unique values for the specified key in the dataset.
    """
    return set(item[key] for item in dataset)

def transform_data(dataset, key, fun):
    """
    Transform data in a dataset for a specific key using a function.
    
    Parameters:
    dataset (list): A list of dictionaries representing the dataset.
    key (str): The key whose values are to be transformed.
    fun (function): A function to apply to each value under the specified key.
    
    Returns:
    list: The dataset with transformed values for the specified key.
    """
    for item in dataset:
        item[key] = fun(item[key])
    return dataset

def describe_data(dataset, key):
    """
    Calculate mean and median for a specific key in a dataset.
    
    Parameters:
    dataset (list): A list of dictionaries representing the dataset.
    key (str): The key for which the mean and median are to be calculated.
    
    Returns:
    tuple: A tuple containing the mean and median of the values under the specified key.
    """
    values = [item[key] for item in dataset]
    return calculate_mean(values), calculate_median(values)

def aggregate_data(dataset, key_to_group):
    """
    Aggregate data by counting occurrences of each unique value for a specified key.
    
    Parameters:
    dataset (list): A list of dictionaries representing the dataset.
    key_to_group (str): The key to aggregate data by.
    
    Returns:
    dict: A dictionary with keys representing unique values of the specified key and values being the count of occurrences.
    """
    data = {}
    for item in dataset:
        if item[key_to_group] in data:
            data[item[key_to_group]] += 1
        else:
            data[item[key_to_group]] = 1
    return data
