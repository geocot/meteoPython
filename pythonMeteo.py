# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'pythonMeteo.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import objMeteo, time

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        self.objM = objMeteo.Meteo('https://meteo.gc.ca/rss/city/qc-133_f.xml')
        Dialog.setObjectName("Dialog")
        Dialog.setFixedSize(400, 206)
        self.btnFermer = QtWidgets.QPushButton(Dialog)
        self.btnFermer.setGeometry(QtCore.QRect(310, 180, 75, 23))
        self.btnFermer.setObjectName("btnFermer")
        self.btnFermer.clicked.connect(self._ferme)
        self.groupTemp = QtWidgets.QGroupBox(Dialog)
        self.groupTemp.setGeometry(QtCore.QRect(190, 10, 191, 80))
        self.groupTemp.setObjectName("groupTemp")
        self.lTemp = QtWidgets.QLabel(self.groupTemp)
        self.lTemp.setGeometry(QtCore.QRect(10, 10, 111, 61))
        font = QtGui.QFont()
        font.setPointSize(25)
        font.setItalic(False)
        self.lTemp.setFont(font)
        self.lTemp.setObjectName("lTemp")
        self.lTemp_2 = QtWidgets.QLabel(self.groupTemp)
        self.lTemp_2.setGeometry(QtCore.QRect(120, 70, 111, 61))
        self.lTempTendance = QtWidgets.QLabel(self.groupTemp)
        self.lTempTendance.setGeometry(QtCore.QRect(140, 10, 41, 61))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setItalic(False)
        self.lTempTendance.setFont(font)
        self.lTempTendance.setObjectName("lTempTendance")
        self.groupPression = QtWidgets.QGroupBox(Dialog)
        self.groupPression.setGeometry(QtCore.QRect(190, 100, 191, 80))
        self.groupPression.setObjectName("groupPression")
        self.lPression = QtWidgets.QLabel(self.groupPression)
        self.lPression.setGeometry(QtCore.QRect(10, 10, 111, 61))
        font = QtGui.QFont()
        font.setPointSize(25)
        font.setItalic(False)
        self.lPression.setFont(font)
        self.lPression.setObjectName("lPression")
        self.lPressionTendance = QtWidgets.QLabel(self.groupPression)
        self.lPressionTendance.setGeometry(QtCore.QRect(140, 10, 41, 61))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setItalic(False)
        self.lPressionTendance.setFont(font)
        self.lPressionTendance.setObjectName("lPressionTendance")
        self.lHeure = QtWidgets.QLabel(Dialog)
        self.lHeure.setGeometry(QtCore.QRect(10, 0, 171, 21))
        self.lHeure.setAlignment(QtCore.Qt.AlignCenter)
        self.lHeure.setObjectName("lHeure")
        self.lCondition = QtWidgets.QLabel(Dialog)
        self.lCondition.setGeometry(QtCore.QRect(20, 20, 151, 141))
        self.lCondition.setText("")
        self.lCondition.setPixmap(QtGui.QPixmap("images/nuageux_soleil.png"))
        self.lCondition.setScaledContents(True)
        self.lCondition.setObjectName("lCondition")
        self.lConditionTxt = QtWidgets.QLabel(Dialog)
        self.lConditionTxt.setGeometry(QtCore.QRect(20, 150, 161, 31))
        self.lConditionTxt.setAlignment(QtCore.Qt.AlignCenter)
        self.lConditionTxt.setObjectName("lConditionTxt")
        self.lAlerte = QtWidgets.QLabel(Dialog)
        self.lAlerte.setGeometry(QtCore.QRect(20, 170, 161, 31))
        self.lAlerte.setObjectName("lAlerte")
        self._afficheMeteo()

        #Raffraichir la page
        # make QTimer
        self.qTimer = QtCore.QTimer()
        # set interval to 1 s
        self.qTimer.setInterval(600000)  # 1000 ms = 1 s
        # connect timeout signal to signal handler
        self.qTimer.timeout.connect(self._afficheMeteo)
        # start timer
        self.qTimer.start()

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)


    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Météo Québec"))
        self.btnFermer.setText(_translate("Dialog", "Fermer"))
        self.groupTemp.setTitle(_translate("Dialog", "Température"))
        #self.lTemp.setText(_translate("Dialog", "0"))
        #self.lTemp_2.setText(_translate("Dialog", "0"))
        #self.lTempTendance.setText(_translate("Dialog", "Hausse"))
        self.groupPression.setTitle(_translate("Dialog", "Pression Kpa"))
        #self.lPression.setText(_translate("Dialog", "1023"))
        #self.lPressionTendance.setText(_translate("Dialog", "Baisse"))
        #self.lHeure.setText(_translate("Dialog", "Heure: 12:00"))
        #self.lConditionTxt.setText(_translate("Dialog", "Soleil"))
        #self.lAlerte.setText(_translate("Dialog", "Aucune alerte"))

    def _ferme(self):
        QtCore.QCoreApplication.quit()

    def _afficheMeteo(self):
            self.objM.lireMeteo()
            self.lTemp.setText(self.objM.temperature)
            self.lPression.setText(self.objM.pression)
            self.lPressionTendance.setText(self.objM.tendancePression)
            self.lHeure.setText(self.objM.dateHeure)
            self.lConditionTxt.setText(self.objM.condition)
            self.lAlerte.setText(self.objM.avertissement)
            self.lTempTendance.setText(self.objM.tendanceTemperature)
            self._icone(self.objM.condition)

    def _icone(self, condition):
        if condition == "Nuageux":
            self.lCondition.setPixmap(QtGui.QPixmap("images/nuageux.png"))
        elif condition == "Ensoleillé":
            self.lCondition.setPixmap(QtGui.QPixmap("images/soleil.png"))
        elif condition == "Alternance de soleil et de nuages":
            self.lCondition.setPixmap(QtGui.QPixmap("images/nuageux_soleil.png"))
        elif condition == "Dégagé":
            self.lCondition.setPixmap(QtGui.QPixmap("images/lune.png"))
        elif condition == "Passages nuageux":
            self.lCondition.setPixmap(QtGui.QPixmap("images/nuageux_lune.pnglune.png"))
        elif condition == "Alternance de soleil et de nuages":
                self.lCondition.setPixmap(QtGui.QPixmap("images/nuageux_soleil.png"))
        elif condition == "Poudrerie basse":
                self.lCondition.setPixmap(QtGui.QPixmap("images/venteux.png"))
        elif condition == "Partiellement nuageux":
            self.lCondition.setPixmap(QtGui.QPixmap("images/nuageux_soleil.png"))
        elif condition == "Généralement nuageux":
            self.lCondition.setPixmap(QtGui.QPixmap("images/nuageux_soleil.png"))
        else:
            self.lCondition.setPixmap(QtGui.QPixmap("images/nulle.png"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_Dialog()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())