# Exercise 2 - Lists

1. Create a list named `details` that contains your name, your age, and a list of hobbies (at least 3).
2. Display the message `My age is 24`, age must be extracted from the list.
3. Display the last hobby in the list.
4. Add another value to the list storing your email.
5. Print the list.
6. Add another hobby to the list.
7. Print the list.
8. Create an empty list called `details_copy`.
9. Use list iteration to copy every element from `details` to `details_copy`.
10. Print `details_copy` to ensure it copied successfully.
11. Remove the email from `details_copy`.
12. Display the message `I have 4 hobbies` making sure not to hard-code the number of hobbies.
13. Sort `details_copy`.

<details>
    <summary>Answers</summary>

```
details = ['Alex', 24, ['Bungee Jumping', 'Reading', 'Snorkelling']]

print ('My age is ' + str(details[1]))

print (details[2][-1])

details.append('alex@yahoo.com')
print(details)

details[2].append('Cooking')
print(details[2])

details_copy = []

for item in details:
    details_copy.append(item)

print (details_copy)

details_copy.pop()

print (details_copy)

print ("I have " + str(len(details_copy[2])) + " hobbies")

details_copy.sort(key=str)
print (details_copy)
```

</details>
