def check_pawn(position, color, location_b, location_r):
    moves_list = []
    if color == 'black':
        if (position[0], position[1] + 1) not in location_b and position[1] + 1 <= 9:
            moves_list.append((position[0], position[1] + 1))
        if position[1] >= 5:
            if (position[0] + 1, position[1]) not in location_b and position[0] + 1 <= 8:
                moves_list.append((position[0] + 1, position[1]))
            if (position[0] - 1, position[1]) not in location_b and position[0] - 1 >= 0:
                moves_list.append((position[0] - 1, position[1]))
    elif color == "red":
        if (position[0], position[1] - 1) not in location_r and position[1] - 1 >= 0:
            moves_list.append((position[0], position[1] - 1))
        if position[1] <= 4:
            if (position[0] + 1, position[1]) not in location_r and position[0] + 1 <= 8:
                moves_list.append((position[0] + 1, position[1]))
            if (position[0] - 1, position[1]) not in location_r and position[0] - 1 >= 0:
                moves_list.append((position[0] - 1, position[1]))
    return moves_list

def check_rook(position, color, location_b, location_r):
    moves_list = []
    if color == 'black':
        friends_list, enemies_list = location_b, location_r
    else:
        friends_list, enemies_list = location_r, location_b

    for i in range(4):
        path = True
        chain = 1
        if i == 0:
            x, y = -1, 0
        elif i == 1:
            x, y = 1, 0
        elif i == 2:
            x, y = 0, 1
        elif i == 3:
            x, y = 0, -1
        while path: 
            if (position[0] + chain * x, position[1] + chain * y) not in friends_list and 0 <= position[0] + chain * x <= 8 and 0 <= position[1] + chain * y <= 9:
                moves_list.append((position[0] + chain * x, position[1] + chain * y))
                if (position[0] + chain * x, position[1] + chain * y) in enemies_list:
                    path = False
                chain += 1
            else:
                path = False
        
    return moves_list

def check_knight(position, color, location_b, location_r):
    moves_list = []
    if color == 'black':
        friends_list = location_b
    else:
        friends_list = location_r

    # 8 squares to check for knights, they can go two squares in one direction and one in another
    targets = [(2, 1), (2, -1), (1, 2), (-1, 2), (-2, 1), (-2, -1), (-1, -2), (1, -2)]
    blockages = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    for i in range(8):
        target = (position[0] + targets[i][0], position[1] + targets[i][1])
        blockage = (position[0] + blockages[i//2][0], position[1] + blockages[i//2][1])
        if target not in friends_list and 0 <= target[0] <= 8 and 0 <= target[1] <= 9 and blockage not in (location_r + location_b):
            moves_list.append(target)
    return moves_list

def check_advisor(position, color, location_b, location_r):
    moves_list = []
    if color == 'black':
        friends_list = location_b
        box = [(3, 0), (5, 0), (3, 2), (5,2), (4, 1)]
    else:
        friends_list = location_r
        box = [(3, 9), (3, 7), (5, 9), (5,7), (4, 8)]
    
    targets = [(1, 1), (1, -1), (-1, 1), (-1, -1)]
    for i in range(4):
        coord = (position[0] + targets[i][0], position[1] + targets[i][1]) 
        if coord not in friends_list and coord in box:
            moves_list.append(coord)

    return moves_list

def check_cannon(position, color, location_b, location_r):
    moves_list = []
    if color == 'black':
        friends_list, enemies_list = location_b, location_r
    else:
        friends_list, enemies_list = location_r, location_b

    for i in range(4):
        path = True
        chain = 1
        if i == 0:
            x, y = -1, 0
        elif i == 1:
            x, y = 1, 0
        elif i == 2:
            x, y = 0, 1
        elif i == 3:
            x, y = 0, -1
        while path:
            if 0 <= position[0] + chain * x <= 8 and 0 <= position[1] + chain * y <= 9:
                if (position[0] + chain * x, position[1] + chain * y) not in (friends_list + enemies_list):
                    moves_list.append((position[0] + chain * x, position[1] + chain * y))
                    chain += 1
                else:
                    for j in range(1, 9):
                        if (position[0] + (chain + j) * x, position[1] + (chain + j) * y) in enemies_list:
                            moves_list.append((position[0] + (chain + j) * x, position[1] + (chain + j) * y))
                            break
                    path = False
            else: 
                path = False

 
    return moves_list

def check_elephant(position, color, location_b, location_r):
    moves_list = []
    if color == 'black':
        friends_list = location_b
        box = [(2, 0), (0, 2), (2, 4), (4, 2), (6, 0), (8, 2), (6, 4)]
    else:
        friends_list = location_r
        box = [(2, 9), (0, 7), (2, 5), (4, 7), (6, 9), (8, 7), (6, 5)]
    
    targets = [(2, 2), (-2, -2), (2, -2), (-2, 2)]
    blockages = [(0.5*x, 0.5*y) for (x,y) in targets]
    for i in range(4):
        coord = (position[0] + targets[i][0], position[1] + targets[i][1]) 
        blockage = (position[0] + blockages[i][0], position[1] + blockages[i][1]) 
        if coord not in friends_list and coord in box and blockage not in (location_r + location_b):
            moves_list.append(coord)

    return moves_list

def check_general(position, color, location_b, location_r):
    moves_list = []
    if color == 'black':
        friends_list = location_b
        box = [(3, 0), (4, 0), (5, 0), (3, 1), (4, 1), (5, 1), (3, 2), (4, 2), (5, 2)]
    else:
        friends_list = location_r
        box = [(3, 9), (4, 9), (5, 9), (3, 8), (4, 8), (5, 8), (3,7), (4,7), (5,7)]
    
    targets = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    for i in range(4):
        coord = (position[0] + targets[i][0], position[1] + targets[i][1]) 
        if coord not in friends_list and coord in box:
            moves_list.append(coord)

    return moves_list
