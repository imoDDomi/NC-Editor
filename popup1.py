# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'popup1.ui'
##
## Created by: Qt User Interface Compiler version 6.3.0
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
from PySide6.QtWidgets import (QApplication, QDialog, QPushButton, QSizePolicy,
    QTextBrowser, QWidget)

class Ui_popup1(object):
    def setupUi(self, popup1):
        if not popup1.objectName():
            popup1.setObjectName(u"popup1")
        popup1.resize(320, 229)
        self.popup_textbrowser = QTextBrowser(popup1)
        self.popup_textbrowser.setObjectName(u"popup_textbrowser")
        self.popup_textbrowser.setGeometry(QRect(10, 10, 301, 181))
        font = QFont()
        font.setPointSize(10)
        font.setBold(True)
        self.popup_textbrowser.setFont(font)
        self.pb_popup_OK = QPushButton(popup1)
        self.pb_popup_OK.setObjectName(u"pb_popup_OK")
        self.pb_popup_OK.setGeometry(QRect(240, 200, 75, 24))

        self.retranslateUi(popup1)

        QMetaObject.connectSlotsByName(popup1)
    # setupUi

    def retranslateUi(self, popup1):
        popup1.setWindowTitle(QCoreApplication.translate("popup1", u"Fehler Klammerncheck", None))
        self.pb_popup_OK.setText(QCoreApplication.translate("popup1", u"OK", None))
    # retranslateUi

