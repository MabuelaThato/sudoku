def check_blocks(rows):
    counter = 0
    for row in rows:
        if '0' in row:
            counter += 1

    if counter > 0:
        return False
    else:
        return True