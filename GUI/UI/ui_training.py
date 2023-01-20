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
        self.data_tab = QWidget()
        self.data_tab.setObjectName(u"data_tab")
        self.verticalLayout_5 = QVBoxLayout(self.data_tab)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.training_graphs = QLabel(self.data_tab)
        self.training_graphs.setObjectName(u"training_graphs")

        self.verticalLayout_4.addWidget(self.training_graphs)

        self.Mathlibgraphs = QWidget(self.data_tab)
        self.Mathlibgraphs.setObjectName(u"Mathlibgraphs")
        self.Mathlibgraphs.setMinimumSize(QSize(500, 300))

        self.verticalLayout_4.addWidget(self.Mathlibgraphs)

        self.console_output_label = QLabel(self.data_tab)
        self.console_output_label.setObjectName(u"console_output_label")

        self.verticalLayout_4.addWidget(self.console_output_label)

        self.console_output_textbox = QTextEdit(self.data_tab)
        self.console_output_textbox.setObjectName(u"console_output_textbox")
        self.console_output_textbox.setReadOnly(True)

        self.verticalLayout_4.addWidget(self.console_output_textbox)

        self.label_4 = QLabel(self.data_tab)
        self.label_4.setObjectName(u"label_4")

        self.verticalLayout_4.addWidget(self.label_4)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.pushButton_3 = QPushButton(self.data_tab)
        self.pushButton_3.setObjectName(u"pushButton_3")

        self.horizontalLayout_5.addWidget(self.pushButton_3)


        self.verticalLayout_4.addLayout(self.horizontalLayout_5)


        self.verticalLayout_5.addLayout(self.verticalLayout_4)

        self.tabWidget.addTab(self.data_tab, "")
        self.image_viewer_tab = QWidget()
        self.image_viewer_tab.setObjectName(u"image_viewer_tab")
        self.tabWidget.addTab(self.image_viewer_tab, "")

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

        self.select_new_dataset_button = QPushButton(Form)
        self.select_new_dataset_button.setObjectName(u"select_new_dataset_button")
        self.select_new_dataset_button.setMinimumSize(QSize(0, 30))

        self.verticalLayout_3.addWidget(self.select_new_dataset_button)

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

        self.train_button = QPushButton(Form)
        self.train_button.setObjectName(u"train_button")
        self.train_button.setMinimumSize(QSize(0, 30))

        self.verticalLayout_3.addWidget(self.train_button)

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

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.training_graphs.setText(QCoreApplication.translate("Form", u"Training Graphs", None))
        self.console_output_label.setText(QCoreApplication.translate("Form", u"Console Output:", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"Options:", None))
        self.pushButton_3.setText(QCoreApplication.translate("Form", u"placeholder", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.data_tab), QCoreApplication.translate("Form", u"Data", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.image_viewer_tab), QCoreApplication.translate("Form", u"Image Viewer", None))
        self.select_new_dataset_button.setText(QCoreApplication.translate("Form", u"Run on new dataset...", None))
        self.label.setText(QCoreApplication.translate("Form", u"Number of Epochs:", None))
        self.train_button.setText(QCoreApplication.translate("Form", u"Train", None))
    # retranslateUi

