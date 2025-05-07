"""
This is a collection of useful functions
to be used for graph analysis
"""

### [2 mai 2025] Master version — this file must be always up to date until I have a pip/conda repo


import pprint as pprint
import networkx as nx
import pandas as pd
import matplotlib.pyplot as plt


### Basic properties of a graph

# MultiGraph: Undirected graphs with self loops and parallel edges
# https://networkx.org/documentation/stable/reference/classes/index.html

def basic_graph_properties(G):

    pprint.pprint({'is_multigraph':G.is_multigraph(), 
        'is_directed':G.is_directed(), 
        'number_of_nodes': G.number_of_nodes(), 
        'number_of_edges':G.number_of_edges(),
         '------' : '------',
        'is connected': nx.is_connected(nx.to_undirected(G)), 
        'components': len(list(nx.connected_components(nx.to_undirected(G)))),
        'density': nx.density(G)}, sort_dicts=False)



### Remove the attributes listed in a Python list from all nodes

# attrs_to_remove : the list of attribute names

def remove_node_attributes(G, attrs_to_remove):
    for node in G.nodes():
        for attr in attrs_to_remove:
            if attr in G.nodes[node]:
                del G.nodes[node][attr]



###  Describe and plot distribution of integers' list

def describe_plot_integers_distribution(il, plot_width, plot_heigth, plot_title):

    sl_id = pd.Series(il)
    print(sl_id.describe())

    ## Distribution of the indegree
    df_l = pd.DataFrame(sl_id.groupby(by=sl_id).size().items())
    df_l.columns=['value', 'number']

    fig, ax = plt.subplots(1,1, figsize=(plot_width,plot_heigth))

    plt.bar(df_l.value, df_l.number)

    # ax.xaxis.get_major_locator().set_params(integer=True)
    plt.xticks(range(min(df_l.value), max(df_l.value)+1));
    ax.yaxis.get_major_locator().set_params(integer=True)
    ax.bar_label(ax.containers[-1])
    plt.xticks(size=8)
    plt.xlabel('Values', size=9)
    plt.yticks(size=8)
    plt.ylabel('Number of values', size=9)
    plt.title(plot_title, size=10)

    plt.margins(x=0.02, y=0.1)

    plt.tight_layout()

    plt.show()           