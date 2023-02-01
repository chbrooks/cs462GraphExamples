## The OO approach is cool, but keeping the Nodes inside the Edges
## might get messy if we start to store more complex data. We'll need
## to be careful about objects vs references.
## Instead, let's keep a separate structure that has an index (an int)
## mapping to each Node, and use that as our key.

class Node :
    ### here's how we do constructors.
    def __init__(self, val=0):
        self.value = val
    def __hash__(self):
        return hash(self.value)
    def __repr__(self):
        return str(self.value)
    def __eq__(self, other):
        return self.value == other.value

## now src and dest are going to be integers.
class Edge:
    def __init__(self, src, dest, val=0):
        self.src = src
        self.dest = dest
        self.val = val
    def __repr__(self):
        return "(%d %d %d)" % (self.src, self.dest, self.val)

class Graph :
    def __init__(self,n_vertices=5):
        ## our adjacency list
        self.g = {}
        ## a dict that maps ints onto Nodes
        self.nodeDictionary = {}

    def add_node(self, index, data=0):
        if index not in self.nodeDictionary :
            self.nodeDictionary[index] = Node(data)
            self.g[index] = []

    def get_data(self, index):
        return self.nodeDictionary[index].data

    def add_edge(self, e):
        self.g[e.src].append(e)

    def get_edge(self, src, dest):
        if src in self.g :
            edges = self.g[src]
            for e in edges :
                if e.dest == dest :
                    return e

    def read_from_file(self, fname):
        with open(fname) as f:
            line1 = f.readline()
            comment, nodes, sources, sinks = f.readline().split(' ')

        with open(fname) as f:
            lines = [line for line in f.readlines() if not line.startswith("%")]
            for line in lines:
                x, y, val = [int(z) for z in line.split(' ')]
                self.add_node(x)
                self.add_node(y)
                self.add_edge(Edge(x, y, val))
                self.add_edge(Edge(y, x, val))

    def djikstra(self, start_vertex):
        dist = {}
        prev = {}

        for n in self.g.keys() :
            dist[n] = 100
            prev[n] = -1

        queue = list(self.g.keys())
        dist[start_vertex] = 0
        while len(queue) > 0:
            ## find the closest vertex
            closest = queue[0]
            d = dist[closest]
            for item in queue :
                if dist[item] < d :
                    closest = item
                    d = dist[item]
            ## remove that item
            queue.remove(closest)
            ## we will change this to a priority queue later.

            ## update its neighbors
            neighbors = self.g[closest]
            for edge in neighbors :
                new_value = dist[closest] + edge.val
                if new_value < dist[edge.dest]:
                        dist[edge.dest] = new_value
                        prev[edge.dest] = closest
        return dist, prev



if __name__ == "__main__" :
    g = Graph()
    g.read_from_file("example1")
    print(g.djikstra(1))
