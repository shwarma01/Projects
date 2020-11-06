import cv2, os, sys
import numpy as np
import random

orig_and_translations = []
orig_nums = []
rotation_180 = [0, 1, 8]
vertically_flipped = [0, 1, 3, 8]
horizontally_flipped = [0, 1, 8]
ROWS = 28
COLS = 28

for filename in os.listdir("Numbers"):
    img = cv2.imread(os.path.join("Numbers", filename), cv2.IMREAD_GRAYSCALE) / 255.0
    img = cv2.resize(img, (COLS, ROWS))
    orig_nums.append(img)


for i in range(0, 10):
    img = []
    img.append(orig_nums[i])

    if i in rotation_180:
        Matrix = cv2.getRotationMatrix2D((COLS / 2, ROWS / 2), 180, 1)
        img.append(cv2.warpAffine(orig_nums[i], Matrix, (COLS, ROWS)))

    if i in vertically_flipped:
        img.append(cv2.flip(orig_nums[i], 0))

    if i in horizontally_flipped:
        img.append(cv2.flip(orig_nums[i], 1))

    if i not in rotation_180 and i not in vertically_flipped and i not in horizontally_flipped:
        orig_and_translations.append(img[0])
    else:
        orig_and_translations.append(img)

"""
I have chose to have one of my dataset's image be 300 X 300 pixels.
I will have at most 5 numbers in a row together and at most three rows of numbers together
"""

dataset = []

for examples in range(int(sys.argv[1])):
    flat_arr = []
    dataset_img = []
    row_arr = []
    space_count = 0

    while True:
        random_num = random.randint(0, 100)

        if random_num <= 9:
            numbers_to_show = []
            number_count = 0

            for i in range(1, 6):
                if (300 - len(row_arr)) > (28 * (6 - i) + 4 * (i - 1)):
                    number_count = 6 - i
                    break

            if number_count == 0:
                continue

            for i in range(number_count):
                numbers_to_show.append(random.randint(0, 9))

            translations = []
            space_count = len(row_arr)

            for i in numbers_to_show:
                if i == 3:
                    translations.append(random.randint(0, 1))
                elif i in rotation_180:
                    translations.append(random.randint(0, 3))
                else:
                    translations.append(-1)

            for i in range(28):
                row_arr = []

                for k in range(space_count):
                    row_arr.append(0)

                for translation, number in zip(translations, numbers_to_show):
                    for j in range(28):
                        if number in rotation_180 or number == 3:
                            row_arr.append(orig_and_translations[number][translation][i][j])
                        else:
                            row_arr.append(orig_and_translations[number][i][j])

                    for j in range(4):
                        row_arr.append(0.0)

                for i in  range(300 - len(row_arr)):
                    row_arr.append(0.0)

                dataset_img.append(row_arr)
        else:
            if len(row_arr) != 300:
                row_arr.append(0)
            else:
                dataset_img.append(row_arr)
                row_arr = []

        if (300 - len(dataset_img)) < 28 and (300 - len(dataset_img)) > 0:
            for i in range(300 - len(dataset_img)):
                for j in range(300):
                    row_arr.append(0.0)

                dataset_img.append(row_arr)
                row_arr = []

            break

    values = 0
    for row in dataset_img:
        for val in row:
            values += 1
            flat_arr.append(val)

    print(values)

    dataset.append(flat_arr)

if sys.argv[2] == "train":
    np.savetxt("train.csv", dataset, fmt = '%s')
else:
    np.savetxt("test.csv", dataset, fmt = '%s')
