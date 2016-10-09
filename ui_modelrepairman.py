# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'modelrepairman.ui'
#
# Created by: PyQt5 UI code generator 5.7
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_ModelRepairman(object):
    def setupUi(self, ModelRepairman):
        ModelRepairman.setObjectName("ModelRepairman")
        ModelRepairman.resize(400, 300)
        self.pushButton = QtWidgets.QPushButton(ModelRepairman)
        self.pushButton.setGeometry(QtCore.QRect(140, 130, 75, 23))
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(ModelRepairman)
        QtCore.QMetaObject.connectSlotsByName(ModelRepairman)

    def retranslateUi(self, ModelRepairman):
        _translate = QtCore.QCoreApplication.translate
        ModelRepairman.setWindowTitle(_translate("ModelRepairman", "Dialog"))
        self.pushButton.setText(_translate("ModelRepairman", "PushButton"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ModelRepairman = QtWidgets.QDialog()
    ui = Ui_ModelRepairman()
    ui.setupUi(ModelRepairman)
    ModelRepairman.show()
    sys.exit(app.exec_())

