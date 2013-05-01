# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Association_Rule.ui'
#
# Created: Sat Apr 27 23:56:41 2013
#      by: PyQt4 UI code generator 4.9.6
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
import json

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Dialog(object):
    def setupUi(self, Dialog, tag):
        self.pic = "res/ass/" + tag + ".png"
        self.career = "<p style=\"font-size:12pt;color:BLACK;\"><center><font face=\"Georgia\"><B><I>"+str(tag).upper()+"</I></B></font></center></p>"
        self.json_file = "res/ass_json/" + tag + ".json"
        
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.setFixedSize(800, 585)
        Dialog.setWindowIcon( QtGui.QIcon( "res/icon/icon.png" ) )
        self.Association_Rule = QtGui.QTabWidget(Dialog)
        self.Association_Rule.setGeometry(QtCore.QRect(70, 30, 675, 531))
        self.Association_Rule.setObjectName(_fromUtf8("Association_Rule"))
        
        self.SkillSkill = QtGui.QWidget()
        self.SkillSkill.setObjectName(_fromUtf8("SkillSkill"))
        self.textBrowser = QtGui.QTextBrowser(self.SkillSkill)
        self.textBrowser.setGeometry(QtCore.QRect(219, 0, 451, 31))
        self.textBrowser.setObjectName(_fromUtf8("textBrowser"))
        self.textBrowser.setHtml(self.career)
        self.textBrowser_2 = QtGui.QTextBrowser(self.SkillSkill)
        self.textBrowser_2.setGeometry(QtCore.QRect(219, 30, 451, 481))
        self.textBrowser_2.setObjectName(_fromUtf8("textBrowser_2"))
        self.graphicsView = QtGui.QGraphicsView(self.SkillSkill)
        self.graphicsView.setGeometry(QtCore.QRect(0, 0, 220, 506))
        self.graphicsView.setObjectName(_fromUtf8("Skill_Skill"))
        self.QGraphicsScene = QtGui.QGraphicsScene(self.graphicsView)
        self.QGraphicsScene.setSceneRect(QtCore.QRectF(0, 0, 195, 475))
        self.graphicsView.setScene(self.QGraphicsScene)
        pic = QtGui.QPixmap(self.pic)
        pic = pic.scaled(self.graphicsView.size())
        self.QGraphicsScene.clear()
        self.QGraphicsScene.addPixmap(pic)

        self.SkillEquipment = QtGui.QWidget()
        self.SkillEquipment.setObjectName(_fromUtf8("SkillEquipment"))
        self.textBrowser_5 = QtGui.QTextBrowser(self.SkillEquipment)
        self.textBrowser_5.setGeometry(QtCore.QRect(219, 0, 451, 31))
        self.textBrowser_5.setObjectName(_fromUtf8("textBrowser_5"))
        self.textBrowser_5.setHtml(self.career)
        self.textBrowser_6 = QtGui.QTextBrowser(self.SkillEquipment)
        self.textBrowser_6.setGeometry(QtCore.QRect(219, 30, 451, 481))
        self.textBrowser_6.setObjectName(_fromUtf8("textBrowser_6"))
        self.graphicsView_3 = QtGui.QGraphicsView(self.SkillEquipment)
        self.graphicsView_3.setGeometry(QtCore.QRect(0, 0, 220, 506))
        self.graphicsView_3.setObjectName(_fromUtf8("graphicsView_3"))
        self.QGraphicsScene_3 = QtGui.QGraphicsScene(self.graphicsView_3)
        self.QGraphicsScene_3.setSceneRect(QtCore.QRectF(0, 0, 195, 475))
        self.graphicsView_3.setScene(self.QGraphicsScene_3)
        pic = QtGui.QPixmap(self.pic)
        pic = pic.scaled(self.graphicsView_3.size())
        self.QGraphicsScene_3.clear()
        self.QGraphicsScene_3.addPixmap(pic)

        self.Association_Rule.addTab(self.SkillEquipment, _fromUtf8(""))
        self.Association_Rule.addTab(self.SkillSkill, _fromUtf8(""))
        
        self.EquipmentSet = QtGui.QWidget()
        self.EquipmentSet.setObjectName(_fromUtf8("EquipmentSet"))
        self.textBrowser_11 = QtGui.QTextBrowser(self.EquipmentSet)
        self.textBrowser_11.setGeometry(QtCore.QRect(219, 0, 451, 31))
        self.textBrowser_11.setObjectName(_fromUtf8("textBrowser_11"))
        self.textBrowser_11.setHtml(self.career)
        self.textBrowser_12 = QtGui.QTextBrowser(self.EquipmentSet)
        self.textBrowser_12.setGeometry(QtCore.QRect(219, 30, 451, 481))
        self.textBrowser_12.setObjectName(_fromUtf8("textBrowser_12"))
        self.Association_Rule.addTab(self.EquipmentSet, _fromUtf8(""))
        self.graphicsView_6 = QtGui.QGraphicsView(self.EquipmentSet)
        self.graphicsView_6.setGeometry(QtCore.QRect(0, 0, 220, 506))
        self.graphicsView_6.setObjectName(_fromUtf8("graphicsView_6"))         
        self.QGraphicsScene_6 = QtGui.QGraphicsScene(self.graphicsView_6)
        self.QGraphicsScene_6.setSceneRect(QtCore.QRectF(0, 0, 195, 475))
        self.graphicsView_6.setScene(self.QGraphicsScene_6)
        pic = QtGui.QPixmap(self.pic)
        pic = pic.scaled(self.graphicsView_6.size())
        self.QGraphicsScene_6.clear()
        self.QGraphicsScene_6.addPixmap(pic)

        self.retranslateUi(Dialog)
        self.Association_Rule.setCurrentIndex(2)
        QtCore.QMetaObject.connectSlotsByName(Dialog)


        ItemToItem, SkillToSkill, SkillToItem = self.parse( self.json_file )
        ItemToItem_str = ""
        SkillToSkill_str = ""
        SkillToItem_str = ""
        for items in ItemToItem["ItemToItem"]:
            ItemToItem_str += self.processing(items)+"</br>"
        self.textBrowser_12.setHtml( "<p style=\"font-size:10pt;color:BLACK;\"><font face=\"Georgia\"><B><I>"+ItemToItem_str+"</I></B></font></p>" )

        for items in SkillToSkill["SkillToSkill"]:
            SkillToSkill_str += self.processing(items)+"</br>"
        self.textBrowser_2.setHtml( "<p style=\"font-size:10pt;color:BLACK;\"><font face=\"Georgia\"><B><I>"+SkillToSkill_str+"</I></B></font></p>" )

        for items in SkillToItem["SkillToItem"]:
            SkillToItem_str += self.processing(items)+"</br>"
        self.textBrowser_6.setHtml( "<p style=\"font-size:10pt;color:BLACK;\"><font face=\"Georgia\"><B><I>"+SkillToItem_str+"</I></B></font></p>" )

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", " Association UI| CS670-IR-Prj | Copyright@ X.Y L.G ZL.Y", None))
        self.Association_Rule.setTabText(self.Association_Rule.indexOf(self.SkillSkill), _translate("Dialog", "SkillSkill", None))
        self.Association_Rule.setTabText(self.Association_Rule.indexOf(self.SkillEquipment), _translate("Dialog", "SkillEquipment", None))
        self.Association_Rule.setTabText(self.Association_Rule.indexOf(self.EquipmentSet), _translate("Dialog", "EquipmentSet", None))

    def parse(self, path):
        ass_list = []
        with open(path) as f:
            for line in f.readlines():
                ass_list.append( line )
        ItemToItem = json.loads(ass_list[0])
        SkillToSkill = json.loads(ass_list[1])
        SkillToItem = json.loads(ass_list[3])
        
        return ItemToItem, SkillToSkill, SkillToItem

    def processing( self, items ):
        #[" u'5_Buckler'", " u'5_Weathered Hand Axe'"]
        after_processing = ""
        for item in items:
            item = item.strip()[4:-1]#-1: the last character is not included
            after_processing += item + "&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"
        return after_processing+"<br/><br/>"

