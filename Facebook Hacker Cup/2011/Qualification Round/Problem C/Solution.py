file = open("studious_student_input.txt", "r+")
file_input = []
for line in file:
    file_input.append(line[:-1])
file.close()

N = int(file_input[0])
file = open("output.txt", "w+")

for n in range(1, N + 1):
    line = file_input[n] + " "
    words_num = None
    words = []
    output = ""
    index = 0
    for i in range(len(line)):
        if line[i] == " ":
            if index == 0:
                words_num = int(line[:i])
                index = i + 1
            else:
                words.append(line[index:i])
                index = i + 1

    for k in range(words_num):
        lowest = float("inf")
        index = None

        for i in range(len(words)):
            num = ord(words[i][0])
            if num < lowest:
                index = i
                lowest = num
            elif num == lowest:
                solved = False
                for j in range(min(len(words[index]), len(words[i]))):
                    if ord(words[i][j]) < ord(words[index][j]):
                        index = i
                        solved = True
                        break
                    elif ord(words[i][j]) > ord(words[index][j]):
                        solved = True
                        break

                if not solved:
                    if len(words[i]) > len(words[index]):
                        index = i

        output += words[index]
        words.remove(words[index])

    print(f"Case #{n}: {output}")
    file.write(f"Case #{n}: {output}")

file.close()
