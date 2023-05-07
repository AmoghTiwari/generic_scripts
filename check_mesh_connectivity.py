import os
import trimesh
import networkx as nx
from random import randint

""" Things to be Changed Below"""

MESH_PATH = "/data/groot/Datasets/3DHumans/our_scans_image/data_release_face_blurred/1/1.obj"
# MESH_PATH = "/data/groot/Datasets/3DHumans/our_scans_image/mesh_data/1/1.obj"
NUM_ITERS = 10
""" Things to be Changed Above"""


MESH = None
MESH_GRAPH = None

def load_mesh(tgt_mesh_path):
    global MESH
    global MESH_GRAPH
    print(f"!!! Loading mesh GLOBALLY !!!")
    print(f"Mesh path: {tgt_mesh_path}")
    MESH = trimesh.load(tgt_mesh_path, process=False)
    MESH_GRAPH = nx.Graph()
    for edge in MESH.edges:
        MESH_GRAPH.add_edge(*edge)
    print("!!! Finished loading mesh GLOBALLY !!!")
    print()
    return None


""" Main Function Below"""
load_mesh(MESH_PATH)

vtx_count = len(MESH.vertices)
no_path_list = []


for iter in range(NUM_ITERS):
    src = randint(1, vtx_count) - 1
    dst = randint(1, vtx_count) - 1
    dst = src

    try:
        spl = nx.shortest_path_length(MESH_GRAPH, src, dst)
        # sp = nx.shortest_path(MESH_GRAPH, src, dst)
        # spl = len(sp) - 1
        # dist = 0
        # for i in range(len(sp)-1):
        #     dist+= math.dist(MESH.vertices[sp[i]], MESH.vertices[sp[i+1]])
   
    except nx.NetworkXNoPath:
        no_path_list.append([MESH_PATH, src, dst])
        dist = -1        

print(no_path_list)
print(f"Didn't find a path {len(no_path_list)} times in {NUM_ITERS} iterations i.e. path was NOT found {100 * len(no_path_list) / NUM_ITERS} percentage times")

print(f"Number of connected componenets = ", nx.number_connected_components(MESH_GRAPH))