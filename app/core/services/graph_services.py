from app.core import GraphRepository

class GraphService:
    def __init__(self, graph_repository: GraphRepository):
        self.graph_repository = graph_repository