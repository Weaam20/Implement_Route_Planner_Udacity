from PriorityQueue import PriorityQueue
import math


def create_dic(Map, start):
    """
    this method will initialize dictionary with infinite values for all nodes in the map.
    """
    score = dict()
    for node in Map.intersections:
        score[node] = math.inf
    score[start] = 0
    return score


def heuristic(a, b):
    """
    this method will calculate the heuristic value.
    """
    return distance(a, b)


def goal_test(node, goal):
    """
    this method will check if node equal to goal.
    """
    return node == goal


def distance(a, b):
    """
    this method will calculate the distance between two node.
    """
    (x1, y1) = a  # point a coordinates.
    (x2, y2) = b  # point b coordinates.

    return math.sqrt(((x1 - x2) ** 2) + ((y1 - y2) ** 2))


def generate_path(come_from, start, goal, path):
    """
    this method will return the shortest path list after we know the shortest path from start to goal.
    """
    # path = []
    # start from the bottom.
    curr = goal
    # add goal to the list.
    path.append(goal)
    while curr != start:
        # insert in the beginning of the list.
        path.insert(0, come_from.get(curr))
        # update current to the next node.
        curr = come_from.get(curr)
    return path


def shortest_path(Map, start, goal):
    """
    this method will returns the shortest path between a start point and a goal pint by using A* algorithm.
   _____________________________________________________________
   :param start:is the number of starting node in the Map.
   :param Map: is a Map.
   :param goal: is the number of target node in the Map.
   _____________________________________________________________
   :return: a list contains the shortest path from start to goal.
   """

    # if something wrong
    if Map is None or start is None or goal is None:
        return []
    # if starting node equal to goal.
    if goal_test(start, goal):
        return [start]

    # Initialize data structures.
    closed_set = set()  # set for store all explore nodes.
    open_queue = PriorityQueue()  # Queue for store nodes according to its priority which is (f(n)= g(n) +h(n)).
    open_dic = dict()  # this dictionary will track the content of the queue ( for fast look up).
    come_from = {start: None}  # this dictionary will store the parent of each node.
    g_score = create_dic(Map, start)  # this dictionary will store the costs of all nodes.
    path = []  # this list will store the shortest path from start to goal.
    Nodes = Map.intersections  # this dictionary contains {key of node : node location(list)}.
    Edges = dict()  # this dictionary contains {key of node : children of that node(list)}.

    for i, value in zip(range(len(Map.roads)), Map.roads):
        Edges[i] = value

    # insert the starting node in the open queue and open_dic
    open_queue.push(start, 0, 0)
    open_dic.update({start: None})

    while open_queue.size() > 0:
        # pop the node that has the smallest f(n) from the queue.
        curr_node = open_queue.pop()

        # if the current node is equal to the goal.
        if goal_test(curr_node[1].key, goal):
            path = generate_path(come_from, start, goal, path)
            break

        # add the current node to the explore set.
        closed_set.add(curr_node[1].key)

        # after we popped node from the queue(open_queue) we have to remove it from the open_dic.
        del open_dic[curr_node[1].key]

        # bring all children of the current node and do all these instructions for each.
        for i in Edges.get(curr_node[1].key):
            # if the child is not in explore set.
            if i not in closed_set:
                # calculate the heuristic value for the child.
                h = heuristic(Nodes[i], Nodes.get(goal))
                # calculate the cost value for the child.
                g = curr_node[1].cost + distance(Nodes.get(curr_node[1].key), Nodes[i])
                # the total cost.
                f = g + h
                """if the child is in open_dic and the total cost is greater than or equal to the previous cost for 
                this child then skipped this child."""
                if i in open_dic and f >= g_score[i]:
                    continue
                # else insert child (i=key of the node,g=the cost of the node,f =total cost) to open_queue and open_dic.
                open_queue.push(i, g, f)
                open_dic.update({i: f})
                # update cost of this child in g_cost.
                g_score.update({i: f})
                # change the parent of this child.
                come_from[i] = curr_node[1].key

    return path


"""

Submission Checklist

Does my code pass all tests?  yes

Does my code implement A* search and not some other search algorithm?  yes

Do I use an admissible heuristic to direct search efforts towards the goal? 
yes, because all values of h(n) are smaller than the actual values g(n) of the path.

Do I use data structures which avoid unnecessarily slow lookups?  yes, I used dictionary and set for fast look up.

"""
