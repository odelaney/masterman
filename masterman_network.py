from pyvis.network import Network
import networkx as nx
import pandas as pd

nodes_data = pd.read_csv("data/address_book_nodes.csv", keep_default_na=False)
edges_data = pd.read_csv("data/address_book_edges.csv")

def create_node_list(data):
    nodes = []
    for idx, row in data.iterrows():
        nodes.append((row["entity_name"], {"color": row.colour, "source": row.source, "title": "Description: " + row.description + "\nAddress: " + row.location}))

    return nodes

def create_edges_list(data):
    edges = []
    for idx, row in data.iterrows():
        edges.append((row.source, row.target, {"color": "black"}))
    
    return edges

def create_graph(nodes,edges):
    G = nx.Graph()

    G.add_nodes_from(nodes)
    G.add_edges_from(edges)

    return G

def visualise_graph(graph):
    net = Network(filter_menu=True)
    net.from_nx(graph)
    net.force_atlas_2based()

    net.save_graph("index.html")

nodes = create_node_list(nodes_data)
edges = create_edges_list(edges_data)

graph = create_graph(nodes,edges)
visualise_graph(graph)
