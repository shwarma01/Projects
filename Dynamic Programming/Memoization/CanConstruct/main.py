"""
Given a word bank and a target
Figure out if you can construct the target using the words in the word bank
You can use the words in the word bank as many times as you want
"""


# Brute force method
def canConstruct(wordBank, target):
    if target == "":
        return True

    for word in wordBank:
        if len(word) <= len(target):
            if target[:len(word)] == word:
                if canConstruct(wordBank, target[len(word):]) == True:
                    return True

    return False


print("Brute force method")
print(canConstruct(["ab", "abc", "cd", "def", "abcd"], "abcdef"))
print(canConstruct(["bo", "rd", "ate", "t", "ska", "sk", "boar"], "skateboard"))
print(canConstruct(["a", "p", "ent", "enter", "ot", "o", "t"], "enterapotentpot"))
# print(canConstruct(["e", "ee", "eee", "eeee", "eeeee", "eeeee"], "eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef")) # Takes too long


# Memoization method
def canConstruct(bank, original):
    memo = {}

    def helper(wordBank, target):
        if target == "":
            return True

        if target in memo:
            return memo[target]

        for word in wordBank:
            if len(word) <= len(target):
                if target[:len(word)] == word:
                    memo[target] = helper(wordBank, target[len(word):])
                    if memo[target] == True:
                        return True

        memo[target] = False
        return False

    return helper(bank, original)


print("\nMemoization method")
print(canConstruct(["ab", "abc", "cd", "def", "abcd"], "abcdef"))
print(canConstruct(["bo", "rd", "ate", "t", "ska", "sk", "boar"], "skateboard"))
print(canConstruct(["a", "p", "ent", "enter", "ot", "o", "t"], "enterapotentpot"))
print(canConstruct(["e", "ee", "eee", "eeee", "eeeee", "eeeee"], "eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef"))
