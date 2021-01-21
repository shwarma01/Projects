"""
Given an array of numbers and a target sum is it possible to get the target sum?
Yuo can use the numbers in the array however many times you need
"""


# Brute force method
def canSum(numbers, target):
    if target == 0:
        return True

    if target < 0:
        return False

    for i in numbers:
        if canSum(numbers, target - i) is True:
            return True

    return False


print("Brute force method")
print(canSum([2, 3], 5))
print(canSum([2, 3, 4], 7))
print(canSum([2], 19))


# print(canSum([7, 14], 300)) # Takes too long


# Memoization method
def canSum(numbers, target):
    memo = {}

    def helper(numbers, target):
        if target == 0:
            return True

        if target < 0:
            return False

        if target in memo:
            return memo[target]

        for i in numbers:
            memo[target] = helper(numbers, target - i)
            if memo[target] is True:
                return True

        return False

    return helper(numbers, target)


print("\nMemoization method")
print(canSum([2, 3], 5))
print(canSum([2, 3, 4], 7))
print(canSum([2], 19))
print(canSum([7, 14], 300))
