# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ZhengLiang.ui'
#
# Created: Sat Apr 27 15:14:44 2013
#      by: PyQt4 UI code generator 4.9.6
#
# WARNING! All changes made in this file will be lost!

from collections import defaultdict
from PyQt4 import QtCore, QtGui
import Recommendation
import Diablo3_UI
import heroview
import json
import sys

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

Property_dict = defaultdict()

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        #self.career_recommendation = []
        #self.friend_recommendation = []
        Dialog.setObjectName(_fromUtf8("dialog"))
        Dialog.setWindowIcon( QtGui.QIcon( "res/icon/icon.png" ) )
        #Dialog.minimumSizeHint()
        #Dialog.resize(654, 591)
        Dialog.setFixedSize(545, 525)
        Dialog.setWindowTitle( "Diablo3 Novice Assitance" )
        self.textBrowser = QtGui.QLabel(Dialog)
        self.textBrowser.setGeometry(QtCore.QRect(30, 40, 61, 31))
        self.textBrowser.setObjectName(_fromUtf8("textBrowser"))
        self.textBrowser_2 = QtGui.QLabel(Dialog)
        self.textBrowser_2.setGeometry(QtCore.QRect(290, 40, 61, 31))
        self.textBrowser_2.setObjectName(_fromUtf8("textBrowser_2"))
        self.textBrowser_3 = QtGui.QLabel(Dialog)
        self.textBrowser_3.setGeometry(QtCore.QRect(30, 89, 61, 31))
        self.textBrowser_3.setObjectName(_fromUtf8("textBrowser_3"))
        self.textBrowser_4 = QtGui.QLabel(Dialog)
        self.textBrowser_4.setGeometry(QtCore.QRect(290, 89, 61, 31))
        self.textBrowser_4.setObjectName(_fromUtf8("textBrowser_4"))
        self.textBrowser_5 = QtGui.QLabel(Dialog)
        self.textBrowser_5.setGeometry(QtCore.QRect(290, 190, 61, 31))
        self.textBrowser_5.setObjectName(_fromUtf8("textBrowser_5"))
        self.textBrowser_6 = QtGui.QLabel(Dialog)
        self.textBrowser_6.setGeometry(QtCore.QRect(30, 190, 61, 31))
        self.textBrowser_6.setObjectName(_fromUtf8("textBrowser_6"))
        self.textBrowser_7 = QtGui.QLabel(Dialog)
        self.textBrowser_7.setGeometry(QtCore.QRect(30, 141, 61, 31))
        self.textBrowser_7.setObjectName(_fromUtf8("textBrowser_7"))
        self.textBrowser_8 = QtGui.QLabel(Dialog)
        self.textBrowser_8.setGeometry(QtCore.QRect(290, 141, 61, 31))
        self.textBrowser_8.setObjectName(_fromUtf8("textBrowser_8"))
        self.textBrowser_9 = QtGui.QLabel(Dialog)
        self.textBrowser_9.setGeometry(QtCore.QRect(30, 240, 61, 31))
        self.textBrowser_9.setObjectName(_fromUtf8("textBrowser_9"))
        self.groupBox = QtGui.QGroupBox(Dialog)
        self.groupBox.setGeometry(QtCore.QRect(280, 240, 241, 271))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.textBrowser_14 = QtGui.QLabel(self.groupBox)
        self.textBrowser_14.setGeometry(QtCore.QRect(10, 230, 31, 31))
        self.textBrowser_14.setObjectName(_fromUtf8("textBrowser_14"))
        self.textBrowser_11 = QtGui.QLabel(self.groupBox)
        self.textBrowser_11.setGeometry(QtCore.QRect(10, 80, 31, 31))
        self.textBrowser_11.setObjectName(_fromUtf8("textBrowser_11"))
        self.textBrowser_13 = QtGui.QLabel(self.groupBox)
        self.textBrowser_13.setGeometry(QtCore.QRect(10, 180, 31, 31))
        self.textBrowser_13.setObjectName(_fromUtf8("textBrowser_13"))
        self.textBrowser_12 = QtGui.QLabel(self.groupBox)
        self.textBrowser_12.setGeometry(QtCore.QRect(10, 130, 31, 31))
        self.textBrowser_12.setObjectName(_fromUtf8("textBrowser_12"))
        self.textBrowser_10 = QtGui.QLabel(self.groupBox)
        self.textBrowser_10.setGeometry(QtCore.QRect(10, 30, 31, 31))
        self.textBrowser_10.setObjectName(_fromUtf8("textBrowser_10"))
        self.groupBox1 = QtGui.QGroupBox(Dialog)
        self.groupBox1.setGeometry(QtCore.QRect(30, 290, 231, 221))
        self.groupBox1.setObjectName(_fromUtf8("groupBox1"))
        self.textBrowser_101 = QtGui.QTextBrowser(self.groupBox1)
        self.textBrowser_101.setGeometry(QtCore.QRect(10, 50, 211, 161))
        self.textBrowser_101.setObjectName(_fromUtf8("textBrowser_101"))
        self.pushButton = QtGui.QPushButton(self.groupBox1)
        self.pushButton.setGeometry(QtCore.QRect(180, 20, 41, 23))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.comboBox = QtGui.QComboBox(self.groupBox1)
        self.comboBox.setGeometry(QtCore.QRect(10, 20, 161, 22))
        self.comboBox.setObjectName(_fromUtf8("comboBox"))
        self.Melee = QtGui.QSlider(Dialog)
        self.Melee.setGeometry(QtCore.QRect(110, 50, 151, 20))
        self.Melee.setInputMethodHints(QtCore.Qt.ImhDigitsOnly|QtCore.Qt.ImhPreferNumbers)
        self.Melee.setMinimum(1)
        self.Melee.setMaximum(5)
        self.Melee.setPageStep(1)
        self.Melee.setOrientation(QtCore.Qt.Horizontal)
        self.Melee.setObjectName(_fromUtf8("Melee"))
        self.Physical = QtGui.QSlider(Dialog)
        self.Physical.setGeometry(QtCore.QRect(110, 100, 151, 20))
        self.Physical.setMinimum(1)
        self.Physical.setMaximum(5)
        self.Physical.setPageStep(1)
        self.Physical.setOrientation(QtCore.Qt.Horizontal)
        self.Physical.setObjectName(_fromUtf8("Physical"))
        self.Damage = QtGui.QSlider(Dialog)
        self.Damage.setGeometry(QtCore.QRect(110, 150, 151, 20))
        self.Damage.setMinimum(1)
        self.Damage.setMaximum(5)
        self.Damage.setPageStep(1)
        self.Damage.setOrientation(QtCore.Qt.Horizontal)
        self.Damage.setObjectName(_fromUtf8("Damage"))
        self.Solo = QtGui.QSlider(Dialog)
        self.Solo.setGeometry(QtCore.QRect(110, 200, 151, 20))
        self.Solo.setMinimum(1)
        self.Solo.setMaximum(5)
        self.Solo.setPageStep(1)
        self.Solo.setOrientation(QtCore.Qt.Horizontal)
        self.Solo.setObjectName(_fromUtf8("Solo"))
        self.Team = QtGui.QSlider(Dialog)
        self.Team.setGeometry(QtCore.QRect(110, 250, 151, 20))
        self.Team.setMinimum(1)
        self.Team.setMaximum(5)
        self.Team.setPageStep(1)
        self.Team.setOrientation(QtCore.Qt.Horizontal)
        self.Team.setObjectName(_fromUtf8("Team"))
        self.Range = QtGui.QSlider(Dialog)
        self.Range.setGeometry(QtCore.QRect(370, 50, 151, 20))
        self.Range.setMinimum(1)
        self.Range.setMaximum(5)
        self.Range.setPageStep(1)
        self.Range.setOrientation(QtCore.Qt.Horizontal)
        self.Range.setObjectName(_fromUtf8("Range"))
        self.Magical = QtGui.QSlider(Dialog)
        self.Magical.setGeometry(QtCore.QRect(370, 100, 151, 20))
        self.Magical.setMinimum(1)
        self.Magical.setMaximum(5)
        self.Magical.setPageStep(1)
        self.Magical.setOrientation(QtCore.Qt.Horizontal)
        self.Magical.setObjectName(_fromUtf8("Magical"))
        self.Tank = QtGui.QSlider(Dialog)
        self.Tank.setGeometry(QtCore.QRect(370, 150, 151, 20))
        self.Tank.setMinimum(1)
        self.Tank.setMaximum(5)
        self.Tank.setPageStep(1)
        self.Tank.setOrientation(QtCore.Qt.Horizontal)
        self.Tank.setObjectName(_fromUtf8("Tank"))
        self.Support = QtGui.QSlider(Dialog)
        self.Support.setGeometry(QtCore.QRect(370, 200, 151, 20))
        self.Support.setMinimum(1)
        self.Support.setMaximum(5)
        self.Support.setPageStep(1)
        self.Support.setOrientation(QtCore.Qt.Horizontal)
        self.Support.setObjectName(_fromUtf8("Support"))

        #Graphics
        self.pic_path = "res/main_ui/"
        self.graphicsView = QtGui.QGraphicsView(self.groupBox)
        self.graphicsView.setGeometry(QtCore.QRect(40, 20, 61, 51))
        self.graphicsView.setObjectName(_fromUtf8("graphicsView"))         
        self.QGraphicsScene = QtGui.QGraphicsScene(self.graphicsView)
        self.QGraphicsScene.setSceneRect(QtCore.QRectF(0, 0, 55, 45))
        self.graphicsView.setScene(self.QGraphicsScene)
        pic = QtGui.QPixmap(self.pic_path + "Barbarian.png")
        pic = pic.scaled(self.graphicsView.size())
        self.QGraphicsScene.clear()
        self.QGraphicsScene.addPixmap(pic)
        
        self.graphicsView_2 = QtGui.QGraphicsView(self.groupBox)
        self.graphicsView_2.setGeometry(QtCore.QRect(40, 70, 61, 51))
        self.graphicsView_2.setObjectName(_fromUtf8("graphicsView_2"))         
        self.QGraphicsScene_2 = QtGui.QGraphicsScene(self.graphicsView_2)
        self.QGraphicsScene_2.setSceneRect(QtCore.QRectF(0, 0, 55, 45))
        self.graphicsView_2.setScene(self.QGraphicsScene_2)
        pic = QtGui.QPixmap(self.pic_path + "Demon-Hunter.png")
        pic = pic.scaled(self.graphicsView_2.size())
        self.QGraphicsScene_2.clear()
        self.QGraphicsScene_2.addPixmap(pic)

        self.graphicsView_3 = QtGui.QGraphicsView(self.groupBox)
        self.graphicsView_3.setGeometry(QtCore.QRect(40, 120, 61, 51))
        self.graphicsView_3.setObjectName(_fromUtf8("graphicsView_3"))         
        self.QGraphicsScene_3 = QtGui.QGraphicsScene(self.graphicsView_3)
        self.QGraphicsScene_3.setSceneRect(QtCore.QRectF(0, 0, 55, 45))
        self.graphicsView_3.setScene(self.QGraphicsScene_3)
        pic = QtGui.QPixmap(self.pic_path + "monk.png")
        pic = pic.scaled(self.graphicsView_3.size())
        self.QGraphicsScene_3.clear()
        self.QGraphicsScene_3.addPixmap(pic)

        self.graphicsView_4 = QtGui.QGraphicsView(self.groupBox)
        self.graphicsView_4.setGeometry(QtCore.QRect(40, 170, 61, 51))
        self.graphicsView_4.setObjectName(_fromUtf8("graphicsView_4"))         
        self.QGraphicsScene_4 = QtGui.QGraphicsScene(self.graphicsView_4)
        self.QGraphicsScene_4.setSceneRect(QtCore.QRectF(0, 0, 55, 45))
        self.graphicsView_4.setScene(self.QGraphicsScene_4)
        pic = QtGui.QPixmap(self.pic_path + "Witch-Doctor.png")
        pic = pic.scaled(self.graphicsView_4.size())
        self.QGraphicsScene_4.clear()
        self.QGraphicsScene_4.addPixmap(pic)

        self.graphicsView_5 = QtGui.QGraphicsView(self.groupBox)
        self.graphicsView_5.setGeometry(QtCore.QRect(40, 220, 61, 51))
        self.graphicsView_5.setObjectName(_fromUtf8("graphicsView_5"))         
        self.QGraphicsScene_5 = QtGui.QGraphicsScene(self.graphicsView_5)
        self.QGraphicsScene_5.setSceneRect(QtCore.QRectF(0, 0, 55, 45))
        self.graphicsView_5.setScene(self.QGraphicsScene_5)
        pic = QtGui.QPixmap(self.pic_path + "Wizard.png")
        pic = pic.scaled(self.graphicsView_5.size())
        self.QGraphicsScene_5.clear()
        self.QGraphicsScene_5.addPixmap(pic)

        #buttons
        self.commandLinkButton = QtGui.QCommandLinkButton(self.groupBox)
        self.commandLinkButton.setGeometry(QtCore.QRect(100, 20, 141, 51))
        self.commandLinkButton.setObjectName(_fromUtf8("commandLinkButton"))
        self.commandLinkButton_2 = QtGui.QCommandLinkButton(self.groupBox)
        self.commandLinkButton_2.setGeometry(QtCore.QRect(100, 70, 141, 51))
        self.commandLinkButton_2.setObjectName(_fromUtf8("commandLinkButton_2"))
        self.commandLinkButton_3 = QtGui.QCommandLinkButton(self.groupBox)
        self.commandLinkButton_3.setGeometry(QtCore.QRect(100, 120, 141, 51))
        self.commandLinkButton_3.setObjectName(_fromUtf8("commandLinkButton_3"))
        self.commandLinkButton_4 = QtGui.QCommandLinkButton(self.groupBox)
        self.commandLinkButton_4.setGeometry(QtCore.QRect(100, 170, 141, 51))
        self.commandLinkButton_4.setObjectName(_fromUtf8("commandLinkButton_4"))
        self.commandLinkButton_5 = QtGui.QCommandLinkButton(self.groupBox)
        self.commandLinkButton_5.setGeometry(QtCore.QRect(100, 220, 141, 51))
        self.commandLinkButton_5.setObjectName(_fromUtf8("commandLinkButton_5"))
        self.commandLinkButton.setText( "barbarian" )
        self.commandLinkButton_2.setText( "demon-hunter" )
        self.commandLinkButton_3.setText( "monk" )
        self.commandLinkButton_4.setText( "witch-doctor" )
        self.commandLinkButton_5.setText( "wizard" )

        self.retranslateUi(Dialog)
        QtCore.QObject.connect(self.Melee, QtCore.SIGNAL(_fromUtf8("valueChanged(int)")), Dialog.slider_response)
        QtCore.QObject.connect(self.Physical, QtCore.SIGNAL(_fromUtf8("valueChanged(int)")), Dialog.slider_response)
        QtCore.QObject.connect(self.Damage, QtCore.SIGNAL(_fromUtf8("valueChanged(int)")), Dialog.slider_response)
        QtCore.QObject.connect(self.Solo, QtCore.SIGNAL(_fromUtf8("valueChanged(int)")), Dialog.slider_response)
        QtCore.QObject.connect(self.Team, QtCore.SIGNAL(_fromUtf8("valueChanged(int)")), Dialog.slider_response)
        QtCore.QObject.connect(self.Range, QtCore.SIGNAL(_fromUtf8("valueChanged(int)")), Dialog.slider_response)
        QtCore.QObject.connect(self.Magical, QtCore.SIGNAL(_fromUtf8("valueChanged(int)")), Dialog.slider_response)
        QtCore.QObject.connect(self.Tank, QtCore.SIGNAL(_fromUtf8("valueChanged(int)")), Dialog.slider_response)
        QtCore.QObject.connect(self.Support, QtCore.SIGNAL(_fromUtf8("valueChanged(int)")), Dialog.slider_response)
        QtCore.QObject.connect(self.pushButton, QtCore.SIGNAL(_fromUtf8("clicked()")), Dialog.viewDetail)
        QtCore.QObject.connect(self.comboBox, QtCore.SIGNAL(_fromUtf8("currentIndexChanged(int)")), Dialog.comboBox_response)
        QtCore.QObject.connect(self.commandLinkButton, QtCore.SIGNAL(_fromUtf8("clicked()")), Dialog.association_rule_response)
        QtCore.QObject.connect(self.commandLinkButton_2, QtCore.SIGNAL(_fromUtf8("clicked()")), Dialog.association_rule_response_2)
        QtCore.QObject.connect(self.commandLinkButton_3, QtCore.SIGNAL(_fromUtf8("clicked()")), Dialog.association_rule_response_3)
        QtCore.QObject.connect(self.commandLinkButton_4, QtCore.SIGNAL(_fromUtf8("clicked()")), Dialog.association_rule_response_4)
        QtCore.QObject.connect(self.commandLinkButton_5, QtCore.SIGNAL(_fromUtf8("clicked()")), Dialog.association_rule_response_5)
        QtCore.QMetaObject.connectSlotsByName(Dialog)


    def slider_response( self ):
        Property_dict[ "Melee" ] = self.Melee.value()
        Property_dict[ "Physical" ] = self.Physical.value()
        Property_dict[ "Damage" ] = self.Damage.value()
        Property_dict[ "Solo" ] = self.Solo.value()
        Property_dict[ "Team" ] = self.Team.value()
        Property_dict[ "Range" ] = self.Range.value()
        Property_dict[ "Magical" ] = self.Magical.value()
        Property_dict[ "Tank" ] = self.Tank.value()
        Property_dict[ "Support" ] = self.Support.value()

        #self.career_recommendation = []
        #self.friend_recommendation = []
        self.career_recommendation, self.friend_recommendation = Recommendation.getInput( Property_dict )

        self.comboBox.clear()
        self.comboBox.addItems( self.friend_recommendation )

        pic = QtGui.QPixmap(self.pic_path + self.career_recommendation[0]+'.png')
        pic = pic.scaled(self.graphicsView.size())
        self.QGraphicsScene.clear()
        self.QGraphicsScene.addPixmap(pic)
        self.commandLinkButton.setText(self.career_recommendation[0])
        
        pic = QtGui.QPixmap(self.pic_path + self.career_recommendation[1]+'.png')
        pic = pic.scaled(self.graphicsView_2.size())
        self.QGraphicsScene_2.clear()
        self.QGraphicsScene_2.addPixmap(pic)
        self.commandLinkButton_2.setText(self.career_recommendation[1])

        pic = QtGui.QPixmap(self.pic_path + self.career_recommendation[2]+'.png')
        pic = pic.scaled(self.graphicsView_3.size())
        self.QGraphicsScene_3.clear()
        self.QGraphicsScene_3.addPixmap(pic)
        self.commandLinkButton_3.setText(self.career_recommendation[2])

        pic = QtGui.QPixmap(self.pic_path + self.career_recommendation[3]+'.png')
        pic = pic.scaled(self.graphicsView_4.size())
        self.QGraphicsScene_4.clear()
        self.QGraphicsScene_4.addPixmap(pic)
        self.commandLinkButton_4.setText(self.career_recommendation[3])

        pic = QtGui.QPixmap(self.pic_path + self.career_recommendation[4]+'.png')
        pic = pic.scaled(self.graphicsView_5.size())
        self.QGraphicsScene_5.clear()
        self.QGraphicsScene_5.addPixmap(pic)
        self.commandLinkButton_5.setText(self.career_recommendation[4])

    #View Detail
    def viewDetail( self ):
        user_tag = str( self.comboBox.currentText() )
        User_Detail_Dialog = heroview.Ui_Dialog(user_tag)
        User_Detail_Dialog.exec_()
        

    def comboBox_response( self ):
        display = ""
        if self.comboBox.count() != 0:
            user_tag = str( self.comboBox.currentText() )
            with open( "timePlayed.json" ) as g:
                user_timePlayed = json.loads( g.readline() )
            for target_career in self.career_recommendation:
                for played_career in user_timePlayed[user_tag]:
                    if played_career == target_career:
                        if user_timePlayed[user_tag][played_career] >= 0.9:
                            display += "<p style=\"font-size:12pt;color:RED\">" + played_career + ": Master\n" + "</p>"
                            break
                        if user_timePlayed[user_tag][played_career] >= 0.7:
                            display += "<p style=\"font-size:12pt;color:ORANGE\">" + played_career + ": Professonal\n" + "</p>"
                            break
                        if user_timePlayed[user_tag][played_career] >= 0.4:
                            display += "<p style=\"font-size:12pt;color:BLUE\">" + played_career + ": Average\n" + "</p>"
                            break
                        if user_timePlayed[user_tag][played_career] >= 0.0:
                            display += "<p style=\"font-size:12pt;color:GREY\">" + played_career + ": Newbie\n" + "</p>"
                            break
            #self.textBrowser_101.setText( display )
            self.textBrowser_101.setHtml( display )


    def association_rule_response(self):
        tag = self.commandLinkButton.text()
        Association_Rule_Dialog = Diablo3_UI.Ui_Dialog("Association_Rule_UI", tag)
        Association_Rule_Dialog.exec_()

    def association_rule_response_2(self):
        tag = self.commandLinkButton_2.text()
        Association_Rule_Dialog = Diablo3_UI.Ui_Dialog("Association_Rule_UI", tag)
        Association_Rule_Dialog.exec_()

    def association_rule_response_3(self):
        tag = self.commandLinkButton_3.text()
        Association_Rule_Dialog = Diablo3_UI.Ui_Dialog("Association_Rule_UI", tag)
        Association_Rule_Dialog.exec_()

    def association_rule_response_4(self):
        tag = self.commandLinkButton_4.text()
        Association_Rule_Dialog = Diablo3_UI.Ui_Dialog("Association_Rule_UI", tag)
        Association_Rule_Dialog.exec_()

    def association_rule_response_5(self):
        tag = self.commandLinkButton_5.text()
        Association_Rule_Dialog = Diablo3_UI.Ui_Dialog("Association_Rule_UI", tag)
        Association_Rule_Dialog.exec_()
            
    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Diablo3 Novice Assitance  | CS670-IR-Prj | Copyright@ X.Y L.G ZL.Y", None))
        self.textBrowser.setText(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"right\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">M</span><span style=\" font-size:11pt;\">elee</span></p></body></html>", None))
        self.textBrowser_2.setText(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"right\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">R</span><span style=\" font-size:11pt;\">ange</span></p></body></html>", None))
        self.textBrowser_3.setText(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"right\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">P</span><span style=\" font-size:11pt;\">hysical</span></p></body></html>", None))
        self.textBrowser_4.setText(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"right\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">M</span><span style=\" font-size:11pt;\">agical</span></p></body></html>", None))
        self.textBrowser_5.setText(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"right\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">S</span><span style=\" font-size:11pt;\">upport</span></p></body></html>", None))
        self.textBrowser_6.setText(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"right\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">S</span><span style=\" font-size:11pt;\">olo</span></p></body></html>", None))
        self.textBrowser_7.setText(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"right\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">Damage</span></p></body></html>", None))
        self.textBrowser_8.setText(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"right\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">T</span><span style=\" font-size:11pt;\">ank</span></p></body></html>", None))
        self.textBrowser_9.setText(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"right\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">T</span><span style=\" font-size:11pt;\">eam</span></p></body></html>", None))
        self.groupBox.setTitle(_translate("Dialog", "Hero Ranking", None))
        self.textBrowser_14.setText(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">#5</span></p></body></html>", None))
        self.textBrowser_11.setText(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">#2</span></p></body></html>", None))
        self.textBrowser_13.setText(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">#4</span></p></body></html>", None))
        self.textBrowser_12.setText(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">#3</span></p></body></html>", None))
        self.textBrowser_10.setText(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">#1</span></p></body></html>", None))
        
        self.groupBox1.setTitle(_translate("Dialog", "Friendship/Player Recommending", None))
        self.pushButton.setText(_translate("Dialog", "View", None))
