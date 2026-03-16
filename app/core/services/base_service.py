from app.core import Node
from app.core.domain_services import IGraph, IConverterInputData

class GraphServiceFile:
    def __init__(self, graph_repository: IGraph, converter: IConverterInputData, path: str):
        self.converter = converter(path)
        graph_data = self.converter.load()
        self.graph_repository = graph_repository(graph_data)

    def get_graph(self) -> dict[int, Node]:
        return self.graph_repository.graph

    def round_graph_depth(self):
        self.graph_repository.dfs()

    def round_graph_width(self):
        self.graph_repository.bfs()

    def get_path(self, start: str|int, end: str|int):
        graph = self.graph_repository.get_graph()
        node_start = graph.get(start)
        node_end = graph.get(end)
        if node_start is None or node_end is None:
            return None
        path = self.graph_repository.get_path(node_start, node_end)
        return path

    def get_graph_info(self):
        count_nodes = self.graph_repository.get_count_node()
        count_edges = self.graph_repository.get_count_edge()
        isolated_nodes = [node.value for node in self.graph_repository.searching_isolated_node() if node]
        loop_nodes = [node.value for node in self.graph_repository.searching_loop_node() if node]
        sorted_degree_nodes = self.graph_repository.get_sorted_degree_nodes()
        matrix_adjacent = self.converter.get_matrix_adjacent()
        info = {
            'graph_info': {
                'count_nodes': count_nodes,
                'count_edges': count_edges,
                'isolated_nodes': isolated_nodes if len(isolated_nodes) != 0 else None,
                'loop_nodes': loop_nodes if len(loop_nodes) != 0 else None,
                'sorted_degree_nodes': sorted_degree_nodes,
                'matrix_adjacent': matrix_adjacent,
            }
        }
        return info

    def save_matrix(self) -> bool:
        matrix = self.converter.get_matrix_adjacent()
        return self.converter.save(matrix)
