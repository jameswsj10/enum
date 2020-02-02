# from "../runner.py" import mapper 
from webscrape import webscrape

global txtfile, headers = webscrape("http://www.eecs70.org/")

class Node():
    def __init__(self, topic, dist, children):
        self.topic = topic
        self.dist = dist
        self.children = children



def BFS(Node n):
    """ Traverse n by 2 levels and add every node's topic traversed to a set
    1. access new subnodes through Wikimap
    2. traverse every node in the first level and add to set
    3. recurse on each node in the first level. Stop after.

    Input -> Node
    Output -> Set of subnodes connected to Node w/in 2 lvls
    """
    set = set([])



def populate_map():
    """ creates hashmap between each topic node and the set of subnodes it is connected to within 2 levels
    key -> topic node
    value -> set of subnodes

    Input -> none  (global var headers)
    Output -> set of nodes and its corresponding subnodes
    """
    map = {}
    for header in headers:
        header_node = Node(header, 0, None)
        subnodes_set = BFS(header_node)
        map.add(header_node, subnodes_set)


def calc_relations(map):
    """ Given the hashmap, we look for duplicates in the values of every 2-combination of topics
    and create a mapping from every 2 combinations to a true or false, indicating whether there is
    a relation between the 2 topics or not.
    """
