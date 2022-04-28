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
        PopUpBracketCheck.resize(400, 300)
        icon = QIcon()
        icon.addFile(u"icons/warning.png", QSize(), QIcon.Normal, QIcon.Off)
        PopUpBracketCheck.setWindowIcon(icon)
        self.pb_popup_OK = QDialogButtonBox(PopUpBracketCheck)
        self.pb_popup_OK.setObjectName(u"pb_popup_OK")
        self.pb_popup_OK.setGeometry(QRect(30, 240, 341, 32))
        self.pb_popup_OK.setOrientation(Qt.Horizontal)
        self.pb_popup_OK.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)
        self.tb_popup = QTextBrowser(PopUpBracketCheck)
        self.tb_popup.setObjectName(u"tb_popup")
        self.tb_popup.setGeometry(QRect(10, 10, 341, 211))

        self.retranslateUi(PopUpBracketCheck)
        self.pb_popup_OK.accepted.connect(PopUpBracketCheck.accept)
        self.pb_popup_OK.rejected.connect(PopUpBracketCheck.reject)

        QMetaObject.connectSlotsByName(PopUpBracketCheck)
    # setupUi

    def retranslateUi(self, PopUpBracketCheck):
        PopUpBracketCheck.setWindowTitle(QCoreApplication.translate("PopUpBracketCheck", u"Klammercheck Fehler", None))
    # retranslateUi

