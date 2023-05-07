import os

PRESENT_DIR = "."
TARGET_DIR = "/new"
names = os.listdir(PRESENT_DIR)

for i in range(len(names)):
    name = names[i]
    print(name)
    name_idx = int(name.split("-")[0][3:])
    print(name_idx)
    name_idx_new = f"{name_idx:04d}"
    cmd = f"cp {os.path.join(PRESENT_DIR, name)} {os.path.join(TARGET_DIR, f'{name_idx_new}-dpt_beit_large_512.pfm')}"
    print(cmd)
    os.system(cmd)

