def calculate(blocks,rows, columns):
    needed_rows = {}
    needed_cols = {}
    counter = 0
    for x in range(9):
        nums1 = []
        nums2 = []
        indexes1 = []
        indexes2 = []
        for i in range(1,10):
            if f"{i}" not in rows[x]:
                nums1.append(f"{i}")
            if f"{i}" not in columns[x]:
                nums2.append(f"{i}")
        for i in range(9):
            if rows[x][i] == "0":
                indexes1.append(i)
            if columns[x][i] == "0":
                indexes2.append(i)
        needed_rows[counter] = [nums1, indexes1, x]
        needed_cols[counter] = [nums2, indexes2, x]
        counter += 1

# CHECK ROWS
    for x,y in needed_rows.items():
        row_missing = y[0]
        zero_indexes = y[1]
        row = y[2]
        for num in row_missing:
            possible_cols = []
            for index in zero_indexes:
                if num not in columns[index] and num not in rows[row]:
                    possible_cols.append(index)
            if len(possible_cols) == 1:
                index = possible_cols[0]
                rows[x][index] = num 
                columns[index][x] = num

# CHECK COLUMNS
    for x,y in needed_cols.items():
        col_missing = y[0]
        zero_indexes = y[1]
        column = y[2]
        for num in col_missing:
            possible_rows = []
            for index in zero_indexes:
                if num not in rows[index] and num not in columns[column] :
                    possible_rows.append(index)
            if len(possible_rows) == 1:
                index = possible_rows[0]
                rows[index][x] = num 
                columns[x][index] = num
    
    # # CHECK BLOCKS
    # for x,y in blocks.items():
    #     current_needed = {}
    #     zeros_indexes = []
    #     left = [1,4,7]
    #     middle = [2,5,8]
    #     if x in left:
    #         for i in range(3):
    #             for z in range(3):
    #                 if y[i][z] == "0":
    #                     current_needed[[i,z]] = 

    return [needed_rows, needed_cols]