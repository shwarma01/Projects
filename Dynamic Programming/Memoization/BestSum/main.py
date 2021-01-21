"""
Given an array of numbers and a target
Return the shortest way to sum a set of numbers from the numbers array to make the target
The numbers in the array can be used as many times as you want
"""


# Brute force method
def bestSum(numbers, target):
    if target == 0:
        return []

    if target < 0:
        return None

    best = None

    for i in numbers:
        other = bestSum(numbers, target - i)
        if other is not None:
            other.append(i)
            if best is not None:
                if len(other) < len(best):
                    best = other
            else:
                best = other

    return best


print("Brute force method")
print(bestSum([5, 3, 4, 7], 7))
print(bestSum([2, 3, 5], 8))
print(bestSum([1, 4, 5], 8))
# print(bestSum([1, 2, 5, 25], 100)) # Takes too long


# Memoization method
def bestSum(numbers, original):
    memo = {}

    def helper(numbers, target):
        if target in memo:
            return memo[target]

        if target == 0:
            return []

        if target < 0:
            return None

        best = None

        for i in numbers:
            other = helper(numbers, target - i)
            if other is not None:
                other.append(i)
                if best is not None:
                    if len(other) < len(best):
                        best = other
                else:
                    best = other

        memo[target] = best
        return best

    return helper(numbers, original)


print("Memoization method")
print(bestSum([5, 3, 4, 7], 7))
print(bestSum([2, 3, 5], 8))
print(bestSum([1, 4, 5], 8))
print(bestSum([1, 2, 5, 25], 100))
