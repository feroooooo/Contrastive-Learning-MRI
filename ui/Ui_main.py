# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 6.6.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QFrame, QGridLayout,
    QHBoxLayout, QLabel, QLineEdit, QMainWindow,
    QProgressBar, QPushButton, QSizePolicy, QSpacerItem,
    QSpinBox, QStackedWidget, QVBoxLayout, QWidget)
import ui.resource_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1280, 720)
        MainWindow.setMinimumSize(QSize(1280, 720))
        font = QFont()
        font.setPointSize(12)
        MainWindow.setFont(font)
        self.styleSheet = QWidget(MainWindow)
        self.styleSheet.setObjectName(u"styleSheet")
        self.styleSheet.setStyleSheet(u"QFrame#background{\n"
"	color: #dedede;\n"
"	background-color:#1b1b1b;\n"
"}\n"
"QFrame#leftFrame{\n"
"	background-color:#1b1b1b;\n"
"}\n"
"QFrame#infoFrame{\n"
"	background-color:#1b1b1b;\n"
"}\n"
"QFrame#extraFrame{\n"
"	background-color:#282828;\n"
"}\n"
"QFrame#contentFrame{\n"
"	background-color:#1b1b1b;\n"
"}\n"
"QLabel#topLabel{\n"
"	background-color:#1b1b1b;\n"
"	color:#dedede;\n"
"	font-size:16pt;\n"
"	letter-spacing:8px;\n"
"	font-weight:bold;\n"
"}\n"
"QLabel#settingLabel{\n"
"	color:#dedede;\n"
"}\n"
"QLabel#lineLabel{\n"
"	background-color:#dedede;\n"
"}\n"
"QLabel{\n"
"	color:#dedede;\n"
"}")
        self.gridLayout = QGridLayout(self.styleSheet)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.background = QFrame(self.styleSheet)
        self.background.setObjectName(u"background")
        self.horizontalLayout = QHBoxLayout(self.background)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.leftFrame = QFrame(self.background)
        self.leftFrame.setObjectName(u"leftFrame")
        self.leftFrame.setMinimumSize(QSize(60, 0))
        self.leftFrame.setMaximumSize(QSize(60, 16777215))
        self.leftFrame.setStyleSheet(u"")
        self.verticalLayout_2 = QVBoxLayout(self.leftFrame)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.iconFrame = QFrame(self.leftFrame)
        self.iconFrame.setObjectName(u"iconFrame")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.iconFrame.sizePolicy().hasHeightForWidth())
        self.iconFrame.setSizePolicy(sizePolicy)
        self.iconFrame.setMaximumSize(QSize(16777215, 60))
        self.verticalLayout_5 = QVBoxLayout(self.iconFrame)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.iconLabel = QLabel(self.iconFrame)
        self.iconLabel.setObjectName(u"iconLabel")
        self.iconLabel.setMinimumSize(QSize(40, 40))
        self.iconLabel.setMaximumSize(QSize(40, 40))
        self.iconLabel.setPixmap(QPixmap(u":/resource/img/icon.png"))
        self.iconLabel.setScaledContents(True)
        self.iconLabel.setAlignment(Qt.AlignCenter)

        self.verticalLayout_5.addWidget(self.iconLabel, 0, Qt.AlignHCenter|Qt.AlignVCenter)


        self.verticalLayout_2.addWidget(self.iconFrame)

        self.buttonFrame = QFrame(self.leftFrame)
        self.buttonFrame.setObjectName(u"buttonFrame")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.buttonFrame.sizePolicy().hasHeightForWidth())
        self.buttonFrame.setSizePolicy(sizePolicy1)
        self.buttonFrame.setMinimumSize(QSize(60, 0))
        self.buttonFrame.setStyleSheet(u"QPushButton{\n"
"	background-color:transparent;\n"
"	border: none;\n"
"	color:#dedede;\n"
"	font-size:12pt;\n"
"	font-weight:400;\n"
"	letter-spacing:5px;\n"
"}")
        self.verticalLayout_6 = QVBoxLayout(self.buttonFrame)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.extractButton = QPushButton(self.buttonFrame)
        self.extractButton.setObjectName(u"extractButton")
        sizePolicy2 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.extractButton.sizePolicy().hasHeightForWidth())
        self.extractButton.setSizePolicy(sizePolicy2)
        self.extractButton.setMinimumSize(QSize(60, 60))
        self.extractButton.setMaximumSize(QSize(60, 60))
        self.extractButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.extractButton.setStyleSheet(u"background-color:#464646;\n"
"")
        icon = QIcon()
        icon.addFile(u":/resource/img/extract.png", QSize(), QIcon.Normal, QIcon.Off)
        self.extractButton.setIcon(icon)
        self.extractButton.setIconSize(QSize(24, 24))

        self.verticalLayout_6.addWidget(self.extractButton)

        self.classificationButton = QPushButton(self.buttonFrame)
        self.classificationButton.setObjectName(u"classificationButton")
        sizePolicy2.setHeightForWidth(self.classificationButton.sizePolicy().hasHeightForWidth())
        self.classificationButton.setSizePolicy(sizePolicy2)
        self.classificationButton.setMinimumSize(QSize(60, 60))
        self.classificationButton.setMaximumSize(QSize(60, 60))
        self.classificationButton.setCursor(QCursor(Qt.PointingHandCursor))
        icon1 = QIcon()
        icon1.addFile(u":/resource/img/classification.png", QSize(), QIcon.Normal, QIcon.Off)
        self.classificationButton.setIcon(icon1)
        self.classificationButton.setIconSize(QSize(24, 24))

        self.verticalLayout_6.addWidget(self.classificationButton, 0, Qt.AlignLeft)

        self.batchButton = QPushButton(self.buttonFrame)
        self.batchButton.setObjectName(u"batchButton")
        sizePolicy2.setHeightForWidth(self.batchButton.sizePolicy().hasHeightForWidth())
        self.batchButton.setSizePolicy(sizePolicy2)
        self.batchButton.setMinimumSize(QSize(60, 60))
        self.batchButton.setMaximumSize(QSize(60, 60))
        self.batchButton.setCursor(QCursor(Qt.PointingHandCursor))
        icon2 = QIcon()
        icon2.addFile(u":/resource/img/batch.png", QSize(), QIcon.Normal, QIcon.Off)
        self.batchButton.setIcon(icon2)
        self.batchButton.setIconSize(QSize(24, 24))

        self.verticalLayout_6.addWidget(self.batchButton, 0, Qt.AlignLeft)

        self.hintButton = QPushButton(self.buttonFrame)
        self.hintButton.setObjectName(u"hintButton")
        sizePolicy2.setHeightForWidth(self.hintButton.sizePolicy().hasHeightForWidth())
        self.hintButton.setSizePolicy(sizePolicy2)
        self.hintButton.setMinimumSize(QSize(60, 60))
        self.hintButton.setMaximumSize(QSize(60, 60))
        self.hintButton.setCursor(QCursor(Qt.PointingHandCursor))
        icon3 = QIcon()
        icon3.addFile(u":/resource/img/hint.png", QSize(), QIcon.Normal, QIcon.Off)
        self.hintButton.setIcon(icon3)
        self.hintButton.setIconSize(QSize(24, 24))

        self.verticalLayout_6.addWidget(self.hintButton, 0, Qt.AlignLeft)


        self.verticalLayout_2.addWidget(self.buttonFrame)

        self.settingFrame = QFrame(self.leftFrame)
        self.settingFrame.setObjectName(u"settingFrame")
        self.verticalLayout_7 = QVBoxLayout(self.settingFrame)
        self.verticalLayout_7.setSpacing(5)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 10)
        self.infoButton = QPushButton(self.settingFrame)
        self.infoButton.setObjectName(u"infoButton")
        sizePolicy2.setHeightForWidth(self.infoButton.sizePolicy().hasHeightForWidth())
        self.infoButton.setSizePolicy(sizePolicy2)
        self.infoButton.setMinimumSize(QSize(60, 40))
        self.infoButton.setMaximumSize(QSize(60, 40))
        self.infoButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.infoButton.setStyleSheet(u"background-color:transparent;")
        icon4 = QIcon()
        icon4.addFile(u":/resource/img/list.png", QSize(), QIcon.Normal, QIcon.Off)
        self.infoButton.setIcon(icon4)
        self.infoButton.setIconSize(QSize(28, 28))

        self.verticalLayout_7.addWidget(self.infoButton)

        self.settingButton = QPushButton(self.settingFrame)
        self.settingButton.setObjectName(u"settingButton")
        sizePolicy2.setHeightForWidth(self.settingButton.sizePolicy().hasHeightForWidth())
        self.settingButton.setSizePolicy(sizePolicy2)
        self.settingButton.setMinimumSize(QSize(60, 40))
        self.settingButton.setMaximumSize(QSize(60, 40))
        self.settingButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.settingButton.setStyleSheet(u"background-color:transparent;")
        icon5 = QIcon()
        icon5.addFile(u":/resource/img/setting.png", QSize(), QIcon.Normal, QIcon.Off)
        self.settingButton.setIcon(icon5)
        self.settingButton.setIconSize(QSize(28, 28))
        self.settingButton.setAutoRepeat(False)

        self.verticalLayout_7.addWidget(self.settingButton)


        self.verticalLayout_2.addWidget(self.settingFrame, 0, Qt.AlignBottom)


        self.horizontalLayout.addWidget(self.leftFrame)

        self.infoFrame = QFrame(self.background)
        self.infoFrame.setObjectName(u"infoFrame")
        sizePolicy3 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.infoFrame.sizePolicy().hasHeightForWidth())
        self.infoFrame.setSizePolicy(sizePolicy3)
        self.infoFrame.setMinimumSize(QSize(0, 0))
        self.infoFrame.setMaximumSize(QSize(100, 16777215))
        self.infoFrame.setStyleSheet(u"QLabel{\n"
"	color:#dedede;\n"
"	font-size:12pt;\n"
"	font-weight:400;\n"
"}")
        self.verticalLayout_9 = QVBoxLayout(self.infoFrame)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.topFrame = QFrame(self.infoFrame)
        self.topFrame.setObjectName(u"topFrame")
        self.topFrame.setMinimumSize(QSize(0, 60))
        self.topFrame.setMaximumSize(QSize(16777215, 60))
        self.topFrame.setStyleSheet(u"padding-right:3px;")
        self.verticalLayout_10 = QVBoxLayout(self.topFrame)
        self.verticalLayout_10.setSpacing(0)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.topLabel_2 = QLabel(self.topFrame)
        self.topLabel_2.setObjectName(u"topLabel_2")
        sizePolicy4 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.topLabel_2.sizePolicy().hasHeightForWidth())
        self.topLabel_2.setSizePolicy(sizePolicy4)
        font1 = QFont()
        font1.setPointSize(16)
        font1.setBold(True)
        self.topLabel_2.setFont(font1)
        self.topLabel_2.setStyleSheet(u"font-size:16pt;font-weight:bold;letter-spacing:2px;")

        self.verticalLayout_10.addWidget(self.topLabel_2, 0, Qt.AlignHCenter)


        self.verticalLayout_9.addWidget(self.topFrame)

        self.upFrame = QFrame(self.infoFrame)
        self.upFrame.setObjectName(u"upFrame")
        sizePolicy3.setHeightForWidth(self.upFrame.sizePolicy().hasHeightForWidth())
        self.upFrame.setSizePolicy(sizePolicy3)
        self.upFrame.setStyleSheet(u"QLabel{\n"
"	letter-spacing:5px;\n"
"	padding-left:1px;\n"
"}")
        self.verticalLayout_11 = QVBoxLayout(self.upFrame)
        self.verticalLayout_11.setSpacing(0)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.extractLabel = QLabel(self.upFrame)
        self.extractLabel.setObjectName(u"extractLabel")
        sizePolicy1.setHeightForWidth(self.extractLabel.sizePolicy().hasHeightForWidth())
        self.extractLabel.setSizePolicy(sizePolicy1)
        self.extractLabel.setMinimumSize(QSize(0, 60))
        self.extractLabel.setMaximumSize(QSize(16777215, 60))
        self.extractLabel.setCursor(QCursor(Qt.PointingHandCursor))
        self.extractLabel.setStyleSheet(u"background-color:#464646")

        self.verticalLayout_11.addWidget(self.extractLabel)

        self.classificationLabel = QLabel(self.upFrame)
        self.classificationLabel.setObjectName(u"classificationLabel")
        sizePolicy1.setHeightForWidth(self.classificationLabel.sizePolicy().hasHeightForWidth())
        self.classificationLabel.setSizePolicy(sizePolicy1)
        self.classificationLabel.setMinimumSize(QSize(0, 60))
        self.classificationLabel.setMaximumSize(QSize(16777215, 60))
        self.classificationLabel.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_11.addWidget(self.classificationLabel)

        self.batchLabel = QLabel(self.upFrame)
        self.batchLabel.setObjectName(u"batchLabel")
        sizePolicy1.setHeightForWidth(self.batchLabel.sizePolicy().hasHeightForWidth())
        self.batchLabel.setSizePolicy(sizePolicy1)
        self.batchLabel.setMinimumSize(QSize(0, 60))
        self.batchLabel.setMaximumSize(QSize(16777215, 60))
        self.batchLabel.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_11.addWidget(self.batchLabel)

        self.hintLabel = QLabel(self.upFrame)
        self.hintLabel.setObjectName(u"hintLabel")
        sizePolicy1.setHeightForWidth(self.hintLabel.sizePolicy().hasHeightForWidth())
        self.hintLabel.setSizePolicy(sizePolicy1)
        self.hintLabel.setMinimumSize(QSize(0, 60))
        self.hintLabel.setMaximumSize(QSize(16777215, 60))
        self.hintLabel.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_11.addWidget(self.hintLabel)


        self.verticalLayout_9.addWidget(self.upFrame, 0, Qt.AlignTop)

        self.downFrame = QFrame(self.infoFrame)
        self.downFrame.setObjectName(u"downFrame")
        self.verticalLayout_101 = QVBoxLayout(self.downFrame)
        self.verticalLayout_101.setSpacing(0)
        self.verticalLayout_101.setObjectName(u"verticalLayout_101")
        self.verticalLayout_101.setContentsMargins(0, 0, 0, 0)
        self.label_4 = QLabel(self.downFrame)
        self.label_4.setObjectName(u"label_4")

        self.verticalLayout_101.addWidget(self.label_4)


        self.verticalLayout_9.addWidget(self.downFrame)


        self.horizontalLayout.addWidget(self.infoFrame)

        self.extraFrame = QFrame(self.background)
        self.extraFrame.setObjectName(u"extraFrame")
        sizePolicy3.setHeightForWidth(self.extraFrame.sizePolicy().hasHeightForWidth())
        self.extraFrame.setSizePolicy(sizePolicy3)
        self.extraFrame.setMinimumSize(QSize(0, 0))
        self.extraFrame.setMaximumSize(QSize(240, 16777215))
        self.verticalLayout_3 = QVBoxLayout(self.extraFrame)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 20, 0, 0)
        self.settingLabel = QLabel(self.extraFrame)
        self.settingLabel.setObjectName(u"settingLabel")
        sizePolicy5 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Minimum)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.settingLabel.sizePolicy().hasHeightForWidth())
        self.settingLabel.setSizePolicy(sizePolicy5)
        self.settingLabel.setStyleSheet(u"font-size:18pt;\n"
"font-weight:600;")
        self.settingLabel.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.settingLabel)

        self.verticalSpacer = QSpacerItem(20, 6, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_3.addItem(self.verticalSpacer)

        self.lineLabel = QLabel(self.extraFrame)
        self.lineLabel.setObjectName(u"lineLabel")
        self.lineLabel.setMinimumSize(QSize(0, 2))
        self.lineLabel.setMaximumSize(QSize(16777215, 2))
        self.lineLabel.setStyleSheet(u"margin:0 20px;")

        self.verticalLayout_3.addWidget(self.lineLabel)

        self.frame = QFrame(self.extraFrame)
        self.frame.setObjectName(u"frame")
        sizePolicy6 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy6)
        self.frame.setStyleSheet(u"QLabel{\n"
"	font-size:12pt;\n"
"}\n"
"QLineEdit{\n"
"	background-color:#dedede;\n"
"	border:0px;\n"
"	padding: 0 5px;\n"
"	border-radius:5px;\n"
"}\n"
"QPushButton{\n"
"	background-color:#dedede;\n"
"	color:#1b1b1b;\n"
"	border-radius:10px;\n"
"	font-size:11pt;\n"
"	letter-spacing:2px;\n"
"	font-weight:400;\n"
"}\n"
"QPushButton:hover{\n"
"	background-color:#f1f1f1;\n"
"}")
        self.default_input_dir_label = QLabel(self.frame)
        self.default_input_dir_label.setObjectName(u"default_input_dir_label")
        self.default_input_dir_label.setGeometry(QRect(20, 10, 211, 30))
        self.default_input_dir_lineEdit = QLineEdit(self.frame)
        self.default_input_dir_lineEdit.setObjectName(u"default_input_dir_lineEdit")
        self.default_input_dir_lineEdit.setGeometry(QRect(20, 45, 201, 25))
        self.default_input_dir_lineEdit.setFont(font)
        self.default_output_dir_label = QLabel(self.frame)
        self.default_output_dir_label.setObjectName(u"default_output_dir_label")
        self.default_output_dir_label.setGeometry(QRect(20, 80, 211, 30))
        self.default_output_dir_lineEdit = QLineEdit(self.frame)
        self.default_output_dir_lineEdit.setObjectName(u"default_output_dir_lineEdit")
        self.default_output_dir_lineEdit.setGeometry(QRect(20, 115, 201, 25))
        self.default_output_dir_lineEdit.setFont(font)
        self.setting_save_button = QPushButton(self.frame)
        self.setting_save_button.setObjectName(u"setting_save_button")
        self.setting_save_button.setGeometry(QRect(80, 180, 75, 30))
        font2 = QFont()
        font2.setPointSize(11)
        font2.setBold(False)
        self.setting_save_button.setFont(font2)
        self.setting_save_button.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_3.addWidget(self.frame)


        self.horizontalLayout.addWidget(self.extraFrame)

        self.contentFrame = QFrame(self.background)
        self.contentFrame.setObjectName(u"contentFrame")
        self.verticalLayout_4 = QVBoxLayout(self.contentFrame)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.topLabel = QLabel(self.contentFrame)
        self.topLabel.setObjectName(u"topLabel")
        sizePolicy3.setHeightForWidth(self.topLabel.sizePolicy().hasHeightForWidth())
        self.topLabel.setSizePolicy(sizePolicy3)
        self.topLabel.setMinimumSize(QSize(0, 60))
        self.topLabel.setMaximumSize(QSize(16777215, 60))
        font3 = QFont()
        font3.setFamilies([u"Microsoft YaHei UI"])
        font3.setPointSize(16)
        font3.setBold(True)
        self.topLabel.setFont(font3)
        self.topLabel.setAlignment(Qt.AlignCenter)

        self.verticalLayout_4.addWidget(self.topLabel)

        self.contentContainer = QFrame(self.contentFrame)
        self.contentContainer.setObjectName(u"contentContainer")
        self.contentContainer.setFrameShape(QFrame.NoFrame)
        self.contentContainer.setFrameShadow(QFrame.Plain)
        self.verticalLayout_8 = QVBoxLayout(self.contentContainer)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.stackedWidget = QStackedWidget(self.contentContainer)
        self.stackedWidget.setObjectName(u"stackedWidget")
        font4 = QFont()
        font4.setKerning(True)
        self.stackedWidget.setFont(font4)
        self.stackedWidget.setStyleSheet(u"QFrame{\n"
"	background-color:#323232;\n"
"}")
        self.batchPage = QWidget()
        self.batchPage.setObjectName(u"batchPage")
        self.batchPage.setStyleSheet(u"QLabel{font-size:30px;}")
        self.gridLayoutClassification = QGridLayout(self.batchPage)
        self.gridLayoutClassification.setObjectName(u"gridLayoutClassification")
        self.gridLayoutClassification.setContentsMargins(0, 0, 0, 0)
        self.batchFrameV = QFrame(self.batchPage)
        self.batchFrameV.setObjectName(u"batchFrameV")
        self.horizontalLayoutClassification = QHBoxLayout(self.batchFrameV)
        self.horizontalLayoutClassification.setSpacing(0)
        self.horizontalLayoutClassification.setObjectName(u"horizontalLayoutClassification")
        self.horizontalLayoutClassification.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacerBatch2 = QSpacerItem(0, 0, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayoutClassification.addItem(self.horizontalSpacerBatch2)

        self.batchFrameH = QFrame(self.batchFrameV)
        self.batchFrameH.setObjectName(u"batchFrameH")
        self.batchFrameH.setMinimumSize(QSize(0, 0))
        self.batchFrameH.setStyleSheet(u"")
        self.verticalLayoutClassification = QVBoxLayout(self.batchFrameH)
        self.verticalLayoutClassification.setSpacing(0)
        self.verticalLayoutClassification.setObjectName(u"verticalLayoutClassification")
        self.verticalLayoutClassification.setContentsMargins(0, 0, 0, 0)
        self.verticalSpacerBatch1 = QSpacerItem(0, 0, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayoutClassification.addItem(self.verticalSpacerBatch1)

        self.batchFrame = QFrame(self.batchFrameH)
        self.batchFrame.setObjectName(u"batchFrame")
        self.batchFrame.setMinimumSize(QSize(880, 660))
        self.batchFrame.setStyleSheet(u"QLabel{\n"
"	font-size:16pt;\n"
"}\n"
"QProgressBar{\n"
"	color:#dedede;\n"
"	font-size:12pt;\n"
"}\n"
"QLineEdit{\n"
"	background-color:#dedede;\n"
"	border:0px;\n"
"	padding: 0 5px;\n"
"	border-radius:5px;\n"
"}\n"
"QPushButton{\n"
"	background-color:#dedede;\n"
"	color:#1b1b1b;\n"
"	border-radius:15px;\n"
"	font-size:11pt;\n"
"	letter-spacing:2px;\n"
"	font-weight:400;\n"
"}\n"
"QPushButton:hover{\n"
"	background-color:#f1f1f1;\n"
"}\n"
"QPushButton#pushButton_output, QPushButton#pushButton_input{\n"
"	border-radius:10px;\n"
"}")
        self.input_dir_label = QLabel(self.batchFrame)
        self.input_dir_label.setObjectName(u"input_dir_label")
        self.input_dir_label.setGeometry(QRect(100, 60, 211, 41))
        self.pushButton_input = QPushButton(self.batchFrame)
        self.pushButton_input.setObjectName(u"pushButton_input")
        self.pushButton_input.setGeometry(QRect(680, 110, 75, 30))
        self.pushButton_input.setFont(font2)
        self.pushButton_input.setCursor(QCursor(Qt.PointingHandCursor))
        self.lineEdit_input = QLineEdit(self.batchFrame)
        self.lineEdit_input.setObjectName(u"lineEdit_input")
        self.lineEdit_input.setGeometry(QRect(100, 110, 571, 30))
        font5 = QFont()
        font5.setPointSize(13)
        self.lineEdit_input.setFont(font5)
        self.output_dir_label = QLabel(self.batchFrame)
        self.output_dir_label.setObjectName(u"output_dir_label")
        self.output_dir_label.setGeometry(QRect(100, 150, 211, 41))
        self.lineEdit_output = QLineEdit(self.batchFrame)
        self.lineEdit_output.setObjectName(u"lineEdit_output")
        self.lineEdit_output.setGeometry(QRect(100, 200, 571, 30))
        self.lineEdit_output.setFont(font5)
        self.pushButton_output = QPushButton(self.batchFrame)
        self.pushButton_output.setObjectName(u"pushButton_output")
        self.pushButton_output.setGeometry(QRect(680, 200, 75, 30))
        self.pushButton_output.setFont(font2)
        self.pushButton_output.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_batch_extract = QPushButton(self.batchFrame)
        self.pushButton_batch_extract.setObjectName(u"pushButton_batch_extract")
        self.pushButton_batch_extract.setGeometry(QRect(380, 380, 111, 41))
        self.pushButton_batch_extract.setFont(font2)
        self.pushButton_batch_extract.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_batch_predict = QPushButton(self.batchFrame)
        self.pushButton_batch_predict.setObjectName(u"pushButton_batch_predict")
        self.pushButton_batch_predict.setGeometry(QRect(380, 450, 111, 41))
        self.pushButton_batch_predict.setFont(font2)
        self.pushButton_batch_predict.setCursor(QCursor(Qt.PointingHandCursor))
        self.progressBar_batch = QProgressBar(self.batchFrame)
        self.progressBar_batch.setObjectName(u"progressBar_batch")
        self.progressBar_batch.setGeometry(QRect(100, 560, 701, 23))
        self.progressBar_batch.setValue(24)
        self.batch_label_condition = QLabel(self.batchFrame)
        self.batch_label_condition.setObjectName(u"batch_label_condition")
        self.batch_label_condition.setGeometry(QRect(370, 510, 131, 31))
        self.batch_label_condition.setAlignment(Qt.AlignCenter)
        self.batch_label_num = QLabel(self.batchFrame)
        self.batch_label_num.setObjectName(u"batch_label_num")
        self.batch_label_num.setGeometry(QRect(340, 310, 191, 31))
        self.batch_label_num.setStyleSheet(u"font-size:13pt;")
        self.batch_label_num.setAlignment(Qt.AlignCenter)
        self.pushButton_batch_read = QPushButton(self.batchFrame)
        self.pushButton_batch_read.setObjectName(u"pushButton_batch_read")
        self.pushButton_batch_read.setGeometry(QRect(380, 260, 111, 41))
        self.pushButton_batch_read.setFont(font2)
        self.pushButton_batch_read.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayoutClassification.addWidget(self.batchFrame)

        self.verticalSpacerBatch2 = QSpacerItem(0, 0, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayoutClassification.addItem(self.verticalSpacerBatch2)


        self.horizontalLayoutClassification.addWidget(self.batchFrameH)

        self.horizontalSpacerBatch1 = QSpacerItem(0, 0, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayoutClassification.addItem(self.horizontalSpacerBatch1)


        self.gridLayoutClassification.addWidget(self.batchFrameV, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.batchPage)
        self.extractPage = QWidget()
        self.extractPage.setObjectName(u"extractPage")
        self.gridLayoutExtract = QGridLayout(self.extractPage)
        self.gridLayoutExtract.setObjectName(u"gridLayoutExtract")
        self.gridLayoutExtract.setContentsMargins(0, 0, 0, 0)
        self.extractFrameV = QFrame(self.extractPage)
        self.extractFrameV.setObjectName(u"extractFrameV")
        self.horizontalLayout_2 = QHBoxLayout(self.extractFrameV)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacerExtract2 = QSpacerItem(0, 0, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacerExtract2)

        self.extractFrameH = QFrame(self.extractFrameV)
        self.extractFrameH.setObjectName(u"extractFrameH")
        self.extractFrameH.setMinimumSize(QSize(0, 0))
        self.extractFrameH.setStyleSheet(u"")
        self.verticalLayout = QVBoxLayout(self.extractFrameH)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalSpacerExtract1 = QSpacerItem(0, 0, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacerExtract1)

        self.extractFrame = QFrame(self.extractFrameH)
        self.extractFrame.setObjectName(u"extractFrame")
        self.extractFrame.setMinimumSize(QSize(880, 660))
        self.extractFrame.setStyleSheet(u"QLabel#axialLabel, QLabel#coronalLabel, QLabel#saggitalLabel{\n"
"	border: 2px solid #dedede;\n"
"	background-color:black;\n"
"}\n"
"QLabel#axial_text_label, QLabel#saggital_text_label, QLabel#coronal_text_label{\n"
"	border: 2px solid #dedede;\n"
"	background-color:#1b1b1b;\n"
"}\n"
"QPushButton{\n"
"	background-color:#dedede;\n"
"	color:#1b1b1b;\n"
"	border-radius:20px;\n"
"	font-size:12pt;\n"
"	letter-spacing:2px;\n"
"	font-weight:400;\n"
"}\n"
"QPushButton:hover{\n"
"	background-color:#f1f1f1;\n"
"}\n"
"QSpinBox{\n"
"	background-color:#dedede;\n"
"	font-size:14pt;\n"
"}\n"
"QLabel#extract_condition_label, QLabel#classification_condition_label{\n"
"	border-bottom:2px solid #dedede;\n"
"}\n"
"QCheckBox{\n"
"	color:#dedede;\n"
"	font-size:12pt;\n"
"}")
        self.axialLabel = QLabel(self.extractFrame)
        self.axialLabel.setObjectName(u"axialLabel")
        self.axialLabel.setGeometry(QRect(50, 60, 250, 250))
        self.axialLabel.setAlignment(Qt.AlignCenter)
        self.saggitalLabel = QLabel(self.extractFrame)
        self.saggitalLabel.setObjectName(u"saggitalLabel")
        self.saggitalLabel.setGeometry(QRect(350, 60, 250, 250))
        self.saggitalLabel.setAlignment(Qt.AlignCenter)
        self.coronalLabel = QLabel(self.extractFrame)
        self.coronalLabel.setObjectName(u"coronalLabel")
        self.coronalLabel.setGeometry(QRect(350, 388, 250, 250))
        self.coronalLabel.setAlignment(Qt.AlignCenter)
        self.selectButton = QPushButton(self.extractFrame)
        self.selectButton.setObjectName(u"selectButton")
        self.selectButton.setGeometry(QRect(115, 350, 121, 41))
        self.selectButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.label_name_contrainer = QLabel(self.extractFrame)
        self.label_name_contrainer.setObjectName(u"label_name_contrainer")
        self.label_name_contrainer.setGeometry(QRect(50, 580, 250, 60))
        self.label_name_contrainer.setFont(font5)
        self.label_name_contrainer.setStyleSheet(u"background-color:#1b1b1b;border-radius:30px;")
        self.label_name_contrainer.setScaledContents(True)
        self.label_name_contrainer.setAlignment(Qt.AlignBottom|Qt.AlignHCenter)
        self.label_name_contrainer.setWordWrap(True)
        self.spinBox_x = QSpinBox(self.extractFrame)
        self.spinBox_x.setObjectName(u"spinBox_x")
        self.spinBox_x.setGeometry(QRect(120, 414, 60, 30))
        font6 = QFont()
        font6.setPointSize(14)
        self.spinBox_x.setFont(font6)
        self.spinBox_x.setAlignment(Qt.AlignCenter)
        self.spinBox_x.setMinimum(1)
        self.spinBox_x.setMaximum(1)
        self.spinBox_y = QSpinBox(self.extractFrame)
        self.spinBox_y.setObjectName(u"spinBox_y")
        self.spinBox_y.setGeometry(QRect(120, 459, 60, 30))
        self.spinBox_y.setFont(font6)
        self.spinBox_y.setAlignment(Qt.AlignCenter)
        self.spinBox_y.setMinimum(1)
        self.spinBox_y.setMaximum(1)
        self.spinBox_z = QSpinBox(self.extractFrame)
        self.spinBox_z.setObjectName(u"spinBox_z")
        self.spinBox_z.setGeometry(QRect(120, 504, 60, 30))
        self.spinBox_z.setAlignment(Qt.AlignCenter)
        self.spinBox_z.setMinimum(1)
        self.spinBox_z.setMaximum(1)
        self.label_x = QLabel(self.extractFrame)
        self.label_x.setObjectName(u"label_x")
        self.label_x.setGeometry(QRect(71, 406, 30, 40))
        font7 = QFont()
        font7.setPointSize(20)
        self.label_x.setFont(font7)
        self.label_y = QLabel(self.extractFrame)
        self.label_y.setObjectName(u"label_y")
        self.label_y.setGeometry(QRect(70, 451, 30, 40))
        self.label_y.setFont(font7)
        self.label_z = QLabel(self.extractFrame)
        self.label_z.setObjectName(u"label_z")
        self.label_z.setGeometry(QRect(70, 496, 30, 40))
        self.label_z.setFont(font7)
        self.start_extract_button = QPushButton(self.extractFrame)
        self.start_extract_button.setObjectName(u"start_extract_button")
        self.start_extract_button.setGeometry(QRect(680, 140, 121, 41))
        self.start_extract_button.setCursor(QCursor(Qt.PointingHandCursor))
        self.saveButton = QPushButton(self.extractFrame)
        self.saveButton.setObjectName(u"saveButton")
        self.saveButton.setGeometry(QRect(680, 480, 121, 41))
        self.saveButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.axial_text_label = QLabel(self.extractFrame)
        self.axial_text_label.setObjectName(u"axial_text_label")
        self.axial_text_label.setGeometry(QRect(50, 22, 250, 40))
        self.axial_text_label.setFont(font)
        self.axial_text_label.setAlignment(Qt.AlignCenter)
        self.saggital_text_label = QLabel(self.extractFrame)
        self.saggital_text_label.setObjectName(u"saggital_text_label")
        self.saggital_text_label.setGeometry(QRect(350, 22, 250, 40))
        self.saggital_text_label.setFont(font)
        self.saggital_text_label.setAlignment(Qt.AlignCenter)
        self.coronal_text_label = QLabel(self.extractFrame)
        self.coronal_text_label.setObjectName(u"coronal_text_label")
        self.coronal_text_label.setGeometry(QRect(350, 350, 250, 40))
        self.coronal_text_label.setFont(font)
        self.coronal_text_label.setAlignment(Qt.AlignCenter)
        self.label_x_range = QLabel(self.extractFrame)
        self.label_x_range.setObjectName(u"label_x_range")
        self.label_x_range.setGeometry(QRect(200, 408, 101, 40))
        font8 = QFont()
        font8.setPointSize(17)
        self.label_x_range.setFont(font8)
        self.label_y_range = QLabel(self.extractFrame)
        self.label_y_range.setObjectName(u"label_y_range")
        self.label_y_range.setGeometry(QRect(200, 453, 101, 40))
        self.label_y_range.setFont(font8)
        self.label_z_range = QLabel(self.extractFrame)
        self.label_z_range.setObjectName(u"label_z_range")
        self.label_z_range.setGeometry(QRect(200, 498, 101, 40))
        self.label_z_range.setFont(font8)
        self.extract_condition_label = QLabel(self.extractFrame)
        self.extract_condition_label.setObjectName(u"extract_condition_label")
        self.extract_condition_label.setGeometry(QRect(675, 305, 131, 41))
        font9 = QFont()
        font9.setPointSize(16)
        self.extract_condition_label.setFont(font9)
        self.extract_condition_label.setAlignment(Qt.AlignCenter)
        self.label_name_label = QLabel(self.extractFrame)
        self.label_name_label.setObjectName(u"label_name_label")
        self.label_name_label.setGeometry(QRect(135, 553, 81, 21))
        font10 = QFont()
        font10.setPointSize(13)
        font10.setBold(True)
        self.label_name_label.setFont(font10)
        self.label_name_label.setStyleSheet(u"background-color:transparent;")
        self.label_name_label.setScaledContents(True)
        self.label_name_label.setAlignment(Qt.AlignCenter)
        self.label_name_label.setWordWrap(True)
        self.label_name = QLabel(self.extractFrame)
        self.label_name.setObjectName(u"label_name")
        self.label_name.setGeometry(QRect(50, 584, 250, 48))
        self.label_name.setFont(font5)
        self.label_name.setStyleSheet(u"background-color:transparent;")
        self.label_name.setScaledContents(True)
        self.label_name.setAlignment(Qt.AlignCenter)
        self.label_name.setWordWrap(True)
        self.start_classification_button = QPushButton(self.extractFrame)
        self.start_classification_button.setObjectName(u"start_classification_button")
        self.start_classification_button.setGeometry(QRect(680, 140, 121, 41))
        self.start_classification_button.setCursor(QCursor(Qt.PointingHandCursor))
        self.classification_condition_label = QLabel(self.extractFrame)
        self.classification_condition_label.setObjectName(u"classification_condition_label")
        self.classification_condition_label.setGeometry(QRect(675, 305, 131, 41))
        self.classification_condition_label.setFont(font9)
        self.classification_condition_label.setAlignment(Qt.AlignCenter)
        self.heatmap_checkBox = QCheckBox(self.extractFrame)
        self.heatmap_checkBox.setObjectName(u"heatmap_checkBox")
        self.heatmap_checkBox.setGeometry(QRect(690, 490, 101, 20))

        self.verticalLayout.addWidget(self.extractFrame)

        self.verticalSpacerExtract2 = QSpacerItem(0, 0, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacerExtract2)


        self.horizontalLayout_2.addWidget(self.extractFrameH)

        self.horizontalSpacerExtract1 = QSpacerItem(0, 0, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacerExtract1)


        self.gridLayoutExtract.addWidget(self.extractFrameV, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.extractPage)
        self.hintPage = QWidget()
        self.hintPage.setObjectName(u"hintPage")
        self.hintPage.setStyleSheet(u"QLabel{font-size:30px;}")
        self.gridLayoutHint = QGridLayout(self.hintPage)
        self.gridLayoutHint.setObjectName(u"gridLayoutHint")
        self.gridLayoutHint.setContentsMargins(0, 0, 0, 0)
        self.hintFrameV = QFrame(self.hintPage)
        self.hintFrameV.setObjectName(u"hintFrameV")
        self.horizontalLayoutHint = QHBoxLayout(self.hintFrameV)
        self.horizontalLayoutHint.setSpacing(0)
        self.horizontalLayoutHint.setObjectName(u"horizontalLayoutHint")
        self.horizontalLayoutHint.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacerHint2 = QSpacerItem(0, 0, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayoutHint.addItem(self.horizontalSpacerHint2)

        self.hintFrameH = QFrame(self.hintFrameV)
        self.hintFrameH.setObjectName(u"hintFrameH")
        self.hintFrameH.setMinimumSize(QSize(0, 0))
        self.hintFrameH.setStyleSheet(u"")
        self.verticalLayoutHint = QVBoxLayout(self.hintFrameH)
        self.verticalLayoutHint.setSpacing(0)
        self.verticalLayoutHint.setObjectName(u"verticalLayoutHint")
        self.verticalLayoutHint.setContentsMargins(0, 0, 0, 0)
        self.verticalSpacerHint1 = QSpacerItem(0, 0, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayoutHint.addItem(self.verticalSpacerHint1)

        self.hintFrame = QFrame(self.hintFrameH)
        self.hintFrame.setObjectName(u"hintFrame")
        self.hintFrame.setMinimumSize(QSize(880, 660))
        self.hintFrame.setStyleSheet(u"QLabel#operator_content_label{\n"
"	font-size:13pt;\n"
"	line-height:20px;\n"
"}\n"
"QLabel#operator_title_label{\n"
"	font-size:16pt;\n"
"	font-weight:bold;\n"
"}")
        self.operator_title_label = QLabel(self.hintFrame)
        self.operator_title_label.setObjectName(u"operator_title_label")
        self.operator_title_label.setGeometry(QRect(50, 30, 101, 41))
        self.operator_content_label = QLabel(self.hintFrame)
        self.operator_content_label.setObjectName(u"operator_content_label")
        self.operator_content_label.setGeometry(QRect(50, 80, 781, 461))
        self.operator_content_label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.operator_content_label.setWordWrap(True)

        self.verticalLayoutHint.addWidget(self.hintFrame)

        self.verticalSpacerHint2 = QSpacerItem(0, 0, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayoutHint.addItem(self.verticalSpacerHint2)


        self.horizontalLayoutHint.addWidget(self.hintFrameH)

        self.horizontalSpacerHint1 = QSpacerItem(0, 0, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayoutHint.addItem(self.horizontalSpacerHint1)


        self.gridLayoutHint.addWidget(self.hintFrameV, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.hintPage)

        self.verticalLayout_8.addWidget(self.stackedWidget)


        self.verticalLayout_4.addWidget(self.contentContainer)


        self.horizontalLayout.addWidget(self.contentFrame)


        self.gridLayout.addWidget(self.background, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.styleSheet)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"\u57fa\u4e8e\u5bf9\u6bd4\u5b66\u4e60\u7684\u8111\u7ed3\u6784\u78c1\u5171\u632f\u5f71\u50cf\u7279\u5f81\u63d0\u53d6\u7cfb\u7edf", None))
        self.iconLabel.setText("")
        self.extractButton.setText("")
        self.classificationButton.setText("")
        self.batchButton.setText("")
        self.hintButton.setText("")
        self.infoButton.setText("")
        self.settingButton.setText("")
        self.topLabel_2.setText(QCoreApplication.translate("MainWindow", u"MRI", None))
        self.extractLabel.setText(QCoreApplication.translate("MainWindow", u"\u7279\u5f81\u63d0\u53d6", None))
        self.classificationLabel.setText(QCoreApplication.translate("MainWindow", u"\u56fe\u50cf\u5206\u7c7b", None))
        self.batchLabel.setText(QCoreApplication.translate("MainWindow", u"\u6279\u91cf\u5904\u7406", None))
        self.hintLabel.setText(QCoreApplication.translate("MainWindow", u"\u76f8\u5173\u8bf4\u660e", None))
        self.label_4.setText("")
        self.settingLabel.setText(QCoreApplication.translate("MainWindow", u"\u8bbe\u7f6e", None))
        self.lineLabel.setText("")
        self.default_input_dir_label.setText(QCoreApplication.translate("MainWindow", u"\u9ed8\u8ba4\u8f93\u5165\u76ee\u5f55\uff1a", None))
        self.default_input_dir_lineEdit.setText("")
        self.default_output_dir_label.setText(QCoreApplication.translate("MainWindow", u"\u9ed8\u8ba4\u8f93\u51fa\u76ee\u5f55\uff1a", None))
        self.default_output_dir_lineEdit.setText("")
        self.setting_save_button.setText(QCoreApplication.translate("MainWindow", u"\u4fdd\u5b58", None))
        self.topLabel.setText(QCoreApplication.translate("MainWindow", u"\u57fa\u4e8e\u5bf9\u6bd4\u5b66\u4e60\u7684\u8111\u7ed3\u6784\u78c1\u5171\u632f\u5f71\u50cf\u7279\u5f81\u63d0\u53d6\u7cfb\u7edf", None))
        self.input_dir_label.setText(QCoreApplication.translate("MainWindow", u"\u5f85\u5904\u7406\u56fe\u50cf\u6240\u5728\u76ee\u5f55\uff1a", None))
        self.pushButton_input.setText(QCoreApplication.translate("MainWindow", u"\u9009\u62e9", None))
        self.lineEdit_input.setText("")
        self.lineEdit_input.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u8f93\u5165\u76ee\u5f55", None))
        self.output_dir_label.setText(QCoreApplication.translate("MainWindow", u"\u8f93\u51fa\u76ee\u5f55\uff1a", None))
        self.lineEdit_output.setText("")
        self.lineEdit_output.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u8f93\u51fa\u76ee\u5f55", None))
        self.pushButton_output.setText(QCoreApplication.translate("MainWindow", u"\u9009\u62e9", None))
        self.pushButton_batch_extract.setText(QCoreApplication.translate("MainWindow", u"\u7279\u5f81\u63d0\u53d6", None))
        self.pushButton_batch_predict.setText(QCoreApplication.translate("MainWindow", u"\u5206\u7c7b\u9884\u6d4b", None))
        self.batch_label_condition.setText(QCoreApplication.translate("MainWindow", u"\u5904\u7406\u4e2d...", None))
        self.batch_label_num.setText(QCoreApplication.translate("MainWindow", u"\u56fe\u50cf\u6570\u91cf\uff1a3600", None))
        self.pushButton_batch_read.setText(QCoreApplication.translate("MainWindow", u"\u8bfb\u53d6\u56fe\u50cf", None))
        self.axialLabel.setText("")
        self.saggitalLabel.setText("")
        self.coronalLabel.setText("")
        self.selectButton.setText(QCoreApplication.translate("MainWindow", u"\u9009\u62e9\u56fe\u50cf", None))
        self.label_name_contrainer.setText("")
        self.label_x.setText(QCoreApplication.translate("MainWindow", u"x\uff1a", None))
        self.label_y.setText(QCoreApplication.translate("MainWindow", u"y\uff1a", None))
        self.label_z.setText(QCoreApplication.translate("MainWindow", u"z\uff1a", None))
        self.start_extract_button.setText(QCoreApplication.translate("MainWindow", u"\u63d0\u53d6\u7279\u5f81", None))
        self.saveButton.setText(QCoreApplication.translate("MainWindow", u"\u4fdd\u5b58\u6587\u4ef6", None))
        self.axial_text_label.setText(QCoreApplication.translate("MainWindow", u"\u8f74\u4f4d\uff08Axial\uff09", None))
        self.saggital_text_label.setText(QCoreApplication.translate("MainWindow", u"\u77e2\u72b6\u4f4d\uff08Saggital\uff09", None))
        self.coronal_text_label.setText(QCoreApplication.translate("MainWindow", u"\u51a0\u72b6\u4f4d\uff08Coronal\uff09", None))
        self.label_x_range.setText(QCoreApplication.translate("MainWindow", u"\uff08\u5f85\u5b9a\uff09", None))
        self.label_y_range.setText(QCoreApplication.translate("MainWindow", u"\uff08\u5f85\u5b9a\uff09", None))
        self.label_z_range.setText(QCoreApplication.translate("MainWindow", u"\uff08\u5f85\u5b9a\uff09", None))
        self.extract_condition_label.setText(QCoreApplication.translate("MainWindow", u"\u63d0\u53d6\u4e2d...", None))
        self.label_name_label.setText(QCoreApplication.translate("MainWindow", u"\u5f53\u524d\u56fe\u50cf", None))
        self.label_name.setText(QCoreApplication.translate("MainWindow", u"mri_get_sdhjksa_fsm_\n"
"stdn_0001_gz.nii", None))
        self.start_classification_button.setText(QCoreApplication.translate("MainWindow", u"\u9884\u6d4b\u5206\u7c7b", None))
        self.classification_condition_label.setText(QCoreApplication.translate("MainWindow", u"\u9884\u6d4b\u4e2d...", None))
        self.heatmap_checkBox.setText(QCoreApplication.translate("MainWindow", u"\u5c55\u793a\u70ed\u529b\u56fe", None))
        self.operator_title_label.setText(QCoreApplication.translate("MainWindow", u"\u64cd\u4f5c\u8bf4\u660e", None))
        self.operator_content_label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p style='line-height: 125%;'><b>\u7279\u5f81\u63d0\u53d6\u754c\u9762\uff1a</b>\u7528\u4e8e\u5c06\u8111\u7ed3\u6784\u78c1\u5171\u632f\u56fe\u50cf\u8f6c\u6362\u4e3a\u5411\u91cf\u5f62\u5f0f\uff0c\u4f9b\u4e0b\u6e38\u4efb\u52a1\u4f7f\u7528\u3002\u70b9\u51fb\u9009\u62e9\u56fe\u50cf\u6309\u94ae\u9009\u62e9\u8981\u63d0\u53d6\u7279\u5f81\u7684\u56fe\u50cf\uff08nii\u6216gz\u683c\u5f0f\uff09\uff0c\u52a0\u8f7d\u56fe\u50cf\u540e\u53ef\u5728\u754c\u9762\u8fdb\u884c\u9884\u89c8\uff0c\u901a\u8fc7\u9009\u62e9x\uff0cy\uff0cz\u6765\u89c2\u5bdf\u4e0d\u540c\u7684\u5207\u7247\u3002\u70b9\u51fb\u63d0\u53d6\u7279\u5f81\u6309\u94ae\u8fdb\u884c\u7279\u5f81\u63d0\u53d6\uff0c\u7b49\u5f85\u63d0\u53d6\u5b8c\u6210\u3002\u63d0\u53d6\u5b8c\u6210\u540e\u70b9\u51fb\u4fdd\u5b58\u6587\u4ef6\u6309\u94ae\u5c06\u4ee5vector\u6587\u4ef6\u683c\u5f0f\u5c06\u5411\u91cf\u5f62\u5f0f\u7684\u7279\u5f81\u4fdd\u5b58\u3002</p><p style='line-height: 125%;'><b>\u56fe\u50cf\u5206\u7c7b\u754c\u9762\uff1a</b>\u52a0\u8f7d\u56fe\u50cf\u64cd\u4f5c\u540c"
                        "\u4e0a\u3002\u70b9\u51fb\u9884\u6d4b\u5206\u7c7b\u6309\u94ae\u53ef\u5bf9\u56fe\u50cf\u8fdb\u884c\u5206\u7c7b\uff0c\u7ed3\u679c\u5305\u62ecCN\uff08\u8ba4\u77e5\u6b63\u5e38\uff09\u3001MCI\uff08\u8f7b\u5ea6\u8ba4\u77e5\u969c\u788d\uff09\u3001AD\uff08\u8ba4\u77e5\u969c\u788d\uff09\u3002\u5206\u7c7b\u5b8c\u6210\u540e\uff0c\u901a\u8fc7\u52fe\u9009\u5c55\u793a\u70ed\u529b\u56fe\u590d\u9009\u6846\u53ef\u89c2\u5bdf\u6a21\u578b\u5bf9\u56fe\u50cf\u5404\u90e8\u5206\u5173\u6ce8\u7a0b\u5ea6\u7684\u70ed\u529b\u56fe\u3002</p><p style='line-height: 125%;'><b>\u6279\u91cf\u5904\u7406\u754c\u9762\uff1a</b>\u901a\u8fc7\u8bbe\u7f6e\u8f93\u5165\u548c\u8f93\u51fa\u76ee\u5f55\uff0c\u53ef\u8fdb\u884c\u6279\u91cf\u7279\u5f81\u63d0\u53d6\u548c\u5206\u7c7b\u3002</p></body></html>", None))
    # retranslateUi

