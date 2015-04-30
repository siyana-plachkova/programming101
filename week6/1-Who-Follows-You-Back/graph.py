from exceptions import NodeNotFound


class DirectedGraph:

    def __init__(self):
        self._nodes = []
        self._edges = {}

    def add_edge(self, node_a, node_b):
        if node_a not in self._nodes:
            self._nodes.append(node_a)

        if node_b not in self._nodes:
            self._nodes.append(node_b)

        if node_a not in self._edges.keys():
            self._edges[node_a] = []

        self._edges[node_a].append(node_b)

    def get_neighbours_from(self, node):
        if node not in self._nodes:
            raise NodeNotFound("There is no such node in the graph")

        if node not in self._edges.keys():
            return []

        return self._edges[node]

    def path_between(self, node_a, node_b):
        if node_b in self.get_neighbours_from(node_a):
            return True

        visited = []
        visited.append(node_a)
        queue = []
        queue.append(node_a)

        while len(queue) != 0:
            current_node = queue.pop()
            neighbours = self.get_neighbours_from(current_node)

            if node_b in neighbours:
                return True

            for neighbour in neighbours:
                if neighbour not in visited:
                    queue.append(neighbour)
                    visited.append(neighbour)

        return False

    def get_starting_nodes(self, node):
        return list(filter(lambda x: node in self.get_neighbours_from(x), self._nodes))
