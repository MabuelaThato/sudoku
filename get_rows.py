def get_rows(blocks,block):
    rows = []
    block_rows = list(blocks.values())
    for i in range(0,9,3):
        for x in range(3):
            current = []
            current += block_rows[i][x]
            current += block_rows[i + 1][x]
            current += block_rows[i + 2][x]
            rows.append(current)
    match block:
        case 1 | 2 | 3:
            return rows[0:3]
        case 4 | 5 | 6:
            return rows[3:6]
        case 7 | 8 | 9:
            return rows[6:9]