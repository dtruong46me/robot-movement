from find_schedule import find_schedule
from read_graph import Graph

def main():
    filename = 'data_1.txt'
    G = Graph(filename)

    schedule, distance = find_schedule(G.edge, G.a, G.b, G.c, G.d, G.r)
    print(schedule)
    print(distance)

if __name__ == '__main__':
    main()
