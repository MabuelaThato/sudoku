import sys

def get_blocks():
    with open(sys.argv[1],"r") as file:
        puzzle_str = file.readlines()
        puzzle = []
        puzzle1 = []
        for line in puzzle_str:
            line = line.replace(" ","")
            line = list(line.strip())
            puzzle.append(line)

        for i in range(0, len(puzzle), 3):
            puzzle1.append(puzzle[i:i+3])

        blocks = {}
        blocks[1] = [puzzle1[0][0][0:3],puzzle1[0][1][0:3],puzzle1[0][2][0:3]]
        blocks[2] = [puzzle1[0][0][3:6],puzzle1[0][1][3:6],puzzle1[0][2][3:6]]
        blocks[3] = [puzzle1[0][0][6:9],puzzle1[0][1][6:9],puzzle1[0][2][6:9]]
        blocks[4] = [puzzle1[1][0][0:3],puzzle1[1][1][0:3],puzzle1[1][2][0:3]]
        blocks[5] = [puzzle1[1][0][3:6],puzzle1[1][1][3:6],puzzle1[1][2][3:6]]
        blocks[6] = [puzzle1[1][0][6:9],puzzle1[1][1][6:9],puzzle1[1][2][6:9]]
        blocks[7] = [puzzle1[2][0][0:3],puzzle1[2][1][0:3],puzzle1[2][2][0:3]]
        blocks[8] = [puzzle1[2][0][3:6],puzzle1[2][1][3:6],puzzle1[2][2][3:6]]
        blocks[9] = [puzzle1[2][0][6:9],puzzle1[2][1][6:9],puzzle1[2][2][6:9]]
    return blocks