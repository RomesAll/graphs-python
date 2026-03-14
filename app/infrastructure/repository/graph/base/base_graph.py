from app.core import Matrix, Node, Edge, GraphRepository
from collections import deque

class Graph(GraphRepository):
    """

    """

    def get_all_path(self, start: Node, end: Node):
        pass

    def get_path(self, start: Node, end: Node):
        passed: set = set()
        path: deque = deque([start])
        stack: deque = deque([start])
        while stack:
            current_node = stack[-1]
            passed.add(current_node)
            for edge in current_node.edges:
                if edge.adjacent not in passed:
                    stack.append(edge.adjacent)
                    break
            if current_node != end:
                stack.pop()
                continue
            path = stack.copy()
            stack.clear()
        if path[-1] != end:
            return None
        return path

    def __init__(self, matrix: Matrix):
        self._matrix: Matrix = matrix
        self._graph: dict | None = None
        self.initialization_graph(matrix)

    @property
    def graph(self):
        return self._graph

    @property
    def matrix(self):
        return self._matrix

    @matrix.setter
    def matrix(self, matrix: Matrix):
        self._matrix = matrix
        self.initialization_graph(matrix)

    def initialization_graph(self, matrix: Matrix):
        self._graph: dict = dict()
        for row_ind, row in enumerate(matrix):
            node: Node = self.create_or_get_node(row_ind)
            for col_ind, col in enumerate(row):
                if col == 0:
                    continue
                node_edge: Edge | None = None
                if col == 1 and col_ind != row_ind:
                    node_adjacent: Node = self.create_or_get_node(col_ind)
                    node_adjacent.parents.append(node)
                    node_edge: Edge = Edge(node_adjacent)
                if col == 2 and col_ind == row_ind:
                    node_edge: Edge = Edge(node)
                node.edges.append(node_edge)
            self._graph.update({row_ind: node})

    def create_or_get_node(self, value: int):
        if self._graph.get(value) is None:
            self._graph[value] = Node(value)
        return self._graph[value]

    def dfs(self):
        passed: set = set()
        def dfs_inner(node: Node):
            nonlocal passed
            print(node.value, node)
            passed.add(node.value)
            for edge in node.edges:
                if edge.adjacent.value not in passed:
                    dfs_inner(edge.adjacent)
        for current_node in self._graph.values():
            if current_node.value not in passed:
                dfs_inner(current_node)

    def bfs(self):
        passed: set = set()
        def bfs_inner(node_start: Node):
            nonlocal passed
            current_level = deque([node_start])
            new_level = deque()
            level = 0
            while current_level:
                node = current_level.popleft()
                passed.add(node.value)
                print(level, node.value, node)
                for edge in node.edges:
                    if edge.adjacent.value not in passed:
                        new_level.append(edge.adjacent)
                if not current_level:
                    current_level = new_level.copy()
                    new_level.clear()
                    level += 1
        for current_node in self._graph.values():
            if current_node.value not in passed:
                bfs_inner(current_node)


g = Graph(matrix=[
    [2, 1, 1, 0, 0, 0],
    [1, 0, 0, 1, 1, 0],
    [1, 0, 0, 0, 0, 1],
    [0, 1, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0],
    [0, 0, 1, 0, 0, 0],
])
g.get_path(g.graph.get(0), g.graph.get(5))