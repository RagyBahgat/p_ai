import copy

puzzle = []
def print_puzzle(p):
    str = ""
    for i in range(3):
        for j in range(3):
            if p[i][j] == '0':
                str += '  '
            else:
                str += p[i][j] + ' '
        str += '\n'
    print str

with open('path','r') as file:
    for line in file:
        puzzle.append(line.strip().split(' '))

print_puzzle(puzzle)

fin_puzzle = [['1','2','3'],['4','5','6'],['7','8','0']]

def check(state,final):
    errors=0;
    for i in range(3):
        for j in range(3):
            if state[i][j] != final[i][j] and state[i][j] != '0':
                errors += 1
    return errors

def mann(state):
    errors = 0;
    for i in range(3):
        for j in range(3):
            if state[i][j] == '1':
                errors += abs(0-i)+abs(0-j)
            elif state[i][j] == '2':
                errors += abs(0 - i) + abs(1 - j)
            elif state[i][j] == '3':
                errors += abs(0 - i) + abs(2 - j)
            elif state[i][j] == '4':
                errors += abs(1 - i) + abs(0 - j)
            elif state[i][j] == '5':
                errors += abs(1 - i) + abs(1 - j)
            elif state[i][j] == '6':
                errors += abs(1 - i) + abs(2 - j)
            elif state[i][j] == '7':
                errors += abs(2 - i) + abs(0 - j)
            elif state[i][j] == '8':
                errors += abs(2 - i) + abs(1 - j)
    return errors
def find_zero(state):
    for i in range(3):
        for j in range(3):
            if state[i][j] == '0':
                return [i,j]

def nodes(lis):
    #print lis

    if(lis[:]==[0,0]):
        return [[0,1],[1,0]]

    elif(lis[:]==[0,1]):
        return [[0,0],[0,2],[1,1]]

    elif(lis[:]==[0,2]):
        return [[0,1],[1,2]]

    elif(lis[:]==[1,0]):
        return [[0,0],[1,1],[2,0]]

    elif(lis[:]==[1,1]):
        return [[1,0],[1,2],[0,1],[2,1]]

    elif(lis[:]==[1,2]):
        return [[1,1],[0,2],[2,2]]

    elif(lis[:]==[2,0]):
        return [[1,0],[2,1]]

    elif(lis[:]==[2,1]):
        return [[1,1],[2,0],[2,2]]

    elif(lis[:]==[2,2]):
        return [[2,1],[1,2]]

def move_node(place,zero_place,state):
    temp = state[place[0]][place[1]]
    state[place[0]][place[1]] = state[zero_place[0]][zero_place[1]]
    state[zero_place[0]][zero_place[1]] = temp
    return state

def min_moves(list):
    min = list[0]
    counter = -1
    min_place =-1;
    for i in list:
        counter += 1
        if i <= min:
            min = i
            min_place = counter
    return min_place

num_of_moves = 0
def arrange(state, final,zero,num_of_moves):
    error = check(state, final)
    h = []
    if (error == 0):
        print 'Minimum number of moves = %s' %num_of_moves
        return
    else:
        zero_place = find_zero(state)
        places_to_move = nodes(zero_place)
        for i in places_to_move:
            if i == zero:
                h.append(100)
            else:
                copy_state = copy.deepcopy(state)
                test_state = move_node(i,zero_place,copy_state)
                h.append(mann(test_state))
        min_move = min_moves(h)
        move_node(places_to_move[min_move],zero_place,state)
        print_puzzle(state)
        num_of_moves += 1
        arrange(state,final,zero_place,num_of_moves)

arrange(puzzle,fin_puzzle,[10,10],num_of_moves)