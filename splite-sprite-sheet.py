import yaml
from PIL import Image

image_file_path = r'C:\Users\25722\Documents\Tencent Files\2572261667\FileRecv\stg02\Ground2Atlas.png'
meta_file_path = image_file_path + '.meta'

im = Image.open(image_file_path)
_, height = im.size
with open(meta_file_path, 'r') as file:
    data = yaml.load(file.read(), Loader=yaml.FullLoader)
    sprites = data['TextureImporter']['spriteSheet']['sprites']
    for sprite in sprites:
        rect = sprite['rect']
        y = height - rect['y'] - rect['height']
        box = (
            rect['x'],
            y,
            rect['x'] + rect['width'],
            y + rect['height']
        )
        region = im.crop(box)
        region.save(sprite['name'] + '.png')
