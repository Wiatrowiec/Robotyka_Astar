from math import sqrt
class Node():

    def __init__(self, parent=None, position=None):
        self.parent = parent
        self.position = position
        self.g = self.h = self.f = 0

    def __eq__(self, other):
        return self.position == other.position

def heuro(a, b):
    return sqrt(((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2))

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
    moves = [[-1, 0], [0, -1], [0, 1], [1, 0]]
    success = 1
    while len(open_list) > 0:
        current_node = open_list[0]
        current_index = 0
        for index, item in enumerate(open_list):
            if item.f < current_node.f:
                current_node = item
                current_index = index
        open_list.pop(current_index)
        closed_list.append(current_node)
        if current_node == end_node:
            print ("Udalo sie dotrzec do celu: \n")
            return path(current_node,marx)
        children = []
        for nowa in moves:
            node_poz = (current_node.position[0] + nowa[0], current_node.position[1] + nowa[1])
            if node_poz[0] > (len(marx) - 1) or node_poz[0] < 0 or node_poz[1] > (len(marx[len(marx)-1]) - 1)\
                    or node_poz[1] < 0:
                continue
            if marx[node_poz[0]][node_poz[1]] != 0:
                continue
            new_node = Node(current_node, node_poz)
            children.append(new_node)
        for dziedzic in children:
            for closed_child in closed_list:
                if dziedzic == closed_child:
                    continue
            dziedzic.g = current_node.g + 1
            dziedzic.h = ((dziedzic.position[0] - end_node.position[0]) ** 2) + ((dziedzic.position[1] - end_node.position[1]) ** 2)
            dziedzic.f = dziedzic.g + dziedzic.h
            for open_node in open_list:
                if dziedzic == open_node and dziedzic.g > open_node.g:
                    continue
            open_list.append(dziedzic)
    if (success == 1):
        return 0

def main():

    marx = []

    with open('grid.txt', 'r') as f:
        x = f.read().splitlines()
        for i in x:
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
