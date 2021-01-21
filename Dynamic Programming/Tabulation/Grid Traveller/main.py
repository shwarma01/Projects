"""
On a grid of mxn
You start at the top left of the grid
How many ways to get to the bottom right
"""


def gridTraveller(m, n):
    # table variable is not the grid
    # The indices are the mxn values
    # So any element in the table that has an index of 0 at any axis will be 0
    # Since a 2D grid having a length of 0 on any axis is not possible
    table = []
    for M in range(m + 1):
        table.append([0 for _ in range(n + 1)])
    table[1][1] = 1

    for M in range(m + 1):
        for N in range(n + 1):
            if M < m:
                table[M + 1][N] += table[M][N]

            if N < n:
                table[M][N + 1] += table[M][N]

    return table[m][n]


print(gridTraveller(1, 1))
print(gridTraveller(2, 3))
print(gridTraveller(3, 2))
print(gridTraveller(3, 3))
print(gridTraveller(18, 18))
