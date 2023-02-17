from PIL import Image, ImageEnhance, ImageFilter
import os

path = './images'
pathOut = './edited-images'

for filename in os.listdir(path):
    image = Image.open(f"{path}/{filename}")

    edit = image.filter(ImageFilter.SHARPEN)

    factor = 1.5
    enhancer = ImageEnhance.Contrast(edit)
    edit = enhancer.enhance(factor)

    clean_name = os.path.splitext(filename)[0]

    edit.save(f'{pathOut}/{clean_name}_edited.jpg')
