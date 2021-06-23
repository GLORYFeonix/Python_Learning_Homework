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

        self.adjust_tab = AdjustTab()

        self.addTab(self.adjust_tab, "调整参数")

        self.setMaximumHeight(300)


class PS(QMainWindow):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        # 设置状态栏
        self.statusbar = self.statusBar()
        self.statusbar.showMessage('Ready')
        # 设置菜单栏
        openAct = QAction('打开', self)
        openAct.setShortcut('Ctrl+O')
        openAct.setStatusTip('打开文件')
        openAct.triggered.connect(self.openImage)
        saveAct = QAction('保存', self)
        saveAct.setShortcut('Ctrl+S')
        saveAct.setStatusTip('保存文件')
        saveAct.triggered.connect(self.SaveEvent)
        exitAct = QAction('退出', self)
        exitAct.setShortcut('Ctrl+E')
        exitAct.setStatusTip('退出软件')
        exitAct.triggered.connect(self.close)
        menubar = self.menuBar()
        fileMenu = menubar.addMenu('文件')
        fileMenu.addAction(openAct)
        fileMenu.addAction(saveAct)
        fileMenu.addAction(exitAct)

        # layout
        imagelabel = QLabel("")
        Variable.set_imagelabel(imagelabel)
        imagelabel.setAlignment(Qt.AlignCenter)
        vbox = QVBoxLayout()
        self.mytab = MyTab(self)
        vbox.addWidget(imagelabel)
        vbox.addWidget(self.mytab)

        main_frame = QWidget()
        main_frame.setLayout(vbox)
        self.setCentralWidget(main_frame)
        # 窗口设置
        self.resize(Variable.WINDOW_WIDTH, Variable.WINDOW_HEIGHT)
        self.center()
        self.setWindowTitle('简易PS')
        self.setWindowIcon(QIcon('ps.ico'))
        self.show()

    def openImage(self):
        # 打开文件
        imagelabel = Variable.get_imagelabel()

        fname, _ = QFileDialog.getOpenFileName(self, '打开图片',
                                               'C:\\Users\\gzy88\\Desktop\\Python_Learning_Homework\\Photo Wall\\photo',
                                               "Image files ("
                                               "*.jpg *.png)")
        if fname:
            image = Image.open(fname)
            Variable.set_image(image)

            self.mytab.adjust_tab.reset()
            self.mytab.adjust_tab.resize()
            self.mytab.adjust_tab.rerotation()

            qimg = ImageQt(image)
            img_pix = QPixmap.fromImage(qimg, Qt.AutoColor)
            img_pix = img_pix.scaled(
                Variable.DEFAULT_WIDTH, Variable.DEFAULT_HEIGHT, Qt.KeepAspectRatio)
            Variable.set_width(img_pix.width())
            Variable.set_height(img_pix.height())
            imagelabel.setPixmap(img_pix)
        else:
            pass

    def closeEvent(self, event):
        reply = QMessageBox.question(self, '温馨提示',
                                     "你确定要退出吗？", QMessageBox.Yes |
                                     QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

    def SaveEvent(self):
        # image = Variable.get_image()
        filename, _ = QFileDialog.getSaveFileName(
            self, "文件保存", 'c:\\', "Image files (*.jpg *.png)")
        # img_save = Process.process_photo(image)
        # img_save.save(filename)
        if filename:
            # image.save(filename)
            # Variable.
            print("save")
        else:
            pass

    def contextMenuEvent(self, event):

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
