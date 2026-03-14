from ..domain_services import IGraph

class GraphService:
    def __init__(self, graph_repository: IGraph):
        self.graph_repository = graph_repository