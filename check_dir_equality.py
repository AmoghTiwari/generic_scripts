import os
from natsort import natsorted

DIR_A = "/data/amogh/ConVol_E/icvgip_data/3DHumans_70_views/bodymap_representation/bodymap_gt/train"
DIR_B = "/data/amogh/ConVol_E/icvgip_data/3DHumans_70_views/ConVol_E_representation/anchor_cse/train"

def get_expected_file_name(input_file_name):
    """For complete equality, simply return input_file_name directly"""
    # return input_file_name
    return input_file_name.replace("bodymap", "0_00")

file_names_a = natsorted(os.listdir(DIR_A))
file_names_b = natsorted(os.listdir(DIR_B))

if len(file_names_a) != len(file_names_b):
    print("Number of files in both directories is different. Hence, directories can't be same")
    exit()

for i, file_name_a in enumerate(file_names_a):
    file_name_b = file_names_b[i]
    expected_file_name_b = get_expected_file_name(file_name_a)
    print(f"file_name_a: {file_name_a}; file_name_b: {file_name_b}; expected_file_name_b: {expected_file_name_b}")
    
    if expected_file_name_b != file_name_b:
        print(f"Inequality found at idx: {i}")
        print(f"file_name_a: {file_name_a}; expected_file_name_b: {expected_file_name_b}; file_name_b: {file_name_b}")
        exit()
    os.system(f"ls {os.path.join(DIR_B, expected_file_name_b)}1")
print("Exitted Normally! Both dirs seem to be equal. But still, double check stuff before deleting anything!!!")

