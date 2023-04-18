'''
10 12 
0 4 10
0 9 11
1 4 9
2 6 5
2 8 1
3 4 11
3 6 5
4 5 2
5 7 9
7 8 3
7 9 10
8 9 4
1 3 
3 4 
7
'''
import os

class Graph:
    def __init__(self, filename) -> None:
        self.filepath = os.path.join(os.path.dirname(__file__),'..','data',filename)
            
        
        # open data
        with open(self.filepath,'r') as f:
            # n_vertices, m_edges        
            [n,m] = [int(x) for x in f.readline().split()]
            
            self.edge = [[] for _ in range(n)]

            for _ in range(m):
                [u,v,w] = [int(x) for x in f.readline().split()]
                self.edge[u].append((v,w))
                self.edge[v].append((u,w))
            
            
            [self.a,self.b] = [int(x) for x in f.readline().split()]
            [self.c,self.d] = [int(x) for x in f.readline().split()]
            self.r = int(f.readline())

# if __name__ == '__main__':
#     filename = 'data_1.txt'

#     G = Graph(filename)
#     print(G.edge)
#     print(G.a,G.b,G.c,G.d,G.r)