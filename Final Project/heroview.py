# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'heroview.ui'
#
# Created: Sat Apr 27 23:24:10 2013
#      by: PyQt4 UI code generator 4.9.6
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyQt4 import *
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

class Ui_Dialog(QDialog):
    def setupUi(self, Dialog):
        self.tab = []
        self.label_3 = []
        self.HeroName = []
        self.label_2 = []
        self.HeroType = []
        self.label_4 = []
        self.HeroLevel = []
        self.groupBox = []
        self.label_44 = []
        self.label_45 = []
        self.label_46 = []
        self.label_47 = []
        self.label_48 = []
        self.label_49 = []
        self.label_50 = []
        self.label_51 = []
        self.label_53 = []
        self.label_54 = []
        self.label_55 = []
        self.label_56 = []
        self.label_57 = []
        self.label_59 = []
        self.Head = []
        self.Neck = []
        self.Torso = []
        self.Shoulders = []
        self.Hands = []
        self.MainHand = []
        self.Wrist = []
        self.Waist = []
        self.Legs = []
        self.Feet = []
        self.LeftFinger = []
        self.RightFinger = []
        self.Bracers = []
        self.Jewelry = []
        self.groupBox_2 = []
        self.label_20 = []
        self.label_33 = []
        self.label_34 = []
        self.label_35 = []
        self.label_36 = []
        self.label_37 = []
        self.label_38 = []
        self.label_39 = []
        self.label_40 = []
        self.label_41 = []
        self.label_42 = []
        self.label_43 = []
        self.line_4 = []
        self.line_5 = []
        self.label_52 = []
        self.label_58 = []
        self.label_60 = []
        self.Active_1 = []
        self.Active_2 = []
        self.Active_3 = []
        self.Active_4 = []
        self.Active_5 = []
        self.Active_6 = []
        self.Rune_1 = []
        self.Rune_4 = []
        self.Rune_5 = []
        self.Rune_6 = []
        self.Rune_2 = []
        self.Passive_3 = []
        self.Rune_3 = []
        self.Passive_1 = []
        self.Passive_2 = []
        self.line_2 = []
        self.groupBox_3 = []
        self.label_5 = []
        self.label_6 = []
        self.label_7 = []
        self.label_8 = []
        self.label_9 = []
        self.label_10 = []
        self.label_11 = []
        self.label_12 = []
        self.label_13 = []
        self.label_14 = []
        self.label_15 = []
        self.label_16 = []
        self.label_17 = []
        self.label_18 = []
        self.label_19 = []
        self.label_21 = []
        self.label_22 = []
        self.label_23 = []
        self.label_24 = []
        self.label_25 = []
        self.label_26 = []
        self.label_27 = []
        self.label_28 = []
        self.label_29 = []
        self.label_30 = []
        self.label_31 = []
        self.label_32 = []
        self.label_str = []
        self.lifeValue = []
        self.DamageValue = []
        self.AttackSpeedValue = []
        self.ArmorValue = []
        self.DexterityValue = []
        self.VitalityValue = []
        self.IntelligenceValue = []
        self.PhysicalResistValue = []
        self.FireResistValue = []
        self.ColdResistValue = []
        self.LightninResistValue = []
        self.PoisonResistValue = []
        self.ArcaneResistValue = []
        self.CritDamageValue = []
        self.BlockAmountMinValue = []
        self.BlockAmountMaxValue = []
        self.BlockChanceValue = []
        self.DamageIncreaseValue = []
        self.CritChanceValue = []
        self.DamageReductionValue = []
        self.LifeStealValue = []
        self.LifePerKillValue = []
        self.GoldFindValue = []
        self.MagicFindValue = []
        self.LifeOnHitValue = []
        self.PrimaryResourceValue = []
        self.SecondaryResourceValue = []
        self.StrengthValue = []
        self.line = []
        self.line_3 = []
        
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.setFixedSize(545, 525)
        Dialog.setWindowIcon( QtGui.QIcon( "res/icon/icon.png" ) )
        self.buttonBox = QtGui.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(180, 490, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.tabWidget = QtGui.QTabWidget(Dialog)
        self.tabWidget.setGeometry(QtCore.QRect(10, 30, 521, 461))
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        
        for i in range(len(self.stats)):
            
            self.tab.append(QtGui.QWidget())
            self.tab[i].setObjectName(_fromUtf8("tab"))

            
            self.label_3.append(QtGui.QLabel(self.tab[i]))
            self.label_3[i].setGeometry(QtCore.QRect(20, 10, 61, 16))
            self.label_3[i].setObjectName(_fromUtf8("label_3"))

            
            self.HeroName.append(QtGui.QLabel(self.tab[i]))
            self.HeroName[i].setGeometry(QtCore.QRect(90, 10, 141, 16))
            self.HeroName[i].setObjectName(_fromUtf8("HeroName"))

            
            self.label_2.append(QtGui.QLabel(self.tab[i]))
            self.label_2[i].setGeometry(QtCore.QRect(20, 30, 61, 16))
            self.label_2[i].setObjectName(_fromUtf8("label_2"))

            
            self.HeroType.append(QtGui.QLabel(self.tab[i]))
            self.HeroType[i].setGeometry(QtCore.QRect(90, 30, 141, 16))
            self.HeroType[i].setObjectName(_fromUtf8("HeroType"))

            
            self.label_4.append(QtGui.QLabel(self.tab[i]))
            self.label_4[i].setGeometry(QtCore.QRect(20, 50, 61, 16))
            self.label_4[i].setObjectName(_fromUtf8("label_4"))

            
            self.HeroLevel.append(QtGui.QLabel(self.tab[i]))
            self.HeroLevel[i].setGeometry(QtCore.QRect(90, 50, 141, 16))
            self.HeroLevel[i].setObjectName(_fromUtf8("HeroLevel"))

            
            self.groupBox.append(QtGui.QGroupBox(self.tab[i]))
            self.groupBox[i].setGeometry(QtCore.QRect(280, 10, 221, 241))
            self.groupBox[i].setObjectName(_fromUtf8("groupBox"))

            
            self.label_44.append(QtGui.QLabel(self.groupBox[i]))
            self.label_44[i].setGeometry(QtCore.QRect(10, 20, 46, 13))
            self.label_44[i].setObjectName(_fromUtf8("label_44"))

            
            self.label_45.append(QtGui.QLabel(self.groupBox[i]))
            self.label_45[i].setGeometry(QtCore.QRect(10, 50, 46, 13))
            self.label_45[i].setObjectName(_fromUtf8("label_45"))

            
            self.label_46.append(QtGui.QLabel(self.groupBox[i]))
            self.label_46[i].setGeometry(QtCore.QRect(110, 50, 46, 13))
            self.label_46[i].setObjectName(_fromUtf8("label_46"))

            
            self.label_47.append(QtGui.QLabel(self.groupBox[i]))
            self.label_47[i].setGeometry(QtCore.QRect(110, 110, 46, 13))
            self.label_47[i].setObjectName(_fromUtf8("label_47"))

            
            self.label_48.append(QtGui.QLabel(self.groupBox[i]))
            self.label_48[i].setGeometry(QtCore.QRect(110, 80, 46, 13))
            self.label_48[i].setObjectName(_fromUtf8("label_48"))

            
            self.label_49.append(QtGui.QLabel(self.groupBox[i]))
            self.label_49[i].setGeometry(QtCore.QRect(10, 110, 46, 13))
            self.label_49[i].setObjectName(_fromUtf8("label_49"))

            
            self.label_50.append(QtGui.QLabel(self.groupBox[i]))
            self.label_50[i].setGeometry(QtCore.QRect(110, 140, 46, 13))
            self.label_50[i].setObjectName(_fromUtf8("label_50"))

            
            self.label_51.append(QtGui.QLabel(self.groupBox[i]))
            self.label_51[i].setGeometry(QtCore.QRect(10, 140, 46, 13))
            self.label_51[i].setObjectName(_fromUtf8("label_51"))

            
            self.label_53.append(QtGui.QLabel(self.groupBox[i]))
            self.label_53[i].setGeometry(QtCore.QRect(10, 200, 46, 13))
            self.label_53[i].setObjectName(_fromUtf8("label_53"))

            
            self.label_54.append(QtGui.QLabel(self.groupBox[i]))
            self.label_54[i].setGeometry(QtCore.QRect(10, 80, 46, 13))
            self.label_54[i].setObjectName(_fromUtf8("label_54"))

            
            self.label_55.append(QtGui.QLabel(self.groupBox[i]))
            self.label_55[i].setGeometry(QtCore.QRect(110, 200, 46, 13))
            self.label_55[i].setObjectName(_fromUtf8("label_55"))

            
            self.label_56.append(QtGui.QLabel(self.groupBox[i]))
            self.label_56[i].setGeometry(QtCore.QRect(110, 170, 46, 13))
            self.label_56[i].setObjectName(_fromUtf8("label_56"))

            
            self.label_57.append(QtGui.QLabel(self.groupBox[i]))
            self.label_57[i].setGeometry(QtCore.QRect(10, 170, 51, 16))
            self.label_57[i].setObjectName(_fromUtf8("label_57"))

            
            self.label_59.append(QtGui.QLabel(self.groupBox[i]))
            self.label_59[i].setGeometry(QtCore.QRect(110, 20, 46, 13))
            self.label_59[i].setObjectName(_fromUtf8("label_59"))

            
            self.Head.append(QtGui.QLabel(self.groupBox[i]))
            self.Head[i].setGeometry(QtCore.QRect(10, 30, 101, 24))
            self.Head[i].setObjectName(_fromUtf8("Head"))

            
            self.Neck.append(QtGui.QLabel(self.groupBox[i]))
            self.Neck[i].setGeometry(QtCore.QRect(110, 30, 101, 24))
            self.Neck[i].setObjectName(_fromUtf8("Neck"))

            
            self.Torso.append(QtGui.QLabel(self.groupBox[i]))
            self.Torso[i].setGeometry(QtCore.QRect(110, 60, 101, 24))
            self.Torso[i].setObjectName(_fromUtf8("Torso"))

            
            self.Shoulders.append(QtGui.QLabel(self.groupBox[i]))
            self.Shoulders[i].setGeometry(QtCore.QRect(10, 60, 101, 24))
            self.Shoulders[i].setObjectName(_fromUtf8("Shoulders"))

            
            self.Hands.append(QtGui.QLabel(self.groupBox[i]))
            self.Hands[i].setGeometry(QtCore.QRect(110, 90, 101, 24))
            self.Hands[i].setObjectName(_fromUtf8("Hands"))

            
            self.MainHand.append(QtGui.QLabel(self.groupBox[i]))
            self.MainHand[i].setGeometry(QtCore.QRect(10, 90, 101, 24))
            self.MainHand[i].setObjectName(_fromUtf8("MainHand"))

            
            self.Wrist.append(QtGui.QLabel(self.groupBox[i]))
            self.Wrist[i].setGeometry(QtCore.QRect(110, 120, 101, 24))
            self.Wrist[i].setObjectName(_fromUtf8("Wrist"))

            
            self.Waist.append(QtGui.QLabel(self.groupBox[i]))
            self.Waist[i].setGeometry(QtCore.QRect(10, 120, 101, 24))
            self.Waist[i].setObjectName(_fromUtf8("Waist"))

            
            self.Legs.append(QtGui.QLabel(self.groupBox[i]))
            self.Legs[i].setGeometry(QtCore.QRect(110, 150, 101, 24))
            self.Legs[i].setObjectName(_fromUtf8("Legs"))

            
            self.Feet.append(QtGui.QLabel(self.groupBox[i]))
            self.Feet[i].setGeometry(QtCore.QRect(10, 150, 101, 24))
            self.Feet[i].setObjectName(_fromUtf8("Feet"))

            
            self.LeftFinger.append(QtGui.QLabel(self.groupBox[i]))
            self.LeftFinger[i].setGeometry(QtCore.QRect(110, 180, 101, 24))
            self.LeftFinger[i].setObjectName(_fromUtf8("LeftFinger"))

            
            self.RightFinger.append(QtGui.QLabel(self.groupBox[i]))
            self.RightFinger[i].setGeometry(QtCore.QRect(10, 180, 101, 24))
            self.RightFinger[i].setObjectName(_fromUtf8("RightFinger"))

            
            self.Bracers.append(QtGui.QLabel(self.groupBox[i]))
            self.Bracers[i].setGeometry(QtCore.QRect(10, 210, 101, 24))
            self.Bracers[i].setObjectName(_fromUtf8("Bracers"))

            
            self.Jewelry.append(QtGui.QLabel(self.groupBox[i]))
            self.Jewelry[i].setGeometry(QtCore.QRect(110, 210, 101, 24))
            self.Jewelry[i].setObjectName(_fromUtf8("Jewelry"))
                                 
            
            self.groupBox_2.append(QtGui.QGroupBox(self.tab[i]))
            self.groupBox_2[i].setGeometry(QtCore.QRect(10, 260, 491, 171))
            self.groupBox_2[i].setObjectName(_fromUtf8("groupBox_2"))

            
            self.label_20.append(QtGui.QLabel(self.groupBox_2[i]))
            self.label_20[i].setGeometry(QtCore.QRect(400, 20, 51, 16))
            self.label_20[i].setObjectName(_fromUtf8("label_20"))
                                 
            
            self.label_33.append( QtGui.QLabel(self.groupBox_2[i]) )
            self.label_33[i].setGeometry(QtCore.QRect(400, 70, 61, 16))
            self.label_33[i].setObjectName(_fromUtf8("label_33"))

            
            self.label_34.append( QtGui.QLabel(self.groupBox_2[i]) )
            self.label_34[i].setGeometry(QtCore.QRect(400, 120, 61, 16))
            self.label_34[i].setObjectName(_fromUtf8("label_34"))

            
            self.label_35.append( QtGui.QLabel(self.groupBox_2[i]) )
            self.label_35[i].setGeometry(QtCore.QRect(120, 70, 46, 13))
            self.label_35[i].setObjectName(_fromUtf8("label_35"))

            
            self.label_36.append(QtGui.QLabel(self.groupBox_2[i]))
            self.label_36[i].setGeometry(QtCore.QRect(10, 120, 46, 13))
            self.label_36[i].setObjectName(_fromUtf8("label_36"))

            
            self.label_37.append( QtGui.QLabel(self.groupBox_2[i]) )
            self.label_37[i].setGeometry(QtCore.QRect(120, 120, 46, 13))
            self.label_37[i].setObjectName(_fromUtf8("label_37"))

            
            self.label_38.append(QtGui.QLabel(self.groupBox_2[i]))
            self.label_38[i].setGeometry(QtCore.QRect(220, 70, 46, 13))
            self.label_38[i].setObjectName(_fromUtf8("label_38"))

            
            self.label_39.append(QtGui.QLabel(self.groupBox_2[i]))
            self.label_39[i].setGeometry(QtCore.QRect(320, 20, 46, 13))
            self.label_39[i].setObjectName(_fromUtf8("label_39"))

            
            self.label_40.append(QtGui.QLabel(self.groupBox_2[i]))
            self.label_40[i].setGeometry(QtCore.QRect(220, 120, 46, 13))
            self.label_40[i].setObjectName(_fromUtf8("label_40"))

            
            self.label_41.append(QtGui.QLabel(self.groupBox_2[i]))
            self.label_41[i].setGeometry(QtCore.QRect(320, 120, 46, 13))
            self.label_41[i].setObjectName(_fromUtf8("label_41"))

            
            self.label_42.append(QtGui.QLabel(self.groupBox_2[i]))
            self.label_42[i].setGeometry(QtCore.QRect(320, 70, 46, 13))
            self.label_42[i].setObjectName(_fromUtf8("label_42"))

            
            self.label_43.append(QtGui.QLabel(self.groupBox_2[i]))
            self.label_43[i].setGeometry(QtCore.QRect(220, 20, 46, 13))
            self.label_43[i].setObjectName(_fromUtf8("label_43"))

            
            self.line_4.append(QtGui.QFrame(self.groupBox_2[i]))
            self.line_4[i].setGeometry(QtCore.QRect(200, 20, 20, 141))
            self.line_4[i].setFrameShape(QtGui.QFrame.VLine)
            self.line_4[i].setFrameShadow(QtGui.QFrame.Sunken)
            self.line_4[i].setObjectName(_fromUtf8("line_4"))

            
            self.line_5.append(QtGui.QFrame(self.groupBox_2[i]))
            self.line_5[i].setGeometry(QtCore.QRect(380, 20, 20, 141))
            self.line_5[i].setFrameShape(QtGui.QFrame.VLine)
            self.line_5[i].setFrameShadow(QtGui.QFrame.Sunken)
            self.line_5[i].setObjectName(_fromUtf8("line_5"))

            
            self.label_52.append(QtGui.QLabel(self.groupBox_2[i]))
            self.label_52[i].setGeometry(QtCore.QRect(10, 20, 51, 16))
            self.label_52[i].setObjectName(_fromUtf8("label_52"))

            
            self.label_58.append(QtGui.QLabel(self.groupBox_2[i]))
            self.label_58[i].setGeometry(QtCore.QRect(10, 70, 61, 16))
            self.label_58[i].setObjectName(_fromUtf8("label_58"))

            
            self.label_60.append(QtGui.QLabel(self.groupBox_2[i]))
            self.label_60[i].setGeometry(QtCore.QRect(120, 20, 61, 16))
            self.label_60[i].setObjectName(_fromUtf8("label_60"))

            
            self.Active_1.append(QtGui.QLabel(self.groupBox_2[i]))
            self.Active_1[i].setGeometry(QtCore.QRect(10, 40, 81, 31))
            self.Active_1[i].setObjectName(_fromUtf8("Active_1"))

            
            self.Active_2.append(QtGui.QLabel(self.groupBox_2[i]))
            self.Active_2[i].setGeometry(QtCore.QRect(120, 40, 81, 31))
            self.Active_2[i].setObjectName(_fromUtf8("Active_2"))

            
            self.Active_3.append(QtGui.QLabel(self.groupBox_2[i]))
            self.Active_3[i].setGeometry(QtCore.QRect(10, 90, 81, 31))
            self.Active_3[i].setObjectName(_fromUtf8("Active_3"))

            
            self.Active_4.append(QtGui.QLabel(self.groupBox_2[i]))
            self.Active_4[i].setGeometry(QtCore.QRect(120, 90, 81, 31))
            self.Active_4[i].setObjectName(_fromUtf8("Active_4"))

            
            self.Active_5.append(QtGui.QLabel(self.groupBox_2[i]))
            self.Active_5[i].setGeometry(QtCore.QRect(10, 140, 81, 31))
            self.Active_5[i].setObjectName(_fromUtf8("Active_5"))

            
            self.Active_6.append(QtGui.QLabel(self.groupBox_2[i]))
            self.Active_6[i].setGeometry(QtCore.QRect(120, 140, 81, 31))
            self.Active_6[i].setObjectName(_fromUtf8("Active_6"))

            
            self.Rune_1.append(QtGui.QLabel(self.groupBox_2[i]))
            self.Rune_1[i].setGeometry(QtCore.QRect(220, 40, 61, 31))
            self.Rune_1[i].setObjectName(_fromUtf8("Rune_1"))

            
            self.Rune_4.append(QtGui.QLabel(self.groupBox_2[i]))
            self.Rune_4[i].setGeometry(QtCore.QRect(320, 90, 61, 31))
            self.Rune_4[i].setObjectName(_fromUtf8("Rune_4"))

            
            self.Rune_5.append(QtGui.QLabel(self.groupBox_2[i]))
            self.Rune_5[i].setGeometry(QtCore.QRect(220, 140, 61, 31))
            self.Rune_5[i].setObjectName(_fromUtf8("Rune_5"))

            
            self.Rune_6.append(QtGui.QLabel(self.groupBox_2[i]))
            self.Rune_6[i].setGeometry(QtCore.QRect(320, 140, 61, 31))
            self.Rune_6[i].setObjectName(_fromUtf8("Rune_6"))

            
            self.Rune_2.append(QtGui.QLabel(self.groupBox_2[i]))
            self.Rune_2[i].setGeometry(QtCore.QRect(320, 40, 61, 31))
            self.Rune_2[i].setObjectName(_fromUtf8("Rune_2"))

            
            self.Rune_3.append(QtGui.QLabel(self.groupBox_2[i]))
            self.Rune_3[i].setGeometry(QtCore.QRect(220, 90, 61, 31))
            self.Rune_3[i].setObjectName(_fromUtf8("Rune_3"))


            
            self.Passive_3.append(QtGui.QLabel(self.groupBox_2[i]))
            self.Passive_3[i].setGeometry(QtCore.QRect(400, 140, 81, 31))
            self.Passive_3[i].setObjectName(_fromUtf8("Passive_3"))

            
            self.Passive_1.append(QtGui.QLabel(self.groupBox_2[i]))
            self.Passive_1[i].setGeometry(QtCore.QRect(400, 40, 81, 31))
            self.Passive_1[i].setObjectName(_fromUtf8("Passive_1"))

            
            self.Passive_2.append(QtGui.QLabel(self.groupBox_2[i]))
            self.Passive_2[i].setGeometry(QtCore.QRect(400, 90, 81, 31))
            self.Passive_2[i].setObjectName(_fromUtf8("Passive_2"))

            
            self.line_2.append(QtGui.QFrame(self.tab[i]))
            self.line_2[i].setGeometry(QtCore.QRect(270, 10, 16, 241))
            self.line_2[i].setFrameShape(QtGui.QFrame.VLine)
            self.line_2[i].setFrameShadow(QtGui.QFrame.Sunken)
            self.line_2[i].setObjectName(_fromUtf8("line_2"))

            
            self.groupBox_3.append(QtGui.QGroupBox(self.tab[i]))
            self.groupBox_3[i].setGeometry(QtCore.QRect(10, 80, 261, 171))
            self.groupBox_3[i].setObjectName(_fromUtf8("groupBox_3"))

            
            self.label_5.append(QtGui.QLabel(self.groupBox_3[i]))
            self.label_5[i].setGeometry(QtCore.QRect(10, 20, 71, 16))
            self.label_5[i].setObjectName(_fromUtf8("label_5"))

            
            self.label_6.append(QtGui.QLabel(self.groupBox_3[i]))
            self.label_6[i].setGeometry(QtCore.QRect(10, 30, 71, 16))
            self.label_6[i].setObjectName(_fromUtf8("label_6"))

            
            self.label_7.append(QtGui.QLabel(self.groupBox_3[i]))
            self.label_7[i].setGeometry(QtCore.QRect(10, 40, 71, 16))
            self.label_7[i].setObjectName(_fromUtf8("label_7"))

            
            self.label_8.append(QtGui.QLabel(self.groupBox_3[i]))
            self.label_8[i].setGeometry(QtCore.QRect(10, 50, 71, 16))
            self.label_8[i].setObjectName(_fromUtf8("label_8"))

            
            self.label_9.append(QtGui.QLabel(self.groupBox_3[i]))
            self.label_9[i].setGeometry(QtCore.QRect(10, 60, 71, 16))
            self.label_9[i].setObjectName(_fromUtf8("label_9"))

            
            self.label_10.append(QtGui.QLabel(self.groupBox_3[i]))
            self.label_10[i].setGeometry(QtCore.QRect(10, 70, 71, 16))
            self.label_10[i].setObjectName(_fromUtf8("label_10"))

            
            self.label_11.append(QtGui.QLabel(self.groupBox_3[i]))
            self.label_11[i].setGeometry(QtCore.QRect(10, 80, 71, 16))
            self.label_11[i].setObjectName(_fromUtf8("label_11"))

            
            self.label_12.append(QtGui.QLabel(self.groupBox_3[i]))
            self.label_12[i].setGeometry(QtCore.QRect(10, 90, 71, 16))
            self.label_12[i].setObjectName(_fromUtf8("label_12"))

            
            self.label_13.append(QtGui.QLabel(self.groupBox_3[i]))
            self.label_13[i].setGeometry(QtCore.QRect(10, 100, 71, 16))
            self.label_13[i].setObjectName(_fromUtf8("label_13"))

            
            self.label_14.append(QtGui.QLabel(self.groupBox_3[i]))
            self.label_14[i].setGeometry(QtCore.QRect(10, 110, 71, 16))
            self.label_14[i].setObjectName(_fromUtf8("label_14"))

            
            self.label_15.append(QtGui.QLabel(self.groupBox_3[i]))
            self.label_15[i].setGeometry(QtCore.QRect(10, 120, 71, 16))
            self.label_15[i].setObjectName(_fromUtf8("label_15"))

            
            self.label_16.append(QtGui.QLabel(self.groupBox_3[i]))
            self.label_16[i].setGeometry(QtCore.QRect(10, 130, 71, 16))
            self.label_16[i].setObjectName(_fromUtf8("label_16"))

            
            self.label_17.append(QtGui.QLabel(self.groupBox_3[i]))
            self.label_17[i].setGeometry(QtCore.QRect(10, 140, 71, 16))
            self.label_17[i].setObjectName(_fromUtf8("label_17"))

            
            self.label_18.append(QtGui.QLabel(self.groupBox_3[i]))
            self.label_18[i].setGeometry(QtCore.QRect(10, 150, 71, 16))
            self.label_18[i].setObjectName(_fromUtf8("label_18"))

            
            self.label_19.append(QtGui.QLabel(self.groupBox_3[i]))
            self.label_19[i].setGeometry(QtCore.QRect(130, 40, 71, 16))
            self.label_19[i].setObjectName(_fromUtf8("label_19"))

            
            self.label_21.append(QtGui.QLabel(self.groupBox_3[i]))
            self.label_21[i].setGeometry(QtCore.QRect(130, 20, 81, 16))
            self.label_21[i].setObjectName(_fromUtf8("label_21"))

            
            self.label_22.append(QtGui.QLabel(self.groupBox_3[i]))
            self.label_22[i].setGeometry(QtCore.QRect(130, 30, 81, 16))
            self.label_22[i].setObjectName(_fromUtf8("label_22"))

            
            self.label_23.append(QtGui.QLabel(self.groupBox_3[i]))
            self.label_23[i].setGeometry(QtCore.QRect(130, 50, 81, 16))
            self.label_23[i].setObjectName(_fromUtf8("label_23"))

            
            self.label_24.append(QtGui.QLabel(self.groupBox_3[i]))
            self.label_24[i].setGeometry(QtCore.QRect(130, 60, 81, 16))
            self.label_24[i].setObjectName(_fromUtf8("label_24"))

            
            self.label_25.append(QtGui.QLabel(self.groupBox_3[i]))
            self.label_25[i].setGeometry(QtCore.QRect(130, 70, 91, 16))
            self.label_25[i].setObjectName(_fromUtf8("label_25"))
            
            
            self.label_26.append(QtGui.QLabel(self.groupBox_3[i]))
            self.label_26[i].setGeometry(QtCore.QRect(130, 80, 91, 16))
            self.label_26[i].setObjectName(_fromUtf8("label_26"))

            
            self.label_27.append(QtGui.QLabel(self.groupBox_3[i]))
            self.label_27[i].setGeometry(QtCore.QRect(130, 90, 71, 16))
            self.label_27[i].setObjectName(_fromUtf8("label_27"))

            
            self.label_28.append(QtGui.QLabel(self.groupBox_3[i]))
            self.label_28[i].setGeometry(QtCore.QRect(130, 100, 71, 16))
            self.label_28[i].setObjectName(_fromUtf8("label_28"))

            
            self.label_29.append(QtGui.QLabel(self.groupBox_3[i]))
            self.label_29[i].setGeometry(QtCore.QRect(130, 110, 71, 16))
            self.label_29[i].setObjectName(_fromUtf8("label_29"))

            
            self.label_30.append(QtGui.QLabel(self.groupBox_3[i]))
            self.label_30[i].setGeometry(QtCore.QRect(130, 120, 71, 16))
            self.label_30[i].setObjectName(_fromUtf8("label_30"))

            
            self.label_31.append(QtGui.QLabel(self.groupBox_3[i]))
            self.label_31[i].setGeometry(QtCore.QRect(130, 130, 91, 16))
            self.label_31[i].setObjectName(_fromUtf8("label_31"))

            
            self.label_32.append(QtGui.QLabel(self.groupBox_3[i]))
            self.label_32[i].setGeometry(QtCore.QRect(130, 140, 101, 16))
            self.label_32[i].setObjectName(_fromUtf8("label_32"))

            
            self.label_str.append(QtGui.QLabel(self.groupBox_3[i]))
            self.label_str[i].setGeometry(QtCore.QRect(130, 150, 71, 13))
            self.label_str[i].setObjectName(_fromUtf8("label_str"))

################################################################################################            
            
            self.lifeValue.append(QtGui.QLabel(self.groupBox_3[i]))
            self.lifeValue[i].setGeometry(QtCore.QRect(90, 20, 46, 13))
            self.lifeValue[i].setObjectName(_fromUtf8("lifeValue"))

            
            self.DamageValue.append(QtGui.QLabel(self.groupBox_3[i]))
            self.DamageValue[i].setGeometry(QtCore.QRect(90, 30, 46, 13))
            self.DamageValue[i].setObjectName(_fromUtf8("DamageValue"))

            
            self.AttackSpeedValue.append(QtGui.QLabel(self.groupBox_3[i]))
            self.AttackSpeedValue[i].setGeometry(QtCore.QRect(90, 40, 46, 13))
            self.AttackSpeedValue[i].setObjectName(_fromUtf8("AttackSpeedValue"))

            
            self.ArmorValue.append(QtGui.QLabel(self.groupBox_3[i]))
            self.ArmorValue[i].setGeometry(QtCore.QRect(90, 50, 46, 13))
            self.ArmorValue[i].setObjectName(_fromUtf8("ArmorValue"))

            
            self.DexterityValue.append(QtGui.QLabel(self.groupBox_3[i]))
            self.DexterityValue[i].setGeometry(QtCore.QRect(90, 60, 46, 13))
            self.DexterityValue[i].setObjectName(_fromUtf8("DexterityValue"))

            
            self.VitalityValue.append(QtGui.QLabel(self.groupBox_3[i]))
            self.VitalityValue[i].setGeometry(QtCore.QRect(90, 70, 46, 13))
            self.VitalityValue[i].setObjectName(_fromUtf8("VitalityValue"))


            
            self.IntelligenceValue.append(QtGui.QLabel(self.groupBox_3[i]))
            self.IntelligenceValue[i].setGeometry(QtCore.QRect(90, 80, 46, 13))
            self.IntelligenceValue[i].setObjectName(_fromUtf8("IntelligenceValue"))

            
            self.PhysicalResistValue.append(QtGui.QLabel(self.groupBox_3[i]))
            self.PhysicalResistValue[i].setGeometry(QtCore.QRect(90, 90, 46, 13))
            self.PhysicalResistValue[i].setObjectName(_fromUtf8("PhysicalResistValue"))

            
            self.FireResistValue.append(QtGui.QLabel(self.groupBox_3[i]))
            self.FireResistValue[i].setGeometry(QtCore.QRect(90, 100, 46, 13))
            self.FireResistValue[i].setObjectName(_fromUtf8("FireResistValue"))

##############################

            
            self.ColdResistValue.append(QtGui.QLabel(self.groupBox_3[i]))
            self.ColdResistValue[i].setGeometry(QtCore.QRect(90, 110, 46, 13))
            self.ColdResistValue[i].setObjectName(_fromUtf8("ColdResistValue"))

            
            self.LightninResistValue.append(QtGui.QLabel(self.groupBox_3[i]))
            self.LightninResistValue[i].setGeometry(QtCore.QRect(90, 120, 46, 13))
            self.LightninResistValue[i].setObjectName(_fromUtf8("LightninResistValue"))

            
            self.PoisonResistValue.append(QtGui.QLabel(self.groupBox_3[i]))
            self.PoisonResistValue[i].setGeometry(QtCore.QRect(90, 130, 46, 13))
            self.PoisonResistValue[i].setObjectName(_fromUtf8("PoisonResistValue"))

            
            self.ArcaneResistValue.append(QtGui.QLabel(self.groupBox_3[i]))
            self.ArcaneResistValue[i].setGeometry(QtCore.QRect(90, 140, 46, 13))
            self.ArcaneResistValue[i].setObjectName(_fromUtf8("ArcaneResistValue"))

            
            self.CritDamageValue.append(QtGui.QLabel(self.groupBox_3[i]))
            self.CritDamageValue[i].setGeometry(QtCore.QRect(90, 150, 46, 13))
            self.CritDamageValue[i].setObjectName(_fromUtf8("CritDamageValue"))

            
            self.BlockAmountMinValue.append(QtGui.QLabel(self.groupBox_3[i]))
            self.BlockAmountMinValue[i].setGeometry(QtCore.QRect(220, 20, 46, 13))
            self.BlockAmountMinValue[i].setObjectName(_fromUtf8("BlockAmountMinValue"))

            
            self.BlockAmountMaxValue.append(QtGui.QLabel(self.groupBox_3[i]))
            self.BlockAmountMaxValue[i].setGeometry(QtCore.QRect(220, 30, 46, 13))
            self.BlockAmountMaxValue[i].setObjectName(_fromUtf8("BlockAmountMaxValue"))

            
            self.BlockChanceValue.append(QtGui.QLabel(self.groupBox_3[i]))
            self.BlockChanceValue[i].setGeometry(QtCore.QRect(220, 40, 46, 13))
            self.BlockChanceValue[i].setObjectName(_fromUtf8("BlockChanceValue"))

            
            self.DamageIncreaseValue.append(QtGui.QLabel(self.groupBox_3[i]))
            self.DamageIncreaseValue[i].setGeometry(QtCore.QRect(220, 50, 46, 13))
            self.DamageIncreaseValue[i].setObjectName(_fromUtf8("DamageIncreaseValue"))

            
            self.CritChanceValue.append(QtGui.QLabel(self.groupBox_3[i]))
            self.CritChanceValue[i].setGeometry(QtCore.QRect(220, 60, 46, 13))
            self.CritChanceValue[i].setObjectName(_fromUtf8("CritChanceValue"))

            
            self.DamageReductionValue.append(QtGui.QLabel(self.groupBox_3[i]))
            self.DamageReductionValue[i].setGeometry(QtCore.QRect(220, 70, 46, 13))
            self.DamageReductionValue[i].setObjectName(_fromUtf8("DamageReductionValue"))

##########################################
            
            self.LifeStealValue.append(QtGui.QLabel(self.groupBox_3[i]))
            self.LifeStealValue[i].setGeometry(QtCore.QRect(220, 80, 46, 13))
            self.LifeStealValue[i].setObjectName(_fromUtf8("LifeStealValue"))

            
            self.LifePerKillValue.append(QtGui.QLabel(self.groupBox_3[i]))
            self.LifePerKillValue[i].setGeometry(QtCore.QRect(220, 90, 46, 13))
            self.LifePerKillValue[i].setObjectName(_fromUtf8("LifePerKillValue"))

            
            self.GoldFindValue.append(QtGui.QLabel(self.groupBox_3[i]))
            self.GoldFindValue[i].setGeometry(QtCore.QRect(220, 100, 46, 13))
            self.GoldFindValue[i].setObjectName(_fromUtf8("GoldFindValue"))

            
            self.MagicFindValue.append(QtGui.QLabel(self.groupBox_3[i]))
            self.MagicFindValue[i].setGeometry(QtCore.QRect(220, 110, 46, 13))
            self.MagicFindValue[i].setObjectName(_fromUtf8("MagicFindValue"))

            
            self.LifeOnHitValue.append(QtGui.QLabel(self.groupBox_3[i]))
            self.LifeOnHitValue[i].setGeometry(QtCore.QRect(220, 120, 46, 13))
            self.LifeOnHitValue[i].setObjectName(_fromUtf8("LifeOnHitValue"))

            
            self.PrimaryResourceValue.append(QtGui.QLabel(self.groupBox_3[i]))
            self.PrimaryResourceValue[i].setGeometry(QtCore.QRect(220, 130, 46, 13))
            self.PrimaryResourceValue[i].setObjectName(_fromUtf8("PrimaryResourceValue"))

            
            self.SecondaryResourceValue.append(QtGui.QLabel(self.groupBox_3[i]))
            self.SecondaryResourceValue[i].setGeometry(QtCore.QRect(220, 140, 46, 13))
            self.SecondaryResourceValue[i].setObjectName(_fromUtf8("SecondaryResourceValue"))

            
            self.StrengthValue.append(QtGui.QLabel(self.groupBox_3[i]))
            self.StrengthValue[i].setGeometry(QtCore.QRect(220, 150, 46, 13))
            self.StrengthValue[i].setObjectName(_fromUtf8("StrengthValue"))

            
            self.line.append(QtGui.QFrame(self.tab[i]))
            self.line[i].setGeometry(QtCore.QRect(20, 250, 471, 16))
            self.line[i].setFrameShape(QtGui.QFrame.HLine)
            self.line[i].setFrameShadow(QtGui.QFrame.Sunken)
            self.line[i].setObjectName(_fromUtf8("line"))

            
            self.line_3.append(QtGui.QFrame(self.tab[i]))
            self.line_3[i].setGeometry(QtCore.QRect(20, 70, 251, 16))
            self.line_3[i].setFrameShape(QtGui.QFrame.HLine)
            self.line_3[i].setFrameShadow(QtGui.QFrame.Sunken)
            self.line_3[i].setObjectName(_fromUtf8("line_3"))
            
            self.tabWidget.addTab(self.tab[i], _fromUtf8(""))

            
            
        self.label = QtGui.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(10, 10, 61, 16))
        self.label.setObjectName(_fromUtf8("label"))
        self.UserName = QtGui.QLabel(Dialog)
        self.UserName.setGeometry(QtCore.QRect(80, 10, 200, 13))
        self.UserName.setObjectName(_fromUtf8("UserName"))

        self.retranslateUi(Dialog)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), Dialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Details Viewer | CS670-IR-Prj | Copyright@ X.Y L.G ZL.Y", None))
        for i in range(len(self.stats)):
            self.label_3[i].setText(_translate("Dialog", "Hero Name:", None))
            self.HeroName[i].setText(_translate("Dialog", self.stats[i]["name"], None))
            self.label_2[i].setText(_translate("Dialog", "Hero Type:", None))
            self.HeroType[i].setText(_translate("Dialog", self.stats[i]["class"], None))
            self.label_4[i].setText(_translate("Dialog", "Hero Level:", None))
            self.HeroLevel[i].setText(_translate("Dialog", str(self.stats[i]["level"]), None))
            self.groupBox[i].setTitle(_translate("Dialog", "Equipments", None))
            self.label_44[i].setText(_translate("Dialog", "head", None))
            self.label_45[i].setText(_translate("Dialog", "shoulders", None))
            self.label_46[i].setText(_translate("Dialog", "torso", None))
            self.label_47[i].setText(_translate("Dialog", "wrist", None))
            self.label_48[i].setText(_translate("Dialog", "hands", None))
            self.label_49[i].setText(_translate("Dialog", "waist", None))
            self.label_50[i].setText(_translate("Dialog", "legs", None))
            self.label_str[i].setText(_translate("Dialog", "strength", None))
            self.label_51[i].setText(_translate("Dialog", "feet", None))
            self.label_53[i].setText(_translate("Dialog", "bracers", None))
            self.label_54[i].setText(_translate("Dialog", "mainHand", None))
            self.label_55[i].setText(_translate("Dialog", "jewelry", None))
            self.label_56[i].setText(_translate("Dialog", "leftFinger", None))
            self.label_57[i].setText(_translate("Dialog", "rightFinger", None))
            self.label_59[i].setText(_translate("Dialog", "neck", None))
            self.Head[i].setText(_translate("Dialog", self.stats[i]["items"]["head"], None))
            self.Neck[i].setText(_translate("Dialog", self.stats[i]["items"]["neck"], None))
            self.Torso[i].setText(_translate("Dialog", self.stats[i]["items"]["torso"], None))
            self.Shoulders[i].setText(_translate("Dialog", self.stats[i]["items"]["shoulders"], None))
            self.Hands[i].setText(_translate("Dialog", self.stats[i]["items"]["hands"], None))
            self.MainHand[i].setText(_translate("Dialog", self.stats[i]["items"]["mainHand"], None))
            self.Wrist[i].setText(_translate("Dialog", self.stats[i]["items"]["wrist"], None))
            self.Waist[i].setText(_translate("Dialog", self.stats[i]["items"]["waist"], None))
            self.Legs[i].setText(_translate("Dialog", self.stats[i]["items"]["legs"], None))
            self.Feet[i].setText(_translate("Dialog", self.stats[i]["items"]["feet"], None))
            self.LeftFinger[i].setText(_translate("Dialog", self.stats[i]["items"]["leftFinger"], None))
            self.RightFinger[i].setText(_translate("Dialog", self.stats[i]["items"]["rightFinger"], None))
            self.Bracers[i].setText(_translate("Dialog", self.stats[i]["items"]["bracers"], None))
            self.Jewelry[i].setText(_translate("Dialog", self.stats[i]["items"]["jewelry"], None))
            self.groupBox_2[i].setTitle(_translate("Dialog", "Skills", None))
            self.label_20[i].setText(_translate("Dialog", "Passive #1", None))
            self.label_33[i].setText(_translate("Dialog", "Passive #2", None))
            self.label_34[i].setText(_translate("Dialog", "Passive #3", None))
            self.label_35[i].setText(_translate("Dialog", "Active #4", None))
            self.label_36[i].setText(_translate("Dialog", "Active #5", None))
            self.label_37[i].setText(_translate("Dialog", "Active #6", None))
            self.label_38[i].setText(_translate("Dialog", "Rune #3", None))
            self.label_39[i].setText(_translate("Dialog", "Rune #2", None))
            self.label_40[i].setText(_translate("Dialog", "Rune #5", None))
            self.label_41[i].setText(_translate("Dialog", "Rune #6", None))
            self.label_42[i].setText(_translate("Dialog", "Rune #4", None))
            self.label_43[i].setText(_translate("Dialog", "Rune #1", None))
            self.label_52[i].setText(_translate("Dialog", "Active #1", None))
            self.label_58[i].setText(_translate("Dialog", "Active #3", None))
            self.label_60[i].setText(_translate("Dialog", "Active #2", None))
            self.Active_1[i].setText(_translate("Dialog", self.stats[i]["skills"]["active"][0]["name"], None))
            self.Active_2[i].setText(_translate("Dialog", self.stats[i]["skills"]["active"][1]["name"], None))
            self.Active_3[i].setText(_translate("Dialog", self.stats[i]["skills"]["active"][2]["name"], None))
            self.Active_4[i].setText(_translate("Dialog", self.stats[i]["skills"]["active"][3]["name"], None))
            self.Active_5[i].setText(_translate("Dialog", self.stats[i]["skills"]["active"][4]["name"], None))
            self.Active_6[i].setText(_translate("Dialog", self.stats[i]["skills"]["active"][5]["name"], None))
            self.Rune_1[i].setText(_translate("Dialog", self.stats[i]["skills"]["rune"][0]["name"], None))
            self.Rune_4[i].setText(_translate("Dialog", self.stats[i]["skills"]["rune"][3]["name"], None))
            self.Rune_5[i].setText(_translate("Dialog", self.stats[i]["skills"]["rune"][4]["name"], None))
            self.Rune_6[i].setText(_translate("Dialog", self.stats[i]["skills"]["rune"][5]["name"], None))
            self.Rune_2[i].setText(_translate("Dialog", self.stats[i]["skills"]["rune"][1]["name"], None))
            self.Rune_3[i].setText(_translate("Dialog", self.stats[i]["skills"]["rune"][2]["name"], None))
            self.Passive_3[i].setText(_translate("Dialog", self.stats[i]["skills"]["passive"][2]["name"], None))
            self.Passive_1[i].setText(_translate("Dialog", self.stats[i]["skills"]["passive"][0]["name"], None))
            self.Passive_2[i].setText(_translate("Dialog", self.stats[i]["skills"]["passive"][1]["name"], None))
            self.groupBox_3[i].setTitle(_translate("Dialog", "Stats", None))
            self.label_5[i].setText(_translate("Dialog", "life", None))
            self.label_6[i].setText(_translate("Dialog", "damage", None))
            self.label_7[i].setText(_translate("Dialog", "attackSpeed", None))
            self.label_8[i].setText(_translate("Dialog", "armor", None))
            self.label_9[i].setText(_translate("Dialog", "dexterity", None))
            self.label_10[i].setText(_translate("Dialog", "vitality", None))
            self.label_11[i].setText(_translate("Dialog", "intelligence", None))
            self.label_12[i].setText(_translate("Dialog", "physicalResist", None))
            self.label_13[i].setText(_translate("Dialog", "fireResist", None))
            self.label_14[i].setText(_translate("Dialog", "coldResist", None))
            self.label_15[i].setText(_translate("Dialog", "lightningResist", None))
            self.label_16[i].setText(_translate("Dialog", "poisonResist", None))
            self.label_17[i].setText(_translate("Dialog", "arcaneResist", None))
            self.label_18[i].setText(_translate("Dialog", "critDamage", None))
            self.label_19[i].setText(_translate("Dialog", "blockChance", None))
            self.label_21[i].setText(_translate("Dialog", "blockAmountMin", None))
            self.label_22[i].setText(_translate("Dialog", "blockAmountMax", None))
            self.label_23[i].setText(_translate("Dialog", "damageIncrease", None))
            self.label_24[i].setText(_translate("Dialog", "critChance", None))
            self.label_25[i].setText(_translate("Dialog", "damageReduction", None))
            self.label_26[i].setText(_translate("Dialog", "lifeSteal", None))
            self.label_27[i].setText(_translate("Dialog", "lifePerKill", None))
            self.label_28[i].setText(_translate("Dialog", "goldFind", None))
            self.label_29[i].setText(_translate("Dialog", "magicFind", None))
            self.label_30[i].setText(_translate("Dialog", "lifeOnHit", None))
            self.label_31[i].setText(_translate("Dialog", "primaryResource", None))
            self.label_32[i].setText(_translate("Dialog", "2ndResource", None))
            self.lifeValue[i].setText(_translate("Dialog", self.stats[i]["stats"]["life"], None))
            self.DamageValue[i].setText(_translate("Dialog", self.stats[i]["stats"]["damage"], None))
            self.AttackSpeedValue[i].setText(_translate("Dialog", self.stats[i]["stats"]["attackSpeed"], None))
            self.ArmorValue[i].setText(_translate("Dialog", self.stats[i]["stats"]["armor"], None))
            self.DexterityValue[i].setText(_translate("Dialog", self.stats[i]["stats"]["dexterity"], None))
            self.VitalityValue[i].setText(_translate("Dialog", self.stats[i]["stats"]["vitality"], None))
            self.IntelligenceValue[i].setText(_translate("Dialog", self.stats[i]["stats"]["intelligence"], None))
            self.PhysicalResistValue[i].setText(_translate("Dialog", self.stats[i]["stats"]["physicalResist"], None))
            self.FireResistValue[i].setText(_translate("Dialog", self.stats[i]["stats"]["fireResist"], None))
            self.ColdResistValue[i].setText(_translate("Dialog", self.stats[i]["stats"]["coldResist"], None))
            self.LightninResistValue[i].setText(_translate("Dialog", self.stats[i]["stats"]["lightningResist"], None))
            self.PoisonResistValue[i].setText(_translate("Dialog", self.stats[i]["stats"]["poisonResist"], None))
            self.ArcaneResistValue[i].setText(_translate("Dialog", self.stats[i]["stats"]["arcaneResist"], None))
            self.CritDamageValue[i].setText(_translate("Dialog", self.stats[i]["stats"]["critDamage"], None))
            self.BlockAmountMinValue[i].setText(_translate("Dialog", self.stats[i]["stats"]["blockAmountMin"], None))
            self.BlockAmountMaxValue[i].setText(_translate("Dialog", self.stats[i]["stats"]["blockAmountMax"], None))
            self.BlockChanceValue[i].setText(_translate("Dialog", self.stats[i]["stats"]["blockChance"], None))
            self.DamageIncreaseValue[i].setText(_translate("Dialog", self.stats[i]["stats"]["damageIncrease"], None))
            self.CritChanceValue[i].setText(_translate("Dialog", self.stats[i]["stats"]["critChance"], None))
            self.DamageReductionValue[i].setText(_translate("Dialog", self.stats[i]["stats"]["damageReduction"], None))
            self.LifeStealValue[i].setText(_translate("Dialog", self.stats[i]["stats"]["lifeSteal"], None))
            self.LifePerKillValue[i].setText(_translate("Dialog", self.stats[i]["stats"]["lifePerKill"], None))
            self.GoldFindValue[i].setText(_translate("Dialog", self.stats[i]["stats"]["goldFind"], None))
            self.MagicFindValue[i].setText(_translate("Dialog", self.stats[i]["stats"]["magicFind"], None))
            self.LifeOnHitValue[i].setText(_translate("Dialog", self.stats[i]["stats"]["lifeOnHit"], None))
            self.PrimaryResourceValue[i].setText(_translate("Dialog", self.stats[i]["stats"]["primaryResource"], None))
            self.SecondaryResourceValue[i].setText(_translate("Dialog", self.stats[i]["stats"]["secondaryResource"], None))
            self.StrengthValue[i].setText(_translate("Dialog", self.stats[i]["stats"]["strength"], None))
            self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab[i]), _translate("Dialog", self.stats[i]["name"], None))
            #self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("Dialog", "Tab 2", None))
        self.label.setText(_translate("Dialog", "User Name:", None))
        self.UserName.setText(_translate("Dialog", self.username, None))

    def __init__(self, string, parent=None):
        super(Ui_Dialog, self).__init__(parent)
        # get hero list
        self.username = string
        infile1 = open("user-hero.json","r")
        record1 = json.load(infile1)
        herolist = record1[self.username]

        infile1.close()

        # get hero detail info
        infile2 = open("hero-brief-info.json", "r")
        record2 = json.load(infile2)
        self.stats = []
        for hero in herolist:
            self.stats.append(record2[str(hero["id"])])

        infile2.close()
       
        self.setupUi(self)
        QDialog.exec_
