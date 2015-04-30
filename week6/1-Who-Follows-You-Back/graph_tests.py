import unittest

from graph import DirectedGraph
from exceptions import NodeNotFound


class TestDirectedGraph(unittest.TestCase):

    def setUp(self):
        self._graph = DirectedGraph()

    def test_add_edge(self):
        self._graph.add_edge(1, 2)

        self.assertIn(1, self._graph._nodes)
        self.assertIn(2, self._graph._nodes)

        self.assertIn(1, self._graph._edges.keys())

    def test_get_neighbours_from(self):
        self._graph.add_edge(1, 2)
        self._graph.add_edge(1, 3)

        self.assertEqual(self._graph.get_neighbours_from(1), [2, 3])

        with self.assertRaises(NodeNotFound):
            self._graph.get_neighbours_from(4)

    def test_path_between(self):
        self._graph.add_edge(1, 2)
        self._graph.add_edge(1, 3)
        self._graph.add_edge(3, 2)
        self._graph.add_edge(2, 4)

        self.assertTrue(self._graph.path_between(1, 2))
        self.assertTrue(self._graph.path_between(1, 4))
        self.assertFalse(self._graph.path_between(4, 2))

        self._graph.add_edge(4, 1)

        self.assertTrue(self._graph.path_between(4, 2))

if __name__ == '__main__':
    unittest.main()
