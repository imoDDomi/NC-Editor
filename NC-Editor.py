# --coding: utf-8 --
import fnmatch
import itertools
import os
import re
import sys

from PySide6.QtCore import Qt
from PySide6.QtGui import QFont, QFontDatabase, QGuiApplication

# from os import* MERKE! niemals alles importieren, hat standard openfile mit os.openfile() überschrieben :(
from PySide6.QtWidgets import QApplication, QDialog, QFileDialog, QMainWindow

from help import Ui_Hilfe
from nc_editor_mainwindow import Ui_Hauptfenster
from PopUpBracketCheck import Ui_PopUpBracketCheck

# in exe umwandeln:
# auto-py-to-exe


class MainWindow(QMainWindow, Ui_Hauptfenster):  # hier werden Pushbuttons usw. programmiert, alles was auf geerbte Klasse Ui_Hauptfenster zurückgreift
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        QFontDatabase.addApplicationFont("fonts/JetBrainsMono-Regular.ttf")
        self.le_input.setFont("JetBrains Mono")
        self.textbrowser.setFont(QFont("JetBrains Mono", 12))
        self.pb_quelle.clicked.connect(open_file)
        self.pb_check_program.clicked.connect(check_config)
        self.pb_save_as.clicked.connect(save_as_file)
        self.pb_save.clicked.connect(save_file)
        self.mb_info.triggered.connect(open_help)
        self.mb_version.triggered.connect(open_version)
        self.lb_saved.setHidden(True)  # Button saved ausblenden weil Domi zu blöd zum einstellen im Designer ist
        self.lb_saved_text.setHidden(True)
        self.progressBar.setHidden(True)

        self.rb_directory.clicked.connect(disable_IDS_checkbox)
        self.rb_file.clicked.connect(enable_IDS_checkbox)
        self.lb_version.setText("v1.5 Dominik Polo")
        self.pb_reset_file.clicked.connect(reset_file)


class PopUp(QDialog, Ui_PopUpBracketCheck):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.tb_popup.setFont("JetBrains Mono NL Light")


class Help(QDialog, Ui_Hilfe):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.helptext.setFont(QFont("JetBrains Mono", 10))


# hier werden Funktionen definiert


def disable_IDS_checkbox():
    window.cb_ids.setEnabled(False)


def enable_IDS_checkbox():
    window.cb_ids.setEnabled(True)


def check_config():
    if window.rb_file.isChecked():

        if window.cb_satznummern.isChecked():
            correct_lines()

        if window.cb_ids.isChecked():
            check_IDS()

        if window.cb_klammern.isChecked():
            check_brackets()

    if window.rb_directory.isChecked():

        if window.cb_satznummern.isChecked():
            correct_lines_in_dir()

        if window.cb_klammern.isChecked():
            check_brackets_in_dir()


def reset_file():

    with open(Path_single_file, "r") as rf:
        Satznummern_string = rf.read()
        window.textbrowser.setPlainText(Satznummern_string)


def open_file():  # open file
    global Satznummern_liste
    global Satznummern_string
    global files_Satznummern_liste
    global Path_single_file
    window.lb_saved.setHidden(True)
    window.lb_saved_text.setHidden(True)

    if window.rb_file.isChecked():

        fname = QFileDialog.getOpenFileName(
            None,
            "NC Programme auswählen",
            "C:/Users/domin/Desktop/NC Programme",
            "NC Programme (*.SPF *.MPF *.DEF)",
        )
        window.le_input.setText(fname[0])
        Path_single_file = fname[0]

        with open(fname[0], "r", encoding="utf-8") as rf:
            Satznummern_string = rf.read()
            window.textbrowser.setPlainText(Satznummern_string)

        with open(fname[0], "r") as rf_2:
            Satznummern_liste = rf_2.readlines()

    if window.rb_directory.isChecked():

        files = QFileDialog.getExistingDirectory(None, "NC Programm Ordner auswählen", "C:/Users/Dominik/Desktop/CNC")
        window.le_input.setText(files)
        raw_files_Satznummern_liste = os.listdir(files)

        pattern = ["*.SPF", "*.MPF", "*.DEF"]
        x = 0
        files_Satznummern_liste = []
        for i in pattern:

            filtered_list = fnmatch.filter(raw_files_Satznummern_liste, pattern[x])
            files_Satznummern_liste.append(filtered_list)
            x += 1

        files_Satznummern_liste = list(itertools.chain(*files_Satznummern_liste))

        loop_directories(files)


def loop_directories(path):
    # globaler directory path erzeugen + Text im Browser setzen
    global directory_path
    directory_path = path + "/"

    for i in files_Satznummern_liste:

        zeilenumbruch = "\n"
        w = zeilenumbruch.join(files_Satznummern_liste)
        window.textbrowser.setPlainText(w)


def correct_lines_in_dir():

    global files_Satznummern_liste

    window.progressBar.setHidden(False)

    line_offset = 0
    x = []
    Liste_fertig = []
    l = 0
    g = 0

    for i in files_Satznummern_liste:

        current_file_name = i

        with open(directory_path + current_file_name, "r") as q:
            lokal_Satznummern_liste = q.readlines()

        line_offset = 0
        l = 0
        for s in lokal_Satznummern_liste:
            x = re.sub(
                "N" + "\d" + "\d" + "\d*",
                "N" + str(window.sb_startnummer.value() + line_offset),
                lokal_Satznummern_liste[l],
            )
            Liste_fertig.append(x)
            if re.match("N" + "\d" + "\d" + "\d*", lokal_Satznummern_liste[l]):
                line_offset += window.sb_schrittweite.value()

            l += 1
            s = Liste_fertig
        Liste_fertig = []

        with open(directory_path + current_file_name, "w") as save_new_text:
            for item in s:
                save_new_text.write("%s" % item)
        g += 1
        # time.sleep(0.5)

        window.progressBar.setValue(g / len(files_Satznummern_liste) * 100)

        if window.progressBar.value() == 100:
            window.progressBar.setHidden(True)

    window.lb_saved.setHidden(False)
    window.lb_saved_text.setHidden(False)


def check_brackets_in_dir():

    Instanz_PopUp2 = PopUp()
    Fehlerzeilennummer = []
    i = 0

    for c in files_Satznummern_liste:

        current_file_name = c

        with open(directory_path + current_file_name, "r") as q:
            lokal_Satznummern_liste = q.readlines()

        i = 0

        cut_lokal_Satznummern_liste = []

        for r in lokal_Satznummern_liste:

            cut_lokal_Satznummern = r.split(";")[0]
            cut_lokal_Satznummern_liste.append(cut_lokal_Satznummern)

        for s in cut_lokal_Satznummern_liste:
            x = re.findall("\(", cut_lokal_Satznummern_liste[i])
            y = re.findall("\)", cut_lokal_Satznummern_liste[i])

            if not len(x) == len(y):
                Fehlerzeilennummer.append("Fehler in " + current_file_name + " in Zeile: " + str(i + 1) + "\n")
                x = []
                y = []
            i += 1

    if len(Fehlerzeilennummer) > 0:
        str3 = "".join(Fehlerzeilennummer)
        Instanz_PopUp2.tb_popup.setText(str3)
        Instanz_PopUp2.exec()

    if len(Fehlerzeilennummer) == 0:
        Instanz_PopUp2.tb_popup.setText("Keine Fehler gefunden")
        Instanz_PopUp2.exec()


def correct_lines():
    global Satznummern_liste
    global Satznummern_string
    window.lb_saved.setHidden(True)
    window.lb_saved_text.setHidden(True)
    line_offset = 0
    i = 0
    x = []
    Liste_fertig = []

    for s in Satznummern_liste:
        x = re.sub(
            "N" + "\d" + "\d" + "\d*",
            "N" + str(window.sb_startnummer.value() + line_offset),
            Satznummern_liste[i],
        )
        Liste_fertig.append(x)
        if re.match("N" + "\d" + "\d" + "\d*", Satznummern_liste[i]):
            line_offset += window.sb_schrittweite.value()
        i += 1
    Satznummern_liste = Liste_fertig
    Satznummern_string = "".join(Liste_fertig)
    window.textbrowser.setPlainText(Satznummern_string)


def check_brackets():  # brav
    global Satznummern_liste
    global Satznummern_string

    window.lb_saved.setHidden(True)
    window.lb_saved_text.setHidden(True)

    Instanz_PopUp = PopUp()
    i = 0
    Fehlerzeilennummer = []
    cut_Satznummern_liste_without_line_comments_list = []

    for r in Satznummern_liste:

        cut_Satznummern_liste_without_line_comments = r.split(";")[0]
        cut_Satznummern_liste_without_line_comments_list.append(cut_Satznummern_liste_without_line_comments)

    for s in cut_Satznummern_liste_without_line_comments_list:

        x = re.findall("\(", cut_Satznummern_liste_without_line_comments_list[i])
        y = re.findall("\)", cut_Satznummern_liste_without_line_comments_list[i])

        if not len(x) == len(y):
            Fehlerzeilennummer.append("Fehler in Zeile: " + str(i + 1) + "\n")

        i += 1

    if len(Fehlerzeilennummer) > 0:
        str2 = "".join(Fehlerzeilennummer)
        Instanz_PopUp.tb_popup.setText(str2)
        Instanz_PopUp.exec()

    if len(Fehlerzeilennummer) == 0:
        Instanz_PopUp.tb_popup.setText("Keine Fehler gefunden")
        Instanz_PopUp.exec()


def check_IDS():
    global Satznummern_liste
    global Satznummern_string

    window.lb_saved.setHidden(True)
    window.lb_saved_text.setHidden(True)

    line_offset = 0
    i = 0
    x = []
    Liste_fertig = []
    pattern = "^IDS=\s?\d*"

    for s in Satznummern_liste:
        x = re.sub(
            pattern,
            "IDS" + "=" + str(window.sb_startnummer.value() + line_offset),
            Satznummern_liste[i],
        )
        Liste_fertig.append(x)
        if re.match(pattern, Satznummern_liste[i]):
            line_offset += window.sb_schrittweite.value()
        i += 1

    Satznummern_liste = Liste_fertig
    Satznummern_string = "".join(Liste_fertig)
    window.textbrowser.setPlainText(Satznummern_string)


def save_as_file():  # close and save file
    global Satznummern_liste
    global Satznummern_string
    save_file_instance = QFileDialog.getSaveFileName(
        None,
        "NC Programme speichern unter",
        "C:/Users/domin/Desktop/NC Programme",
        "NC Programme (*.SPF *.MPF *.SAFE *.DEF)",
    )
    with open(save_file_instance[0], "w", encoding="utf-8") as save_new_text:
        save_new_text.write(Satznummern_string)
        window.lb_saved.setHidden(False)


def save_file():
    global Satznummern_liste
    global Satznummern_string

    plain_text_content = window.textbrowser.toPlainText()
    with open(Path_single_file, "w", encoding="utf-8") as save_new_text_2:

        save_new_text_2.write(plain_text_content)
        window.lb_saved.setHidden(False)
        window.lb_saved_text.setHidden(False)


def open_help():
    Instanz_Hilfe = Help()

    with open("textfiles/help.txt", "r", encoding="utf-8") as ht:
        helptextfile = ht.read()
        Instanz_Hilfe.helptext.setPlainText(helptextfile)

    Instanz_Hilfe.exec()


def open_version():
    Instanz_Version = Help()

    with open("textfiles/changelog.txt", "r", encoding="utf-8") as cl:
        changelogfile = cl.read()
        Instanz_Version.helptext.setPlainText(changelogfile)

    Instanz_Version.exec()


def main():
    QGuiApplication.setHighDpiScaleFactorRoundingPolicy(Qt.HighDpiScaleFactorRoundingPolicy.Round)


app = QApplication([])
window = MainWindow()
window.show()
sys.exit(app.exec())


if __name__ == "__main__":
    main()
