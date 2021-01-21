"""
Given an array of words and a target
Find how many ways you can make the target using combinations of the words
"""


def countConstruct(target, wordBank):
    table = [0 for _ in range(len(target) + 1)]
    table[0] = 1

    for start in range(len(target) + 1):
        if table[start] != 0:
            for end in range(start + 1, len(target) + 1):
                if target[start:end] in wordBank:
                    table[end] += table[start]

    return table[len(target)]

print(countConstruct("abcdef", ["ab", "abc", "def", "cd", "abcd", "ef"]))
