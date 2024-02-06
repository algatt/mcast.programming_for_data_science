# Exercise 01 - Data Types

1. Create the following variables.
   - `length` which contains `56`
   - `width` which contains `34.56`
   - `shape` which contains `rectangle`
2. Print their type.
3. Calculate the area of the rectangle, and store it in a variable `area`.
4. Calculate the perimiter of the rectangle, and store in a variable `perimiter`.
5. Print the `area` and the `perimiter`.
6. Re-calculate the area but this time, make sure to convert the width into `int` before multiplying. Store the result in `area_int`.
7. Check if the type of `area` and `area_int` are the same.
8. Create a variable `msg` that contains `The area of the rectangle is 1904cm2.` Make sure that for the word `rectangle` and `1904` you use the appropriate variables. Use the `join` function.
9. Print `msg`.
10. Use `msg` to extract `cm`, and display a message `The unit of measurment is cm`.

<details>
    <summary>Answers</summary>

```
length=56
width=34.56
shape='rectangle'
print(type(length))
print(type(width))
print(type(shape))

area = length * width
perimiter = (length+width)*2

print (area)
print (perimiter)

area_int = length \* int(width)
print(area_int)

print (type(area)==type(area_int))

msg = "".join(['The area of the ', shape, ' is ', str(area_int), 'cm2'])
print(msg)

print ('The unit of measurement is ' + msg[-3:-1])

```

</details>
