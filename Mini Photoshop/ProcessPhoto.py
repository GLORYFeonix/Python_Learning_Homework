from PIL import ImageEnhance, ImageDraw, ImageFont

from PIL.ImageQt import ImageQt
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap

import Variable


class Process():
    # 修改类
    imagelabel = Variable.get_imagelabel()

    def __init__(self):
        self.bright = 1
        self.sharpness = 1
        self.contrast = 1
        self.angle = 0
        self.height = 0
        self.width = 0
        self.watermark = False
        self.save = ""

    # 改变属性值的函数
    def change_bright(self, bright):
        self.bright = bright

    def change_width(self, value):
        self.width = Variable.get_width() + value

    def change_height(self, value):
        self.height = Variable.get_height() + value

    def change_angle(self, angle):
        self.angle = angle

    def change_watermark(self):
        self.watermark = not self.watermark

    def get_watermark(self):
        return self.watermark

    def change_save(self, path):
        self.save = path

    def process_photo(self, image):
        # 应用修改
        if image is not None:
            enhancer = ImageEnhance.Brightness(image)   # 获取图片亮度
            image = enhancer.enhance(self.bright)   # 修改图片亮度

            if self.watermark:
                idraw = ImageDraw.Draw(image)   # 添加水印
                # 设置水印内容
                text = "Watermark"
                font = ImageFont.truetype("arial.ttf", size=200)
                idraw.text((10, 10), text, font=font)

            # 应用图片旋转
            image = image.rotate(self.angle)

            # 显示图片修改效果
            imagelabel = Variable.get_imagelabel()
            qimg = ImageQt(image)
            img_pix = QPixmap.fromImage(qimg, Qt.AutoColor)
            img_pix = img_pix.scaled(self.width, self.height)   # 应用图片大小设置
            imagelabel.setPixmap(img_pix)

            # 如果存储标准不为False，则进行保存，保存完将标志重新设置为False
            if self.save:
                img_pix.save(self.save)
                self.save = False
