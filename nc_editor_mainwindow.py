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
from PySide6.QtWidgets import (QApplication, QCheckBox, QFrame, QGridLayout,
    QGroupBox, QLabel, QLineEdit, QMainWindow,
    QPlainTextEdit, QProgressBar, QPushButton, QRadioButton,
    QSizePolicy, QSpacerItem, QSpinBox, QStatusBar,
    QVBoxLayout, QWidget)

class Ui_Hauptfenster(object):
    def setupUi(self, Hauptfenster):
        if not Hauptfenster.objectName():
            Hauptfenster.setObjectName(u"Hauptfenster")
        Hauptfenster.resize(831, 735)
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
        self.rb_file = QRadioButton(self.centralwidget)
        self.rb_file.setObjectName(u"rb_file")
        self.rb_file.setChecked(True)

        self.gridLayout.addWidget(self.rb_file, 0, 2, 1, 1)

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
        self.le_input.setStyleSheet(u"")
        self.le_input.setReadOnly(True)

        self.gridLayout.addWidget(self.le_input, 0, 0, 1, 1)

        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setEnabled(True)
        self.groupBox.setStyleSheet(u"color: rgb(0, 0, 0);")
        self.gridLayout_2 = QGridLayout(self.groupBox)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_4, 0, 4, 1, 4)

        self.sb_startnummer = QSpinBox(self.groupBox)
        self.sb_startnummer.setObjectName(u"sb_startnummer")
        self.sb_startnummer.setStyleSheet(u"color: rgb(0, 0, 0);")
        self.sb_startnummer.setMaximum(10000)
        self.sb_startnummer.setSingleStep(100)
        self.sb_startnummer.setValue(1000)

        self.gridLayout_2.addWidget(self.sb_startnummer, 0, 2, 1, 1)

        self.lb_version = QLabel(self.groupBox)
        self.lb_version.setObjectName(u"lb_version")
        self.lb_version.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.lb_version, 3, 9, 1, 1)

        self.lb_saved = QLabel(self.groupBox)
        self.lb_saved.setObjectName(u"lb_saved")
        self.lb_saved.setEnabled(True)
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.lb_saved.sizePolicy().hasHeightForWidth())
        self.lb_saved.setSizePolicy(sizePolicy1)
        self.lb_saved.setMaximumSize(QSize(24, 24))
        self.lb_saved.setPixmap(QPixmap(u"icons/uberpruft.png"))
        self.lb_saved.setScaledContents(True)

        self.gridLayout_2.addWidget(self.lb_saved, 1, 9, 1, 1)

        self.sb_schrittweite = QSpinBox(self.groupBox)
        self.sb_schrittweite.setObjectName(u"sb_schrittweite")
        self.sb_schrittweite.setStyleSheet(u"color: rgb(0, 0, 0);")
        self.sb_schrittweite.setMinimum(0)
        self.sb_schrittweite.setMaximum(1000)
        self.sb_schrittweite.setValue(10)

        self.gridLayout_2.addWidget(self.sb_schrittweite, 1, 2, 1, 1)

        self.cb_klammern = QCheckBox(self.groupBox)
        self.cb_klammern.setObjectName(u"cb_klammern")
        self.cb_klammern.setStyleSheet(u"color: rgb(0, 0, 0);")
        self.cb_klammern.setChecked(True)

        self.gridLayout_2.addWidget(self.cb_klammern, 1, 0, 1, 1)

        self.pb_save_as = QPushButton(self.groupBox)
        self.pb_save_as.setObjectName(u"pb_save_as")
        self.pb_save_as.setStyleSheet(u"")

        self.gridLayout_2.addWidget(self.pb_save_as, 0, 9, 1, 1)

        self.cb_satznummern = QCheckBox(self.groupBox)
        self.cb_satznummern.setObjectName(u"cb_satznummern")
        self.cb_satznummern.setStyleSheet(u"color: rgb(0, 0, 0);")
        self.cb_satznummern.setChecked(True)

        self.gridLayout_2.addWidget(self.cb_satznummern, 0, 0, 1, 1)

        self.lb_saved_text = QLabel(self.groupBox)
        self.lb_saved_text.setObjectName(u"lb_saved_text")
        self.lb_saved_text.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_2.addWidget(self.lb_saved_text, 1, 8, 1, 1)

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

        self.gridLayout_2.addWidget(self.pb_check_program, 3, 2, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer, 1, 4, 1, 4)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_3, 3, 4, 1, 5)

        self.lb_schrittweite = QLabel(self.groupBox)
        self.lb_schrittweite.setObjectName(u"lb_schrittweite")
        self.lb_schrittweite.setStyleSheet(u"color: rgb(0, 0, 0);")

        self.gridLayout_2.addWidget(self.lb_schrittweite, 1, 1, 1, 1)

        self.cb_ids = QCheckBox(self.groupBox)
        self.cb_ids.setObjectName(u"cb_ids")
        self.cb_ids.setStyleSheet(u"color: rgb(0, 0, 0);")

        self.gridLayout_2.addWidget(self.cb_ids, 3, 0, 1, 1)

        self.lb_startnummer = QLabel(self.groupBox)
        self.lb_startnummer.setObjectName(u"lb_startnummer")
        self.lb_startnummer.setStyleSheet(u"color: rgb(0, 0, 0);")

        self.gridLayout_2.addWidget(self.lb_startnummer, 0, 1, 1, 1)

        self.pb_save = QPushButton(self.groupBox)
        self.pb_save.setObjectName(u"pb_save")

        self.gridLayout_2.addWidget(self.pb_save, 0, 8, 1, 1)

        self.textbrowser = QPlainTextEdit(self.groupBox)
        self.textbrowser.setObjectName(u"textbrowser")
        palette = QPalette()
        brush = QBrush(QColor(0, 0, 0, 255))
        brush.setStyle(Qt.SolidPattern)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Active, QPalette.PlaceholderText, brush)
#endif
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush)
#endif
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush)
#endif
        self.textbrowser.setPalette(palette)
        font = QFont()
        font.setFamilies([u"Courier New"])
        font.setPointSize(10)
        self.textbrowser.setFont(font)
        self.textbrowser.viewport().setProperty("cursor", QCursor(Qt.IBeamCursor))
        self.textbrowser.setFrameShape(QFrame.NoFrame)
        self.textbrowser.setFrameShadow(QFrame.Plain)

        self.gridLayout_2.addWidget(self.textbrowser, 4, 0, 1, 10)


        self.gridLayout.addWidget(self.groupBox, 6, 0, 1, 6)

        self.rb_directory = QRadioButton(self.centralwidget)
        self.rb_directory.setObjectName(u"rb_directory")

        self.gridLayout.addWidget(self.rb_directory, 4, 2, 1, 1)

        self.progressBar = QProgressBar(self.centralwidget)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setEnabled(False)
        self.progressBar.setMaximumSize(QSize(16777215, 20))
        self.progressBar.setValue(24)

        self.gridLayout.addWidget(self.progressBar, 4, 0, 1, 2)

        self.pb_quelle = QPushButton(self.centralwidget)
        self.pb_quelle.setObjectName(u"pb_quelle")
        sizePolicy2 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.pb_quelle.sizePolicy().hasHeightForWidth())
        self.pb_quelle.setSizePolicy(sizePolicy2)
        self.pb_quelle.setMinimumSize(QSize(100, 0))
        self.pb_quelle.setMaximumSize(QSize(100, 50))
        self.pb_quelle.setStyleSheet(u"")

        self.gridLayout.addWidget(self.pb_quelle, 0, 5, 1, 1)

        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        sizePolicy2.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy2)
        self.pushButton.setMaximumSize(QSize(20, 20))
        self.pushButton.setLayoutDirection(Qt.LeftToRight)
        self.pushButton.setAutoFillBackground(False)
        icon1 = QIcon()
        icon1.addFile(u"icons/reset.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton.setIcon(icon1)
        self.pushButton.setIconSize(QSize(32, 16))

        self.gridLayout.addWidget(self.pushButton, 0, 4, 1, 1)


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
        self.rb_file.setText(QCoreApplication.translate("Hauptfenster", u"Datei ausw\u00e4hlen", None))
        self.le_input.setText("")
        self.le_input.setPlaceholderText(QCoreApplication.translate("Hauptfenster", u"NC Programm Pfad", None))
        self.groupBox.setTitle(QCoreApplication.translate("Hauptfenster", u"Setup", None))
        self.lb_version.setText(QCoreApplication.translate("Hauptfenster", u"Version", None))
        self.lb_saved.setText("")
        self.cb_klammern.setText(QCoreApplication.translate("Hauptfenster", u"Klammern", None))
        self.pb_save_as.setText(QCoreApplication.translate("Hauptfenster", u"Speichern unter", None))
        self.cb_satznummern.setText(QCoreApplication.translate("Hauptfenster", u"Satznummern", None))
        self.lb_saved_text.setText(QCoreApplication.translate("Hauptfenster", u"gespeichert!", None))
        self.pb_check_program.setText(QCoreApplication.translate("Hauptfenster", u"Check NC-Programm", None))
        self.lb_schrittweite.setText(QCoreApplication.translate("Hauptfenster", u"Schrittweite", None))
        self.cb_ids.setText(QCoreApplication.translate("Hauptfenster", u"IDS Nummern", None))
        self.lb_startnummer.setText(QCoreApplication.translate("Hauptfenster", u"Startnummer", None))
        self.pb_save.setText(QCoreApplication.translate("Hauptfenster", u"Speichern", None))
        self.textbrowser.setPlaceholderText("")
        self.rb_directory.setText(QCoreApplication.translate("Hauptfenster", u"Ordner ausw\u00e4hlen", None))
        self.pb_quelle.setText(QCoreApplication.translate("Hauptfenster", u"Quelle", None))
    # retranslateUi

