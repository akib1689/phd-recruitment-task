"""Utility functions to parse and analyze CFG DOT strings."""

__all__ = ["dot_to_graph", "count_nodes_edges", "get_depth"]

import re
from typing import Optional, Tuple

import networkx as nx
import numpy as np
import pandas as pd
import pydot


def dot_to_graph(dot_str: str) -> nx.DiGraph:
    """
    Convert a DOT string (e.g., from Boa) to a NetworkX directed graph.
    Returns empty DiGraph on failure.
    """
    if pd.isna(dot_str) or not isinstance(dot_str, str) or not dot_str.strip():
        return nx.DiGraph()
    
    # Skip abnormally large inputs (likely corrupted or non-CFG)
    if len(dot_str) > 200_000:
        return nx.DiGraph()

    try:
        # Normalize line breaks and escape issues
        dot_clean = re.sub(r'\\[ln]', ' ', dot_str)  # replace \l, \n in labels

        # Ensure valid digraph wrapper
        if 'digraph' not in dot_clean:
            dot_clean = f'digraph G {{\n{dot_clean}\n}}'

        graphs = pydot.graph_from_dot_data(dot_clean)
        if not graphs or len(graphs) == 0:
            return nx.DiGraph()
        
        pydot_graph = graphs[0]
        
        # Build NetworkX graph
        G = nx.DiGraph()

        # Add real nodes (exclude 'node'/'edge' attribute blocks)
        for node in pydot_graph.get_nodes():
            name = node.get_name()
            if name and name.strip('"') not in {'node', 'edge', ''}:
                G.add_node(name.strip('"'))

        # Add edges
        for edge in pydot_graph.get_edges():
            src = edge.get_source().strip('"') if edge.get_source() else None
            dst = edge.get_destination().strip('"') if edge.get_destination() else None
            if src and dst and src in G and dst in G:
                G.add_edge(src, dst)
            # Skip edges involving non-existent nodes (e.g., dangling)
        
        return G

    except Exception:
        # Silent fail → empty graph; optionally log if needed
        return nx.DiGraph()


def count_nodes_edges(G: nx.DiGraph) -> Tuple[int, int]:
    """Return (node_count, edge_count) for a NetworkX DiGraph."""
    return len(G.nodes), len(G.edges)


def get_depth(G: nx.DiGraph) -> int:
    """
    Compute CFG depth = length of longest path (in edges).
    For cyclic CFGs (e.g., loops), uses SCC condensation to get DAG longest path.
    Returns -1 on error, 0 for empty graph.
    """
    if len(G) == 0:
        return 0

    try:
        if nx.is_directed_acyclic_graph(G):
            return nx.dag_longest_path_length(G)
        else:
            # Condense strongly connected components (e.g., loops) → DAG
            C = nx.condensation(G)
            return nx.dag_longest_path_length(C)
    except Exception:
        return -1