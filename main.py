import sys, re, time
from PySide6.QtWidgets import QApplication, QMainWindow, QFileDialog, QDialog
from nc_editor_mainwindow import Ui_Hauptfenster
from PopUpBracketCheck import Ui_PopUpBracketCheck







class MainWindow(QMainWindow, Ui_Hauptfenster): # hier werden Pushbuttons usw. programmiert, alles was auf geerbte Klasse Ui_Hauptfenster zurückgreift
    def __init__(self):
        super().__init__()
        self.setupUi(self) 
        self.pb_quelle.clicked.connect(open_file)
        self.pb_check_program.clicked.connect(check_config)
        self.pb_save_as.clicked.connect(save_file)
        self.lb_saved.setHidden(True) # Button saved ausblenden weil Domi zu blöd zum einstellen im Designer ist
        

    
class PopUp(QDialog, Ui_PopUpBracketCheck):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        

    

# hier werden Funktionen definiert
         



def check_config():
    
        if window.cb_satznummern.isChecked():
            correct_lines()
           
        if window.cb_ids.isChecked():
            check_IDS()

        if window.cb_klammern.isChecked():
            check_brackets()           

def open_file(): # open file
    global Satznummern_liste
    global Satznummern_string
    fname = QFileDialog.getOpenFileName(None, "NC Programme auswählen", "C:/Users/domin/Desktop/NC Programme" , "NC Programme (*.SPF *.MPF *.SAFE *.DEF)")
    window.le_input.setText(fname[0])
    
    
    with open(fname[0], "r") as rf:
        Satznummern_string = rf.read()
        window.textBrowser.setText(Satznummern_string)
        
    
    with open(fname[0], "r") as rf_2:    
        Satznummern_liste = rf_2.readlines()
        



def correct_lines():
    global Satznummern_liste
    global Satznummern_string
    window.lb_saved.setHidden(True)
    line_offset = 0
    i = 0
    x = []
    Liste_fertig = []
    
    
    for s in Satznummern_liste:
        x = re.sub("N"+"\d"+"\d"+"\d*", "N" + str(window.sb_startnummer.value() + line_offset), Satznummern_liste[i])
        Liste_fertig.append(x)
        if re.match("N"+"\d"+"\d"+"\d*", Satznummern_liste[i]):
            line_offset += window.sb_schrittweite.value()
        i += 1
    Satznummern_liste = Liste_fertig
    Satznummern_string = ''.join(Liste_fertig) 
    window.textBrowser.setText(Satznummern_string)
    
def check_brackets():  # brav
    global Satznummern_liste
    global Satznummern_string
    Instanz_PopUP = PopUp()
    i = 0
    bo = 0  #Klammer wird geoeffnet
    bc = 0  #Klammer wird geschlossen
    pattern = "("
    Liste_Anzahl_bo = []
    Fehlerzeilennummer = []
    for s in Satznummern_liste:
        x = re.findall("\(", Satznummern_liste[i])
        y = re.findall("\)", Satznummern_liste[i])
        
        if not len(x) == len(y):
            Fehlerzeilennummer.append("Fehler in Zeile: "+str(i+1)+"\n")
        
        i += 1
    
    
    if len(Fehlerzeilennummer) > 0:
        str2 = ''.join(Fehlerzeilennummer)
        Instanz_PopUP.tb_popup.setText(str2)
        Instanz_PopUP.exec()

def check_IDS():
    global Satznummern_liste
    global Satznummern_string
    window.lb_saved.setHidden(True)
    line_offset = 0
    i = 0
    x = []
    Liste_fertig = []
    pattern = "^IDS\s=\s\d*"
    

    
    for s in Satznummern_liste:
        x = re.sub(pattern, "IDS " + "= " + str(window.sb_startnummer.value() + line_offset), Satznummern_liste[i])
        Liste_fertig.append(x)
        if re.match(pattern, Satznummern_liste[i]):
            line_offset += window.sb_schrittweite.value()
        i += 1
        
    Satznummern_liste = Liste_fertig
    Satznummern_string = ''.join(Liste_fertig) 
    window.textBrowser.setText(Satznummern_string)
    
              

               
def save_file(): # close and save file
    global Satznummern_liste
    global Satznummern_string
    save_file_instance = QFileDialog.getSaveFileName(None, "NC Programme speichern unter", "C:/Users/domin/Desktop/NC Programme" , "NC Programme (*.SPF *.MPF *.SAFE *.DEF)")
    with open(save_file_instance[0], 'w') as save_new_text:
        for item in Satznummern_string:
            save_new_text.write("%s" % item)
        window.lb_saved.setHidden(False)    




#Bereich immer gleich lassen, dient zum aufrufen der Applikation

app = QApplication([])
window = MainWindow()
window.show()
sys.exit(app.exec())
#Bereich Ende




