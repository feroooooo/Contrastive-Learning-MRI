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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QMainWindow, QPushButton, QSizePolicy, QSpacerItem,
    QStackedWidget, QVBoxLayout, QWidget)
import ui.resource_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1280, 720)
        MainWindow.setMinimumSize(QSize(960, 540))
        self.styleSheet = QWidget(MainWindow)
        self.styleSheet.setObjectName(u"styleSheet")
        self.styleSheet.setStyleSheet(u"QWidget#styleSheet{\n"
"	color: #dedede;\n"
"	background-color:#383838;\n"
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
"	background-color:#323232;\n"
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
"}")
        self.verticalLayout = QVBoxLayout(self.styleSheet)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
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

        self.hintButton = QPushButton(self.buttonFrame)
        self.hintButton.setObjectName(u"hintButton")
        sizePolicy2.setHeightForWidth(self.hintButton.sizePolicy().hasHeightForWidth())
        self.hintButton.setSizePolicy(sizePolicy2)
        self.hintButton.setMinimumSize(QSize(60, 60))
        self.hintButton.setMaximumSize(QSize(60, 60))
        self.hintButton.setCursor(QCursor(Qt.PointingHandCursor))
        icon2 = QIcon()
        icon2.addFile(u":/resource/img/hint.png", QSize(), QIcon.Normal, QIcon.Off)
        self.hintButton.setIcon(icon2)
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
        icon3 = QIcon()
        icon3.addFile(u":/resource/img/list.png", QSize(), QIcon.Normal, QIcon.Off)
        self.infoButton.setIcon(icon3)
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
        icon4 = QIcon()
        icon4.addFile(u":/resource/img/setting.png", QSize(), QIcon.Normal, QIcon.Off)
        self.settingButton.setIcon(icon4)
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
        font = QFont()
        font.setPointSize(16)
        font.setBold(True)
        self.topLabel_2.setFont(font)
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
        font1 = QFont()
        font1.setFamilies([u"Microsoft YaHei UI"])
        font1.setPointSize(16)
        font1.setBold(True)
        self.topLabel.setFont(font1)
        self.topLabel.setAlignment(Qt.AlignCenter)

        self.verticalLayout_4.addWidget(self.topLabel)

        self.contentContainer = QFrame(self.contentFrame)
        self.contentContainer.setObjectName(u"contentContainer")
        self.contentContainer.setFrameShape(QFrame.StyledPanel)
        self.contentContainer.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.contentContainer)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.stackedWidget = QStackedWidget(self.contentContainer)
        self.stackedWidget.setObjectName(u"stackedWidget")
        font2 = QFont()
        font2.setKerning(True)
        self.stackedWidget.setFont(font2)
        self.stackedWidget.setStyleSheet(u"color:#dedede;")
        self.classificationPage = QWidget()
        self.classificationPage.setObjectName(u"classificationPage")
        self.label = QLabel(self.classificationPage)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(440, 330, 111, 16))
        self.stackedWidget.addWidget(self.classificationPage)
        self.extractPage = QWidget()
        self.extractPage.setObjectName(u"extractPage")
        self.label_2 = QLabel(self.extractPage)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(420, 310, 54, 16))
        self.stackedWidget.addWidget(self.extractPage)
        self.hintPage = QWidget()
        self.hintPage.setObjectName(u"hintPage")
        self.label_3 = QLabel(self.hintPage)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(580, 320, 54, 16))
        self.stackedWidget.addWidget(self.hintPage)

        self.verticalLayout_8.addWidget(self.stackedWidget)


        self.verticalLayout_4.addWidget(self.contentContainer)


        self.horizontalLayout.addWidget(self.contentFrame)


        self.verticalLayout.addWidget(self.background)

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
        self.hintButton.setText("")
        self.infoButton.setText("")
        self.settingButton.setText("")
        self.topLabel_2.setText(QCoreApplication.translate("MainWindow", u"MRI", None))
        self.extractLabel.setText(QCoreApplication.translate("MainWindow", u"\u7279\u5f81\u63d0\u53d6", None))
        self.classificationLabel.setText(QCoreApplication.translate("MainWindow", u"\u56fe\u50cf\u5206\u7c7b", None))
        self.hintLabel.setText(QCoreApplication.translate("MainWindow", u"\u76f8\u5173\u8bf4\u660e", None))
        self.label_4.setText("")
        self.settingLabel.setText(QCoreApplication.translate("MainWindow", u"\u8bbe\u7f6e", None))
        self.lineLabel.setText("")
        self.topLabel.setText(QCoreApplication.translate("MainWindow", u"\u57fa\u4e8e\u5bf9\u6bd4\u5b66\u4e60\u7684\u8111\u7ed3\u6784\u78c1\u5171\u632f\u5f71\u50cf\u7279\u5f81\u63d0\u53d6\u7cfb\u7edf", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"classification", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"extract", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Hint", None))
    # retranslateUi

