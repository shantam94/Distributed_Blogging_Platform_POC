# Compute a simple distance metric (Manhattan distance)
def compute_distance(loc1, loc2):
    return abs(loc1[0] - loc2[0]) + abs(loc1[1] - loc2[1])

# Find the closest node based on location
def find_closest_node(data_location, NODES_LOCATIONS):
    distances = {node: compute_distance(data_location, node_location)
                 for node, node_location in NODES_LOCATIONS.items()}
    return min(distances, key=distances.get)