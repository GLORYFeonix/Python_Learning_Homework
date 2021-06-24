from PyQt5.QtWidgets import QWidget, QLabel, QSlider, QPushButton, QHBoxLayout, QVBoxLayout

from ProcessPhoto import *

image = Variable.get_image()
imageLabel = Variable.get_imagelabel()
process = Process()


class AdjustTab(QWidget):
    # 自定义的控件
    def __init__(self):
        # 初始化界面
        super().__init__()
        # 加入亮度调整部分
        self.bright_label = QLabel("亮度")  # 显示内容，下同
        self.bright_label_value = QLabel('0')   # 显示数值，下同
        self.bright_slider = QSlider(Qt.Horizontal, self)   # 加入滑动条，下同
        # 设置滑动条最大最小值，下同
        self.bright_slider.setMaximum(100)
        self.bright_slider.setMinimum(-100)
        self.bright_slider.setValue(0)  # 设置滑动条初始值，下同
        self.bright_slider.valueChanged[int].connect(
            self.changeImage)  # 连接参数变更事件，下同
        # 加入高度调整部分
        self.high_label = QLabel("高度")
        self.high_label_value = QLabel('0')
        self.high_slider = QSlider(Qt.Horizontal, self)
        self.high_slider.setMaximum(100)
        self.high_slider.setMinimum(-100)
        self.high_slider.setValue(0)
        self.high_slider.valueChanged[int].connect(self.changeImage)
        # 加入宽度调整部分
        self.width_label = QLabel("宽度")
        self.width_label_value = QLabel('0')
        self.width_slider = QSlider(Qt.Horizontal, self)
        self.width_slider.setMaximum(100)
        self.width_slider.setMinimum(-100)
        self.width_slider.setValue(0)
        self.width_slider.valueChanged[int].connect(self.changeImage)
        # 加入角度调整部分
        self.rotation_label = QLabel("角度")
        self.rotation_label_value = QLabel('0')
        self.rotation_slider = QSlider(Qt.Horizontal, self)
        self.rotation_slider.setMaximum(180)
        self.rotation_slider.setMinimum(-180)
        self.rotation_slider.setValue(0)
        self.rotation_slider.valueChanged[int].connect(self.changeImage)
        # 加入重置部分
        self.reset_button = QPushButton("重置亮度")  # 加入重置亮度按钮
        self.reset_button.clicked.connect(self.reset)   # 连接重置亮度事件
        self.bind_button = QPushButton("重置大小")  # 加入重置大小按钮
        self.bind_button.clicked.connect(self.resize)   # 连接重置大小事件
        self.rerotation_button = QPushButton("重置角度")    # 加入重置角度按钮
        self.rerotation_button.clicked.connect(self.rerotation)  # 连接重置角度事件
        self.watermark_button = QPushButton("添加水印")  # 加入添加水印按钮
        self.watermark_button.clicked.connect(self.add_watermark)   # 加入添加水印事件

        # 款式布局
        # 水平部分
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
        # 垂直部分
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
        # 改变参数事件
        # 从全局变量中获取image进行修改
        image = Variable.get_image()

        # 获取修改参数
        source = self.sender()  # 判断修改参数来源，获取具体修改内容
        if source == self.bright_slider:
            # 修改亮度
            self.bright_label_value.setText(str(value))  # 改变显示的值，下同
            bright = (self.bright_slider.value() + 100) / 100   # 获取参数，下同
            process.change_bright(bright)   # 改变图片相应属性值，下同
        elif source == self.high_slider:
            # 修改高度
            self.high_label_value.setText(str(value))
            high = self.high_slider.value()
            process.change_height(high)
        elif source == self.width_slider:
            # 修改宽度
            self.width_label_value.setText(str(value))
            width = self.width_slider.value()
            process.change_width(width)
        elif source == self.rotation_slider:
            # 修改角度
            self.rotation_label_value.setText(str(value))
            angle = self.rotation_slider.value()
            process.change_angle(angle)

        # 应用修改
        process.process_photo(image)

    def reset(self):
        # 重置亮度事件
        self.bright_slider.setValue(0)  # 将相关值设置为初始值0，下同

    def resize(self):
        # 重置大小事件
        self.width_slider.setValue(0)
        self.high_slider.setValue(0)

    def rerotation(self):
        # 重置角度事件
        self.rotation_slider.setValue(0)

    def add_watermark(self):
        # 添加水印事件
        image = Variable.get_image()
        process.change_watermark()  # 改变水印标志
        process.process_photo(image)    # 应用修改

        # 修改按钮显示内容
        if process.get_watermark():
            self.watermark_button.setText("取消水印")
        else:
            self.watermark_button.setText("添加水印")
