class Node():
    def __init__(self, state, action):
        self.state = state
        self.action = action

file = open("peg_game_sample_input.txt", "r+")
file_input = []
for line in file:
    file_input.append(line[:-1])
file.close()

N = int(file_input[0])

for n in range(1, N + 1):
    line = file_input[n] + " "
    holes = []
    R = C = M = K = None
    index1 = index2 = None

    for i in range(len(line)):
        if line[i] == " ":
            if R == None:
                R = int(line[:i])
                index1 = i + 1
            elif C == None:
                C = int(line[index1:i])
                index1 = i + 1
            elif K == None:
                K = int(line[index1:i])
                index1 = i + 1
            elif M == None:
                M = int(line[index1:i])
                index1 = i + 1
            else:
                if index1 == None:
                    index1 = i - 1
                elif index2 == None:
                    index2 = i
                else:
                    holes.append((int(line[index1:index2]), int(line[index2 + 1:i])))
                    index1 = index2 = None


    print(line)
    print(holes)
    print("")

probability = 1
round(probability, 6)
