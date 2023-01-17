# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'training.ui'
##
## Created by: Qt User Interface Compiler version 6.4.0
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QProgressBar,
    QPushButton, QSizePolicy, QSpacerItem, QTabWidget,
    QTextEdit, QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(936, 607)
        self.horizontalLayout_2 = QHBoxLayout(Form)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.tabWidget = QTabWidget(Form)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setMinimumSize(QSize(600, 400))
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.verticalLayout_5 = QVBoxLayout(self.tab_3)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label_3 = QLabel(self.tab_3)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout_4.addWidget(self.label_3)

        self.Mathlibgraphs = QWidget(self.tab_3)
        self.Mathlibgraphs.setObjectName(u"Mathlibgraphs")
        self.Mathlibgraphs.setMinimumSize(QSize(500, 300))

        self.verticalLayout_4.addWidget(self.Mathlibgraphs)

        self.label_2 = QLabel(self.tab_3)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout_4.addWidget(self.label_2)

        self.textEdit_2 = QTextEdit(self.tab_3)
        self.textEdit_2.setObjectName(u"textEdit_2")
        self.textEdit_2.setReadOnly(True)

        self.verticalLayout_4.addWidget(self.textEdit_2)

        self.label_4 = QLabel(self.tab_3)
        self.label_4.setObjectName(u"label_4")

        self.verticalLayout_4.addWidget(self.label_4)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.pushButton_3 = QPushButton(self.tab_3)
        self.pushButton_3.setObjectName(u"pushButton_3")

        self.horizontalLayout_5.addWidget(self.pushButton_3)


        self.verticalLayout_4.addLayout(self.horizontalLayout_5)


        self.verticalLayout_5.addLayout(self.verticalLayout_4)

        self.tabWidget.addTab(self.tab_3, "")
        self.tab_4 = QWidget()
        self.tab_4.setObjectName(u"tab_4")
        self.tabWidget.addTab(self.tab_4, "")

        self.horizontalLayout.addWidget(self.tabWidget)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.HighestConfidenceImages = QWidget(Form)
        self.HighestConfidenceImages.setObjectName(u"HighestConfidenceImages")
        self.HighestConfidenceImages.setMinimumSize(QSize(150, 300))

        self.horizontalLayout_3.addWidget(self.HighestConfidenceImages)

        self.WorstConfidenceImages = QWidget(Form)
        self.WorstConfidenceImages.setObjectName(u"WorstConfidenceImages")
        self.WorstConfidenceImages.setMinimumSize(QSize(150, 300))

        self.horizontalLayout_3.addWidget(self.WorstConfidenceImages)


        self.verticalLayout_2.addLayout(self.horizontalLayout_3)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer)

        self.pushButton = QPushButton(Form)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMinimumSize(QSize(0, 30))

        self.verticalLayout_3.addWidget(self.pushButton)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer_2)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer)

        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        self.label.setMaximumSize(QSize(150, 30))

        self.horizontalLayout_4.addWidget(self.label)

        self.textEdit = QTextEdit(Form)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setMaximumSize(QSize(80, 29))

        self.horizontalLayout_4.addWidget(self.textEdit)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_2)


        self.verticalLayout_3.addLayout(self.horizontalLayout_4)

        self.pushButton_2 = QPushButton(Form)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setMinimumSize(QSize(0, 30))

        self.verticalLayout_3.addWidget(self.pushButton_2)

        self.progressBar = QProgressBar(Form)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setValue(24)

        self.verticalLayout_3.addWidget(self.progressBar)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer_3)


        self.verticalLayout_2.addLayout(self.verticalLayout_3)


        self.horizontalLayout.addLayout(self.verticalLayout_2)

        self.horizontalLayout.setStretch(0, 4)
        self.horizontalLayout.setStretch(1, 2)

        self.horizontalLayout_2.addLayout(self.horizontalLayout)


        self.retranslateUi(Form)

        self.tabWidget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"Training Graphs", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"Console Output:", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"Options:", None))
        self.pushButton_3.setText(QCoreApplication.translate("Form", u"placeholder", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), QCoreApplication.translate("Form", u"Data", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), QCoreApplication.translate("Form", u"Image Viewer", None))
        self.pushButton.setText(QCoreApplication.translate("Form", u"Run on new dataset...", None))
        self.label.setText(QCoreApplication.translate("Form", u"Number of Epochs:", None))
        self.pushButton_2.setText(QCoreApplication.translate("Form", u"Train", None))
    # retranslateUi

