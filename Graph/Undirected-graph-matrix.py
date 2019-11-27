
import queue

class UndirectedGraph:
    """
    Undirected Graph with graph represented as an adjacency matrix
    """

    def __init__(self, vertices):
        self.adjacency_matrix = []
        for i in range(vertices):
            self.adjacency_matrix.append([0] * vertices)

    def add_edge(self, source, destination):
        self.adjacency_matrix[source][destination] = 1
        self.adjacency_matrix[destination][source] = 1


def main():
    print("Test complete")

if __name__ == "__main__":
    main()