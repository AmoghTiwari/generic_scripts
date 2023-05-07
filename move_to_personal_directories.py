ROOT_DIR = "."

file_names = os.listdir(ROOT_DIR)

for file_name in file_names:
	name, ext = os.path.splitext(file_name)
	os.makedirs(os.path.join(ROOT_DIR, name))
	shutil.copy2(os.path.join(ROOT_DIR, file_name), os.path.join(ROOT_DIR, name, file_name))
