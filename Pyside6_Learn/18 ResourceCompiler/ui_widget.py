# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.7.1
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QPushButton, QSizePolicy,
    QSpinBox, QWidget)

class Ui_Widget(object):
    def setupUi(self, Widget):
        if not Widget.objectName():
            Widget.setObjectName(u"Widget")
        Widget.resize(338, 45)
        self.horizontalLayout = QHBoxLayout(Widget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.plus_button = QPushButton(Widget)
        self.plus_button.setObjectName(u"plus_button")

        self.horizontalLayout.addWidget(self.plus_button)

        self.spin_box = QSpinBox(Widget)
        self.spin_box.setObjectName(u"spin_box")

        self.horizontalLayout.addWidget(self.spin_box)

        self.minus_button = QPushButton(Widget)
        self.minus_button.setObjectName(u"minus_button")

        self.horizontalLayout.addWidget(self.minus_button)


        self.retranslateUi(Widget)

        QMetaObject.connectSlotsByName(Widget)
    # setupUi

    def retranslateUi(self, Widget):
        Widget.setWindowTitle(QCoreApplication.translate("Widget", u"Widget", None))
        self.plus_button.setText(QCoreApplication.translate("Widget", u"Plus", None))
        self.minus_button.setText(QCoreApplication.translate("Widget", u"Minus", None))
    # retranslateUi

