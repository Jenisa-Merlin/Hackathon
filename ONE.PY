import numpy as np

# Define the adjacency matrix for the neighborhood distances
neighborhood_distance = [
    [0, 1135, 2117, 623, 1560, 1641, 1963, 2210, 788, 1581, 1533, 1793, 1241, 510, 1765, 1442, 875, 1858, 1401, 2323], [2495, 0, 2117, 623, 1560, 1641, 1963, 2210, 788, 1581, 1533, 1793, 1241, 510, 1765, 1442, 875, 1858, 1401, 2323], [2495, 1135, 0, 623, 1560, 1641, 1963, 2210, 788, 1581, 1533, 1793, 1241, 510, 1765, 1442, 875, 1858, 1401, 2323], [2495, 1135, 2117, 0, 1560, 1641, 1963, 2210, 788, 1581, 1533, 1793, 1241, 510, 1765, 1442, 875, 1858, 1401, 2323], [2495, 1135, 2117, 623, 0, 1641, 1963, 2210, 788, 1581, 1533, 1793, 1241, 510, 1765, 1442, 875, 1858, 1401, 2323], [2495, 1135, 2117, 623, 1560, 0, 1963, 2210, 788, 1581, 1533, 1793, 1241, 510, 1765, 1442, 875, 1858, 1401, 2323], [2495, 1135, 2117, 623, 1560, 1641, 0, 2210, 788, 1581, 1533, 1793, 1241, 510, 1765, 1442, 875, 1858, 1401, 2323], [2495, 1135, 2117, 623, 1560, 1641, 1963, 0, 788, 1581, 1533, 1793, 1241, 510, 1765, 1442, 875, 1858, 1401, 2323], [2495, 1135, 2117, 623, 1560, 1641, 1963, 2210, 0, 1581, 1533, 1793, 1241, 510, 1765, 1442, 875, 1858, 1401, 2323], [2495, 1135, 2117, 623, 1560, 1641, 1963, 2210, 788, 0, 1533, 1793, 1241, 510, 1765, 1442, 875, 1858, 1401, 2323], [2495, 1135, 2117, 623, 1560, 1641, 1963, 2210, 788, 1581, 0, 1793, 1241, 510, 1765, 1442, 875, 1858, 1401, 2323], [2495, 1135, 2117, 623, 1560, 1641, 1963, 2210, 788, 1581, 1533, 0, 1241, 510, 1765, 1442, 875, 1858, 1401, 2323], [2495, 1135, 2117, 623, 1560, 1641, 1963, 2210, 788, 1581, 1533, 1793, 0, 510, 1765, 1442, 875, 1858, 1401, 2323], [2495, 1135, 2117, 623, 1560, 1641, 1963, 2210, 788, 1581, 1533, 1793, 1241, 0, 1765, 1442, 875, 1858, 1401, 2323], [2495, 1135, 2117, 623, 1560, 1641, 1963, 2210, 788, 1581, 1533, 1793, 1241, 510, 0, 1442, 875, 1858, 1401, 2323], [2495, 1135, 2117, 623, 1560, 1641, 1963, 2210, 788, 1581, 1533, 1793, 1241, 510, 1765, 0, 875, 1858, 1401, 2323], [2495, 1135, 2117, 623, 1560, 1641, 1963, 2210, 788, 1581, 1533, 1793, 1241, 510, 1765, 1442, 0, 1858, 1401, 2323], [2495, 1135, 2117, 623, 1560, 1641, 1963, 2210, 788, 1581, 1533, 1793, 1241, 510, 1765, 1442, 875, 0, 1401, 2323], [2495, 1135, 2117, 623, 1560, 1641, 1963, 2210, 788, 1581, 1533, 1793, 1241, 510, 1765, 1442, 875, 1858, 0, 2323], [2495, 1135, 2117, 623, 1560, 1641, 1963, 2210, 788, 1581, 1533, 1793, 1241, 510, 1765, 1442, 875, 1858, 1401, 0]
]

def convert_distance_list_to_dict(distances):
    length = len(distances)
    distance_dict = {}
    for i in range(length):
        node_distances = {f'n{i}': distances[i][j] for j in range(length)}
        distance_dict[f'n{i}'] = node_distances
    return distance_dict

neighborhood_distance_dict = convert_distance_list_to_dict(neighborhood_distance)
print(neighborhood_distance_dict)
# Define the distance from each restaurant to the neighborhood
restaurant_to_neighborhood = {
    'n0': 797, 'n1': 2156, 'n2': 593, 'n3': 880, 'n4': 521, 'n5': 1258, 'n6': 302, 'n7': 2253, 'n8': 1829, 'n9': 1067, 'n10': 884, 'n11': 1702, 'n12': 162, 'n13': 2070, 'n14': 1527, 'n15': 1719, 'n16': 1589, 'n17': 1604, 'n18': 1706, 'n19': 390
}

# Define the order quantities
order_quantity = {
    'n0': 70, 'n1': 70, 'n2': 90, 'n3': 50, 'n4': 70, 'n5': 90, 'n6': 110, 'n7': 70, 'n8': 110, 'n9': 70, 'n10': 70, 'n11': 110, 'n12': 110, 'n13': 90, 'n14': 50, 'n15': 90, 'n16': 110, 'n17': 90, 'n18': 70, 'n19': 110
}

# Define the vehicle capacity
capacity = 600

node_indices = {node: index for index, node in enumerate(restaurant_to_neighborhood)}

# Adjust the nearest_neighbor_path function
def nearest_neighbor_path(start_node, distances, quantities, capacity):
    path = [start_node]
    current_node = start_node
    remaining_capacity = capacity - quantities[start_node]

    while len(path) < len(distances):
        nearest_node = None
        nearest_distance = np.inf

        # Get the index of the current node
        current_node_index = node_indices[current_node]

        # Iterate over distances from the current node
        for index, distance in enumerate(distances[current_node_index]):
            node = list(restaurant_to_neighborhood.keys())[index]  # Get the node corresponding to the index

            if node != current_node and node not in path and distance < nearest_distance and quantities[node] <= remaining_capacity:
                nearest_node = node
                nearest_distance = distance

        if nearest_node is not None:
            path.append(nearest_node)
            remaining_capacity -= quantities[nearest_node]
            current_node = nearest_node
        else:
            break

    return path

def find_remaining_path(visited_nodes, distances, quantities, capacity):
    path = []
    while True:
        unvisited_nodes = [node for node in quantities.keys() if node not in visited_nodes]
        if not unvisited_nodes:
            break
        
        start_node = visited_nodes[-1]
        new_path = nearest_neighbor_path(start_node, distances, quantities, capacity)
        visited_nodes.extend(new_path)
        path.extend(new_path)
    
    return path

# Start with the first restaurant
start_node = 'n0'
visited_nodes = [start_node]
path = nearest_neighbor_path(start_node, neighborhood_distance, order_quantity, capacity)

# Combine paths
complete_path = find_remaining_path(visited_nodes, neighborhood_distance, order_quantity, capacity)

# Convert to desired format
p = ["r0"]
for node in complete_path:
    p.append(node)
p.append("r0")

# Print the complete path
print("Optimal Path:", complete_path)

output_data = {
    "v0": {
        "path1": p
    }
}
print(output_data)

'''
# Find the nearest neighbor path starting from the first restaurant
start_node = 'n0'
visited_nodes = [start_node]
path = nearest_neighbor_path(start_node, neighborhood_distance, order_quantity, capacity)
print(path)
remaining_path = find_remaining_path(visited_nodes, neighborhood_distance, order_quantity, capacity)
print(remaining_path)
# Combine the paths
complete_path = path + remaining_path

# Print the complete path
print("Optimal Path:", complete_path)

output_data = {
    "v0": {
        "path1": ["r0"] + complete_path + ["r0"]
    }
}
print(output_data)

# Find the nearest neighbor path starting from the first restaurant
start_node = 'n0'
p = ["r0"]
path = nearest_neighbor_path(start_node, neighborhood_distance, order_quantity, capacity)
for i in range(len(path)):
    p.append(path[i])
p.append("r0")

# Print the path
print("Optimal Path:", path)

output_data = {
        "v0": {
            "path1": p
        }
    }
print(output_data)'''
