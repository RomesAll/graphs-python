from app.core import Node
from app.core.domain_services import IGraph, IConverterInputData

class GraphServiceFile:
    def __init__(self, graph_repository: IGraph, converter: IConverterInputData):
        self.graph_repository = graph_repository
        self.converter = converter
        self.__build_graph()

    def __build_graph(self):
        converted_data = self.converter.load()
        self.graph_repository = self.graph_repository(converted_data)

    def get_graph(self) -> dict[int, Node]:
        return self.graph_repository.get_graph()

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

    def graph_info(self, save: bool=False):
        info = {
            'output_info': {
                'count_nodes': self.graph_repository.get_count_node(),
                'count_edges': self.graph_repository.get_count_edge(),
                'isolated_nodes': [node.value for node in self.graph_repository.searching_isolated_node() if node],
                'loop_nodes': [node.value for node in self.graph_repository.searching_loop_node() if node],
                'sorted_degree_nodes': self.graph_repository.get_sorted_degree_nodes(),
            }
        }
        if save:
            self.converter.save(info)
        return info
