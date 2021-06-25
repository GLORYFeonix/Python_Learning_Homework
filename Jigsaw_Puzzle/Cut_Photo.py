from PIL import Image

img = Image.open("Jigsaw puzzle/png/原图.jpg")
print(img.size)

num = 0
for j in range(3):
    for i in range(3):
        cropped = img.crop((i*300, j*300, (i+1)*300, (j+1)*300))
        cropped.save("Jigsaw puzzle/png/%s.jpg" % num)
        num = num+1
        i = i+1
    j = j+1
