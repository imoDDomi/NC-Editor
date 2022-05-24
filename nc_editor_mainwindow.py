# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'nc_editor_mainwindow.ui'
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
    QRadioButton, QSizePolicy, QSpacerItem, QSpinBox,
    QStatusBar, QTextBrowser, QVBoxLayout, QWidget)

class Ui_Hauptfenster(object):
    def setupUi(self, Hauptfenster):
        if not Hauptfenster.objectName():
            Hauptfenster.setObjectName(u"Hauptfenster")
        Hauptfenster.resize(1131, 789)
        icon = QIcon()
        icon.addFile(u"icons/lvt.png", QSize(), QIcon.Normal, QIcon.Off)
        Hauptfenster.setWindowIcon(icon)
        Hauptfenster.setStyleSheet(u"")
        self.centralwidget = QWidget(Hauptfenster)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.rb_directory = QRadioButton(self.centralwidget)
        self.rb_directory.setObjectName(u"rb_directory")

        self.gridLayout.addWidget(self.rb_directory, 2, 2, 1, 1)

        self.pb_quelle = QPushButton(self.centralwidget)
        self.pb_quelle.setObjectName(u"pb_quelle")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pb_quelle.sizePolicy().hasHeightForWidth())
        self.pb_quelle.setSizePolicy(sizePolicy)
        self.pb_quelle.setMinimumSize(QSize(100, 0))
        self.pb_quelle.setMaximumSize(QSize(100, 50))
        self.pb_quelle.setStyleSheet(u"")

        self.gridLayout.addWidget(self.pb_quelle, 0, 4, 1, 1)

        self.pb_save_as = QPushButton(self.centralwidget)
        self.pb_save_as.setObjectName(u"pb_save_as")
        self.pb_save_as.setStyleSheet(u"")

        self.gridLayout.addWidget(self.pb_save_as, 2, 4, 1, 1)

        self.rb_file = QRadioButton(self.centralwidget)
        self.rb_file.setObjectName(u"rb_file")
        self.rb_file.setChecked(True)

        self.gridLayout.addWidget(self.rb_file, 0, 2, 1, 1)

        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setEnabled(True)
        self.groupBox.setStyleSheet(u"color: rgb(0, 0, 0);")
        self.gridLayout_2 = QGridLayout(self.groupBox)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.cb_ids = QCheckBox(self.groupBox)
        self.cb_ids.setObjectName(u"cb_ids")
        self.cb_ids.setStyleSheet(u"color: rgb(0, 0, 0);")

        self.gridLayout_2.addWidget(self.cb_ids, 2, 0, 1, 1)

        self.lb_schrittweite = QLabel(self.groupBox)
        self.lb_schrittweite.setObjectName(u"lb_schrittweite")
        self.lb_schrittweite.setStyleSheet(u"color: rgb(0, 0, 0);")

        self.gridLayout_2.addWidget(self.lb_schrittweite, 1, 1, 1, 1)

        self.cb_satznummern = QCheckBox(self.groupBox)
        self.cb_satznummern.setObjectName(u"cb_satznummern")
        self.cb_satznummern.setStyleSheet(u"color: rgb(0, 0, 0);")
        self.cb_satznummern.setChecked(True)

        self.gridLayout_2.addWidget(self.cb_satznummern, 0, 0, 1, 1)

        self.pb_check_program = QPushButton(self.groupBox)
        self.pb_check_program.setObjectName(u"pb_check_program")
        self.pb_check_program.setStyleSheet(u"*{\n"
"	color: rgb(0, 0, 0);\n"
"	background-color: rgb(255, 255, 0);\n"
"	border-style: solid;\n"
"	border-color: rgb(255, 255, 0);\n"
"	border-width: 2px;\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"\n"
"\n"
":hover{\n"
"color:#000000;\n"
"background-color: rgb(200, 200, 0);\n"
"border-color: rgb(200, 200, 0);\n"
"}\n"
"\n"
"")

        self.gridLayout_2.addWidget(self.pb_check_program, 2, 2, 1, 1)

        self.sb_startnummer = QSpinBox(self.groupBox)
        self.sb_startnummer.setObjectName(u"sb_startnummer")
        self.sb_startnummer.setStyleSheet(u"color: rgb(0, 0, 0);")
        self.sb_startnummer.setMaximum(10000)
        self.sb_startnummer.setSingleStep(100)
        self.sb_startnummer.setValue(1000)

        self.gridLayout_2.addWidget(self.sb_startnummer, 0, 2, 1, 1)

        self.textBrowser = QTextBrowser(self.groupBox)
        self.textBrowser.setObjectName(u"textBrowser")
        font = QFont()
        font.setFamilies([u"Courier New"])
        font.setPointSize(10)
        font.setBold(True)
        self.textBrowser.setFont(font)
        self.textBrowser.setStyleSheet(u"")
        self.textBrowser.setReadOnly(True)
        self.textBrowser.setOverwriteMode(False)

        self.gridLayout_2.addWidget(self.textBrowser, 4, 0, 1, 5)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer, 1, 3, 1, 1)

        self.cb_klammern = QCheckBox(self.groupBox)
        self.cb_klammern.setObjectName(u"cb_klammern")
        self.cb_klammern.setStyleSheet(u"color: rgb(0, 0, 0);")
        self.cb_klammern.setChecked(True)

        self.gridLayout_2.addWidget(self.cb_klammern, 1, 0, 1, 1)

        self.lb_startnummer = QLabel(self.groupBox)
        self.lb_startnummer.setObjectName(u"lb_startnummer")
        self.lb_startnummer.setStyleSheet(u"color: rgb(0, 0, 0);")

        self.gridLayout_2.addWidget(self.lb_startnummer, 0, 1, 1, 1)

        self.sb_schrittweite = QSpinBox(self.groupBox)
        self.sb_schrittweite.setObjectName(u"sb_schrittweite")
        self.sb_schrittweite.setStyleSheet(u"color: rgb(0, 0, 0);")
        self.sb_schrittweite.setMinimum(0)
        self.sb_schrittweite.setMaximum(1000)
        self.sb_schrittweite.setValue(10)

        self.gridLayout_2.addWidget(self.sb_schrittweite, 1, 2, 1, 1)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_3, 2, 3, 1, 1)

        self.lb_version = QLabel(self.groupBox)
        self.lb_version.setObjectName(u"lb_version")

        self.gridLayout_2.addWidget(self.lb_version, 2, 4, 1, 1)


        self.gridLayout.addWidget(self.groupBox, 3, 0, 1, 5)

        self.le_input = QLineEdit(self.centralwidget)
        self.le_input.setObjectName(u"le_input")
        self.le_input.setEnabled(True)
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.le_input.sizePolicy().hasHeightForWidth())
        self.le_input.setSizePolicy(sizePolicy1)
        self.le_input.setMinimumSize(QSize(0, 0))
        self.le_input.setBaseSize(QSize(0, 0))
        self.le_input.setLayoutDirection(Qt.LeftToRight)
        self.le_input.setStyleSheet(u"")
        self.le_input.setReadOnly(True)

        self.gridLayout.addWidget(self.le_input, 0, 0, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_2, 2, 0, 1, 1)

        self.lb_saved = QLabel(self.centralwidget)
        self.lb_saved.setObjectName(u"lb_saved")
        self.lb_saved.setEnabled(True)
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.lb_saved.sizePolicy().hasHeightForWidth())
        self.lb_saved.setSizePolicy(sizePolicy2)
        self.lb_saved.setMaximumSize(QSize(24, 24))
        self.lb_saved.setPixmap(QPixmap(u"icons/uberpruft.png"))
        self.lb_saved.setScaledContents(True)

        self.gridLayout.addWidget(self.lb_saved, 2, 3, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout)

        Hauptfenster.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(Hauptfenster)
        self.statusbar.setObjectName(u"statusbar")
        Hauptfenster.setStatusBar(self.statusbar)

        self.retranslateUi(Hauptfenster)

        QMetaObject.connectSlotsByName(Hauptfenster)
    # setupUi

    def retranslateUi(self, Hauptfenster):
        Hauptfenster.setWindowTitle(QCoreApplication.translate("Hauptfenster", u"NC-Checker", None))
        self.rb_directory.setText(QCoreApplication.translate("Hauptfenster", u"Ordner ausw\u00e4hlen", None))
        self.pb_quelle.setText(QCoreApplication.translate("Hauptfenster", u"Quelle", None))
        self.pb_save_as.setText(QCoreApplication.translate("Hauptfenster", u"Speichern unter", None))
        self.rb_file.setText(QCoreApplication.translate("Hauptfenster", u"Datei ausw\u00e4hlen", None))
        self.groupBox.setTitle(QCoreApplication.translate("Hauptfenster", u"Einstellungen was gepr\u00fcft werden soll", None))
        self.cb_ids.setText(QCoreApplication.translate("Hauptfenster", u"IDS Nummern", None))
        self.lb_schrittweite.setText(QCoreApplication.translate("Hauptfenster", u"Schrittweite", None))
        self.cb_satznummern.setText(QCoreApplication.translate("Hauptfenster", u"Satznummern", None))
        self.pb_check_program.setText(QCoreApplication.translate("Hauptfenster", u"Check NC-Programm", None))
        self.textBrowser.setHtml(QCoreApplication.translate("Hauptfenster", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"</style></head><body style=\" font-family:'Courier New'; font-size:10pt; font-weight:700; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'Segoe UI'; font-size:9pt; font-weight:400;\"><br /></p></body></html>", None))
        self.textBrowser.setPlaceholderText(QCoreApplication.translate("Hauptfenster", u"Datei Vorschau", None))
        self.cb_klammern.setText(QCoreApplication.translate("Hauptfenster", u"Klammern", None))
        self.lb_startnummer.setText(QCoreApplication.translate("Hauptfenster", u"Startnummer", None))
        self.lb_version.setText(QCoreApplication.translate("Hauptfenster", u"v1.0 Dominik Polo", None))
        self.le_input.setText("")
        self.le_input.setPlaceholderText(QCoreApplication.translate("Hauptfenster", u"NC Programm Pfad", None))
        self.lb_saved.setText("")
    # retranslateUi

