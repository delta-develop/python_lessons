def right_or_left(matrix, arr, pos):
    if matrix:
        rows = len(matrix)
        
        if pos == "left":
            index = 0
            custom_range = range(rows - 1, -1, -1)
        else:
            index = -1
            custom_range = range(rows)

        for row in custom_range:
            arr += [matrix[row][index]]
            del matrix[row][index]


def top_or_bottom(matrix, arr, pos):
    if matrix:
        
        if pos == "top":
            index = 0
        else:
            index = -1
            matrix[index].reverse()

        arr += matrix[index]
        del matrix[index]

def snail_sort(matrix):
    arr = []
    while matrix:

        top_or_bottom(matrix, arr, "top")

        right_or_left(matrix, arr, "right")

        top_or_bottom(matrix, arr, "bottom")

        right_or_left(matrix, arr, "left")

    return arr


if __name__ == "__main__":

    test_arr_2 = [
        [0, 1, 2, 3, 4, 5],
        [16, 17, 18, 19, 6],
        [15, 24, 25, 20, 7],
        [14, 23, 22, 21, 8],
        [13, 12, 11, 10, 9],
    ]

    print(snail_sort(test_arr_2))
