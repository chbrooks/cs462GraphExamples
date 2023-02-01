## Let's implement a graph as an adjacency matrix, in a non-OO fashion.
import readline


## create a 'graph' (really an adjacency matrix) on nVertices x nVertices
def make_graph(n_vertices) :
    return [[0] * n_vertices] * n_vertices

## add an edge from x to y.
def add_edge(graph, x,y, edge_value) :
    graph[x][y] = edge_value

## get the value stored at (x,y)
def get_edge(graph, x,y) :
    return graph[x][y]


def read_from_file(fname):
    with open(fname) as f :
        line1 = f.readline()
        comment, nodes, sources, sinks = f.readline().split(' ')
        print(sources)

    with open(fname) as f:
        lines = [line for line in f.readlines() if not line.startswith("%")]
        graph = make_graph(int(sources)+1)
        for line in lines :
            x,y,val = line.split(' ')
            add_edge(graph, int(x),int(y),int(val))
    return graph


## given an instantiated graph, run Djikstra's algorithm on it.


def djikstra(graph, startingVertex) :
    dist = [100] * len(graph)
    prev = [-1] * len(graph)

    queue = list(range(len(graph)))

    dist[startingVertex] = 0
    while len(queue) > 0 :
        ## find the min distance.
        min_val = 200
        closest = queue[0]
        for i in queue :
            if dist[i] <= min_val :
                min_val = dist[i]
                closest = i
        ## remove closest.
        next = queue.remove(closest)

        ## update its neighbors
        for i in range(len(graph)):
            edge = get_edge(graph, closest, i)
            if edge != 0 :
                new_value = dist[closest] + edge
                if new_value < dist[i] :
                    dist[i] = new_value
                    prev[i] = closest
    return dist, prev

