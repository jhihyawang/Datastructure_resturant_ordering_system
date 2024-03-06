# 員工送餐最短路徑
import sys
MAX_V = 100
VISITED = 1
NOTVISITED = 0
Inf = 99999

A = [[0] * (MAX_V + 1) for row in range(MAX_V+1)]
D = [0] * (MAX_V+1)
S = [0] * (MAX_V+1)
P = [0] * (MAX_V+1)

source = 0
sink = 0
N = 0
step = 1
top = -1

Stack = [0] * (MAX_V+1)

def init():
    global A
    global S
    global D
    global P
    global Inf
    global N
    global NOTVISITED
    global VISITED
    global source
    global sink

    weight = 0
    done = False

    try:
        inputStream = open('deliverytime.dat', 'r')
    except FileNotFoundError:
        print('File deliverytime.dat not found !!')
        sys.exit(1)

    try:
        N = eval(inputStream.readline().strip('\n'))
    except Exception:
        pass

    for i in range(1, N+1):
        for j in range(1, N+1):
            A[i][j] = Inf

    while done == False:
        try:
            
            temp = inputStream.readline().strip('\n').split(' ')
            i = eval(temp[0])
            j = eval(temp[1])
            weight = eval(temp[2])
            
        except Exception:
            done = True
        A[i][j] = weight
    
    inputStream.close()

    print('<< Staff Shortest Delivery Path >>')
    source = eval(input('Enter start table: '))
    sink = eval(input('Enter final table: '))

    for i in range(1, N+1):
        S[i] = NOTVISITED
        D[i] = A[source][i]
        P[i] = source

    S[source] = VISITED
    D[source] = 0

def access():
    global step
    global A
    global D
    global S
    global P
    global NOTVISITED
    global VISITED
    global N

    for step in range(2, N+1):
        t = minD()
        S[t] = VISITED

        for I in range(1, N+1):
            if S[I] == NOTVISITED and D[t] + A[t][I] <= D[I]:
                D[I] = D[t] + A[t][I]
                P[I] = t

#        output_step()

def minD():
    global Inf
    global S
    global NOTVISITED
    global N

    t = 0
    minimum = Inf
    for i in range(1, N+1):
        if S[i] == NOTVISITED and D[i] < minimum:
            minimum = D[i]
            t = i 
    return t

# def output_step():
#     global Inf
#     global N
#     global D
#     global P

#     print('\n\n Step #%d' % step, end = '')
#     print('\n======================================')
#     for i in range(1, N+1):
#         print(' D[%d] ' % i, end = '')
#     print()

#     for i in range(1, N+1):
#         if D[i] == Inf:
#             print(' ---- ', end = '')
#         else:
#             print(' %4d ' % D[i], end ='')
    
#     print('\n======================================')
#     for i in range(1, N+1):
#         print(' P[%d] ' % i, end = '')
#     print()
    
#     for i in range(1, N+1):
#         print(' %4d ' % P[i], end = '')


def output_path():
    global Inf
    global A
    global D
    global P
    global source
    global sink

    node = sink

    if sink == source or D[sink] == Inf:
        print('Table%d has no Path to Table%d' % (source, sink), end = '')
        return

    print('The shortest Path from Table%d to Table%d: ' % (source, sink), end = '')
    print('\n-------------------------------------------------')

    print('Table%d' % source, end = '')
    while node != source:
        Push(node)
        node = P[node]
    while node != sink:
        node = Pop()
        print('-- %dsteps -->' % A[P[node]][node], end = '')
        print('Table%d' % node, end = '')

    print('\n-------------------------------------------------')
    print('Total Steps: %d' % D[sink])

def Push(value):
    global MAX_V
    global top
    global Stack        

    if top > MAX_V:        
        print('  Error!!')  # Stack overflow
        sys.exit(1)

    else:
        top += 1
        Stack[top] = value        

def Pop():
    global top
    global Stack

    if top < 0:
        print('  Error!!')  # Stack empty

    temp = Stack[top]
    top -= 1
    return temp

def main():
    init()
#    output_step()
    access()
    output_path()



if __name__ == '__main__':
    main()



