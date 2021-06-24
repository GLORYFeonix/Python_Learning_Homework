# Python程序设计 作业

1. 海龟绘图
2. 文本处理
3. [数字照片墙](https://blog.csdn.net/u013748897/article/details/117996577)
4. [送你一首集句诗](https://blog.csdn.net/u013748897/article/details/118028280)
5. [简化的PS](https://blog.csdn.net/u013748897/article/details/118147738)

@[TOC](Python程序设计 大作业 简化的PS)

# 摘要
_完成简易PS的实现，通过编写GUI界面，与用户进行交互，实现显示图片，调整图片亮度，缩放和旋转图片，添加水印等功能。GUI界面的实现，通过PyQt5来进行编写，对于图像的处理，则通过Pillow库对其进行处理，完成所需要的各项功能。布局采用上下格式，用QLabel来存放图片，之后下面用自己定义的Tab组件来实现各种操作，另外添加菜单栏进行文件的操作，如打开和保存、关闭等。_
</br>
</br>
_关键字：Python; Photoshop; PyQt5; Pillow; GUI_
_代码行数：431行_

# 1.	项目背景和意义
## 1.1	项目背景
随着时代的发展，人们对于修图的需求越来越大，在生活中随处可见处理过的图片，原模原样的图片已经很少见了，在基本的手机自带的相机中，都有着一大堆对于图像进行处理的功能。在学习完本学期的Python课程之后，我对GUI界面编程十分感兴趣，所以打算用PyQt5结合Pillow库，制作一个简单的修图软件。
## 1.2	意义
通过搭建基本的软件GUI界面，和对Pillow库的使用，增强了我的编程能力。在项目开始之前，我对于PyQt5的GUI搭建和Pillow库还不是很了解，需要上网寻找资料，进行自学。这锻炼了我们收集信息的能力。在编程过程中，难免会出现一个又一个的bug，这时候就需要自己进行程序的调试。但有的时候是自己对于程序背后的理解有误，例如对于信号传递机制的理解不够到位等。在不断的处理bug的过程中，增强了我解决问题的能力。遇到问题，不断克服问题。看着一个项目从无到有，被自己一点点的构建起来，这极大的增强了我编程的自信和能力。经过此次开发，我对于项目开发的基本流程有了一定的了解，不再是盲目的开发，想到哪里就写哪里。而是在开始就对程序进行拆分，分成不同的部分，一步一步地分开进行实现。先实现最基本的一部分功能，之后为其添砖加瓦。先实现可用的软件，再继续实现其他。并在程序中注意响应变化，为未来程序的扩展进行准备。在真正的项目中，需求也是在一直变化的，所以我们要注意响应的变化。

# 2. 需求分析
## 2.1	基本的主界面的分析
主界面主要是由一个`QLabel`标签和一个自定义的组件（继承于`QTabWidget`）来实现，主窗口继承于`QMainWindow`，`QLabel`用于显示图片的处理结果，`QTabWidget`用来存放对于图片的操作的选项，如调整大小和添加水印等。主页面继承于`QMainWidget`，可以实现对应的菜单栏和状态栏，来实现打开图片和保存图片等功能。
## 2.2	对于图片的各个参数的调整
用四个`QSlider`来实现对于照片的亮度，长宽和旋转角度的调整。为了让调节的参数更加的直观可见，加入`QLabel`来实现对`QSlier`数值的显示。可设置`QSlider`的范围为-100到100，这样就既可以使参数正向增加也可以负向减少了。对于图像的各个参数，直接传入这样的值是显然不行的，要通过一些基础的方法，来进行数值的转换，转成图片可以接受的参数。其中，亮度可以使用`Pillow. ImageEnhance`模块进行操作。大小可以使用`PyQt5.QtGui`的`QPixmap.resize()`进行操作。旋转可以使用`Pillow`的`Image.rotate()`进行操作。在调节过程中，难免会有调错，想要重新复原的需求。为了避免手动调整参数到初始值这种繁杂的操作，因此加入了3个重置按钮来重置照片的各个参数。在打开图片之前，同样需要调用这三个重置方法来实现各个数值和`QSlider`的复位。
## 2.3	水印
要实现图片的添加水印的功能，添加一个按钮来进行水印的添加和去除。使用`Pillow.ImageDraw`模块在图片的左上角添加一个“Watermark”的字样作为水印。并在添加之后，让按钮的显示内容变为“去除水印”，用于去除水印，来灵活地实现水印的添加和去除。

# 3.	概要和详细设计
## 3.1	代码总框图
![代码总框架](https://img-blog.csdnimg.cn/20210624204104643.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3UwMTM3NDg4OTc=,size_16,color_FFFFFF,t_70#pic_center)
其中，`Photoshop.py`是软件主体窗体，以及执行部分，`Widget_self.py`是自定义控件部分，`Variabel.py`是全局变量与常量部分，`ProcessPhoto.py`是图片处理方法部分。
## 3.2	各部分框图
### 3.2.1	菜单栏以及其三个事件
![菜单栏以及其三个事件](https://img-blog.csdnimg.cn/20210624204438288.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3UwMTM3NDg4OTc=,size_16,color_FFFFFF,t_70#pic_center)
### 3.2.2	调整图片的各个参数
![调整图片的各个参数](https://img-blog.csdnimg.cn/20210624204510911.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3UwMTM3NDg4OTc=,size_16,color_FFFFFF,t_70#pic_center)
### 3.2.3	水印
![水印](https://img-blog.csdnimg.cn/20210624204541449.png#pic_center)
### 3.2.4	全局变量与常量
![全局变量与常量](https://img-blog.csdnimg.cn/20210624204611237.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3UwMTM3NDg4OTc=,size_16,color_FFFFFF,t_70#pic_center)
### 3.2.5	处理图片的Process类
![处理图片的Process类](https://img-blog.csdnimg.cn/20210624204644230.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3UwMTM3NDg4OTc=,size_16,color_FFFFFF,t_70#pic_center)
# 4.	代码实现
## 4.1	python版本以及库版本说明
`Python`: 3.9.5 64-bit
`PyQt5`: 5.15.4
`PyQt5-stubs`: 5.15.2.0
`PyQt5-sip`: 12.9.0
`PyQt5-Qt5`: 5.15.2
`Pillow`: 8.2.0

## 4.2	所使用的关键库
### 4.2.1 PyQt5
版本5.15.4，是主要的搭建界面所用的库，完成整个界面的搭建，在整个实验过程中使用了其中的多个组件，并完成事件的响应，响应鼠标的各种点击事件。
### 4.2.2 Pillow
版本8.2.0，`Pillow`是`python`自带的处理图片的库，整个过程中的图片处理都通过这个库来实现，包括调整大小，水印滤镜等功能。
### 4.2.3 Sys
保证程序的正常运行所调用的库。
## 4.3	各个文件的说明
### 4.3.1 Photoshop.py
主要的程序文件，进行主要的界面搭建以及运行，这里是程序的入口文件。
### 4.3.2 Widget_self.py
在该文件中，主要进行自定义组件，包括调整图片参数的`QSlider`，显示`QSlider`数值的`QLabel`，进行重置功能和加水印功能的`QButton`。并为每个组件链接响应事件的函数，来完成对于图片的不同处理。
### 4.3.3 Variable.py
用于存放在整个程序中用到的全局变量，各种常量，并为每种全局变量提供`.get()`和`.set()`方法，用于得到和设置全局变量。各种常量用于规定窗口的大小等。如果将来需求发生变化，需要改变初始窗口的大小，可以直接在这个文件中进行改变，增强了软件响应变化的能力。
### 4.3.4 ProcessPhoto.py
对图片进行处理的文件，每一次对图片进行处理，都需要进行调用其中的函数，包括改变亮度、调整大小、旋转图片和添加水印。并提供改变的接口，方便其他`python`文件进行调用。
## 4.4	关键代码说明
### 4.4.1	Photoshop.py
#### (1)	初始化自定义组件

```python
class MyTab(QTabWidget):
    def __init__(self, parent):
        super().__init__()
        self.parent = parent

        # 添加自定义组件
        self.adjust_tab = AdjustTab()
        self.addTab(self.adjust_tab, "调整参数")    # 设置其显示名称
        self.setMaximumHeight(300)      # 设置其最大高度
```
说明：自定义组件`MyTab`的实现，继承于`QTabWidget`类，为其添加了一个Tab用于操作图片。
#### (2)	初始化软件主窗口

```python
    def initUI(self):
        # 初始化界面
        # 设置状态栏
        self.statusbar = self.statusBar()
        self.statusbar.showMessage('Ready')
        # 设置菜单栏
        # 新建打开动作
        openAct = QAction('打开', self)  # 打开动作
        openAct.setShortcut('Ctrl+O')   # 打开快捷键
        openAct.setStatusTip('打开文件')    # 打开提示
        openAct.triggered.connect(self.openImage)   # 连接打开事件
        # 新建保存动作
        saveAct = QAction('保存', self)  # 保存动作
        saveAct.setShortcut('Ctrl+S')   # 保存快捷键
        saveAct.setStatusTip('保存文件')    # 保存提示
        saveAct.triggered.connect(self.SaveEvent)   # 连接保存事件
        # 新建退出动作
        exitAct = QAction('退出', self)  # 退出动作
        exitAct.setShortcut('Ctrl+E')   # 退出快捷键
        exitAct.setStatusTip('退出软件')    # 退出提示
        exitAct.triggered.connect(self.close)   # 连接退出事件

        # 新建一个菜单栏
        menubar = self.menuBar()
        fileMenu = menubar.addMenu('文件')  # 设置菜单栏显示的内容
        # 加入上述三个事件
        fileMenu.addAction(openAct)
        fileMenu.addAction(saveAct)
        fileMenu.addAction(exitAct)

        # 布局
        # 图片显示部分
        imagelabel = QLabel("")  # 使用QLabel来显示图片
        Variable.set_imagelabel(imagelabel)  # 将QLabel放置到全局变量
        imagelabel.setAlignment(Qt.AlignCenter)  # 中心对齐

        # 修改操作部分
        self.mytab = MyTab(self)    # 使用自定义控件来进行操作

        # 设置框垂直布局
        vbox = QVBoxLayout()
        vbox.addWidget(imagelabel)
        vbox.addWidget(self.mytab)
        # 将布局页面设置到主窗口中间
        main_frame = QWidget()
        main_frame.setLayout(vbox)
        self.setCentralWidget(main_frame)

        # 窗口设置
        self.resize(Variable.WINDOW_WIDTH, Variable.WINDOW_HEIGHT)  # 调整大小
        self.center()   # 让窗口出现在屏幕中间
        self.setWindowTitle('简易PS')   # 窗口标题
        self.setWindowIcon(QIcon('Mini Photoshop/ps.ico'))  # 窗口图标
        self.show()  # 呈现窗口
```
说明：实现GUI组件的摆放，并添加菜单栏和状态栏，并为这些东西添加Action，并将其绑定到对应的函数上。
#### (3)	打开文件的方法

```python
    def openImage(self):
        # 打开文件事件
        imagelabel = Variable.get_imagelabel()  # 从全局变量中获取QLabel

        fname, _ = QFileDialog.getOpenFileName(
            self, '打开图片', '/', "Image files (*.jpg *.png)")  # 打开对话框来进行文件选择，获得文件路径

        if fname:   # 防止文件路径为空导致错误，设置一个条件来判断是否执行，之后的其他事件与此相同
            image = Image.open(fname)   # 使用Pillow库来打开文件
            Variable.set_image(image)   # 将其保存到全局变量

            # 将几个操作参数复位
            self.mytab.adjust_tab.reset()
            self.mytab.adjust_tab.resize()
            self.mytab.adjust_tab.rerotation()

            # 呈现图片
            qimg = ImageQt(image)   # 先将Image转成QImage
            img_pix = QPixmap.fromImage(
                qimg, Qt.AutoColor)  # 再从QImage转成QPixmap
            img_pix = img_pix.scaled(
                Variable.DEFAULT_WIDTH, Variable.DEFAULT_HEIGHT, Qt.KeepAspectRatio)    # 将QPixmap按图片比例调整大小至可放入QLabel
            imagelabel.setPixmap(img_pix)   # 放入QLabel
            # 将此时的长宽存入全局变量
            Variable.set_width(img_pix.width())
            Variable.set_height(img_pix.height())
            # 记录图片的现时大小（注：之前只是修改了QPixmap的大小，这里指的是记录图片的目前大小，方便之后复用）
            process.change_width(0)
            process.change_height(0)
        else:
            pass
```
说明：该函数用于打开图片，当用户点击打开时，就会调用这个函数，用`QFileDialog.getOpenFileName`来获得图片的路径，之后调用`Pillow`来打开图片，同时更改用来存储图片的全局变量。为了保证多次打开之间不会相互影响，在每次打开图片之后，调用各个组件的重置函数。
#### (4)	保存文件的方法

```python
    def SaveEvent(self):
        # 保存文件事件
        filename, _ = QFileDialog.getSaveFileName(
            self, "文件保存", '/', "Image files (*.jpg *.png)")
        if filename:
            image = Variable.get_image()    # 获取全局变量中的image进行操作
            process.change_save(filename)   # 改变保存标志
            process.process_photo(image)    # 保存文件
        else:
            pass
```
说明：该函数用来响应保存事件，获得保存路径之后，改变保存标识，调用`process_photo()`方法进行保存。
#### (5)	关闭软件的方法

```python
    def closeEvent(self, event):
        # 关闭软件事件
        reply = QMessageBox.question(self, '温馨提示',
                                     "你确定要退出吗？", QMessageBox.Yes |
                                     QMessageBox.No, QMessageBox.No)    # 关闭弹出确认框

        # 确认框的响应事件
        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()
```
说明：该函数用来响应窗口关闭事件，询问是否退出程序。
#### (6)	设置菜单的功能

```python
    def contextMenuEvent(self, event):
        # 菜单内容
        cmenu = QMenu(self)

        opnAct = cmenu.addAction("打开")
        saveAct = cmenu.addAction("保存")
        action = cmenu.exec_(self.mapToGlobal(event.pos()))

        if action == opnAct:
            self.openImage()
        if action == saveAct:
            self.SaveEvent()
```
说明：用来响应用户在界面上的鼠标右击事件，显示一个菜单，可以进行图片的打开和保存。
### 4.4.2	Widget_self.py
#### (1)	初始化自定义组件的界面和链接各个部件的功能

```python
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
```
说明：实现GUI组件的摆放，并添加`QSlider`和`QLabel`还有`QButton`。为它们添加布局，并为这些东西添加Action，将其绑定到对应的函数上。
#### (2)	改变图片的事件

```python
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
```
说明：本部分响应`QSlider`的改变，通过使用`Process`中的`.change()`方法，来改变图片的属性值。最后通过`process_photo()`方法执行这些改变。
#### (3)	添加水印事件

```python
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
```
说明：本部分响应“增加水印”的`QButton`的响应，通过使用`Process`中的`.change()`方法改变水印标识，再通过`process_photo()`方法执行改变。最后还需将`QButton`的内容进行更改。
#### (4)	复位事件

```python
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
```
说明：本部分包括三个`QSlider`的复位事件，响应的是三个`QButton`的点击事件，以及图片打开事件。
### 4.4.3	ProcessPhoto.py
#### (1)	定义一个类来存储图片属性

```python
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
```
说明：定义`Process`类，专门用于对图像进行处理。因为如果只在其他地方对于图像进行处理，则会导致不同的属性处理的时候，另一属性的处理效果就会消失。所以要进行整体的封装，要将图片的各个属性进行封装，每次进行整体的处理。
#### (2)	改变图片属性值的相关函数

```python
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
```
说明：完成对于图片的不同属性的更改，方便之后进行处理
#### (3)	Process_photo()函数

```python
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
```
说明：对于图像的处理函数，由于`Pillow`库自带的函数性质，可以每次从头进行图片的处理，以达到和GUI界面更好的契合。本函数主要是根据图片的各种参数、标识进行执行修改。
### 4.4.4	Variable.py
#### (1)	全局常量

```python
# 常量的定义
WINDOW_WIDTH = 1000
WINDOW_HEIGHT = 1000
DEFAULT_WIDTH = 800
DEFAULT_HEIGHT = 600
```
说明：对在整个程序中用到的常量进行定义
#### (2)	Variable类存储全局变量

```python
class Variable:
    # 全局变量
    image = None
    imagelabel = None
    width = 0
    height = 0


def set_width(value):
    Variable.width = value


def get_width():
    return Variable.width


def set_height(value):
    Variable.height = value


def get_height():
    return Variable.height


def set_image(image):
    Variable.image = image


def get_image():
    return Variable.image


def set_imagelabel(imagelabel):
    Variable.imagelabel = imagelabel


def get_imagelabel():
    return Variable.imagelabel
```
说明：保存用到的全局变量，并为其添加`.set()`和`.get()`函数用于设置和取得对应的全局变量的值。
# 5.	代码测试
## 5.1程序运行主界面
![程序运行主界面](https://img-blog.csdnimg.cn/20210624210331431.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3UwMTM3NDg4OTc=,size_16,color_FFFFFF,t_70)
## 5.2读取图片之后的界面
![读取图片之后的界面](https://img-blog.csdnimg.cn/2021062421044621.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3UwMTM3NDg4OTc=,size_16,color_FFFFFF,t_70)
## 5.3 使用各种操作调整图片
![使用各种操作调整图片](https://img-blog.csdnimg.cn/20210624210503306.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3UwMTM3NDg4OTc=,size_16,color_FFFFFF,t_70)
## 5.4 保存功能
![保存功能](https://img-blog.csdnimg.cn/2021062421053175.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3UwMTM3NDg4OTc=,size_16,color_FFFFFF,t_70)
## 5.5 重置功能和取消水印
本次使用了重置角度功能和取消水印功能
![重置角度功能和取消水印功能](https://img-blog.csdnimg.cn/20210624210553751.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3UwMTM3NDg4OTc=,size_16,color_FFFFFF,t_70)
## 5.6 退出功能
![退出功能](https://img-blog.csdnimg.cn/20210624210626479.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3UwMTM3NDg4OTc=,size_16,color_FFFFFF,t_70)
# 6.	结论与未来方向
## 6.1	结论
该项目完成了一些图片处理的基本功能，加深了我对于`PyQt5`和`Pillow`库的了解。看着一个项目从无到有，自己的编程信心有了很大的提升。并对开发流程及注意事项有了一定的了解。最令我深刻的体会是，在开发中，要尽量解耦合，时时刻刻准备相应变化，让自己的代码在应对不同的需求的时候可以尽量少的改动。
## 6.2	未来方向
虽然已经完成了大部分的功能，但仍然还有很大的扩展空间，例如滤镜、裁剪等功能，这样对于图片的操作更加的自由地实现对于图片的编辑。但由于时间精力原因无法做到更好，十分遗憾。
# 7.	致谢
感谢常同学的督促与激励。
# 8.	参考文献与链接
[1] [PyQt5 Reference Guide](https://www.riverbankcomputing.com/static/Docs/PyQt5/)
[2] [Pillow — Pillow (PIL Fork) 8.2.0 documentation](https://www.baidu.com/link?url=GcfQN3fUOddnL6zB2AIYUkssiK93ZZduqfUwyYclV6yoQrICSSykRgqgXY4eUAxr&wd=&eqid=a816220e0006db140000000360d47467)
[3] [PyQt5中文教程](http://code.py40.com/pyqt5/14.html)

# 9. 版本管理

本作业已上传至Github以及Gitee，希望各位能点个star再走 :smile:。

[GitHub](https://github.com/GLORYFeonix/Python_Learning_Homework)

[Gitee](https://gitee.com/gzy8810/Python_Learning_Homework)
