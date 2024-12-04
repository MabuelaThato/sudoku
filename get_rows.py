def get_rows(blocks):
    rows = []
    block_rows = list(blocks.values())
    for i in range(0,9,3):
        for x in range(3):
            current = []
            current += block_rows[i][x]
            current += block_rows[i + 1][x]
            current += block_rows[i + 2][x]
            rows.append(current)

    return rows
