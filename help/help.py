import sys

from PySide6.QtGui import QFont
from PySide6.QtWidgets import QApplication, QDialog

from help.UI.help_window import Ui_Hilfe


class Help(QDialog, Ui_Hilfe):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.helptext.setFont(QFont("Calibri", 13))

    def open_help(self, helptext):
        if helptext == True:
            with open("textfiles/help.txt", "r", encoding="utf-8") as ht:
                helptextfile = ht.read()
                self.helptext.setPlainText(helptextfile)
                self.setWindowTitle("Beschreibung")
        else:
            with open("textfiles/changelog.txt", "r", encoding="utf-8") as cl:
                changelog = cl.read()
                self.helptext.setPlainText(changelog)
                self.setWindowTitle("Versionsinfo")


# only for UI debugging
if __name__ == "__main__":
    app = QApplication()
    window = Help()
    window.show()
    sys.exit(app.exec())
