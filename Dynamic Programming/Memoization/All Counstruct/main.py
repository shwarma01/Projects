"""
Given a word bank and a target word
Find all the ways you can create the target word using the word bank
Return the combinations in an array
"""


# Brute force method
def allConstruct(wordBank, target):
    if target == "":
        return [[]]

    combinations = []

    for word in wordBank:
        if target[:min(len(word), len(target))] == word:
            result = allConstruct(wordBank, target[len(word):])
            for combination in result:
                combination.append(word)
                combinations.append(combination)

    return combinations


print("Brute force method")
print(allConstruct(["ab", "abc", "cd", "def", "abcd"], "abcdef"))
print(allConstruct(["bo", "rd", "ate", "t", "ska", "sk", "boar"], "skateboard"))
print(allConstruct(["a", "p", "ent", "enter", "ot", "o", "t"], "enterapotentpot"))
# print(allConstruct(["e", "ee", "eee", "eeee", "eeeee", "eeeeee"], "eeeeee")) # Takes too long


# Memoization method
def allConstruct(bank, original):
    memo = {}

    def helper(wordBank, target):
        if target == "":
            return [[]]

        if target in memo:
            return memo[target]

        combinations = []

        for word in wordBank:
            if target[:min(len(word), len(target))] == word:
                result = helper(wordBank, target[len(word):])
                for combination in result:
                    combination.append(word)
                    combinations.append(combination)

        memo[target] = combinations
        return combinations

    return helper(bank, original)


print("\nMemoization method")
print(allConstruct(["ab", "abc", "cd", "def", "abcd"], "abcdef"))
print(allConstruct(["bo", "rd", "ate", "t", "ska", "sk", "boar"], "skateboard"))
print(allConstruct(["a", "p", "ent", "enter", "ot", "o", "t"], "enterapotentpot"))
print(allConstruct(["e", "ee", "eee", "eeee", "eeeee", "eeeeee"], "eeeeee"))
