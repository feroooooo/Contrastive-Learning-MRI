import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QFileDialog
from PySide6.QtGui import QIcon, QImage, QPixmap
from PySide6.QtCore import Qt, Slot, QPropertyAnimation, QEasingCurve, QEvent, QObject
from ui.Ui_main import Ui_MainWindow

import nibabel as nib
import numpy as np
import os

from util import Util


class EventFilter(QObject):
    group = {}
    selected = 'extract'
    page = {}
    
    def set_group(self, group):
        self.group = group
        
    
    def set_page(self, page):
        self.page = page
    
        
    def set_stackedWidget(self, widget):
        self.stackedWidget = widget
    
    
    # 事件过滤器
    def eventFilter(self, watched: QObject, event: QEvent) -> bool:
        if event.type() in [QEvent.Enter, QEvent.Leave, QEvent.MouseButtonPress, QEvent.MouseButtonRelease]:
            group_name = ''
            for item in self.group:
                if watched in self.group[item]:
                    widgets = self.group[item]
                    # 若当前选择对象为此对象，不进行处理
                    if self.selected == item:
                        return super().eventFilter(watched, event)
                    group_name = item
                    break
        
        if event.type() == QEvent.Enter:
            for item in widgets:
                item.setStyleSheet("background-color:#464646;")
        if event.type() == QEvent.Leave:
            for item in widgets:
                item.setStyleSheet("")
        if event.type() == QEvent.MouseButtonPress:
            for item in widgets:
                item.setStyleSheet("background-color:#666666;")
        if event.type() == QEvent.MouseButtonRelease:
            self.selected = group_name
            for item in self.group:
                if group_name == item:
                    for widget in self.group[item]:
                        widget.setStyleSheet("background-color:#464646;")
                else:
                    for widget in self.group[item]:
                        widget.setStyleSheet("")
            self.stackedWidget.setCurrentWidget(self.page[group_name])
        return super().eventFilter(watched, event)

class MainWindow(QMainWindow):
    settingOpen = False
    infoOpen = False
    lastest_dir = '.'
    
    def __init__(self):
        # 初始化
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        # 关闭设置界面
        self.ui.extraFrame.setMaximumSize(0, 16777215)
        # 设置按钮
        self.ui.settingButton.clicked.connect(self.switch_setting)
        
        # 关闭信息界面
        self.ui.infoFrame.setMaximumSize(0, 16777215)
        # 信息按钮
        self.ui.infoButton.clicked.connect(self.switch_info)
        
        # 设置界面按钮
        self.ui.stackedWidget.setCurrentWidget(self.ui.extractPage)
        group = {"extract":[self.ui.extractButton, self.ui.extractLabel], "classification":[self.ui.classificationButton, self.ui.classificationLabel], "hint":[self.ui.hintButton, self.ui.hintLabel]}
        page = {"extract":self.ui.extractPage, "classification":self.ui.classificationPage, "hint":self.ui.hintPage}
        self.eventFilter = EventFilter()
        self.eventFilter.set_page(page)
        self.eventFilter.set_group(group)
        self.eventFilter.set_stackedWidget(self.ui.stackedWidget)
        
        # 特征提取界面
        self.ui.selectButton.clicked.connect(self.select_file)
        
        for item in group:
            for widget in group[item]:
                widget.installEventFilter(self.eventFilter)
    
    
    # 切换设置界面
    @Slot()
    def switch_setting(self):
        if self.settingOpen:
            self.animation = QPropertyAnimation(self.ui.extraFrame, b"maximumWidth")
            self.animation.setDuration(300)
            self.animation.setStartValue(240)
            self.animation.setEndValue(0)
            self.animation.setEasingCurve(QEasingCurve.InOutQuart)
            self.animation.start()
        else:
            self.animation = QPropertyAnimation(self.ui.extraFrame, b"maximumWidth")
            self.animation.setDuration(300)
            self.animation.setStartValue(0)
            self.animation.setEndValue(240)
            self.animation.setEasingCurve(QEasingCurve.InOutQuart)
            self.animation.start()
        self.settingOpen = not self.settingOpen
        
    
    # 切换信息界面
    @Slot()
    def switch_info(self):
        if self.infoOpen:
            self.animation = QPropertyAnimation(self.ui.infoFrame, b"maximumWidth")
            self.animation.setDuration(300)
            self.animation.setStartValue(100)
            self.animation.setEndValue(0)
            self.animation.setEasingCurve(QEasingCurve.InOutQuart)
            self.animation.start()
        else:
            self.animation = QPropertyAnimation(self.ui.infoFrame, b"maximumWidth")
            self.animation.setDuration(300)
            self.animation.setStartValue(0)
            self.animation.setEndValue(100)
            self.animation.setEasingCurve(QEasingCurve.InOutQuart)
            self.animation.start()
        self.infoOpen = not self.infoOpen
        
        
    @Slot()
    def select_file(self):
        img_path, _ = QFileDialog.getOpenFileName(self, "选择脑结构磁共振图像", self.lastest_dir, "MRI (*.nii *.gz)")
        if img_path:
            self.lastest_dir = os.path.dirname(img_path)
            
            nii_img = nib.load(img_path).get_fdata()
            x, y, z = Util.from_3d_img_get_central_xyz(nii_img)
            saggital_pixmap, coronal_pixmap, axial_pixmap = Util.from_3d_img_get_pixmap(nii_img, x, y, z)
            self.ui.saggitalLabel.setPixmap(saggital_pixmap)
            self.ui.coronalLabel.setPixmap(coronal_pixmap)
            self.ui.axialLabel.setPixmap(axial_pixmap)

if __name__ == "__main__":
    sys.argv += ['-platform', 'windows:darkmode=2']
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon("./ui/icon.ico"))
    window = MainWindow()
    window.show()

    sys.exit(app.exec())