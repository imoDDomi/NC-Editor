import sys

from PySide6.QtWidgets import QApplication, QDialog

from PopUp_Dialog.UI.bracket_check_PopUp_Dialog import Ui_PopUpBracketCheck


class PopUp(QDialog, Ui_PopUpBracketCheck):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.tb_popup.setFont("JetBrains Mono NL Light")


# only for UI debugging
if __name__ == "__main__":
    app = QApplication()
    window = PopUp()
    window.show()
    sys.exit(app.exec())
