import PIL.Image
from PIL import Image
import os


def Interpolation(inputPath, outputPath, method):
    dirs = os.listdir(inputPath)
    print("function dirs: ", dirs)

    for item in dirs:
        print("item in dir: ", item)
        image = Image.open(inputPath + item)
        print("image: ", image)
        print("item path + item: ", inputPath + item)

        new_image_height = int(image.size[0] / (1 / 1.5))
        new_image_length = int(image.size[1] / (1 / 1.5))

        if method == 'b':
            image = image.resize((new_image_height, new_image_length), PIL.Image.Resampling.BICUBIC)
            image.save(outputPath + item.split(sep='.')[0] + '_b.png', 'png', quality=60)

        if method == 'l':
            image = image.resize((new_image_height, new_image_length), PIL.Image.Resampling.LANCZOS)
            image.save(outputPath + item.split(sep='.')[0] + '_l.png', 'png', quality=60)

#Interpolation('C:/Users/Olek/Desktop/SRGAN-PyTorch-master/LR/test/','C:/Users/Olek/Desktop/SRGAN-PyTorch-master/LR/interpolated/','b')