import games
import heuristic

#game = games.TicTacToe(h=3,v=3,k=3)
game = games.ConnectFour()
state = game.initial
player = 'X'
difficultyChoosed = False
playerChoosed = False

while not difficultyChoosed:
    difficultyLevel = int(raw_input("Escoja el nivel de dificultad: 1: Facil, 2: Medio o 3: Dificil ==> "))
    if difficultyLevel == 1 or 2 or 3:
        difficultyChoosed = True
    else:
        print "Tiene que escoger 1: Facil, 2: Medio o 3: Dificil"

while not playerChoosed:
    playerStart = raw_input("Elija quien empieza primero: O: usted o X: maquina ==> ")
    if playerStart == 'X' or 'O':
        playerChoosed = True
    else:
        print "Tiene que escoger O: usted o X: maquina"

while playerChoosed:
    print "Jugador a mover:", game.to_move(state)
    game.display(state)

    if player == 'O':
        col_str = raw_input("Movimiento: ")
        coor = int(str(col_str).strip())
        x = coor
        y = -1
        legal_moves = game.legal_moves(state)
        for lm in legal_moves:
            if lm[0] == x:
                y = lm[1]
    
            state = game.make_move((x, y), state)
            player = 'X'
    else:
        print "Thinking..."
        #move = games.minimax_decision(state, game)
        #move = games.alphabeta_full_search(state, game)
        if difficultyChoosed == 3:
            move = games.alphabeta_search(state, game, 3, heuristic.calculateHeuristic, playerChoosed, 3)
        if difficultyChoosed == 2:
            move = games.alphabeta_search(state, game, 2, heuristic.calculateHeuristic, playerChoosed, 2)
        else:
            move = games.alphabeta_search(state, game, 1, None, playerChoosed, 1)

        state = game.make_move(move, state)
        player = 'O'
    print "-------------------"
    if game.terminal_test(state):
        game.display(state)
        print "Final de la partida"
        if player == playerChoosed:
            print "Has ganado"
        else:
            print "Has perdido"
        break
