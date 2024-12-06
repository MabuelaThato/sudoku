def get_columns(blocks, block):
    columns = []
    block_rows = list(blocks.values())
    
    for y in range(3):
        first = []
        second = []
        third = []

        for i in range(y,9,3):
            for x in range(3):
                first.append(block_rows[i][x][0])
                second.append(block_rows[i][x][1])
                third.append(block_rows[i][x][2])

        columns.append(first)
        columns.append(second)
        columns.append(third)

    match block:
        case 1 | 4 | 7:
            return columns[0:3]
        case 2 | 5 | 8:
            return columns[3:6]
        case 3 | 6 | 9:
            return columns[6:9]