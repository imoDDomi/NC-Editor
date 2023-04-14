# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'popup.ui'
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
from PySide6.QtWidgets import (QAbstractButton, QApplication, QDialog, QDialogButtonBox,
    QSizePolicy, QTextBrowser, QWidget)

class Ui_PopUpBracketCheck(object):
    def setupUi(self, PopUpBracketCheck):
        if not PopUpBracketCheck.objectName():
            PopUpBracketCheck.setObjectName(u"PopUpBracketCheck")
        PopUpBracketCheck.resize(384, 272)
        icon = QIcon()
        icon.addFile(u"icons/alert.png", QSize(), QIcon.Normal, QIcon.Off)
        PopUpBracketCheck.setWindowIcon(icon)
        self.pb_popup_OK = QDialogButtonBox(PopUpBracketCheck)
        self.pb_popup_OK.setObjectName(u"pb_popup_OK")
        self.pb_popup_OK.setGeometry(QRect(30, 230, 341, 32))
        self.pb_popup_OK.setOrientation(Qt.Horizontal)
        self.pb_popup_OK.setStandardButtons(QDialogButtonBox.Ok)
        self.tb_popup = QTextBrowser(PopUpBracketCheck)
        self.tb_popup.setObjectName(u"tb_popup")
        self.tb_popup.setGeometry(QRect(0, 0, 391, 281))
        font = QFont()
        font.setFamilies([u"Courier New"])
        font.setPointSize(12)
        font.setBold(True)
        self.tb_popup.setFont(font)
        self.tb_popup.raise_()
        self.pb_popup_OK.raise_()

        self.retranslateUi(PopUpBracketCheck)
        self.pb_popup_OK.accepted.connect(PopUpBracketCheck.accept)
        self.pb_popup_OK.rejected.connect(PopUpBracketCheck.reject)

        QMetaObject.connectSlotsByName(PopUpBracketCheck)
    # setupUi

    def retranslateUi(self, PopUpBracketCheck):
        PopUpBracketCheck.setWindowTitle(QCoreApplication.translate("PopUpBracketCheck", u"Klammercheck Fehler", None))
        self.tb_popup.setHtml(QCoreApplication.translate("PopUpBracketCheck", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"</style></head><body style=\" font-family:'Courier New'; font-size:12pt; font-weight:700; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
    # retranslateUi

