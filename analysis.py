import os
from natsort import natsorted

root_dir = "/ssd_scratch/cvit/amoghtiwari/test_data/renders/"
for r,d,f in natsorted(os.walk(root_dir)):
    print("Pre sort", f)
    # r = natsorted(r)
    d = natsorted(d)
    f = natsorted(f)
    print("Post sort", f)

    print("root: ", r)
    print("dirs: ", d)
    print("files: ", f)
    print()

