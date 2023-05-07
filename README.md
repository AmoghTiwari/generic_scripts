# Generic Scripts

- `move_to_individual_directories.py`: Given a set of files in a directory, this script is used to create an individual directory for each file, and move the file into that directory. For example, given a ```root_dir``` with files ```1.ply```, ```2.ply```, ```3.ply```, ```4.ply```, ```5.ply```, this script will create directories ```root_dir/1```, ```root_dir/2```, ```root_dir/3```, ```root_dir/4```, ```root_dir/5```, and then place ```1.ply``` inside ```root_dir/1```, ```2.ply``` inside ```root_dir/2``` and so on.
**Note**: Do NOT forget to check stuff first for a single case with a breakpoint, before running the script for the whole directory.

- `check_mesh_connectivity.py`: For a given mesh, check if the mesh is fully connected (in an approximate way). It randomly selects two vertices and checks if they are connected for a certain number of iterations

- `add_leading_zeros_to_filenames.py`: Given a direcotry containing a set of filenames like "9.png", "10.png", "11.png", this script changes the names of files to "09.png", "10.png", "11.png". This leads to better sorting of things at some places
