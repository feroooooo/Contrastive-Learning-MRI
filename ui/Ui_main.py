# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 6.6.0
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
    QHBoxLayout, QLabel, QMainWindow, QPushButton,
    QSizePolicy, QSpacerItem, QSpinBox, QStackedWidget,
    QVBoxLayout, QWidget)
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
        font2 = QFont()
        font2.setFamilies([u"Microsoft YaHei UI"])
        font2.setPointSize(16)
        font2.setBold(True)
        self.topLabel.setFont(font2)
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
        font3 = QFont()
        font3.setKerning(True)
        self.stackedWidget.setFont(font3)
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
        self.batchFrame.setStyleSheet(u"")
        self.batch_label_temp = QLabel(self.batchFrame)
        self.batch_label_temp.setObjectName(u"batch_label_temp")
        self.batch_label_temp.setGeometry(QRect(40, 30, 200, 200))

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
        font4 = QFont()
        font4.setPointSize(13)
        self.label_name_contrainer.setFont(font4)
        self.label_name_contrainer.setStyleSheet(u"background-color:#1b1b1b;border-radius:30px;")
        self.label_name_contrainer.setScaledContents(True)
        self.label_name_contrainer.setAlignment(Qt.AlignBottom|Qt.AlignHCenter)
        self.label_name_contrainer.setWordWrap(True)
        self.spinBox_x = QSpinBox(self.extractFrame)
        self.spinBox_x.setObjectName(u"spinBox_x")
        self.spinBox_x.setGeometry(QRect(120, 414, 60, 30))
        font5 = QFont()
        font5.setPointSize(14)
        self.spinBox_x.setFont(font5)
        self.spinBox_x.setAlignment(Qt.AlignCenter)
        self.spinBox_x.setMinimum(1)
        self.spinBox_x.setMaximum(1)
        self.spinBox_y = QSpinBox(self.extractFrame)
        self.spinBox_y.setObjectName(u"spinBox_y")
        self.spinBox_y.setGeometry(QRect(120, 459, 60, 30))
        self.spinBox_y.setFont(font5)
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
        font6 = QFont()
        font6.setPointSize(20)
        self.label_x.setFont(font6)
        self.label_y = QLabel(self.extractFrame)
        self.label_y.setObjectName(u"label_y")
        self.label_y.setGeometry(QRect(70, 451, 30, 40))
        self.label_y.setFont(font6)
        self.label_z = QLabel(self.extractFrame)
        self.label_z.setObjectName(u"label_z")
        self.label_z.setGeometry(QRect(70, 496, 30, 40))
        self.label_z.setFont(font6)
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
        font7 = QFont()
        font7.setPointSize(17)
        self.label_x_range.setFont(font7)
        self.label_y_range = QLabel(self.extractFrame)
        self.label_y_range.setObjectName(u"label_y_range")
        self.label_y_range.setGeometry(QRect(200, 453, 101, 40))
        self.label_y_range.setFont(font7)
        self.label_z_range = QLabel(self.extractFrame)
        self.label_z_range.setObjectName(u"label_z_range")
        self.label_z_range.setGeometry(QRect(200, 498, 101, 40))
        self.label_z_range.setFont(font7)
        self.extract_condition_label = QLabel(self.extractFrame)
        self.extract_condition_label.setObjectName(u"extract_condition_label")
        self.extract_condition_label.setGeometry(QRect(675, 305, 131, 41))
        font8 = QFont()
        font8.setPointSize(16)
        self.extract_condition_label.setFont(font8)
        self.extract_condition_label.setAlignment(Qt.AlignCenter)
        self.label_name_label = QLabel(self.extractFrame)
        self.label_name_label.setObjectName(u"label_name_label")
        self.label_name_label.setGeometry(QRect(135, 553, 81, 21))
        font9 = QFont()
        font9.setPointSize(13)
        font9.setBold(True)
        self.label_name_label.setFont(font9)
        self.label_name_label.setStyleSheet(u"background-color:transparent;")
        self.label_name_label.setScaledContents(True)
        self.label_name_label.setAlignment(Qt.AlignCenter)
        self.label_name_label.setWordWrap(True)
        self.label_name = QLabel(self.extractFrame)
        self.label_name.setObjectName(u"label_name")
        self.label_name.setGeometry(QRect(50, 584, 250, 48))
        self.label_name.setFont(font4)
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
        self.classification_condition_label.setFont(font8)
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
        self.hintFrame.setStyleSheet(u"")
        self.hintLabel_temp = QLabel(self.hintFrame)
        self.hintLabel_temp.setObjectName(u"hintLabel_temp")
        self.hintLabel_temp.setGeometry(QRect(40, 30, 200, 200))

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

        self.stackedWidget.setCurrentIndex(1)


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
        self.topLabel.setText(QCoreApplication.translate("MainWindow", u"\u57fa\u4e8e\u5bf9\u6bd4\u5b66\u4e60\u7684\u8111\u7ed3\u6784\u78c1\u5171\u632f\u5f71\u50cf\u7279\u5f81\u63d0\u53d6\u7cfb\u7edf", None))
        self.batch_label_temp.setText(QCoreApplication.translate("MainWindow", u"batch", None))
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
        self.axial_text_label.setText(QCoreApplication.translate("MainWindow", u"\u8f74\u72b6\u4f4d\uff08Axial\uff09", None))
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
        self.hintLabel_temp.setText(QCoreApplication.translate("MainWindow", u"hint", None))
    # retranslateUi

