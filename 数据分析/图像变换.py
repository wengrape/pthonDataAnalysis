from PIL import Image
import numpy as np

img = np.array(Image.open("big1.png"))
print(img.shape,img.dtype,img.ndim)
print(img)
b = [255, 255, 255, 255] - img
new_img = Image.fromarray(b.astype("uint8"))
new_img.save("ko.png")