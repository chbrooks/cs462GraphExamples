## The previous setups are a little annoying. What if we want to store
## other information in the nodes and edges? We need to know how we built our
## data structure in order to implement Djikstra's, which is annoying.

## So let's instead make a Node class and an Edge class.

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

class Edge:
    def __init__(self, src, dest, val=0):
        self.src = src
        self.dest = dest
        self.val = val
    def __repr__(self):
        return "(%s %s %d)" % (self.src, self.dest, self.val)

class Graph :
    def __init__(self,n_vertices=5):
        self.g = {}

    def add_node(self, n):
        if n not in self.g :
            self.g[n] = []

    def add_edge(self, e):
            src = e.src
            dest = e.dest
            val = e.val
            self.g[src].append(e)

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
                self.add_node(Node(x))
                self.add_node(Node(y))
                self.add_edge(Edge(Node(x), Node(y), val))
                self.add_edge(Edge(Node(y), Node(x), val))

    def djikstra(self, start_vertex):
        dist = {}
        prev = {}

        for n in self.g.keys() :
            dist[n] = 100
            prev[n] = -1

        ## our vertices or nodes are no longer integers
        queue = list(self.g.keys())
        dist[start_vertex] = 0
        while len(queue) > 0:
            ## find the closest vertex
            closest = queue[0]
            d = dist[closest]
            for item in queue :
                if dist[item] < d :
                    temp = item
                    d = dist[item]
            ## remove that item
            for item in queue :
                if item == closest :
                    queue.remove(item)


            ## update its neighbors
            neighbors = self.g[closest]
            for edge in neighbors :
                new_value = dist[edge.src] + edge.val
                if new_value < dist[edge.dest]:
                        dist[edge.dest] = new_value
                        prev[edge.dest] = closest
        return dist, prev



def uTest() :
    g = Graph()
    g.read_from_file("soc-tribes.edges")
    print(g.djikstra(Node(1)))
    return g