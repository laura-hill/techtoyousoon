loopcount = 0
largest = -float('inf')  # smallest possible value
smallest = float('inf')  # largest possible value
while loopcount < 5:
    loopcount = loopcount + 1

    given = input()
    given_as_integer = int(given)

    # Compare to the current smallest and largest value
    if given_as_integer < smallest:
        smallest = given_as_integer
    if given_as_integer > largest:
        largest = given_as_integer

print('the largest number is', largest)
print('the smallest number is', smallest)