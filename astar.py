from math import sqrt
class Node():

    def __init__(self, parent=None, position=None):
        self.parent = parent
        self.position = position
        self.g = self.h = self.f = 0

    def __eq__(self, other):
        return self.position == other.position

def path(current_node,marx):


    pathx=[]
    current = current_node
    while current is not None:
        pathx.append(current.position)
        current = current.parent
    pathx.reverse()
    for xd in range(len(pathx)):
        marx[pathx[xd][0]][pathx[xd][1]] = 3
    return marx


def astar(marx, start, end):
    start_node = Node(None, start)
    start_node.g = start_node.h = start_node.f = 0
    end_node = Node(None, end)
    end_node.g = end_node.h = end_node.f = 0
    open_list = [start_node]
    closed_list = []
    moves = [[-1, 0], [0, 1], [1, 0], [0, -1]] #gora,prawo,dol,lewo
    cost_move = 1
    kontrola = 1
    while len(open_list) > 0:
        if (kontrola > 1000):
            return 0
        else:
            kontrola=kontrola+1
        current_node = open_list[0]
        current_index = 0
        for idx, obiekt in enumerate(open_list):
            if obiekt.f < current_node.f:
                current_node = obiekt
                current_index = idx
        open_list.pop(current_index)
        closed_list.append(current_node)
        if current_node == end_node:
            print ("Udalo sie dotrzec do celu: \n")
            return path(current_node,marx)
        dziedzice = []
        for nowa in moves:
            node_poz = (current_node.position[0] + nowa[0], current_node.position[1] + nowa[1])
            if node_poz[0] > (len(marx) - 1) or node_poz[0] < 0 or node_poz[1] > (len(marx[len(marx)-1]) - 1) or node_poz[1] < 0:
                continue
            if marx[node_poz[0]][node_poz[1]] != 0:
                continue
            nowy_obiekt = Node(current_node, node_poz)
            dziedzice.append(nowy_obiekt)
        for dziedzic in dziedzice:
            for closed_child in closed_list:
                if dziedzic == closed_child:
                    continue
            dziedzic.g = current_node.g + cost_move
            dziedzic.h = ((dziedzic.position[0] - end_node.position[0]) ** 2) + ((dziedzic.position[1] - end_node.position[1]) ** 2)
            dziedzic.f = dziedzic.g + dziedzic.h
            for otwarty in open_list:
                if dziedzic == otwarty and dziedzic.g > otwarty.g:
                    continue
            open_list.append(dziedzic)


def main():

    marx = []

    with open('grid.txt', 'r') as g:
        y = g.read().splitlines()
        for i in y:
            marx.append(i.split(" "))
    marx_com = [[int(c) for c in line] for line in marx]
    print(" ")
    print("marx wejściowa", "\n")
    for i in marx_com:
        print(i)
    print(" ")
    start_maze = (0, 19)
    end_maze = (19, 0)
    map_complete = astar(marx_com, start_maze, end_maze)

    if map_complete == 0:
        print("Nie udalo sie dostac do celu")
    else:
        print("Trasa")
        for j in map_complete:
            print (j)



if __name__ == '__main__':
    main()
