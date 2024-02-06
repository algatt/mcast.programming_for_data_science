# Exercise 4 - Tuples and Sets

1. Create a set `my_colours` that store the colours `red`, `green`, and `fuchsia`.
2. Create a list `used_colours` that store the colours `red`, `orange`, `purple`.
3. Use list iteration on `used_colours`, add each colour to the set `my_colours`.
4. Print the contents of the set.
5. Create another set `interesting_colours` with the colours `fuchsia` and `turqoise`.
6. Print the common elements between the sets `my_colours` and `interesting_colours`.
7. Check if the colour `brown` appears in the set `my_colours`.
8. Create a frozenset named `frozen_colours` based on `my_colours`.
9. Try to add `brown` to `frozen_colours`.

<details>
    <summary>Answers</summary>

```
my_colours = {"red", "green", "fuchsia"}

other_colours = ["red", "orange", "purple"]

for colour in other_colours:
    my_colours.add(colour)
print (my_colours)

interesting_colours = {"fuchsia", "turqoise"}

print (my_colours & interesting_colours)

print ("brown" in my_colours)

frozen_colours = frozenset(my_colours)
print(frozen_colours)
frozen_colours.add("indigo")

```

</details>
