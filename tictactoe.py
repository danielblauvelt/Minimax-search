import math
import copy

def main():
    # board = [['O', 'O', 'X'], ['X', '_', 'O'], ['_', '_', 'X']]
    # board = [['O', '_', '_'], ['_', '_', '_'], ['_', '_', 'X']]
    # board = [['O', '_', '_'], ['_', 'X', '_'], ['O', '_', 'X']]
    # board = [['O', 'O', '_'], ['X', 'O', '_'], ['X', '_', '_']]
    # board = [['_', '_', '_'], ['_', '_', '_'], ['_', '_', '_']]
    board = [['O', 'O', '_'], ['X', '_', 'O'], ['X', '_', 'X']]

    turn = 0

    # print(minimax(board, 'X'))
    while(utility(board) == None):
        if turn == 0:
            board = minimax(board, 'X')[1]
            print(board)
            turn = 1
        else:
            board = minimax(board, 'O')[1]
            print(board)
            turn = 0
    print(utility(board))
    print(board)

def minimax(board, letter):
    if letter == 'O':
        min_val = min_value(board, 0)
        # print(min_val[0])
        return min_val
    else:
        max_val = max_value(board, 1)
        # print(max_val[0])
        return max_val


def min_value(state, index):

    if utility(state) != None:
        return utility(state), state

    min_value_1 = math.inf
    best_state = None

    if index % 2 == 0:
        states = get_states(state, 'O')
    else:
        states = get_states(state, 'X')
    # if len(states) == 1:
    #     return utility(states[0]), state
    for pos in states:
        next_value = result(pos, index + 1)
        if next_value < min_value_1:
            min_value_1 = next_value
            best_state = pos
    return min_value_1, best_state

def max_value(state, index):

    if utility(state) != None:
        return utility(state), state

    max_value_1 = -math.inf
    best_state = None

    if index % 2 == 1:
        states = get_states(state, 'X')
    else:
        states = get_states(state, 'O')
    # if len(states) == 1:
    #     return utility(states[0]), state
    for pos in states:
        next_value = result(pos, index + 1)
        if next_value > max_value_1:
            max_value_1 = next_value
            best_state = pos
    # print(max_value_1)
    # print(best_state)
    return max_value_1, best_state


def result(state, index):
    if utility(state) != None:
        return utility(state)
    vals = []
    val = 0
    if index % 2 == 1:
        states = get_states(state, 'X')
    else:
        states = get_states(state, 'O')
    for pos in states:
        next_value = utility(pos)
        if next_value == None:
            # print('max state', pos)
            next_value = result(pos, index + 1)
        vals.append(next_value)
    
    if index % 2 == 1:
        val = max(vals)
    if index % 2 == 0:
        val = min(vals)
    return val


def get_states(state, letter):
    states = []
    
    for i in range(len(state)):
        for j in range(len(state[i])):
            if state[i][j] == '_':
                state_c = []
                state_c = copy.deepcopy(state)
                state_c[i][j] = letter
                states.append(state_c)
    return states

def utility(state):
    # print(state)
    o = checkWinner('O', state)
    x = checkWinner('X', state)

    if not o and not x:
        if '_' in state[0] or '_' in state[1] or '_' in state[2]:
            return None
        return 0
    if o:
        return -1
    if x: 
        return 1

def checkWinner(letter, state):
    return ((state[0][0] == letter and state[0][1] == letter and state[0][2] == letter) 
    or (state[1][0] == letter and state[1][1] == letter and state[1][2] == letter) 
    or (state[2][0] == letter and state[2][1] == letter and state[2][2] == letter) 
    or (state[0][0] == letter and state[1][0] == letter and state[2][0] == letter) 
    or (state[0][1] == letter and state[1][1] == letter and state[2][1] == letter)
    or (state[0][2] == letter and state[1][2] == letter and state[2][2] == letter)
    or (state[0][0] == letter and state[1][1] == letter and state[2][2] == letter) 
    or (state[0][2] == letter and state[1][1] == letter and state[2][0] == letter))
    
            



if __name__ == '__main__':
    main()

