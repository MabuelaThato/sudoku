def get_numbers(block):
    numbers = []
    for i in range(3):
        for x in range(3):
            if block[i][x] != "0":
                numbers.append(block[i][x])

    return numbers