# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'nc_editor.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QGridLayout, QGroupBox,
    QLabel, QLineEdit, QMainWindow, QPushButton,
    QSizePolicy, QSpacerItem, QSpinBox, QStatusBar,
    QTextBrowser, QVBoxLayout, QWidget)

class Ui_Hauptfenster(object):
    def setupUi(self, Hauptfenster):
        if not Hauptfenster.objectName():
            Hauptfenster.setObjectName(u"Hauptfenster")
        Hauptfenster.resize(1000, 700)
        self.centralwidget = QWidget(Hauptfenster)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.le_input = QLineEdit(self.centralwidget)
        self.le_input.setObjectName(u"le_input")
        self.le_input.setEnabled(True)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.le_input.sizePolicy().hasHeightForWidth())
        self.le_input.setSizePolicy(sizePolicy)
        self.le_input.setMinimumSize(QSize(0, 0))
        self.le_input.setBaseSize(QSize(0, 0))
        self.le_input.setLayoutDirection(Qt.LeftToRight)
        self.le_input.setReadOnly(True)

        self.gridLayout.addWidget(self.le_input, 0, 0, 1, 2)

        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(u"groupBox")
        self.gridLayout_2 = QGridLayout(self.groupBox)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.textBrowser = QTextBrowser(self.groupBox)
        self.textBrowser.setObjectName(u"textBrowser")

        self.gridLayout_2.addWidget(self.textBrowser, 3, 0, 1, 5)

        self.lb_schrittweite = QLabel(self.groupBox)
        self.lb_schrittweite.setObjectName(u"lb_schrittweite")

        self.gridLayout_2.addWidget(self.lb_schrittweite, 1, 1, 1, 1)

        self.sb_schrittweite = QSpinBox(self.groupBox)
        self.sb_schrittweite.setObjectName(u"sb_schrittweite")
        self.sb_schrittweite.setMinimum(0)
        self.sb_schrittweite.setMaximum(1000)
        self.sb_schrittweite.setValue(10)

        self.gridLayout_2.addWidget(self.sb_schrittweite, 1, 2, 1, 1)

        self.lb_startnummer = QLabel(self.groupBox)
        self.lb_startnummer.setObjectName(u"lb_startnummer")

        self.gridLayout_2.addWidget(self.lb_startnummer, 0, 1, 1, 1)

        self.sb_startnummer = QSpinBox(self.groupBox)
        self.sb_startnummer.setObjectName(u"sb_startnummer")
        self.sb_startnummer.setMaximum(10000)
        self.sb_startnummer.setSingleStep(100)
        self.sb_startnummer.setValue(1000)

        self.gridLayout_2.addWidget(self.sb_startnummer, 0, 2, 1, 1)

        self.cb_satznummern = QCheckBox(self.groupBox)
        self.cb_satznummern.setObjectName(u"cb_satznummern")

        self.gridLayout_2.addWidget(self.cb_satznummern, 0, 0, 1, 1)

        self.cb_klammern = QCheckBox(self.groupBox)
        self.cb_klammern.setObjectName(u"cb_klammern")

        self.gridLayout_2.addWidget(self.cb_klammern, 1, 0, 1, 1)

        self.pb_check_program = QPushButton(self.groupBox)
        self.pb_check_program.setObjectName(u"pb_check_program")

        self.gridLayout_2.addWidget(self.pb_check_program, 2, 2, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer, 1, 3, 1, 1)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_3, 2, 3, 1, 2)


        self.gridLayout.addWidget(self.groupBox, 3, 0, 1, 3)

        self.le_output = QLineEdit(self.centralwidget)
        self.le_output.setObjectName(u"le_output")
        self.le_output.setEnabled(True)
        self.le_output.setReadOnly(True)

        self.gridLayout.addWidget(self.le_output, 2, 0, 1, 2)

        self.pb_quelle = QPushButton(self.centralwidget)
        self.pb_quelle.setObjectName(u"pb_quelle")
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.pb_quelle.sizePolicy().hasHeightForWidth())
        self.pb_quelle.setSizePolicy(sizePolicy1)
        self.pb_quelle.setMinimumSize(QSize(100, 0))
        self.pb_quelle.setMaximumSize(QSize(100, 50))

        self.gridLayout.addWidget(self.pb_quelle, 0, 2, 1, 1)

        self.pb_save_as = QPushButton(self.centralwidget)
        self.pb_save_as.setObjectName(u"pb_save_as")

        self.gridLayout.addWidget(self.pb_save_as, 2, 2, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout)

        Hauptfenster.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(Hauptfenster)
        self.statusbar.setObjectName(u"statusbar")
        Hauptfenster.setStatusBar(self.statusbar)

        self.retranslateUi(Hauptfenster)

        QMetaObject.connectSlotsByName(Hauptfenster)
    # setupUi

    def retranslateUi(self, Hauptfenster):
        Hauptfenster.setWindowTitle(QCoreApplication.translate("Hauptfenster", u"MainWindow", None))
        self.le_input.setText("")
        self.le_input.setPlaceholderText(QCoreApplication.translate("Hauptfenster", u"NC Programm Input", None))
        self.groupBox.setTitle(QCoreApplication.translate("Hauptfenster", u"Einstellungen", None))
        self.textBrowser.setPlaceholderText(QCoreApplication.translate("Hauptfenster", u"Datei Vorschau", None))
        self.lb_schrittweite.setText(QCoreApplication.translate("Hauptfenster", u"Schrittweite", None))
        self.lb_startnummer.setText(QCoreApplication.translate("Hauptfenster", u"Startnummer", None))
        self.cb_satznummern.setText(QCoreApplication.translate("Hauptfenster", u"Satznummer", None))
        self.cb_klammern.setText(QCoreApplication.translate("Hauptfenster", u"Klammern", None))
        self.pb_check_program.setText(QCoreApplication.translate("Hauptfenster", u"Check NC-Programm", None))
        self.le_output.setPlaceholderText(QCoreApplication.translate("Hauptfenster", u"NC Programm Output", None))
        self.pb_quelle.setText(QCoreApplication.translate("Hauptfenster", u"Quelle", None))
        self.pb_save_as.setText(QCoreApplication.translate("Hauptfenster", u"Speichern unter", None))
    # retranslateUi

