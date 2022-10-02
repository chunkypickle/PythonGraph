# There are no restrictions on how you must store
# class or instance variables for this project.
# Use whatever makes the most sense for your 
# design and implementation.

class node:
    def __init__(self, label):
        self.label = label
        self.degree_in = 0
        self.degree_out = 0

    def in_degree(self, ):
        return self.degree_in

    
    def out_degree(self, ):
        return self.degree_out
    
    def __str__(self, ):
        return self.label

class Graph:
    def __init__(self, directed):
        self.directed = directed
        self.nodes = {}

    def num_vertices(self):
        return len(self.nodes)

    def num_edges(self):
        sum_edges = 0
        for node in self.nodes:
            sum_edges = sum_edges + len(self.nodes[node])
        if self.directed == True:
            return sum_edges
        else:
            return int(sum_edges / 2)
    
    def is_directed(self):
        return self.directed

    def is_weighted(self):
        return False

    def add_node(self, label):
        if str(label) in self.nodes:
            raise DuplicateNode
        else:
            self.nodes.update({str(label) : []})
    
    def remove_node(self, label):
        if str(label) not in self.nodes:
            raise NodeNotFound
        else:
            self.nodes.pop(str(label))

            for node in self.nodes:
                if str(label) in self.nodes[node]:
                    self.nodes[node].remove(str(label))

    
    def add_edge(self, n1, n2, weight = 1):
        if self.directed == True:
            if str(n2) in self.nodes[str(n1)]:
                raise DuplicateEdge
            else:
                self.nodes[str(n1)].append(str(n2))
        else:
            if str(n2) in self.nodes[str(n1)]:
                raise DuplicateEdge
            elif str(n1) in self.nodes[str(n2)]:
                raise DuplicateEdge
            else:
                self.nodes[str(n1)].append(str(n2))
                self.nodes[str(n2)].append(str(n1))

    
    def remove_edge(self, n1, n2, weight = 1):
        if self.directed == True:
            if str(n2) not in self.nodes[str(n1)]:
                raise EdgeNotFound
            else:
                self.nodes[str(n1)].remove(str(n2))
        else:
            if str(n2) not in self.nodes[str(n1)]:
                raise EdgeNotFound
            elif str(n1) not in self.nodes[str(n2)]:
                raise EdgeNotFound
            else:
                self.nodes[str(n1)].remove(str(n2))
                self.nodes[str(n2)].remove(str(n1))
    
    def BFS(self, source):
        root = str(source)

        return_array = []

        visited = set()
        queue = []
        queue.append(root)
        visited.add(root)

        while(len(queue) != 0):
            vertex = queue.pop(0)

            return_array.append(vertex)
            
            for linked_node in self.nodes[vertex]:
                if linked_node not in visited:
                    visited.add(linked_node)
                    queue.append(linked_node)

        return return_array


    
    def DFS(self, source):
        visited = set()

        return_array = []

        def dfs_search(visited, graph, node):
            if node not in visited:
                return_array.append(node)
                visited.add(node)
                for linked_node in graph[node]:
                    dfs_search(visited, graph, linked_node)

        dfs_search(visited, self.nodes, str(source))

        return return_array
    
    def has_edge(self, n1, n2):
        if str(n1) not in self.nodes or str(n2) not in self.nodes:
            raise NodeNotFound
        if self.directed == True:
            if str(n2) in self.nodes[str(n1)]:
                return True
            else:
                return False
        else:
            if str(n2) in self.nodes[str(n1)] and str(n1) in self.nodes[str(n2)]:
                return True
            else:
                return False
            

    def get_path(self, n1, n2):
        if str(n1) not in self.nodes or str(n2) not in self.nodes:
            raise NodeNotFound
        BFS_array = self.BFS(n1)
        path = []
        if str(n2) in BFS_array:
            counter = 0
            current_node = BFS_array[counter]
            while(current_node != str(n2)):
                path.append(current_node)
                counter = counter + 1
                current_node = BFS_array[counter]
            path.append(BFS_array[counter])
        else:
            return("No path exists") 
       
        return path

    
    def get_adjacent_nodes(self, label):
        if str(label) not in self.nodes:
            raise NodeNotFound
        else:
            return self.nodes[str(label)]
    
    def print_graph(self):
        print(self.nodes)


class NodeNotFound(Exception):
    pass

class EdgeNotFound(Exception):
    pass

class DuplicateNode(Exception):
    pass

class DuplicateEdge(Exception):
    pass



# Exceptions
"""
If a label is provided that is supposed to exist in the Graph
and a node with that label does not exist, the method should raise 
a "NodeNotFound" exception.

If the remove_edge method is called for an edge that does not 
exist in the Graph, the method should raise an "EdgeNotFound"
exception.

If a method call would result in a duplicate label or duplicate 
edge being added to the Graph, a "DuplicateNode" or "DuplicateEdge"
exception should be raised.

If you are not familiar with defining custom exceptions in Python3,
it's not too complicated. Check out this source for explanation and
examples:
https://www.askpython.com/python/python-custom-exceptions
"""

print("starting...")
n0 = node("0")
n1 = node("1")
n2 = node("2")
n3 = node("3")
n4 = node("4")
n5 = node("5")
n6 = node("6")
n7 = node("7")
n8 = node("8")

g = Graph(False)
print(g.is_directed())

g.add_node(n0)
g.add_node(n1)
g.add_node(n2)
g.add_node(n3)
g.add_node(n4)
g.add_node(n5)
g.add_node(n6)
g.add_node(n7)


g.add_edge(n0, n1)
g.add_edge(n0, n2)
g.add_edge(n1, n2)
g.add_edge(n2, n3)
g.add_edge(n2, n5)
g.add_edge(n3, n4)
g.add_edge(n3, n6)
g.add_edge(n4, n6)
g.add_edge(n5, n7)

# g.remove_edge(n5, n7)

# g.remove_node(n3)
# g.remove_node(n4)
# g.remove_node(n5)

print(g.has_edge(n1, n5))
print(g.has_edge(n2, n3))

print(g.get_adjacent_nodes(n4))

print("Number of nodes -> " + str(g.num_vertices()))
print("Number of edges -> " + str(g.num_edges()))

g.print_graph()
print(g.DFS(n0))
print(g.BFS(n0))
print(g.get_path(n0, n2))


# 0, 1, 2, 3, 5, 4, 6, 7