from typing import Set, Tuple, List

class Graph:
    def __init__(self):
        self.edges: Set[Tuple[str]] = set()
        self.nodes: Set[str] = set()

    def add_node(self, new_node: str) -> None:
        self.nodes.add(new_node)

    def add_edge(self, new_edge: Tuple[str, str]) -> None:
        self.edges.add(new_edge)

    def get_neighbours(self, node: str) -> Set[str]:
        neighbours = set()
        for edge in self.edges:
            if edge[0] == node:
                neighbours.add(edge[1])
            if edge[1] == node:
                neighbours.add(edge[0])
        return neighbours

    def breadth_first_walk(self, start_node: str) -> Set[str]:
        visited = set()
        queue_to_visit = set(start_node)

        while queue_to_visit:
            visiting = queue_to_visit.pop()
            neighbours = self.get_neighbours(visiting)
            visited.add(visiting)
            for node in neighbours:
                if node in visited:
                    queue_to_visit.add(node)
        return visited

    # недоделанная функция поска кратчайшего пути от start до end и вывод пути
    def start_end_walk(self, start_node: str, end_node: str, visited: Set[str]) -> Set[str]:
        queue_to_visit = set(start_node)

        while queue_to_visit:
            visiting = queue_to_visit.pop()
            neighbours = self.get_neighbours(visiting)
            visited.add(visiting)
            for node in neighbours:
                if node in visited:
                    queue_to_visit.add(node)
        return visited

    def depth_first_walk(self, start_node: str, visited = list()) -> List[str]:
        visited.append(start_node)
        neighbors = self.get_neighbours(start_node)
        for node in neighbors:
            if node not in visited:
                self.depth_first_walk(node, visited)
        return visited



graph = Graph()
graph.add_node("A")
graph.add_node("B")
graph.add_node("C")
graph.add_node("D")
graph.add_edge(("A", "B"))
graph.add_edge(("B", "C"))
graph.add_edge(("D", "C"))
graph.add_edge(("B", "D"))

print("nodes ", graph.nodes)
print("edges: ", graph.edges)
print("breadth first: ", graph.breadth_first_walk("A"))
print("deep: ", graph.depth_first_walk("A"))