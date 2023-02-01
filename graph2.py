## Let's implment this again as an adjacency list. Still not OO style.


## create a 'graph' (really an adjacency list) of nVertices
def make_graph(n_vertices) :
    g = {}
    for i in range(n_vertices) :
        g[i] = []
    return g


## add an edge from x to y.
## edges will be represented as tuples of (destination, value)

def add_edge(graph, x,y, edge_value) :
    graph[x].append((y, edge_value))

## get the value stored at (x,y)
def get_edge(graph, x,y) :
    edges = graph[x]
    for edge in edges :
        if edge[0] == y:
            return edge[1]
    return None

def read_from_file(fname):
    with open(fname) as f :
        line1 = f.readline()
        comment, nodes, sources, sinks = f.readline().split(' ')

    with open(fname) as f:
        lines = [line for line in f.readlines() if not line.startswith("%")]
        graph = make_graph(int(sources)+1)
        for line in lines :
            x,y,val = line.split(' ')
            add_edge(graph, int(x),int(y),int(val))
    return graph





def djikstra(graph, startingVertex) :
    dist = [100] * len(graph)
    prev = [-1] * len(graph)

    queue = list(graph.keys())
    dist[startingVertex] = 0
    while len(queue) > 0:
        ## find the min distance.
        min_val = 200
        closest = queue[0]
        for i in queue:
            if dist[i] <= min_val:
                min_val = dist[i]
                closest = i
        ## remove closest.
        next = queue.remove(closest)

        ## update its neighbors
        for i in range(len(graph)):
            edge = get_edge(graph, closest, i)
            if edge is not None:
                new_value = dist[closest] + edge
                if new_value < dist[i]:
                    dist[i] = new_value
                    prev[i] = closest
    return dist, prev


