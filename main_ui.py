import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QFileDialog
from PySide6.QtGui import QIcon, QImage, QPixmap
from PySide6.QtCore import Qt, Slot, QPropertyAnimation, QEasingCurve, QEvent, QObject, QThread, Signal
from ui.Ui_main import Ui_MainWindow

import nibabel as nib
import numpy as np
import os
import time

from util import Util
from predict import Predictor


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


# 特征提取线程
class ExtractThread(QThread):
    signal = Signal(np.ndarray)
    
    
    def __init__(self, predictor: Predictor):
        super().__init__()
        self.predictor = predictor
    
    def run(self):
        if isinstance(self.nii_img, np.ndarray):
            vector = self.predictor.extract(self.nii_img)
            # 模拟耗时
            time.sleep(2)
            self.signal.emit(vector)
        else:
            # 无图像返回零
            self.signal.emit(np.ones(0))
            
    
    # 设置需要提取的图像
    def set_img(self, nii_img):
        self.nii_img = nii_img


class MainWindow(QMainWindow):
    settingOpen = False
    infoOpen = False
    lastest_dir = '.'
    img_name = ''
    nii_img = None
    
    def __init__(self):
        # 初始化
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        self.predictor = Predictor()
        
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
        self.ui.saveButton.clicked.connect(self.save_vector)
        
        self.ui.extract_condition_label.setVisible(False)
        self.ui.start_extract_button.setVisible(False)
        self.ui.saveButton.setVisible(False)
        self.extract_thread = ExtractThread(self.predictor)
        self.extract_thread.signal.connect(self.get_vector)
        self.ui.start_extract_button.clicked.connect(self.start_extract)
        
        self.ui.spinBox_x.valueChanged.connect(self.refresh_pixmap)
        self.ui.spinBox_y.valueChanged.connect(self.refresh_pixmap)
        self.ui.spinBox_z.valueChanged.connect(self.refresh_pixmap)
        
        self.ui.label_name.setText("未选择")
        self.ui.label_x_range.setText("")
        self.ui.label_y_range.setText("")
        self.ui.label_z_range.setText("")
        
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
            self.img_name = os.path.basename(img_path)
            
            self.ui.label_name.setText(Util.add_wrap_to_str(self.img_name))
            
            nii_img = nib.load(img_path).get_fdata()
            self.nii_img = nii_img
            
            x, y, z = Util.from_3d_img_get_central_xyz(nii_img)
            
            # 初始化spinbox
            self.ui.spinBox_x.setMaximum(nii_img.shape[0])
            self.ui.spinBox_y.setMaximum(nii_img.shape[1])
            self.ui.spinBox_z.setMaximum(nii_img.shape[2])
            self.ui.spinBox_x.setValue(x + 1)
            self.ui.spinBox_y.setValue(y + 1)
            self.ui.spinBox_z.setValue(z + 1)
            self.ui.label_x_range.setText(f"(1~{nii_img.shape[0]})")
            self.ui.label_y_range.setText(f"(1~{nii_img.shape[1]})")
            self.ui.label_z_range.setText(f"(1~{nii_img.shape[2]})")
            self.refresh_pixmap()
            
            self.ui.start_extract_button.setVisible(True)

            
    @Slot()
    def refresh_pixmap(self):
        if isinstance(self.nii_img, np.ndarray):
            saggital_pixmap, coronal_pixmap, axial_pixmap = Util.from_3d_img_get_pixmap(self.nii_img, self.ui.spinBox_x.value() - 1, self.ui.spinBox_y.value() - 1, self.ui.spinBox_z.value() - 1)
            self.ui.saggitalLabel.setPixmap(saggital_pixmap)
            self.ui.coronalLabel.setPixmap(coronal_pixmap)
            self.ui.axialLabel.setPixmap(axial_pixmap)
        print("refresh")
            
    
    @Slot()
    def save_vector(self):
        fileName, fileType = QFileDialog.getSaveFileName(self, "保存特征数据", os.path.join(self.lastest_dir, self.img_name[:self.img_name.find('.')]), "特征文件 (*.vector)")
        if fileName and isinstance(self.vector, np.ndarray):
            Util.save_file(self.vector, fileName)
        
        
    @Slot()
    def start_extract(self):
        print("start extract")
        self.ui.start_extract_button.setEnabled(False)
        self.ui.selectButton.setEnabled(False)
        self.ui.saveButton.setVisible(False)
        self.ui.extract_condition_label.setText("提取中...")
        self.ui.extract_condition_label.setVisible(True)
        self.extract_thread.set_img(self.nii_img)
        self.extract_thread.start()

    
    @Slot(np.ndarray)
    def get_vector(self, vector):
        print("finish extract")
        if vector.shape[0] != 0:
            self.vector = vector
            self.ui.start_extract_button.setEnabled(True)
            self.ui.selectButton.setEnabled(True)
            self.ui.extract_condition_label.setText("提取完成")
            self.ui.saveButton.setVisible(True)
        else:
            self.ui.start_extract_button.setEnabled(True)
            self.ui.selectButton.setEnabled(True)
            self.ui.extract_condition_label.setText("未加载图像")
        

if __name__ == "__main__":
    sys.argv += ['-platform', 'windows:darkmode=2']
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon("./ui/icon.ico"))
    window = MainWindow()
    window.show()

    sys.exit(app.exec())