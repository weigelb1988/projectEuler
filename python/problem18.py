from pprint import pprint
from _collections import defaultdict
class Graph:
    def __init__(self):
        self.nodes = set()
        self.edges = defaultdict(list)
        self.distances = {}
    def add_node(self, value):
        self.nodes.add(value)
    
    def add_edge(self, from_node, to_node, distance):
        self.edges[from_node].append(to_node)
#         self.edges[to_node].append(from_node)
        self.distances[(from_node, to_node)] = distance

def max_dijsktra(graph, initial):
    visited  = {initial:75}
    
    path = {}
    nodes = set(graph.nodes)
    while nodes:
        min_node = None
        for node in nodes:
            
            if node in visited:
                
                if min_node is None:
                    min_node = node
                
                if visited[node] > visited[min_node]:
                    min_node=node
        if min_node is None:
            break
        nodes.remove(min_node)
        current_weight = visited[min_node]
        
        for edge in graph.edges[min_node]:
            weight = current_weight + graph.distances[(min_node, edge)]
            if edge not in visited or weight > visited[edge]:
                visited[edge] = weight
                path[edge] = min_node
    return visited, path

#read in from file problem18.txt and parse out nodes
node_counter = 0
node_graph = Graph()
node_list = []
new_highs = [] 
with open('problem67.txt') as f:
    lines = f.readlines()
    for x in range(len(lines)-1, -1 ,-1): # reverse up the lines
        if not new_highs:
            new_highs = lines[x].rstrip("\n").split(" ") # split out the numbers
        prev_line = lines[x-1].rstrip("\n").split(" ")
        row = ""
        this_row = []
        for y in range(0,len(prev_line)): # for each number add it to the connecting line above save higher
            prev_line = lines[x-1].split(" ")
            left  = int(new_highs[y]) + int(prev_line[y])
            right = int(new_highs[y+1]) + int(prev_line[y])
            if(left > right):
                this_row.append(left)
            else:
                this_row.append(right)
        print(this_row)
        new_highs=  this_row
#         print(new_highs)
            
            
        
#fill in the edges of the list
# print("\n")
# print(node_graph.edges['0.0'])
# print(node_graph.distances[('0.0','1.1')])
# 
# print(node_graph.edges['1.1'])
# print(node_graph.distances[('1.0','2.1')])
# print(max_dijsktra(node_graph, '0.0'))

