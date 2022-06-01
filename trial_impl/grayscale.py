import sys
import cv2
import util

for i, image_file in enumerate(util.input_image_files):
    img_bgr = cv2.imread(image_file)
    img_gray = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2GRAY)
    grayscale_file = util.gray_image_files[i]
    cv2.imwrite(grayscale_file, img_gray)

