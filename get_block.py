def get_block(i,x):
    if i < 3:
        if x < 3:
            return "block1"
        elif x < 6:
            return "block2"
        elif x >= 6:
            return "block3"
    elif i < 6:
        if x < 3:
            return "block4"
        elif x < 6:
            return "block5"
        elif x >= 6:
            return "block6"
    elif i >= 6:
        if x < 3:
            return "block7"
        elif x < 6:
            return "block8"
        elif x >= 6:
            return "block9"
