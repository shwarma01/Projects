"""
figure out how many inversions with ? = 0
add 1 to ?
repeat inversion test
"""

def update(i):
    if arr[i] == 0:
        arr[i] = 1
    else:
        arr[i] = 0
        update(question_mark_indices.index(i) - 1)    

string = input()
question_mark_indices = []
arr = []
inversions = 0
for i in range(len(string)):
    if string[i] == "?":
        question_mark_indices.append(i)
        arr.append(0)
    else:
        arr.append(int(string[i]))

for i in range(2 ** len(question_mark_indices)):
    one_indices = []
    for i in question_mark_indices:
        if arr[i] == 1:
            one_indices.append(i)
    
    index = len(arr) - 1
    for one_index in one_indices[::-1]:
        inversions += index - one_index - 1
        index -= 1
    
    update(question_mark_indices[-1])

print(inversions % 1000000007)

"""
how to count inversions:
subtract index of rightmost 1 from next rightmost 1
    0101
    3 - 1 = 2
    need to sub 1
    gotta keep track of left rightmost 1
    how many times repeat?
        sum(arr) - 1?

    010101
    5 - 3 - 1 = 1
    4 - 1 - 1 = 2
    sum(arr) = 3
    sum(arr) - 1 = 2
"""
