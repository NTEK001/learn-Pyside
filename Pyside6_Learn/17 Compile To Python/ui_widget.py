# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'widget.ui'
##
## Created by: Qt User Interface Compiler version 6.7.0
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(400, 300)
        self.widget = QWidget(Form)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(101, 92, 212, 99))
        self.verticalLayout_3 = QVBoxLayout(self.widget)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.fullname_label = QLabel(self.widget)
        self.fullname_label.setObjectName(u"fullname_label")

        self.verticalLayout_2.addWidget(self.fullname_label)

        self.occupation_label = QLabel(self.widget)
        self.occupation_label.setObjectName(u"occupation_label")

        self.verticalLayout_2.addWidget(self.occupation_label)


        self.horizontalLayout.addLayout(self.verticalLayout_2)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.fullname_lineedit = QLineEdit(self.widget)
        self.fullname_lineedit.setObjectName(u"fullname_lineedit")

        self.verticalLayout.addWidget(self.fullname_lineedit)

        self.occupation_lineedit = QLineEdit(self.widget)
        self.occupation_lineedit.setObjectName(u"occupation_lineedit")

        self.verticalLayout.addWidget(self.occupation_lineedit)


        self.horizontalLayout.addLayout(self.verticalLayout)


        self.verticalLayout_3.addLayout(self.horizontalLayout)

        self.submit_button = QPushButton(self.widget)
        self.submit_button.setObjectName(u"submit_button")

        self.verticalLayout_3.addWidget(self.submit_button)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.fullname_label.setText(QCoreApplication.translate("Form", u"Full Name", None))
        self.occupation_label.setText(QCoreApplication.translate("Form", u"Occupation", None))
        self.submit_button.setText(QCoreApplication.translate("Form", u"Submit", None))
    # retranslateUi

