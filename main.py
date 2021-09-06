from io import BytesIO
import cv2
from PIL import Image
import time
cap = cv2.VideoCapture('badapple.mp4') # change this to any filename that you want.
while (cap.isOpened()):
    ret, frame = cap.read()
    if ret == False:
        break
    is_success, buffer = cv2.imencode(".jpg", img=frame)
    image1 = BytesIO(buffer)
    image1.seek(0)
    img = Image.open(image1)
    width, height = img.size
    aspect_ratio = height / width
    new_width = 60 # change this to change size of ASCII render.
    new_height = aspect_ratio * new_width * 0.55
    img = img.resize((new_width, int(new_height)))
    img = img.convert('L')
    pixels = img.getdata()
    chars = ["B", "S", "#", "&", "@", "$", "%", "*", "!", ":", " "]
    new_pixels = [chars[pixel // 25] for pixel in pixels]
    new_pixels = ''.join(new_pixels)
    new_pixels_count = len(new_pixels)
    ascii_image = [new_pixels[index:index + new_width] for index in range(0, new_pixels_count, new_width)]
    ascii_image = "\n".join(ascii_image)
    time.sleep(00.025)
    print(ascii_image)


print("done")