from PIL import ImageEnhance, ImageDraw, ImageFont

from PIL.ImageQt import ImageQt
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap

import Variable


class Process():
    imagelabel = Variable.get_imagelabel()

    def __init__(self):
        self.bright = 1
        self.sharpness = 1
        self.contrast = 1
        self.angle_final = 0
        self.height = Variable.DEFAULT_HEIGHT
        self.width = Variable.DEFAULT_WIDTH
        self.watermark = False
        self.save = False

    def change_bright(self, bright):
        self.bright = bright

    def change_width(self, value):
        self.width = Variable.get_width() + value

    def change_height(self, value):
        self.height = Variable.get_height() + value

    def change_angle_final(self, angle_final):
        self.angle_final = angle_final

    def change_watermark(self):
        self.watermark = not self.watermark

    def get_watermark(self):
        return self.watermark

    def process_photo(self, image):
        if image is not None:
            enhancer = ImageEnhance.Brightness(image)
            image = enhancer.enhance(self.bright)

            # image = image.resize((self.width, self.height))

            if self.watermark:
                idraw = ImageDraw.Draw(image)
                text = "Watermark"
                font = ImageFont.truetype("arial.ttf", size=200)
                idraw.text((10, 10), text, font=font)


        # return image
        imagelabel = Variable.get_imagelabel()
        qimg = ImageQt(image)
        img_pix = QPixmap.fromImage(qimg, Qt.AutoColor)
        img_pix = img_pix.scaled(self.width, self.height)
        imagelabel.setPixmap(img_pix)

