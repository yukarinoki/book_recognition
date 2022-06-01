import os

image_files = os.listdir("../dataset/multiple")
input_image_files =list(map(lambda s: "../dataset/multiple/" + s, image_files))
grayscale_image_files =list(map(lambda s: "../dataset/grayscale/" + s, image_files))
canny_image_files =list(map(lambda s: "../dataset/canny/" + s, image_files))
