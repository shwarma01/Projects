file = open("double_squares_input.txt", "r+")
file_input = []
for line in file:
    file_input.append(int(line[:-1]))
file.close()

file = open("output.txt", "w+")

N = file_input[0]

for n in range(1, N + 1):
    count = 0
    num = file_input[n]

    for i in range(num + 1):
        if i**2 > num:
            break

        for j in range(i, num + 1):
            if (i**2 + j**2) > num:
                break

            if (i**2 + j**2) == num:
                count += 1
                break

    file.write(f"Case #{n}: {count}\n")
    print(f"Case #{n}: {count}")

file.close()
