import sys

from PIL import Image
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QTabWidget, QMainWindow, QAction, QFileDialog, QMessageBox, QMenu, QDesktopWidget, \
    QApplication

from Widget_self import *


class MyTab(QTabWidget):
    def __init__(self, parent):
        super().__init__()
        self.parent = parent

        # 添加自定义组件
        self.adjust_tab = AdjustTab()
        self.addTab(self.adjust_tab, "调整参数")    # 设置其显示名称
        self.setMaximumHeight(300)      # 设置其最大高度


class PS(QMainWindow):

    def __init__(self):
        super().__init__()

        self.initUI()   # 初始化界面

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

    def center(self):
        # 设置屏幕居中
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = PS()
    sys.exit(app.exec_())
