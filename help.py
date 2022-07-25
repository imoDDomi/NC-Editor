# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'help.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QPlainTextEdit, QSizePolicy,
    QVBoxLayout, QWidget)

class Ui_Hilfe(object):
    def setupUi(self, Hilfe):
        if not Hilfe.objectName():
            Hilfe.setObjectName(u"Hilfe")
        Hilfe.resize(898, 549)
        icon = QIcon()
        icon.addFile(u"icons/fragezeichen.png", QSize(), QIcon.Normal, QIcon.Off)
        Hilfe.setWindowIcon(icon)
        Hilfe.setStyleSheet(u"QDialog{\n"
"background-color: rgb(255,255,255);\n"
"}")
        self.verticalLayout = QVBoxLayout(Hilfe)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.helptext = QPlainTextEdit(Hilfe)
        self.helptext.setObjectName(u"helptext")
        self.helptext.viewport().setProperty("cursor", QCursor(Qt.ArrowCursor))
        self.helptext.setStyleSheet(u"QPlainTextEdit{\n"
"border: 0;\n"
"}")
        self.helptext.setReadOnly(True)

        self.verticalLayout.addWidget(self.helptext)


        self.retranslateUi(Hilfe)

        QMetaObject.connectSlotsByName(Hilfe)
    # setupUi

    def retranslateUi(self, Hilfe):
        Hilfe.setWindowTitle(QCoreApplication.translate("Hilfe", u"Hilfe", None))
    # retranslateUi

