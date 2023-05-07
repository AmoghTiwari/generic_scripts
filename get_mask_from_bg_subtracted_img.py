# Get Masks From BG Subtracted Image

import cv2
import numpy as np
import os

IMG_DIR = 'rgb'
BG_MASK_TGT_DIR = 'bg_masks'

SKIPPED = []
img_names = sorted(os.listdir(IMG_DIR))
for img_name in img_names:
    img_path = os.path.join(IMG_DIR, img_name)
    img = cv2.imread(img_path)
	mask = np.zeros_like(img)
	if len(img.shape) == 2:
		print("Got grayscale image as input")
		mask[img > 0] = 1
	elif len(img.shape) == 3 and img.shape[-1] == 3:
		mask[img.sum(2) > 0] = 1
	else:
		print("Got weird image shape as input. Skipping ...")
		print(f"img_name: {img_name}; shape: {img.shape}")
		SKIPPED.append([img_name, idx])
		continue
    cv2.imwrite(os.path.join(BG_MASK_TGT_DIR, img_name.split()[0]+".png"), mask.astype('uint8')*255)

print("Processing Done")
print("Printing Skipped ....")
print(SKIPPED)