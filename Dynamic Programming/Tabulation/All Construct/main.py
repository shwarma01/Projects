"""
Given an array of words and a target
Find all the combinations of words to make the target
"""

def countConstruct(target, wordBank):
    table = [[] for _ in range(len(target) + 1)]
    table[0] = [[]]

    for start in range(len(target) + 1):
        if len(table[start]) != 0:
            for end in range(start + 1, len(target) + 1):
                if target[start:end] in wordBank:
                    for combination in table[start]:
                        new = [word for word in combination]
                        new.append(target[start:end])
                        table[end].append(new)

    return table[len(target)]


print(countConstruct("abcdef", ["ab", "abc", "def", "cd", "abcd", "ef"]))
