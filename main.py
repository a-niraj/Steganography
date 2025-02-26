from LSBSteg import LSBSteg

import cv2
import docopt
import numpy as np

steg = LSBSteg(cv2.imread("/Users/avyankniraj/pythonSteg/image1.png"))
img_encoded = steg.encode_text("secret")
cv2.imwrite("my_new_image.png", img_encoded)

im = cv2.imread("my_new_image.png")
steg = LSBSteg(im)
print("Text value: ",steg.decode_text())
