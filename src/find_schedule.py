import dijkstra

def find_schedule(graph, a, b, c, d, r):
    # find the shortest path from a,b to other vertices
    dist_a = dijkstra(graph, a)
    dist_b = dijkstra(graph, b)
 
    # find the shortest path from c,d to other vertices
    dist_c = dijkstra(graph, c)
    dist_d = dijkstra(graph, d)
 
    # find schedule and distance
    schedule = []
    distance = []
    for u in range(len(graph)):
        # check distance of 2 robots at u
        if dist_a[u] + dist_d[u] > dist_c[d] + r or dist_b[u] + dist_c[u] > dist_c[d] + r:
            return
 
        # if distance of 2 robots at u is <= r, they move the shortest path to u
        if dist_a[u] + dist_b[u] <= r:
            schedule.append((a, u))
            schedule.append((b, u))
            distance.append(dist_a[u] + dist_b[u])
            distance.append(dist_a[u] + dist_b[u])
 
        # if distance of 2 robots at u is > r, robot_1 move the shortest path to u, robot 2 move to the shortest path of adjacent of u and <=r
        else:
            for v,w in graph[u]:
                if (dist_a[v] + dist_b[v] + w <= dist_a[u] + dist_b[u] + r) and (dist_c[v] + dist_d[v] + w <= dist_c[u]+dist_d[u]):
                    schedule.append((a,v))
                    schedule.append((b,v))
                    distance.append(dist_a[v] + dist_b[v] + w)
                    distance.append(dist_a[v] + dist_b[v] + w)

    return schedule, distance