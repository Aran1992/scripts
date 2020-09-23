import json
from PIL import Image

image_file_path = r'C:\Works\xiaoxin\myLaya\laya\assets\animations\cosplay\sns1010_jump_01.png'
meta_file_path = r'C:\Works\xiaoxin\myLaya\laya\assets\animations\cosplay\sns1010-2.json'

im = Image.open(image_file_path)
_, height = im.size
with open(meta_file_path, 'r') as file:
    data = json.loads(file.read())
    print(data)
    sprites = data['frames']
    for sprite in sprites:
        rect = sprites[sprite]['frame']
        y = height - rect['y'] - rect['h']
        box = (
            rect['x'],
            rect['y'],
            rect['x'] + rect['w'],
            rect['y'] + rect['h']
        )
        region = im.crop(box)
        region.save(sprite)
