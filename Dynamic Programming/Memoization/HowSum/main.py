"""
Given an array of numbers and a target
Find the combination of numbers to sum to the target
Return None if no combination possible
"""


# Brute force method
def howSum(numbers, original):
    if original == 0:
        return []

    if len(numbers) == 0:
        return None

    def helper(numbers, target):
        if target < 0:
            return None

        if target == 0:
            return []

        for i in numbers:
            result = helper(numbers, target - i)
            if result is not None:
                result.append(i)
                return result

        return None

    return helper(numbers, original)


print("Brute force method")
print(howSum([2, 3], 5))
print(howSum([2, 5], 13))
print(howSum([3, 4], 50))
# print(howSum([7, 14], 300)) # Takes too long


# Memoization method
def howSum(numbers, original):
    if original == 0:
        return []

    if len(numbers) == 0:
        return None

    memo = {}
    def helper(numbers, target):
        if target < 0:
            return None

        if target == 0:
            return []

        if target in memo:
            return memo[target]

        for i in numbers:
            memo[target] = helper(numbers, target - i)
            if memo[target] is not None:
                memo[target].append(i)
                return memo[target]

        return None

    return helper(numbers, original)


print("\nMemoization method")
print(howSum([2, 3], 5))
print(howSum([2, 5], 13))
print(howSum([3, 4], 50))
print(howSum([7, 14], 300))
