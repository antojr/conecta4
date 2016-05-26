def punctuation(state, coord, player, (mov_x, mov_y)):
    if player == 'X':
        enemy = 'O'
    else:
        enemy = 'X'
    
    x, y = coord
    value = 0

    while (8 > x > 0) and (7 > y > 0):
        if state.board.get((x, y)) == player:
            value += 100
        if state.board.get((x, y)) is None:
            value += 10
        if state.board.get((x, y)) == enemy:
            break
        x, y = x + mov_x, y + mov_y

    x, y = coord
    x, y = x - mov_x, y - mov_y

    while (8 > x > 0) and (7 > y > 0):
        if state.board.get((x, y)) == player:
            value += 100
        if state.board.get((x, y)) is None:
            value += 10
        if state.board.get((x, y)) == enemy:
            break
        x, y = x - mov_x, y - mov_y
    
    return value

def calculateHeuristic(state, player, dificultad):
    if player == 'X':
        enemy = 'O'
    else:
        enemy = 'X'

    if player == 'X' and state.utility != 0:
        return state.utility * 9999

    if player == 'O' and state.utility != 0:
        return state.utility * -9999

    value = 0
    l_moves = []
    for(x, y) in state.moves:
        if y == 1 or(x, y - 1) in state.board:
            l_moves += [(x, y)]

    for i in l_moves:
        x, y = i
        
        if dificultad == 1:
            #Horinzontal
            value += punctuation(state, (x, y), player, (1, 0))
            #Vertical
            value += punctuation(state, (x, y), player, (0, 1))
            #Diagonal de iz a der
            value += punctuation(state, (x, y), player, (1, 1))
            #Diagonal de der a iz
            value += punctuation(state, (x, y), player, (1, -1)) 
            
            value -= punctuation(state, (x, y), enemy, (1, 0))
            value -= punctuation(state, (x, y), enemy, (0, 1))
            
        if dificultad == 2:
            value += punctuation(state, (x, y), player, (1, 0)) 
            value += punctuation(state, (x, y), player, (0, 1)) 
            value += punctuation(state, (x, y), player, (1, 1)) 
            value += punctuation(state, (x, y), player, (1, -1)) 

            value -= punctuation(state, (x, y), enemy, (1, 0))
            value -= punctuation(state, (x, y), enemy, (0, 1))
            value -= punctuation(state, (x, y), enemy, (1, 1))
            value -= punctuation(state, (x, y), enemy, (1, -1))

    return value
