""" BG Subtraction Given Masks """
import os
import numpy as np
import cv2

masks_dir = ""
raw_imgs_dir = ""
output_dir = ""

raw_img_paths = sorted(os.listdir(raw_imgs_dir))
mask_paths = sorted(os.listdir(masks_dir))

for i in range(len(raw_img_paths)):
    raw_img = cv2.imread(os.path.join(raw_imgs_dir, raw_img_paths[i]))
    mask = cv2.imread(os.path.join(masks_dir, mask_paths[i]))
    mask[mask <= 127] = 0
    mask[mask > 127] = 1
    bg_sub_img = raw_img * mask
    cv2.imwrite(os.path.join(output_dir, mask_paths[i]), bg_sub_img)
