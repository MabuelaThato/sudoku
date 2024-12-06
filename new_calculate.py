from get_rows import get_rows
from get_numbers import get_numbers
from get_columns import get_columns

def check(block,rows,x,columns,y,numbers):
    possibles = []
    for i in range(1,10):
        if f"{i}" in numbers or f"{i}" in rows[x] or f"{i}" in columns[y]:
            continue
        else:
            possibles.append(f"{i}")

    if len(possibles) == 1:
        block[x][y] = possibles[0]
    
    return block

def new_calculate(blocks):
    for x,y in blocks.items():
        for row in range(3):
            for column in range(3):
                rows = get_rows(blocks, x)
                columns = get_columns(blocks, x)
                block_numbers = get_numbers(y)
                if y[row][column] == "0":
                    y = check(y,rows,row,columns,column, block_numbers)
                    blocks[x] = y
    return blocks
