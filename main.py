from PIL import Image, ImageOps, ImageDraw
import matplotlib.pyplot as plt

# Dices

dice_1 = Image.open("Images\\1.jpg")
dice_2 = Image.open("Images\\2.jpg")
dice_3 = Image.open("Images\\3.jpg")
dice_4 = Image.open("Images\\4.jpg")
dice_5 = Image.open("Images\\5.jpg")
dice_6 = Image.open("Images\\6.jpg")

image = Image.open("C:\\Users\\MSI-Laptop\\Pictures\\Saved Pictures\\Profile3.jpg")
image = ImageOps.grayscale(image)
image = ImageOps.equalize(image)

dicenumber = 600

dicew = int(image.width / dicenumber)
diceh = int(image.height / dicenumber)

size = (dicew, diceh)


dice_1.resize(size)
dice_2.resize(size)
dice_3.resize(size)
dice_4.resize(size)
dice_5.resize(size)
dice_6.resize(size)

newImage = Image.new("L", (image.width, image.height), 'white')

for y in range(0, image.height - diceh, diceh):
    for x in range(0, image.width - dicew, dicew):
        color = 0
        for j in range(diceh):
            for i in range(dicew):
                thisColor = image.getpixel((x + i, y + j))
                color += thisColor
                
        color /= dicew * diceh
        dice_number = int((255 - color) * 6.0 / 255 + 1)
        if dice_number == 1:
            newImage.paste(dice_1, (x, y))
        elif dice_number == 2:
            newImage.paste(dice_2, (x, y))
        elif dice_number == 3:
            newImage.paste(dice_3, (x, y))
        elif dice_number == 4:
            newImage.paste(dice_4, (x, y))
        elif dice_number == 5:
            newImage.paste(dice_5, (x, y))
        elif dice_number == 6:
            newImage.paste(dice_6, (x, y))

newImage.save("Images\\new.jpg")