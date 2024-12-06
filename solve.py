import sys
from new_calculate import new_calculate
from get_blocks import get_blocks
from check_blocks import check_blocks

def main():
    if len(sys.argv) < 4:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 4:
        sys.exit("Too many command-line arguments")
    else:

            blocks = get_blocks()

    while True:

        if check_blocks(blocks):
            print("DONEEEEE")
            print(blocks)
            break

        else:
            blocks =  new_calculate(blocks)
            
if __name__ == "__main__":
    main()