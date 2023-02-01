from unittest import TestCase
from graph3 import *

class TestGraph(TestCase):
    def test_djikstra(self):
        g = Graph()
        g.read_from_file("soc-tribes.edges")
        print(g.djikstra(Node(1)))
        return g
