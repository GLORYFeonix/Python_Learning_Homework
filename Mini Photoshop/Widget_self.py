from PyQt5.QtWidgets import QWidget, QLabel, QSlider, QPushButton, QHBoxLayout, QVBoxLayout

from ProcessPhoto import *

image = Variable.get_image()
imageLabel = Variable.get_imagelabel()
process = Process()


class AdjustTab(QWidget):
    def __init__(self):
        super().__init__()
        self.bright_label = QLabel("亮度")
        self.bright_label_value = QLabel('0')
        self.bright_slider = QSlider(Qt.Horizontal, self)
        self.bright_slider.setMaximum(100)
        self.bright_slider.setMinimum(-100)
        self.bright_slider.setValue(0)
        self.bright_slider.valueChanged[int].connect(self.changeImage)
        self.high_label = QLabel("高度")
        self.high_label_value = QLabel('0')
        self.high_slider = QSlider(Qt.Horizontal, self)
        self.high_slider.setMaximum(100)
        self.high_slider.setMinimum(-100)
        self.high_slider.setValue(0)
        self.high_slider.valueChanged[int].connect(self.changeImage)
        self.width_label = QLabel("宽度")
        self.width_label_value = QLabel('0')
        self.width_slider = QSlider(Qt.Horizontal, self)
        self.width_slider.setMaximum(100)
        self.width_slider.setMinimum(-100)
        self.width_slider.setValue(0)
        self.width_slider.valueChanged[int].connect(self.changeImage)
        self.rotation_label = QLabel("角度")
        self.rotation_label_value = QLabel('0')
        self.rotation_slider = QSlider(Qt.Horizontal, self)
        self.rotation_slider.setMaximum(180)
        self.rotation_slider.setMinimum(-180)
        self.rotation_slider.setValue(0)
        self.rotation_slider.valueChanged[int].connect(self.changeImage)

        self.reset_button = QPushButton("重置亮度")
        self.reset_button.clicked.connect(self.reset)
        self.bind_button = QPushButton("重置大小")
        self.bind_button.clicked.connect(self.resize)
        self.rerotation_button = QPushButton("重置角度")
        self.rerotation_button.clicked.connect(self.rerotation)
        self.watermark_button = QPushButton("添加水印")
        self.watermark_button.clicked.connect(self.add_watermark)
        # self.sure_button = QPushButton("确认调整")
        # self.sure_button.clicked.connect(self.toadjust)

        hbox1 = QHBoxLayout()
        hbox1.addWidget(self.bright_label)
        hbox1.addWidget(self.bright_label_value)
        hbox2 = QHBoxLayout()
        hbox2.addWidget(self.high_label)
        hbox2.addWidget(self.high_label_value)
        hbox3 = QHBoxLayout()
        hbox3.addWidget(self.width_label)
        hbox3.addWidget(self.width_label_value)
        hbox4 = QHBoxLayout()
        hbox4.addWidget(self.rotation_label)
        hbox4.addWidget(self.rotation_label_value)
        hbox5 = QHBoxLayout()
        hbox5.addStretch()
        hbox5.addWidget(self.reset_button)
        hbox5.addStretch()
        hbox5.addWidget(self.bind_button)
        hbox5.addStretch()
        hbox5.addWidget(self.rerotation_button)
        hbox5.addStretch()
        hbox5.addWidget(self.watermark_button)
        hbox5.addStretch()
        # hbox5.addWidget(self.sure_button)
        # hbox5.addStretch()
        vbox = QVBoxLayout()
        vbox.addLayout(hbox1)
        vbox.addWidget(self.bright_slider)
        vbox.addLayout(hbox2)
        vbox.addWidget(self.high_slider)
        vbox.addLayout(hbox3)
        vbox.addWidget(self.width_slider)
        vbox.addLayout(hbox4)
        vbox.addWidget(self.rotation_slider)
        vbox.addLayout(hbox5)

        self.setLayout(vbox)

    def changeImage(self, value):
        image = Variable.get_image()

        source = self.sender()
        if source == self.bright_slider:
            self.bright_label_value.setText(str(value))
            bright = (self.bright_slider.value() + 100) / 100
            process.change_bright(bright)
        elif source == self.high_slider:
            self.high_label_value.setText(str(value))
            high = self.high_slider.value()
            process.change_height(high)
        elif source == self.width_slider:
            self.width_label_value.setText(str(value))
            width = self.width_slider.value()
            process.change_width(width)
        elif source == self.rotation_slider:
            self.rotation_label_value.setText(str(value))

        process.process_photo(image)
        # imagelabel = Variable.get_imagelabel()
        # qimg = ImageQt(image)
        # img_pix = QPixmap.fromImage(qimg, Qt.AutoColor)
        # img_pix = img_pix.scaled(Variable.get_width(), Variable.get_height())
        # imagelabel.setPixmap(img_pix)

    def reset(self):
        self.bright_slider.setValue(0)

    def resize(self):
        self.width_slider.setValue(0)
        self.high_slider.setValue(0)

    def rerotation(self):
        self.rotation_slider.setValue(0)

    def add_watermark(self):
        image = Variable.get_image()
        process.change_watermark()
        if process.get_watermark():
            self.watermark_button.setText("取消水印")
        else:
            self.watermark_button.setText("添加水印")
