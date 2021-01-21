"""
Given an array of numbers and a target
Find the shortest combination of numbers to sum to the target
"""


def howSum(target, numbers):
    table = [None for _ in range(target + 1)]
    table[0] = []

    for index in range(target + 1):
        if table[index] is not None:
            for number in numbers:
                if (index + number) <= target:
                    combination = [n for n in table[index]]
                    combination.append(number)

                    if table[index + number] is None:
                        table[index + number] = combination
                    elif len(combination) < len(table[index + number]):
                        table[index + number] = combination

    return table[target]


print(howSum(7, [5, 3, 4]))
print(howSum(8, [2, 3, 5]))
print(howSum(100, [1, 2, 4, 25]))
