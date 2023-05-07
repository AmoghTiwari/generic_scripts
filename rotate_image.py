import matplotlib.pyplot as plt
FILE_NAME="kipchoge.jpg" # Ensure that the file extension here is same as that of the image chosen above
img_name = FILE_NAME
import numpy as np

def rotateImage(img, R):
    new_img = np.zeros_like(img)
    if len(img.shape) == 3:
        h,w,_ = img.shape
    else:
        h,w = img.shape
    
    cx, cy = (h-1)//2, (w-1)//2

    for i in range(h):
        for j in range(w):
            # breakpoint()
            try:
                pre_coords = np.floor(R.T @ np.array([i-cx,j-cy])).astype('int') + np.array([cx, cy])
                print((i,j), pre_coords)
                new_img[i,j] = img[pre_coords[0], pre_coords[1], :]
            except:
                breakpoint()
            # new_img[i,j] = img[pre_coords]
    return new_img

def buildRotationMatrix(angle_deg):
    angle_rad = np.radians(angle_deg)
    return np.array([[np.cos(angle_rad), -np.sin(angle_rad)],
              [np.sin(angle_rad), np.cos(angle_rad)]])

""" Rotate Image """
# Assuming you have run the above cells, Otherwise, follow the steps mentioned above to place an image in your runtime
import cv2
img = plt.imread(img_name)
img = cv2.resize(img, (256, 256)) # Resizing, to make operations faster

# plt.imshow(img)
# plt.show()

rotate_angle = 90
R = buildRotationMatrix(rotate_angle)
rotated_image = rotateImage(img, R)
print(f"Image rotated by {rotate_angle} degrees")
plt.imshow(rotated_image)
plt.show()