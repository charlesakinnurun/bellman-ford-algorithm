import matplotlib.pyplot as plt
import networkx as nx
import time

class BellmanFordVisualizer:
    """
    A class to implement the Bellman-Ford algorithm with step-by-step 
    visualization and comprehensive error checking for negative cycles.
    """
    
    def __init__(self, vertices):
        # The number of vertices in the graph
        self.V = vertices 
        # A list to store all edges in the format (source, destination, weight)
        self.graph = []
        # Store node names for better visualization (can be numbers or strings)
        self.nodes = []

    def add_edge(self, u, v, w):
        """
        Adds a directed edge to the graph.
        u: Source node
        v: Destination node
        w: Weight of the edge
        """
        self.graph.append([u, v, w])
        if u not in self.nodes: self.nodes.append(u)
        if v not in self.nodes: self.nodes.append(v)

    def visualize_step(self, distances, pos, title, highlighted_edge=None, final=False):
        """
        Helper method to render the graph state at a specific iteration.
        """
        plt.clf() # Clear current figure
        G = nx.DiGraph()
        
        # Add edges to the NetworkX graph for drawing
        for u, v, w in self.graph:
            G.add_edge(u, v, weight=w)

        # Draw nodes
        node_colors = ['#4fc3f7' if distances[node] != float('inf') else '#e0e0e0' for node in self.nodes]
        nx.draw_networkx_nodes(G, pos, node_size=700, node_color=node_colors)
        nx.draw_networkx_labels(G, pos, font_size=12, font_family="sans-serif")

        # Draw edges
        edge_colors = []
        edge_widths = []
        for u, v in G.edges():
            if highlighted_edge and (u == highlighted_edge[0] and v == highlighted_edge[1]):
                edge_colors.append('red') # Highlight the edge being relaxed
                edge_widths.append(3)
            else:
                edge_colors.append('gray')
                edge_widths.append(1)
        
        nx.draw_networkx_edges(G, pos, width=edge_widths, edge_color=edge_colors, arrowsize=20)
        
        # Draw edge labels (weights)
        edge_labels = nx.get_edge_attributes(G, 'weight')
        nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)

        # Add distance labels above nodes
        dist_labels = {node: (f"dist: {distances[node]}" if distances[node] != float('inf') else "inf") for node in self.nodes}
        # Offset labels slightly above nodes
        pos_higher = {k: (v[0], v[1] + 0.1) for k, v in pos.items()}
        nx.draw_networkx_labels(G, pos_higher, labels=dist_labels, font_color='blue', font_size=10)

        plt.title(title)
        plt.pause(0.5) # Pause to allow for visual inspection

    def run_bellman_ford(self, src):
        """
        The main Bellman-Ford algorithm implementation.
        Step 1: Initialize distances from src to all other vertices as infinite.
        Step 2: Relax all edges |V| - 1 times.
        Step 3: Check for negative weight cycles.
        """
        # Step 1: Initialize distances
        # We use a dictionary to handle non-integer node names
        dist = {node: float("Inf") for node in self.nodes}
        dist[src] = 0

        # Setup visualization layout
        G_viz = nx.DiGraph()
        for u, v, w in self.graph: G_viz.add_edge(u, v)
        pos = nx.spring_layout(G_viz)
        plt.ion() # Interactive mode on
        plt.figure(figsize=(10, 7))

        print(f"--- Starting Bellman-Ford from Source: {src} ---")
        self.visualize_step(dist, pos, f"Initial State (Source: {src})")

        # Step 2: Relax edges |V| - 1 times
        # A shortest path from src to any other node can have at most |V| - 1 edges.
        for i in range(self.V - 1):
            print(f"Iteration {i + 1}...")
            # We iterate through all edges in every iteration
            for u, v, w in self.graph:
                # If the distance to the source 'u' is not infinity 
                # and the new path through 'u' to 'v' is shorter than the current distance to 'v'
                if dist[u] != float("Inf") and dist[u] + w < dist[v]:
                    dist[v] = dist[u] + w
                    self.visualize_step(dist, pos, f"Iter {i+1}: Relaxing Edge {u}->{v}", highlighted_edge=(u,v))

        # Step 3: Check for negative-weight cycles
        # If we can still relax an edge after |V|-1 iterations, there's a negative cycle.
        for u, v, w in self.graph:
            if dist[u] != float("Inf") and dist[u] + w < dist[v]:
                self.visualize_step(dist, pos, "NEGATIVE CYCLE DETECTED!", highlighted_edge=(u,v))
                print("\nGraph contains negative weight cycle!")
                plt.ioff()
                plt.show()
                return None

        # Final Result Visualization
        self.visualize_step(dist, pos, "Final Shortest Paths", final=True)
        print("\nFinal Distances from Source:")
        for node, d in dist.items():
            print(f"Vertex {node}: {d}")
        
        plt.ioff()
        plt.show()
        return dist

# ==========================================
# EXAMPLE 1: Standard Graph (No Negative Cycle)
# ==========================================
def example_standard():
    print("\nRunning Example 1: Standard Directed Graph")
    g = BellmanFordVisualizer(5)
    g.add_edge("A", "B", -1)
    g.add_edge("A", "C", 4)
    g.add_edge("B", "C", 3)
    g.add_edge("B", "D", 2)
    g.add_edge("B", "E", 2)
    g.add_edge("D", "B", 1)
    g.add_edge("D", "C", 5)
    g.add_edge("E", "D", -3)
    
    g.run_bellman_ford("A")

# ==========================================
# EXAMPLE 2: Negative Cycle Detection
# ==========================================
def example_negative_cycle():
    print("\nRunning Example 2: Negative Cycle Detection")
    # A graph where B -> C -> D -> B has a sum of (3 + -6 + 2) = -1
    g = BellmanFordVisualizer(4)
    g.add_edge("A", "B", 4)
    g.add_edge("A", "C", 5)
    g.add_edge("B", "C", 3)
    g.add_edge("C", "D", -6)
    g.add_edge("D", "B", 2)
    
    g.run_bellman_ford("A")

if __name__ == "__main__":
    # Choose which example to run
    # Note: Requires 'matplotlib' and 'networkx' installed: pip install matplotlib networkx
    
    example_standard()
    # example_negative_cycle()