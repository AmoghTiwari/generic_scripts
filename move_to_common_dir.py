import os

target_dir = "/data/amogh/ConVol_E/vertex_maps"
sub_dirs = sorted(os.listdir(target_dir))

for sub_dir in sub_dirs:
    sub_sub_dirs = os.listdir(os.path.join(target_dir, sub_dir))
    for sub_sub_dir in sub_sub_dirs:
        file_name = f"{sub_dir}_{sub_sub_dir}_vertexmap.npz"
        command = f"mv {os.path.join(target_dir, sub_dir, sub_sub_dir,)}/vertexmap.npz {os.path.join(target_dir, file_name)}"
        print(command)
        os.system(command)