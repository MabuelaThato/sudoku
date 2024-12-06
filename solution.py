blocks = {1: [['9', '6', '2'], ['1', '8', '5'], ['3', '7', '4']], 2: [['3', '7', '8'], ['4', '2', '9'], ['5', '6', '1']], 3: [['5', '1', '4'], ['3', '6', '7'], ['8', '2', '9']], 4: [['5', '3', '1'], ['6', '4', '9'], ['8', '2', '7']], 5: [['9', '8', '4'], ['2', '5', '7'], ['6', '1', '3']], 6: [['2', '7', '6'], ['1', '3', '8'], ['9', '4', '5']], 7: [['2', '1', '8'], ['4', '9', '6'], ['7', '5', '3']], 8: [['7', '4', '5'], ['8', '3', '2'], ['1', '9', '6']], 9: [['6', '9', '3'], ['7', '5', '1'], ['4', '8', '2']]}

def solution(blocks):
    rows = []

    for x in range(1,10,3):
        for i in range(3):
            row = ""
            print(str(blocks[x][i] + blocks[x+1][i] + blocks[x+2][i]))
            for num in blocks[x][i]:
                row += f"{num} "
            for num in blocks[x+1][i]:
                row += f"{num} "
            for num in blocks[x+2][i]:
                row += f"{num} "
            rows.append(row)

    try:
        with open("solved_puzzle.txt", "w") as file:
            for row in rows:
                file.write(f"{row}\n")
    except FileNotFoundError:
        print("Failed to write solution to new file")
        return
    
solution(blocks)