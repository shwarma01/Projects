"""
Given an array of words and a target
Figure out if you can combine the words to create the target
"""


def canConstruct(target, wordBank):
    table = [False for _ in range(len(target) + 1)]
    table[0] = True

    for start in range(len(target) + 1):
        if table[start] is True:
            for end in range(start + 1, len(target) + 1):
                if target[start:end] in wordBank:
                    table[end] = True

    return table[len(target)]

print(canConstruct("abcdef", ["ab", "abc", "def", "cd", "abcd"]))