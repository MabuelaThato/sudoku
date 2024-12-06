def check_blocks(blocks):
    counter = 0
    for x,y in blocks.items():
        for row in y:
            if "0" in row:
                counter += 1

    if counter > 0:
        return False
    else:
        return True