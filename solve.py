import sys
from calculate import calculate
from get_blocks import get_blocks
from check_blocks import check_blocks
from get_rows import get_rows 
from get_columns import get_columns

def main():
    if len(sys.argv) < 4:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 4:
        sys.exit("Too many command-line arguments")
    else:
        blocks = get_blocks()

    rows = get_rows(blocks)
    columns = get_columns(blocks)
    blocks_list = []
    for x,y in blocks.items():
        blocks_list.append(y)
  
    while True:
        if check_blocks(rows):
            print("DONEEEEE")
            print(rows)
            break
        else:

            result =  calculate(blocks,rows, columns)
            print(f"rows: {result[0]}")
            
if __name__ == "__main__":
    main()