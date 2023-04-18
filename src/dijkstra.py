from queue import PriorityQueue

def dijkstra(graph, u):
    n = len(graph)
    dist = [float('inf')] * n
    dist[u] = 0
    q = PriorityQueue()
    
    q.put((0, u))
    while not q.empty():
        du, u = q.get()
        if du != dist[u]:
            continue
        for v, w in graph[u]:
            if du + w < dist[v]:
                dist[v] = du + w
                q.put((dist[v], v))
    return dist