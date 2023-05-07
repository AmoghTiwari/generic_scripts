import cv2
import numpy as np
import os

PGN_DIR = 'pgn_masks'
BG_MASK_TGT_DIR = 'bg_masks'

pgn_mask_file_names = sorted(os.listdir(PGN_DIR))
for pgn_mask_file_name in pgn_mask_file_names:
    pgn_mask_file_path = os.path.join(PGN_DIR, pgn_mask_file_name)
    pgn_mask = cv2.imread(pgn_mask_file_path)
    # breakpoint()
    mask = pgn_mask.sum(2)
    mask[mask > 0] = 255
    cv2.imwrite(os.path.join(BG_MASK_TGT_DIR, pgn_mask_file_name.split()[0]+".png"), mask.astype('uint8'))
