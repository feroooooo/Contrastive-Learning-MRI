import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QFileDialog, QMessageBox
from PySide6.QtGui import QIcon
from PySide6.QtCore import Slot, QPropertyAnimation, QEasingCurve, QEvent, QObject, QThread, Signal
from ui.Ui_main import Ui_MainWindow

import nibabel as nib
import numpy as np
import os
import json
import csv

from util import Util
from predict import Predictor


class EventFilter(QObject):
    group = {}
    selected = 'extract'
    page = {}
    extracted = False
    extracting = False
    classifing = False
    classified = False
    loaded = False
    
    def set_group(self, group):
        self.group = group
        
    
    def set_page(self, page):
        self.page = page
    
        
    def set_ui(self, ui:Ui_MainWindow):
        self.ui = ui
    
    
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
            self.ui.stackedWidget.setCurrentWidget(self.page[group_name])
            # 特征提取和分类共用界面，处理不共用部分
            if group_name == "extract":
                self.ui.start_classification_button.setVisible(False)
                self.ui.heatmap_checkBox.setVisible(False)
                self.ui.classification_condition_label.setVisible(False)
                if self.loaded:
                    self.ui.start_extract_button.setVisible(True)
                    if self.extracting:
                        self.ui.extract_condition_label.setVisible(True)
                    elif self.extracted:
                        self.ui.saveButton.setVisible(True)
                        self.ui.extract_condition_label.setVisible(True)
                self.ui.heatmap_checkBox.setChecked(not self.ui.heatmap_checkBox.isChecked())
                self.ui.heatmap_checkBox.setChecked(not self.ui.heatmap_checkBox.isChecked())
            elif group_name == "classification":
                self.ui.start_extract_button.setVisible(False)
                self.ui.saveButton.setVisible(False)
                self.ui.extract_condition_label.setVisible(False)
                if self.loaded:
                    self.ui.start_classification_button.setVisible(True)
                    if self.classifing:
                        self.ui.classification_condition_label.setVisible(True)
                    elif self.classified:
                        self.ui.classification_condition_label.setVisible(True)
                        self.ui.heatmap_checkBox.setVisible(True)
                self.ui.heatmap_checkBox.setChecked(not self.ui.heatmap_checkBox.isChecked())
                self.ui.heatmap_checkBox.setChecked(not self.ui.heatmap_checkBox.isChecked())
        return super().eventFilter(watched, event)


# 特征提取线程
class ExtractThread(QThread):
    signal = Signal(np.ndarray)
    
    # 设置需要提取的图像
    def set_img(self, nii_img):
        self.nii_img = nii_img
    
    def __init__(self, predictor: Predictor):
        super().__init__()
        self.predictor = predictor
    
    def run(self):
        if isinstance(self.nii_img, np.ndarray):
            vector = self.predictor.extract(self.nii_img)
            # 模拟耗时
            # time.sleep(5)
            self.signal.emit(vector)
        else:
            # 无图像返回零
            self.signal.emit(np.ones(0))
            

# 分类预测线程
class ClassifyThread(QThread):
    signal = Signal(tuple)
    
    # 设置需要提取的图像
    def set_img(self, nii_img):
        self.nii_img = nii_img
    
    def __init__(self, predictor: Predictor):
        super().__init__()
        self.predictor = predictor
    
    def run(self):
        if isinstance(self.nii_img, np.ndarray):
            pred = self.predictor.classify(self.nii_img)
            # 模拟耗时
            # time.sleep(5)
            self.signal.emit(pred)
        else:
            # 无图像返回零
            self.signal.emit("")
            
            
# 批量特征提取线程
class BatchExtractThread(QThread):
    signal = Signal(int)
    
    # 设置需要提取的图像
    def set_paths(self, paths):
        self.paths = paths
        
        
    def set_output_dir(self, output_dir):
        self.output_dir = output_dir
    
    def __init__(self, predictor: Predictor):
        super().__init__()
        self.predictor = predictor
    
    
    def run(self):
        try:
            cnt = 0
            for path in self.paths:
                cnt += 1
                nii_img = nib.load(path).get_fdata()
                vector = self.predictor.extract(nii_img)
                file_name = os.path.basename(path)
                file_name = os.path.join(self.output_dir, file_name[:file_name.find('.')] + '.vector')
                Util.save_file(vector, file_name)
                self.signal.emit(cnt)
        except:
            print("error")
            self.signal.emit(-1)
            
            
# 批量特征提取线程
class BatchClassifyThread(QThread):
    signal = Signal(int)
    
    # 设置需要提取的图像
    def set_paths(self, paths):
        self.paths = paths
        
        
    def set_output_dir(self, output_dir):
        self.output_dir = output_dir
    
    def __init__(self, predictor: Predictor):
        super().__init__()
        self.predictor = predictor
    
    
    def run(self):
        try:
            result = {}
            cnt = 0
            for path in self.paths:
                cnt += 1
                nii_img = nib.load(path).get_fdata()
                pred = self.predictor.classify(nii_img)
                result[path] = pred[0]
                self.signal.emit(cnt)
            file_path = os.path.join(self.output_dir, "prediction.csv")
            with open(file_path, 'w', newline='') as csvfile:
                writer = csv.writer(csvfile)
                writer.writerow(['path', 'class'])
                for key, value in result.items():
                    writer.writerow([key, value])
        
        except Exception as e:
            print(e)
            self.signal.emit(-1)


class MainWindow(QMainWindow):
    settingOpen = False
    infoOpen = False
    lastest_dir = './'
    img_name = ''
    nii_img = None
    attention_map = None
    
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
        group = {"extract":[self.ui.extractButton, self.ui.extractLabel], "classification":[self.ui.classificationButton, self.ui.classificationLabel], "batch":[self.ui.batchButton, self.ui.batchLabel], "hint":[self.ui.hintButton, self.ui.hintLabel]}
        page = {"extract":self.ui.extractPage, "classification":self.ui.extractPage, "batch": self.ui.batchPage, "hint":self.ui.hintPage}
        self.eventFilter = EventFilter()
        self.eventFilter.set_page(page)
        self.eventFilter.set_group(group)
        self.eventFilter.set_ui(self.ui)
        
        # 特征提取界面
        self.ui.selectButton.clicked.connect(self.select_file)
        self.ui.saveButton.clicked.connect(self.save_vector)
        
        self.ui.extract_condition_label.setVisible(False)
        self.ui.start_extract_button.setVisible(False)
        self.ui.saveButton.setVisible(False)
        self.extract_thread = ExtractThread(self.predictor)
        self.extract_thread.signal.connect(self.get_vector)
        self.ui.start_extract_button.clicked.connect(self.start_extract)
        
        self.ui.classification_condition_label.setVisible(False)
        self.ui.start_classification_button.setVisible(False)
        self.ui.heatmap_checkBox.setVisible(False)
        self.classify_thread = ClassifyThread(self.predictor)
        self.classify_thread.signal.connect(self.get_prediction)
        self.ui.start_classification_button.clicked.connect(self.start_classify)
        
        self.ui.spinBox_x.valueChanged.connect(self.refresh_pixmap)
        self.ui.spinBox_y.valueChanged.connect(self.refresh_pixmap)
        self.ui.spinBox_z.valueChanged.connect(self.refresh_pixmap)
        
        self.ui.heatmap_checkBox.stateChanged.connect(self.change_heatmap)
        
        self.ui.label_name.setText("未选择")
        # self.ui.label_x_range.setText("")
        # self.ui.label_y_range.setText("")
        # self.ui.label_z_range.setText("")
        
        # 设置
        self.ui.setting_save_button.clicked.connect(self.save_config)
        self.load_config()
        if os.path.exists(self.ui.default_input_dir_lineEdit.text()):
            self.lastest_dir = self.ui.default_input_dir_lineEdit.text()
        self.ui.pushButton_input.clicked.connect(self.select_dir)
        self.ui.pushButton_output.clicked.connect(self.select_dir)
        
        # 批量处理
        self.ui.pushButton_batch_read.clicked.connect(self.read_batch_image)
        self.ui.batch_label_num.setVisible(False)
        self.ui.pushButton_batch_extract.setVisible(False)
        self.ui.pushButton_batch_predict.setVisible(False)
        self.ui.batch_label_condition.setVisible(False)
        self.ui.progressBar_batch.setVisible(False)
        
        self.batch_extract_thread = BatchExtractThread(self.predictor)
        self.ui.pushButton_batch_extract.clicked.connect(self.start_batch)
        self.batch_extract_thread.signal.connect(self.get_process)
        
        self.batch_classify_thread = BatchClassifyThread(self.predictor)
        self.ui.pushButton_batch_predict.clicked.connect(self.start_batch)
        self.batch_classify_thread.signal.connect(self.get_process)
        
        
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
            self.ui.heatmap_checkBox.setChecked(False)
            self.refresh_pixmap()
            
            self.eventFilter.loaded = True
            self.eventFilter.extracted = False
            
            if self.eventFilter.selected == "extract":
                self.ui.start_extract_button.setVisible(True)
                self.ui.start_classification_button.setVisible(False)
            else:
                self.ui.start_extract_button.setVisible(False)
                self.ui.start_classification_button.setVisible(True)
            self.ui.extract_condition_label.setVisible(False)
            self.ui.saveButton.setVisible(False)
            self.ui.heatmap_checkBox.setVisible(False)
            self.ui.classification_condition_label.setVisible(False)

            
    @Slot()
    def refresh_pixmap(self):
        if self.ui.heatmap_checkBox.isChecked() and self.eventFilter.selected == "classification":
            if isinstance(self.nii_img, np.ndarray) and isinstance(self.attention_map, np.ndarray):
                saggital_pixmap, coronal_pixmap, axial_pixmap = Util.from_3d_rgb_img_get_pixmap(self.attention_map, self.ui.spinBox_x.value() - 1, self.ui.spinBox_y.value() - 1, self.ui.spinBox_z.value() - 1)
                self.ui.saggitalLabel.setPixmap(saggital_pixmap)
                self.ui.coronalLabel.setPixmap(coronal_pixmap)
                self.ui.axialLabel.setPixmap(axial_pixmap)
        else:
            if isinstance(self.nii_img, np.ndarray):
                saggital_pixmap, coronal_pixmap, axial_pixmap = Util.from_3d_img_get_pixmap(self.nii_img, self.ui.spinBox_x.value() - 1, self.ui.spinBox_y.value() - 1, self.ui.spinBox_z.value() - 1)
                self.ui.saggitalLabel.setPixmap(saggital_pixmap)
                self.ui.coronalLabel.setPixmap(coronal_pixmap)
                self.ui.axialLabel.setPixmap(axial_pixmap)
        if self.ui.default_input_dir_lineEdit.text() == "save":
            self.ui.axialLabel.pixmap().save(f"attention_maps/brain/{self.ui.default_output_dir_lineEdit.text()}_axial.jpg", "JPG")
            self.ui.coronalLabel.pixmap().save(f"attention_maps/brain/{self.ui.default_output_dir_lineEdit.text()}_coronal.jpg", "JPG")
            self.ui.saggitalLabel.pixmap().save(f"attention_maps/brain/{self.ui.default_output_dir_lineEdit.text()}_saggital.jpg", "JPG")
        # print("refresh")
            
    
    @Slot()
    def save_vector(self):
        fileName, fileType = QFileDialog.getSaveFileName(self, "保存特征数据", os.path.join(self.lastest_dir, self.img_name[:self.img_name.find('.')]), "特征文件 (*.vector)")
        if fileName and isinstance(self.vector, np.ndarray):
            Util.save_file(self.vector, fileName)
        
        
    @Slot()
    def start_extract(self):
        print("start extract")
        self.eventFilter.extracting = True
        self.ui.start_extract_button.setEnabled(False)
        self.ui.selectButton.setEnabled(False)
        self.ui.saveButton.setVisible(False)
        self.ui.extract_condition_label.setText("提取中...")
        self.ui.extract_condition_label.setVisible(True)
        self.extract_thread.set_img(self.nii_img)
        self.extract_thread.start()
        
        
    @Slot()
    def start_classify(self):
        print("start classify")
        self.eventFilter.classifing = True
        self.ui.heatmap_checkBox.setChecked(False)
        self.ui.start_classification_button.setEnabled(False)
        self.ui.selectButton.setEnabled(False)
        self.ui.heatmap_checkBox.setVisible(False)
        self.ui.classification_condition_label.setText("预测中...")
        self.ui.classification_condition_label.setVisible(True)
        self.classify_thread.set_img(self.nii_img)
        self.classify_thread.start()

    
    @Slot(np.ndarray)
    def get_vector(self, vector):
        print("finish extract")
        self.ui.start_extract_button.setEnabled(True)
        self.ui.selectButton.setEnabled(True)
        self.eventFilter.extracting = False
        self.eventFilter.extracted = True
        if vector.shape[0] != 0:
            self.vector = vector
            self.ui.extract_condition_label.setText("提取完成")
            if self.eventFilter.selected == "extract":
                self.ui.saveButton.setVisible(True)
        else:
            self.ui.extract_condition_label.setText("未加载图像")
            
    
    @Slot(tuple)
    def get_prediction(self, result):
        print("finish classify")
        prediction = result[0]
        alpha = 0.7
        self.attention_map = Util.overlap(self.nii_img, result[1], alpha)
        self.ui.start_classification_button.setEnabled(True)
        self.ui.selectButton.setEnabled(True)
        self.eventFilter.classifing = False
        self.eventFilter.classified = True
        if prediction != "":
            self.prediction = prediction
            self.ui.classification_condition_label.setText("结果：" + prediction)
            if self.eventFilter.selected == "classification":
                self.ui.heatmap_checkBox.setVisible(True)
        else:
            self.ui.classification_condition_label.setText("未加载图像")


    @Slot()
    def change_heatmap(self):
        self.refresh_pixmap()
        
        
    @Slot()
    def save_config(self):
        file_path = "./system_config.json"
        config = {}
        config['default_input_dir'] = self.ui.default_input_dir_lineEdit.text()
        config['default_output_dir'] = self.ui.default_output_dir_lineEdit.text()
        with open(file_path, 'w', encoding='utf-8') as file:
            json.dump(config, file, ensure_ascii=False, indent=4)
            
        messageBox = QMessageBox()
        messageBox.setWindowTitle("提示")
        messageBox.setText('<div style="text-align:center; vertical-align:middle;">保存成功。</div>')
        messageBox.exec()
        # QMessageBox.information(self, '信息', '保存成功。')
    
    
    def load_config(self):
        # 文件路径
        file_path = './system_config.json'

        # 检查文件是否存在
        if os.path.exists(file_path):
            # 打开并读取文件
            with open(file_path, 'r', encoding='utf-8') as file:
                config = json.load(file)
            # 输出数据或进行其他处理
            print(config)
            self.ui.default_input_dir_lineEdit.setText(config['default_input_dir'])
            self.ui.default_output_dir_lineEdit.setText(config['default_output_dir'])
            self.ui.lineEdit_input.setText(config['default_input_dir'])
            self.ui.lineEdit_output.setText(config['default_output_dir'])
            self.default_input_dir = config['default_input_dir']
            self.default_output_dir = config['default_output_dir']
        else:
            print('no config file')
    
    
    @Slot()
    def select_dir(self):
        is_input = self.sender().objectName() == "pushButton_input"
        if is_input:
            if os.path.exists(self.ui.lineEdit_input.text()):
                default_dir = self.ui.lineEdit_input.text()
            else:
                default_dir = self.default_input_dir
        else:
            if os.path.exists(self.ui.lineEdit_output.text()):
                default_dir = self.ui.lineEdit_output.text()
            else:
                default_dir = self.default_output_dir
        print(default_dir)
        directory_path = QFileDialog.getExistingDirectory(self, "选择输入路径",  default_dir, options=QFileDialog.ShowDirsOnly)
        if directory_path:
            print(f"选择的目录是: {directory_path}")
            if is_input:
                self.ui.lineEdit_input.setText(directory_path)
            else:
                self.ui.lineEdit_output.setText(directory_path)


    @Slot()
    def read_batch_image(self):
        if not os.path.exists(self.ui.lineEdit_input.text()):
            messageBox = QMessageBox()
            messageBox.setWindowTitle("提示")
            messageBox.setText('<div style="text-align:center; vertical-align:middle;">输入路径错误！</div>')
            messageBox.exec()
            return
        extensions = ('.gz', '.nii')
        image_files = []
        for root, dirs, files in os.walk(self.ui.lineEdit_input.text()):
            for file in files:
                if file.endswith(extensions):
                    image_files.append(os.path.join(root, file))
        self.image_nums = len(image_files)
        self.ui.batch_label_num.setText(f"图像数量：{self.image_nums}")
        self.ui.batch_label_num.setVisible(True)
        self.ui.pushButton_batch_extract.setVisible(True)
        self.ui.pushButton_batch_predict.setVisible(True)
        self.ui.progressBar_batch.setVisible(False)
        self.ui.batch_label_condition.setVisible(False)
        self.batch_extract_thread.set_paths(image_files)
        self.batch_classify_thread.set_paths(image_files)
        self.ui.progressBar_batch.setRange(0, self.image_nums)
        self.ui.progressBar_batch.setValue(0)

        
        
    @Slot()
    def start_batch(self):
        if not os.path.exists(self.ui.lineEdit_output.text()):
            messageBox = QMessageBox()
            messageBox.setWindowTitle("提示")
            messageBox.setText('<div style="text-align:center; vertical-align:middle;">输出路径错误！</div>')
            messageBox.exec()
            return
        self.ui.pushButton_batch_extract.setEnabled(False)
        self.ui.pushButton_batch_predict.setEnabled(False)
        self.ui.pushButton_batch_read.setEnabled(False)
        if self.sender().objectName() == 'pushButton_batch_extract':
            self.batch_extract_thread.set_output_dir(self.ui.lineEdit_output.text())
            self.batch_extract_thread.start()
            self.ui.batch_label_condition.setText("提取中...")
        else:
            self.batch_classify_thread.set_output_dir(self.ui.lineEdit_output.text())
            self.batch_classify_thread.start()
            self.ui.batch_label_condition.setText("分类中...")
        self.ui.batch_label_condition.setVisible(True)
        self.ui.progressBar_batch.setVisible(True)
        
    
    @Slot(int)
    def get_process(self, idx):
        print(idx)
        self.ui.progressBar_batch.setValue(idx)
        if idx == self.image_nums:
            if type(self.sender()) == BatchClassifyThread:
                self.ui.batch_label_condition.setText("分类完成")
            else:
                self.ui.batch_label_condition.setText("提取完成")
            self.ui.pushButton_batch_extract.setEnabled(True)
            self.ui.pushButton_batch_predict.setEnabled(True)
            self.ui.pushButton_batch_read.setEnabled(True)


if __name__ == "__main__":
    sys.argv += ['-platform', 'windows:darkmode=2']
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon("./ui/icon.ico"))
    window = MainWindow()
    window.show()

    sys.exit(app.exec())