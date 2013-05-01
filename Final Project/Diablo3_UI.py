from PyQt4.QtCore import *
from PyQt4.QtGui import *
import Association_Rule
import sys
import re

class Ui_Dialog(QDialog, Association_Rule.Ui_Dialog):
    def __init__(self, text, tag, parent=None):
        super(Ui_Dialog, self).__init__(parent)
        self.__text = unicode(text)
        self.__index = 0
        self.setupUi(self, tag)
        #QDialog.exec_
        #self.updateUi()

'''
def main():
    app = QApplication(sys.argv)
    UI = Ui_Dialog( "Diablo3_UI" )
    UI.show()
    app.exec_()
    

if __name__ == "__main__":
    main()
'''
