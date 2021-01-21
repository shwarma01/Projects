"""
Given an array of numbers and a target
Figure out if you can use the numbers to sum to the target
"""


def canSum(target, numbers):
    table = [False for _ in range(target + 1)]
    table[0] = True

    for index in range(target + 1):
        if table[index] == True:
            for number in numbers:
                if (index + number) <= target:
                    table[index + number] = True

    return table[target]


print(canSum(7, [5, 3, 4]))
print(canSum(300, [7, 14]))
