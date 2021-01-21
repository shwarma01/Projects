"""
Calculate nth fibonacci number using recursion
"""


# Brute force method
def fib(n):
    if n == 1 or n == 2:
        return 1

    return fib(n - 1) + fib(n - 2)


print("Brute force method")
print(fib(3))
print(fib(5))
print(fib(7))
# print(fib(100)) # Takes too long


# Memoization method
def fib(n):
    memo = {}

    def helper(n):
        if n == 1 or n == 2:
            return 1

        if n in memo:
            return memo[n]

        memo[n] = helper(n - 1) + helper(n - 2)
        return memo[n]

    return helper(n)


print("\nMemoization method")
print(fib(3))
print(fib(5))
print(fib(7))
print(fib(100))
