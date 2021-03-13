from PIL import Image

pixelSize = 1

image = Image.open('0.jpg')
image = image.resize((int(image.size[0]/pixelSize), int(image.size[1]/pixelSize)), Image.NEAREST)
image = image.resize((int(image.size[0]*pixelSize), int(image.size[1]*pixelSize)), Image.NEAREST)
pixel = image.load()

image.save(f'0_{pixelSize}.jpg')