"""
Given an array of words and a target word
Find the number of ways that the target word can be created
"""


# Brute force method
def countConstruct(wordBank, target):
    if target == "":
        return 1

    count = 0

    for word in wordBank:
        if target[:min(len(word), len(target))] == word:
            count += countConstruct(wordBank, target[len(word):])

    return count


print("Brute force method")
print(countConstruct(["ab", "abc", "cd", "def", "abcd"], "abcdef"))
print(countConstruct(["bo", "rd", "ate", "t", "ska", "sk", "boar"], "skateboard"))
print(countConstruct(["a", "p", "ent", "enter", "ot", "o", "t"], "enterapotentpot"))
# print(countConstruct(["e", "ee", "eee", "eeee", "eeeee", "eeeee"], "eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef")) # Takes too long


# Memoization method
def countConstruct(bank, original):
    memo = {}

    def helper(wordBank, target):
        if target == "":
            return 1

        if target in memo:
            return memo[target]

        count = 0

        for word in wordBank:
            if target[:min(len(word), len(target))] == word:
                count += helper(wordBank, target[len(word):])

        memo[target] = count
        return count

    return helper(bank, original)


print("\nMemoization method")
print(countConstruct(["ab", "abc", "cd", "def", "abcd"], "abcdef"))
print(countConstruct(["bo", "rd", "ate", "t", "ska", "sk", "boar"], "skateboard"))
print(countConstruct(["a", "p", "ent", "enter", "ot", "o", "t"], "enterapotentpot"))
print(countConstruct(["e", "ee", "eee", "eeee", "eeeee", "eeeee"], "eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef"))