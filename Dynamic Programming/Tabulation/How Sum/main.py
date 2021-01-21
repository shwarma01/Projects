"""
Given an array of numbers and a target
Find a combination of numbers to sum to the target
"""


def howSum(target, numbers):
    table = [None for _ in range(target + 1)]
    table[0] = []

    for index in range(target + 1):
        if table[index] is not None:
            for number in numbers:
                if (index + number) <= target:
                    table[index + number] = [n for n in table[index]]
                    table[index + number].append(number)

    return table[target]


print(howSum(7, [5, 3, 4]))
print(howSum(300, [7, 14]))
