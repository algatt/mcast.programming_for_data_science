# Exercise 3 - Dictionaries

1. Create a dictionary `game` for a video game details. Include at least the following key-value pairs `title`, `price`, `platforms`. `platforms` should be a list.
2. Display the price of the game, reduced by 10%.
3. Add another field storing the `rating` of the game.
4. Add another field storing the `year_released` of the game.
5. Remove the `platforms` key.
6. Print the dictionary to check that it's correct.
7. Display all the `keys` of the dictionary.
8. Create a list `game_list` that stores all the values (without the keys). Make sure the data type is a `list`. Print it out after creating it.
9. Create a new dictionary `game_additional` that contains 2 more keys `publisher` and `dlc_available`, and assign them a value.
10. Merge the dictionary `game_additional` into the dictionary `game`.

<details>
    <summary>Answers</summary>

```
game = {
    "title" : "Baldur's Gate 3",
    "price" : 50,
    "platforms": ["PC", "XBOX One"]
}

print (game["price"]*0.9)

game["rating"] = 9.1
game["year_released"] = 2023

del(game["platforms"])

print(game)

print(game.keys())

game_list = list(game.values())
print(game_list)

game_additional = {
    "publisher" : "Larian Studios",
    "dlc_available": False
}

game.update(game_additional)
print(game)
```

</details>
