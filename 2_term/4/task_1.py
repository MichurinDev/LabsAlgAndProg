import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
from graphviz import Digraph

import os


def change_directory(directory: str):
    os.chdir(directory)


def create_graphs():
    G1 = nx.DiGraph()
    G1.add_nodes_from([1, 2, 3, 4])
    G1.add_edges_from([(1, 2), (2, 3), (3, 4), (4, 1), (1, 1), (2, 2)])

    G2 = nx.DiGraph()
    G2.add_nodes_from([1, 2, 3])
    G2.add_edges_from([(1, 2), (1, 1)])
    
    return G1, G2


def draw_graph(G: nx.DiGraph, title: str):
    plt.figure(figsize=(6, 4))
    pos = nx.spring_layout(G, seed=42)
    nx.draw(G, pos, with_labels=True, node_color='lightblue', 
            node_size=500, arrowsize=15, connectionstyle='arc3,rad=0.1')

    for u, v in G.edges():
        if u == v:
            nx.draw_networkx_edges(G, pos, edgelist=[(u, v)], 
                                  connectionstyle='arc3,rad=0.3', 
                                  arrowsize=15)
    
    plt.title(title)
    plt.axis('off')
    return plt


def graph_union(G1: nx.DiGraph, G2: nx.DiGraph):
    union = nx.DiGraph()

    union.add_nodes_from(set(G1.nodes()).union(set(G2.nodes())))

    union.add_edges_from(G1.edges())
    union.add_edges_from(G2.edges())
    
    return union


def graph_intersection(G1: nx.DiGraph, G2: nx.DiGraph):
    intersection = nx.DiGraph()

    common_nodes = set(G1.nodes()).intersection(set(G2.nodes()))
    intersection.add_nodes_from(common_nodes)

    for u, v in G1.edges():
        if u in common_nodes and v in common_nodes and G2.has_edge(u, v):
            intersection.add_edge(u, v)
    
    return intersection


def graph_composition(G1: nx.DiGraph, G2: nx.DiGraph):
    composition = nx.DiGraph()

    for u in G1.nodes():
        for v in G2.nodes():
            composition.add_node((u, v))

    for u in G1.nodes():
        for v, w in G2.edges():
            composition.add_edge((u, v), (u, w))

    for u, v in G1.edges():
        for w in G2.nodes():
            for x in G2.nodes():
                composition.add_edge((u, w), (v, x))
    
    return composition


def get_adjacency_matrix(G: nx.DiGraph):
    return nx.to_numpy_array(G, nodelist=sorted(G.nodes()))


def get_incidence_matrix(G):
    nodes = sorted(G.nodes())
    edges = list(G.edges())

    incidence = np.zeros((len(nodes), len(edges)))

    for i, (u, v) in enumerate(edges):
        if u != v:
            incidence[nodes.index(u), i] = -1
            incidence[nodes.index(v), i] = 1
        else:
            incidence[nodes.index(u), i] = 2
    
    return incidence, edges


def get_strong_components(G: nx.DiGraph):
    return list(nx.strongly_connected_components(G))


def display_matrix(matrix, row_labels, col_labels, title):
    fig, ax = plt.subplots(figsize=(8, 6))
    ax.grid(False)
    
    table = ax.table(
        cellText=matrix.astype(int),
        rowLabels=row_labels,
        colLabels=col_labels,
        cellLoc='center',
        loc='center'
    )
    
    table.auto_set_font_size(False)
    table.set_fontsize(10)
    table.scale(1.2, 1.2)
    
    ax.axis('off')
    plt.title(title)
    return plt

def visualize_composition(composition: nx.DiGraph, title):
    dot = Digraph(comment=title, format='png')
    dot.attr(rankdir='LR')
    
    for node in composition.nodes():
        label = f"({node[0]},{node[1]})"
        dot.node(str(node), label=label)
    
    for u, v in composition.edges():
        dot.edge(str(u), str(v))

    filename = title.replace(' ', '_').replace('(', '').replace(')', '')
    dot.render(filename)
    return filename


def main():
    change_directory("D:/Projects/LabsAlgAndProg/2_term/4/components/result_1")

    G1, G2 = create_graphs()

    draw_graph(G1, "Граф G1").savefig("G1.png")
    draw_graph(G2, "Граф G2").savefig("G2.png")

    union = graph_union(G1, G2)
    draw_graph(union, "G1 ∪ G2 (Объединение)").savefig("union.png")

    intersection = graph_intersection(G1, G2)
    draw_graph(intersection, "G1 ∩ G2 (Пересечение)").savefig("intersection.png")

    comp_G1_G2 = graph_composition(G1, G2)
    visualize_composition(comp_G1_G2, "G1(G2)")

    comp_G2_G1 = graph_composition(G2, G1)
    visualize_composition(comp_G2_G1, "G2(G1)")

    adj_matrix = get_adjacency_matrix(union)
    nodes = sorted(union.nodes())
    display_matrix(adj_matrix, nodes, nodes, "Матрица смежности для G1 ∪ G2").savefig("adjacency_matrix.png")

    inc_matrix, edges = get_incidence_matrix(union)
    edge_labels = [f"{u}->{v}" for u, v in edges]
    display_matrix(inc_matrix, nodes, edge_labels, "Матрица инцидентности для G1 ∪ G2").savefig("incidence_matrix.png")

    components = get_strong_components(union)

    plt.figure(figsize=(8, 6))
    pos = nx.spring_layout(union, seed=42)
    
    colors = plt.cm.rainbow(np.linspace(0, 1, len(components)))
    
    for i, component in enumerate(components):
        nx.draw_networkx_nodes(union, pos, nodelist=component, 
                               node_color=[colors[i]], node_size=500)
    
    nx.draw_networkx_edges(union, pos, connectionstyle='arc3,rad=0.1', arrowsize=15)
    nx.draw_networkx_labels(union, pos)
    
    plt.title("Сильно связные компоненты в G1 ∪ G2")
    plt.axis('off')
    plt.savefig("strong_components.png")

    print("\nРезультаты:")
    print("================")
    print("Объединение G1 U G2:")
    print(f"Вершины: {sorted(union.nodes())}")
    print(f"Ребра: {sorted(union.edges())}")
    
    print("\nПересечение G1 и G2:")
    print(f"Вершины: {sorted(intersection.nodes())}")
    print(f"Ребра: {sorted(intersection.edges())}")
    
    print("\nКомпозиция G1(G2):")
    print(f"Количество вершин: {len(comp_G1_G2.nodes())}")
    print(f"Количество ребер: {len(comp_G1_G2.edges())}")
    
    print("\nКомпозиция G2(G1):")
    print(f"Количество вершин: {len(comp_G2_G1.nodes())}")
    print(f"Количество ребер: {len(comp_G2_G1.edges())}")
    
    print("\nСильно связные компоненты в G1 U G2:")
    for i, component in enumerate(components):
        print(f"Компонента {i+1}: {sorted(component)}")

