import networkx as nx
import matplotlib.pyplot as plt

g = nx.Graph()
g.add_node("A")
g.add_node("B", text={"Node B"})
g.add_node("C", data={"Node C"})
g.add_node("D", data={"Node D"})

g.add_node("E")
g.add_node("F")
g.add_node("G")
g.add_edge("A","B")
g.add_edge("B","C")
g.add_edge("B","D")
g.add_edge("D","C")
g.add_edge("B","E")
g.add_edge("B","F")
g.add_edge("A","E")
g.add_edge("F","G")
g.add_edge("B","G")
g.add_edge("A","D")
g.add_edge("C","G")
g.add_edge("F","E")

print(g.edges["B","A"])

print(nx.degree(g, "B"))
nx.draw_networkx(g)
plt.show()

