""" To use this directory, change the path to ROOT_DIR 
Further, also note that do NOT use this dir without first checking stuff with a breakpoint
"""

import os
import shutil
from natsort import natsorted

ROOT_DIR = "/data/volumetric/data_seq2/partial_data/data_meshes_post_poisson_post_align_post_clean"

file_names = natsorted(os.listdir(ROOT_DIR))

for file_name in file_names:
	name, ext = os.path.splitext(file_name)

	""" Comment and Uncomment Stuff Below This """

	print("Check the commands first before running the script for all files, search for 'Comment and Uncomment Stuff Above This' ")
	print("### You are going to do the following ###")
	print(f"1. Create a directory named: {os.path.join(ROOT_DIR, name)} ")
	print(f"2. Move the file called {os.path.join(ROOT_DIR, file_name)} to {os.path.join(ROOT_DIR, name, file_name)} ")
	breakpoint()

	""" Comment and Uncomment Stuff Above This """
	
	os.makedirs(os.path.join(ROOT_DIR, name))
	shutil.copy2(os.path.join(ROOT_DIR, file_name), os.path.join(ROOT_DIR, name, file_name))

print(f"1. Check if all the files got copied correctly to the intended data structure")
print(f"2. Create a directory called 'all_<ext_type>' inside the root directory ({ROOT_DIR})")
print(f"3. Then move all the individual files to that dir")
print(f"4. Double check if all the files got copied properly. Then remove the 'all_<ext_type>' directory")

print("!!! Done !!!")
print("!!!!! DO NOT FORGET TO UN-COMMENT THE PART WITH THE BREAKPOINT AGAIN AFTER RUNNING THE SCRIPT !!!!")
