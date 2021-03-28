import math


class Node:
    def __init__(self, nr, x, y):
        self.visited = False
        self.nr = nr
        self.x = x
        self.y = y
        self.g_value = 0
        self.h_value = 0
        self.parent = None

INTERSECTIONS = dict()

def shortest_path(M, start, goal):
    """ return the shortest path between start and goal nodes in a graph M"""
    print("shortest path called")
    start_node = Node(start, M.intersections[start][0], M.intersections[start][1])
    start_node.visited = True
    open_nodes = [start_node]
    INTERSECTIONS[start] = start_node
    goal_node = Node(goal, M.intersections[goal][0], M.intersections[goal][1])

    # loop until goal has been found or open_nodes is empty
    while open_nodes:
        current_node = next_node(open_nodes)
        if current_node.nr == goal:
            path = construct_final_path(current_node)
            INTERSECTIONS.clear()
            return path
        add_neighbors(current_node, open_nodes, goal_node, M)

    return -1


def add_neighbors(parent_node, open_nodes, goal_node, graph):
    """ loop through neighbors, add new ones to the open_list / update nodes already seen if necessary"""
    for neighbor in graph.roads[parent_node.nr]:
        if neighbor not in INTERSECTIONS:
            # create Node from neighbor and add it to the list of unvisited nodes
            new_node = Node(neighbor, graph.intersections[neighbor][0], graph.intersections[neighbor][1])
            new_node.parent = parent_node
            new_node.g_value = distance(new_node, parent_node) + parent_node.g_value
            new_node.h_value = distance(new_node, goal_node)
            INTERSECTIONS[neighbor] = new_node
            open_nodes.append(new_node)
        else:
            # update neighbor if necessary
            neighbor_node = INTERSECTIONS[neighbor]
            if neighbor_node.visited is False:
                g_value_comparison = parent_node.g_value + distance(parent_node, neighbor_node)
                if neighbor_node.g_value > g_value_comparison:
                    neighbor_node.g_value = g_value_comparison
                    neighbor_node.parent = parent_node


def distance(self, other):
    """ return the distance between two nodes that are directly connected """
    dist = math.sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2)
    return dist


def next_node(open_nodes):
    """ returns the next node (the one with the smallest f value or h value if there is a draw) and sets visited parameter to True """
    open_nodes.sort(key=lambda entry: (entry.h_value + entry.g_value, entry.h_value), reverse=True)
    open_nodes[-1].visited = True
    return open_nodes.pop()


def construct_final_path(node):
    """ returns the path from start to goal node """
    path = []
    while node:
        path.append(node.nr)
        node = node.parent
    return path[::-1]


# class Map:
#     def __init__(self):
#         self.intersections = {0: [0.7798606835438107, 0.6922727646627362],
#                              1: [0.7647837074641568, 0.3252670836724646],
#                              2: [0.7155217893995438, 0.20026498027300055],
#                              3: [0.7076566826610747, 0.3278339270610988],
#                              4: [0.8325506249953353, 0.02310946309985762],
#                              5: [0.49016747075266875, 0.5464878695400415],
#                              6: [0.8820353070895344, 0.6791919587749445],
#                              7: [0.46247219371675075, 0.6258061621642713],
#                              8: [0.11622158839385677, 0.11236327488812581],
#                              9: [0.1285377678230034, 0.3285840695698353]}
#         self.roads = [  [7, 6, 5],
#                         [4, 3, 2],
#                         [4, 3, 1],
#                         [5, 4, 1, 2],
#                         [1, 2, 3],
#                         [7, 0, 3],
#                         [0],
#                         [0, 5],
#                         [9],
#                         [8]
#                     ]

class Map:
    def __init__(self):
        self.intersections = {  0: [0.7801603911549438, 0.49474860768712914],
                                1: [0.5249831588690298, 0.14953665513987202],
                                2: [0.8085335344099086, 0.7696330846542071],
                                3: [0.2599134798656856, 0.14485659826020547],
                                4: [0.7353838928272886, 0.8089961609345658],
                                5: [0.09088671576431506, 0.7222846879290787],
                                6: [0.313999018186756, 0.01876171413125327],
                                7: [0.6824813442515916, 0.8016111783687677],
                                8: [0.20128789391122526, 0.43196344222361227],
                                9: [0.8551947714242674, 0.9011339078096633],
                                10: [0.7581736589784409, 0.24026772497187532],
                                11: [0.25311953895059136, 0.10321622277398101],
                                12: [0.4813859169876731, 0.5006237737207431],
                                13: [0.9112422509614865, 0.1839028760606296],
                                14: [0.04580558670435442, 0.5886703168399895],
                                15: [0.4582523173083307, 0.1735506267461867],
                                16: [0.12939557977525573, 0.690016328140396],
                                17: [0.607698913404794, 0.362322730884702],
                                18: [0.719569201584275, 0.13985272363426526],
                                19: [0.8860336256842246, 0.891868301175821],
                                20: [0.4238357358399233, 0.026771817842421997],
                                21: [0.8252497121120052, 0.9532681441921305],
                                22: [0.47415009287034726, 0.7353428557575755],
                                23: [0.26253385360950576, 0.9768234503830939],
                                24: [0.9363713903322148, 0.13022993020357043],
                                25: [0.6243437191127235, 0.21665962402659544],
                                26: [0.5572917679006295, 0.2083567880838434],
                                27: [0.7482655725962591, 0.12631654071213483],
                                28: [0.6435799740880603, 0.5488515965193208],
                                29: [0.34509802713919313, 0.8800306496459869],
                                30: [0.021423673670808885, 0.4666482714834408],
                                31: [0.640952694324525, 0.3232711412508066],
                                32: [0.17440205342790494, 0.9528527425842739],
                                33: [0.1332965908314021, 0.3996510641743197],
                                34: [0.583993110207876, 0.42704536740474663],
                                35: [0.3073865727705063, 0.09186645974288632],
                                36: [0.740625863119245, 0.68128520136847],
                                37: [0.3345284735051981, 0.6569436279895382],
                                38: [0.17972981733780147, 0.999395685828547],
                                39: [0.6315322816286787, 0.7311657634689946]}
        self.roads = [  [36, 34, 31, 28, 17],
                        [35, 31, 27, 26, 25, 20, 18, 17, 15, 6],
                        [39, 36, 21, 19, 9, 7, 4],
                        [35, 20, 15, 11, 6],
                        [39, 36, 21, 19, 9, 7, 2],
                        [32, 16, 14],
                        [35, 20, 15, 11, 1, 3],
                        [39, 36, 22, 21, 19, 9, 2, 4],
                        [33, 30, 14],
                        [36, 21, 19, 2, 4, 7],
                        [31, 27, 26, 25, 24, 18, 17, 13],
                        [35, 20, 15, 3, 6],
                        [37, 34, 31, 28, 22, 17],
                        [27, 24, 18, 10],
                        [33, 30, 16, 5, 8],
                        [35, 31, 26, 25, 20, 17, 1, 3, 6, 11],
                        [37, 30, 5, 14],
                        [34, 31, 28, 26, 25, 18, 0, 1, 10, 12, 15],
                        [31, 27, 26, 25, 24, 1, 10, 13, 17],
                        [21, 2, 4, 7, 9],
                        [35, 26, 1, 3, 6, 11, 15],
                        [2, 4, 7, 9, 19],
                        [39, 37, 29, 7, 12],
                        [38, 32, 29],
                        [27, 10, 13, 18],
                        [34, 31, 27, 26, 1, 10, 15, 17, 18],
                        [34, 31, 27, 1, 10, 15, 17, 18, 20, 25],
                        [31, 1, 10, 13, 18, 24, 25, 26],
                        [39, 36, 34, 31, 0, 12, 17],
                        [38, 37, 32, 22, 23],
                        [33, 8, 14, 16],
                        [34, 0, 1, 10, 12, 15, 17, 18, 25, 26, 27, 28],
                        [38, 5, 23, 29],
                        [8, 14, 30],
                        [0, 12, 17, 25, 26, 28, 31],
                        [1, 3, 6, 11, 15, 20],
                        [39, 0, 2, 4, 7, 9, 28],
                        [12, 16, 22, 29],
                        [23, 29, 32],
                        [2, 4, 7, 22, 28, 36]]


map = Map()
print(shortest_path(map, 8, 34))
print(shortest_path(map, 5, 5))
print(shortest_path(map, 5, 24))