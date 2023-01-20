# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'create_train_menu.ui'
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QPushButton,
    QSizePolicy, QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(416, 301)
        self.horizontalLayout_2 = QHBoxLayout(Form)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.select_model_text = QLabel(Form)
        self.select_model_text.setObjectName(u"select_model_text")
        self.select_model_text.setWordWrap(True)

        self.horizontalLayout_5.addWidget(self.select_model_text)

        self.select_model_button = QPushButton(Form)
        self.select_model_button.setObjectName(u"select_model_button")

        self.horizontalLayout_5.addWidget(self.select_model_button)

        self.horizontalLayout_5.setStretch(0, 1)
        self.horizontalLayout_5.setStretch(1, 1)

        self.verticalLayout.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.select_dataset_text = QLabel(Form)
        self.select_dataset_text.setObjectName(u"select_dataset_text")

        self.horizontalLayout_4.addWidget(self.select_dataset_text)

        self.select_dataset_button = QPushButton(Form)
        self.select_dataset_button.setObjectName(u"select_dataset_button")

        self.horizontalLayout_4.addWidget(self.select_dataset_button)


        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.start_button = QPushButton(Form)
        self.start_button.setObjectName(u"start_button")

        self.verticalLayout.addWidget(self.start_button)


        self.horizontalLayout.addLayout(self.verticalLayout)


        self.horizontalLayout_2.addLayout(self.horizontalLayout)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.select_model_text.setText(QCoreApplication.translate("Form", u"None Selected", None))
        self.select_model_button.setText(QCoreApplication.translate("Form", u"(Optional) Select Model", None))
        self.select_dataset_text.setText(QCoreApplication.translate("Form", u"None Selected", None))
        self.select_dataset_button.setText(QCoreApplication.translate("Form", u"(Optional) Select Dataset", None))
        self.start_button.setText(QCoreApplication.translate("Form", u"Start", None))
    # retranslateUi

