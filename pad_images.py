import os
import cv2
import numpy as np

input_dir = "bg_subtracted_images"
output_dir = "bg_subtracted_images_padded"

target_size = (512, 512)
# breakpoint()
img_paths = os.listdir(input_dir)

target_h, target_w = target_size
for img_path in img_paths:
    img_name = img_path.split(".")[0]
    img_suffix = img_path.split(".")[-1]
    print("Name, Suffix", img_name, img_suffix)
    full_img_path = os.path.join(input_dir, img_path)
    img = cv2.imread(full_img_path)
    h, w, c = img.shape
    if h > target_h or w > target_w:
        print(f"present h,w: ({h,w}) is greater than the target h,w: ({target_h, target_w}).")
        print("Exitting!!!")
        exit(0)
    padded_img = np.zeros((target_h, target_w, c))
    pad_h = (target_h - h) // 2
    pad_w = (target_w - w) // 2
    padded_img[pad_h:target_h-pad_h, pad_w:target_w-pad_w, :] = img
    print(os.path.join(output_dir, img_name, "_padded.", img_suffix))
    cv2.imwrite(os.path.join(output_dir, f"{img_name}_padded.{img_suffix}"), padded_img)