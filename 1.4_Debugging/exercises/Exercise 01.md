# Debugging Exercise

1. For this exercise you can use an existing environment or create a new one.
2. Create an empty Python script file, named `main.py`.
3. In it, paste this code:

```
def calculate_sum(numbers):
    total = 0
    for number in numbers:
        total += number
    return total

def find_average(numbers):
    if len(numbers) == 0:
        return "List is empty"
    total_sum = calculate_sum(numbers)
    average = total_sum / len(numbers)
    return average

# Test data
numbers = [10, 20, 30, 40, 50]

# Function calls
total = calculate_sum(numbers)
average = find_average(numbers)

print("Total:", total)
print("Average:", average)
```

4. Create a breakpoint on `total+=number` (line 4).
5. Debug the script, and observe what's happening to `total` and `number`.
6. Also, you can notice that this function `calculate_sum` is called twice, since it's also used in function `find_average`.
7. Remove the breakpoint, and add another one on `average=total_sum/len(numbers)` (line 11).
8. Debug the script, and hover over `total` and `len(numbers)`. You can see their current values at this point.
9. Even though the `average` will be calculated in the next step, let's add a watch with the expression `total_sum/len(numbers)`. You can see that the average is worked out.
10. Now, edit the existing breakpoint to only be active if the passed numbers' length is 1.
11. Debug the script, the breakpoint should not be triggered.
12. Now, modify `numbers = [10, 20, 30, 40, 50]` and simply use `numbers = [10]`. Debug the script again. Now the breakpoint should be active.
13. Remove the breakpoints.
