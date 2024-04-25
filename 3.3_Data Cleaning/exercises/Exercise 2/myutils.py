from urllib.request import urlopen
from urllib.error import HTTPError, URLError
import json

def get_data(url: str):
    try:
        response = urlopen(url)
        response = response.read()
        return response
    except HTTPError as error:
        print(error.reason)
    except URLError as error:
        print(error.reason)
    except:
        print('There was a problem getting the data')


def get_users():
    return json.loads(get_data("https://dummyjson.com/users"))['users']
  
def get_string_stats(collection: list, field: str):
    try:
        result = {}
        for user in collection:
            if field in user:
                if user[field] in result:
                    result[user[field]] += 1
                else:
                    result[user[field]] = 1
        return result
    except TypeError as e:
        return 'Not a valid string'

def get_numeric_stats(collection:list, field:str):
    total = 0
    count = 0
    for user in collection:
        if field in user and (type(user[field]) == int or type(user[field])==float):
            total += user[field]
            count += 1
    return {"total": total, "count": count, "average": total/count}


