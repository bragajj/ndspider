# Jeff Braga 12/12/22
import json
import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
import random


class Network():
    def __init__(self) -> None:
        self.g = nx.Graph()
        self.RELATIONS = ['Commercial Registered Agent',
                          'Owner Name', 'Registered Agent', 'Owners']
        self.input_file = "data/nd_data.json"

    def create_network(self) -> None:
        edge_list = self.build_edges()
        self.g.add_edges_from(edge_list)

    def build_edges(self) -> list:
        with open(self.input_file, "r") as input_json:
            nd_data = json.load(input_json)['rows']
        return [self.find_relation(nd_data[business]) for business in nd_data]

    def find_relation(self, input_data) -> tuple:
        # Connect each business to its owner/agent for an edge list
        for relation in self.RELATIONS:
            if relation in input_data['INFO'].keys():
                name = input_data['INFO'][relation].split("\n")[0].upper()
                return (input_data['TITLE'][0], name, {"relation": relation})

    def plot_network(self) -> None:
        pos = nx.fruchterman_reingold_layout(self.g, seed=100)
        # Color each individually connected subplot
        C = (self.g.subgraph(c) for c in nx.connected_components(self.g))
        for g in C:
            c = [random.random()] * nx.number_of_nodes(g)
            nx.draw(g, pos, node_size=8, node_color=c,
                    vmin=0.0, vmax=1.0, with_labels=False)
        plt.savefig("data/nd_network.png", dpi=300)


if __name__ == "__main__":
    NDNetwork = Network()
    NDNetwork.create_network()
    NDNetwork.plot_network()