import PIL.Image
from PIL import Image
import os

path = "C:/Users/Olek/Desktop/06/"
out = "C:/Users/Olek/Desktop/06x15l/"
resize_ratio = 1.5  # where 0.5 is half size, 2 is double size


def resize(resize_ratio, path, out):
    dirs = os.listdir(path)
    for item in dirs:
        image = Image.open(path + item)
        file_path, extension = os.path.splitext(path + item)
        out_path, extension1 = os.path.splitext(out + item)

        new_image_height = int(image.size[0] / (1 / resize_ratio))
        new_image_length = int(image.size[1] / (1 / resize_ratio))

        image = image.resize((new_image_height, new_image_length), PIL.Image.Resampling.LANCZOS)
        image.save(out_path + "_res" + extension, 'png', quality=90)


resize()