'''
Level 0
Consultant has mapped Saibaba colony into 20 neighborhoods and also 
suggested location for first Restaurant / cloud kitchen. Steve wants to start from 
the restaurant and cover all neighborhoods and return to the restaurant using the 
shortest possible path avoiding already visited neighborhoods. So we want to write 
a program that can recommend the path Steve needs to traverse to generate 
outfile
'''
'''
Approch: Travelling salesman problem
'''
import json
from sys import maxsize
from itertools import permutations


def tsp(graph, s, V):
    visited = [False] * V
    visited[s] = True
    path = ["r0"]  # Start with the restaurant
    path.append('n'+str(13))
    for _ in range(V - 1):
        min_dist = maxsize
        next_vertex = -1
        for j in range(V):
            if not visited[j] and graph[s][j] < min_dist:
                min_dist = graph[s][j]
                next_vertex = j
        visited[next_vertex] = True
        path.append(f"n{next_vertex}")
        s = next_vertex
    
    path.append("r0")  # Return to the restaurant
    if sum(visited) != V:
        print("error")
    else:
        return path


if __name__ == "__main__":
    #reading input file
    with open("LEVEL 0\level0.json", "r") as file:
        data = json.load(file)
    
    restaurant_data = data['restaurants']['r0']
    neighborhood_distances = restaurant_data['neighbourhood_distance']
    n_neighborhoods = len(neighborhood_distances)
    print(n_neighborhoods)

    neighbourhood_distances = data["restaurants"]["r0"]["neighbourhood_distance"]

    graph = []
    graph.append(neighborhood_distances)

    # Convert the neighborhood distances into a 2D matrix format.
    g = [[0 if i == j else neighborhood_distances[j] for j in range(n_neighborhoods)] for i in range(n_neighborhoods)]
    print(g)
    #restaurant at index 0
    s = 0
    min = maxsize
    for i in range(len(neighborhood_distances)):
        if(neighborhood_distances[i] < min):
            min = neighborhood_distances[i]
            s = i
    
    path = tsp(g, s, n_neighborhoods)
    print(path)
    #dict to store in json file
    output_data = {
        "v0": {
            "path": path
        }
    }

    # output data to a JSON file
    with open("LEVEL 0\level0_output.json", "w") as outfile:
        json.dump(output_data, outfile)
