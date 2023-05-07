import os
from tqdm import tqdm

""" Changes To Be Made """
"""
To run this script, make the following changes first:
1. INPUT_DIR and OUTPUT_DIR paths
2. The get_new_name() function: It must be modified according to the template we need to convert
    the present file name to a new file name
"""

INPUT_DIR = "/share3/amoghtiwari/normal_prediction/THumans2/full_data/RENDER"
OUTPUT_DIR = "/share3/amoghtiwari/normal_prediction/THumans2/full_data/RENDER"

def get_new_name(present_name):
    new_name = present_name.split(".")[0]
    return new_name

file_names = os.listdir(INPUT_DIR)
for file_name in file_names:
    file_path = os.path.join(INPUT_DIR, file_name)
    new_name = get_new_name(file_name)
    new_path = os.path.join(OUTPUT_DIR, new_name)
    command = f"mv {file_path} {new_path}"
    # print(file_path)
    print(command)
    # os.system(command)

print("Done ... !!! Comment out system call !!!")
