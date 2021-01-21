"""
On a grid of mxn you start on the top left corner
How many ways are there to get to the bottom right corner?
You can only move down and right
"""


# Brute force method
def gridTraveller(m, n):
    if m == 1 or n == 1:
        return 1

    return gridTraveller(m - 1, n) + gridTraveller(m, n - 1)


print("Brute force method")
print(gridTraveller(1, 1))
print(gridTraveller(2, 2))
print(gridTraveller(3, 3))
# print(gridTraveller(20, 20)) # Takes too long


def gridTraveller(m, n):
    memo = {}

    def helper(m, n):
        if m == 1 or n == 1:
            return 1

        if m <= 0 or n <= 0:
            return 0

        if f"{m},{n}" in memo or f"{n},{m}" in memo:
            return memo[f"{m},{n}"]

        memo[f"{m},{n}"] = helper(m - 1, n) + helper(m, n - 1)
        memo[f"{n},{m}"] = memo[f"{m},{n}"]
        return memo[f"{m},{n}"]

    return helper(m, n)


print("Memoization method")
print(gridTraveller(1, 1))
print(gridTraveller(2, 2))
print(gridTraveller(3, 3))
print(gridTraveller(20, 20))
