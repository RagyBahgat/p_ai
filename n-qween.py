import random as rand
import copy

qween = []
line = []
for j in range(8):
    line.append('0')
for i in range(8):
   qween.append(line[:])

def print_qween(p):
    str = ""
    for i in range(8):
        for j in range(8):
            if p[i][j] == '2':
                str += '0' + ' '
            else:
                str += p[i][j] + ' '
        str += '\n'
    print str

x = int(rand.uniform(0,8))
y = int(rand.uniform(0,8))

print_qween(qween)

qween[x][y] = '1'


def cancel_nodes(x,y,list):
    x1 = x
    y1 = y
    while True :
        x1 += 1
        y1 += 1
        if x1 == 8 or y1 == 8 :
            break
        else :
            list[x1][y1] = '2'


    x1 = x
    y1 = y

    while True:
        x1 -= 1
        y1 -= 1
        if x1 == -1 or y1 == -1:
            break
        else:
            list[x1][y1] = '2'

    x1 = x
    y1 = y

    while True:
        x1 += 1
        y1 -= 1
        if x1 == 8 or y1 == -1:
            break
        else:
            list[x1][y1] = '2'

    x1 = x
    y1 = y

    while True:
        x1 -= 1
        y1 += 1
        if x1 == -1 or y1 == 8:
            break
        else:
            list[x1][y1] = '2'

    x1 = 0
    y1 = y

    while True:
        if x1 == 8 :
            break
        else:
            if list[x1][y1] != '1' :
                list[x1][y1] = '2'
        x1 += 1

    x1 = x
    y1 = 0

    while True:
        if y1 == 8:
            break
        else:
            if list[x1][y1] != '1':
                list[x1][y1] = '2'
        y1 += 1

cancel_nodes(x,y,qween)
print_qween(qween)

def max_nodes(list):
    max = list[0]
    counter = -1
    max_place =-1;
    for i in list:
        counter += 1
        if i >= max:
            max = i
            max_place = counter
    if max == -1:
        max_place = 100
    return max_place


def calc_nodes(list):
    count = 0
    for i in range(8):
        for j in range(8):
            if list[i][j] == '0':
                count += 1
    return count


def find_1(x,list):
    for i in range(8):
        if list[x][i] == '1':
            return True
    return False

def find_x_y(pos):
    x = pos // 8
    y = pos % 8
    return [x,y]

def find_pos(x,y):
    return (x * 8) + y

def n_qween(list):
    count_1 = 0
    h = []
    for i in range(8):
        if find_1(i,list) == True:
            count_1 += 1
        else:
            break
    if count_1 == 8:
        print_qween(list)
        return
    for i in range(8):
        copy_list = copy.deepcopy(list)
        if list[count_1][i] == '2':
            h.append(-1)
        else:
            copy_list[count_1][i] = '1'
            cancel_nodes(count_1,i,copy_list)
            h.append(calc_nodes(copy_list))
    max_node = max_nodes(h)
    if max_node == 100:
        return
    list[count_1][max_node] = '1'
    cancel_nodes(count_1,max_node,list)
    print_qween(list)
    n_qween(list)

def n_qween2(list):
    count_1 = 0
    h = []
    for i in range(8):
        if find_1(i,list) == True:
            count_1 += 1
    if count_1 == 8:
        return
    for i in range(64):
        h.append(-1)
    for i in range(8):
        for j in range(8):
            copy_list = copy.deepcopy(list)
            if copy_list[i][j] == '0':
                copy_list[i][j] = '1'
                cancel_nodes(i,j,copy_list)
                h[find_pos(i,j)] = calc_nodes(copy_list)

    max_node = max_nodes(h)
    if max_node == 100:
        return
    max_place = find_x_y(max_node)
    list[max_place[0]][max_place[1]] = '1'
    cancel_nodes(max_place[0],max_place[1],list)
    print_qween(list)
    n_qween2(list)

n_qween2(qween)