"""
Calculate the nth fibonacci number
"""

def fib(n):
    if n == 0: return 0
    elif n == 1: return 1

    table = [0 for i in range(n + 1)]
    table[1] = 1

    for i in range(n + 1):
        try:
            table[i + 1] += table[i]
            table[i + 2] += table[i]
        except IndexError as e:
            pass

    return table[n]

"""
# Optimized version of tabulation
def fib(n):
    table = [0, 1]

    for i in range(2, n + 1):
        table[i % 2] = sum(table)

    return table[n % 2]
"""


print(fib(6))
print(fib(7))
print(fib(8))
print(fib(50))