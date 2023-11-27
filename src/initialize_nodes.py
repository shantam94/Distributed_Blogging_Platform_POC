import os

# Initialize nodes (directories)
def initialize_nodes(NODES_LOCATIONS):
    for node in NODES_LOCATIONS:
        os.makedirs("nodes/" + node, exist_ok=True)
