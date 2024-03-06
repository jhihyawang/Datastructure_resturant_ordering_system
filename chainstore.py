# Floyd 最短路徑
import sys
SIZE = 7
NUMBER = 6
INF = 99999

Graph_Matrix = [[0]*SIZE for row in range(SIZE)]
distance = [[0]*SIZE for row in range(SIZE)]

def BuildGraph_Matrix(Path_Cost):
    for i in range(1,SIZE):
        for j in range(1,SIZE):
            if i == j:
                Graph_Matrix[i][j] = 0
            else:
                Graph_Matrix[i][j] = INF

    i = 0
    while i < SIZE:
        Start_Point = Path_Cost[i][0]
        End_Point = Path_Cost[i][1]
        Graph_Matrix[Start_Point][End_Point] = Path_Cost[i][2]
        i += 1

# 單點對全部頂點最短時間
def shortestPath(vertex_total):
    for i in range(1, vertex_total+1):
        for j in range(i, vertex_total+1):
            distance[i][j] = Graph_Matrix[i][j]
            distance[j][i] = Graph_Matrix[i][j]

    for k in range(1, vertex_total+1):
        for i in range(1, vertex_total+1):
            for j in range(1, vertex_total+1):
                if distance[i][k] + distance[k][j] < distance[i][j]:
                    distance[i][j] = distance[i][k] + distance[k][j]

Path_Cost = [[1, 2, 20], [2, 3, 30], [2, 4, 35], [3, 5, 28], [3, 6, 87], [4, 5, 42], [4, 6, 55], [5, 6, 67]]
BuildGraph_Matrix(Path_Cost)
 


# def main():
#     BuildGraph_Matrix()
#     shortestPath()

def main():
    print('-----------------------------------------')
    print('<< Chain Store Shortest Distance >>')
    print('-----------------------------------------')
    shortestPath(NUMBER)   # 找最短時間

    print('Store1 Store2 Store3 Store4 Store5 Store6')
    print('-----------------------------------------')
    for i in range(1, NUMBER+1):
        print('Store%d' %i, end='')
        for j in range(1, NUMBER+1):
            print('%5d ' %distance[i][j], end ='')
        print()
    print('-----------------------------------------')
    print()


if __name__ == '__main__':
    main()


