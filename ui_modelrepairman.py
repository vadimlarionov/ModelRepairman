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
        ModelRepairman.resize(1201, 575)
        self.gridLayout_2 = QtWidgets.QGridLayout(ModelRepairman)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.label_12 = QtWidgets.QLabel(ModelRepairman)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        self.gridLayout.addWidget(self.label_12, 7, 4, 1, 1)
        self.number_variants_lineEdit = QtWidgets.QLineEdit(ModelRepairman)
        self.number_variants_lineEdit.setMinimumSize(QtCore.QSize(70, 0))
        self.number_variants_lineEdit.setMaximumSize(QtCore.QSize(70, 16777215))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.number_variants_lineEdit.setFont(font)
        self.number_variants_lineEdit.setObjectName("number_variants_lineEdit")
        self.gridLayout.addWidget(self.number_variants_lineEdit, 1, 3, 1, 1)
        self.label_14 = QtWidgets.QLabel(ModelRepairman)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_14.setFont(font)
        self.label_14.setObjectName("label_14")
        self.gridLayout.addWidget(self.label_14, 1, 1, 1, 2)
        self.label_4 = QtWidgets.QLabel(ModelRepairman)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 0, 1, 1, 5)
        self.label_7 = QtWidgets.QLabel(ModelRepairman)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 0, 7, 1, 2)
        self.label_8 = QtWidgets.QLabel(ModelRepairman)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setItalic(True)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.gridLayout.addWidget(self.label_8, 2, 1, 1, 1)
        self.label_9 = QtWidgets.QLabel(ModelRepairman)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.gridLayout.addWidget(self.label_9, 6, 1, 1, 1)
        self.N_label = QtWidgets.QLabel(ModelRepairman)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setItalic(True)
        self.N_label.setFont(font)
        self.N_label.setObjectName("N_label")
        self.gridLayout.addWidget(self.N_label, 3, 1, 1, 1)
        self.calculateButton = QtWidgets.QPushButton(ModelRepairman)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.calculateButton.sizePolicy().hasHeightForWidth())
        self.calculateButton.setSizePolicy(sizePolicy)
        self.calculateButton.setMinimumSize(QtCore.QSize(100, 35))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.calculateButton.setFont(font)
        self.calculateButton.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.calculateButton.setObjectName("calculateButton")
        self.gridLayout.addWidget(self.calculateButton, 9, 4, 1, 2)
        self.label_2 = QtWidgets.QLabel(ModelRepairman)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setItalic(True)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 4, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(ModelRepairman)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setItalic(True)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 5, 1, 1, 1)
        self.label_10 = QtWidgets.QLabel(ModelRepairman)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setItalic(True)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.gridLayout.addWidget(self.label_10, 7, 1, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(70, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 9, 6, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(22, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.MinimumExpanding)
        self.gridLayout.addItem(spacerItem1, 11, 6, 1, 1)
        self.tableWidget = QtWidgets.QTableWidget(ModelRepairman)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tableWidget.sizePolicy().hasHeightForWidth())
        self.tableWidget.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.tableWidget.setFont(font)
        self.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableWidget.setWordWrap(True)
        self.tableWidget.setCornerButtonEnabled(True)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.tableWidget.verticalHeader().setVisible(False)
        self.gridLayout.addWidget(self.tableWidget, 2, 7, 10, 1)
        self.label_6 = QtWidgets.QLabel(ModelRepairman)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 5, 4, 1, 1)
        self.label_13 = QtWidgets.QLabel(ModelRepairman)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_13.setFont(font)
        self.label_13.setObjectName("label_13")
        self.gridLayout.addWidget(self.label_13, 8, 1, 1, 1)
        self.label_11 = QtWidgets.QLabel(ModelRepairman)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.gridLayout.addWidget(self.label_11, 6, 4, 1, 1)
        self.label = QtWidgets.QLabel(ModelRepairman)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 2, 4, 1, 1)
        self.tno_lineEdit = QtWidgets.QLineEdit(ModelRepairman)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tno_lineEdit.sizePolicy().hasHeightForWidth())
        self.tno_lineEdit.setSizePolicy(sizePolicy)
        self.tno_lineEdit.setMinimumSize(QtCore.QSize(120, 0))
        self.tno_lineEdit.setMaximumSize(QtCore.QSize(220, 16777215))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.tno_lineEdit.setFont(font)
        self.tno_lineEdit.setObjectName("tno_lineEdit")
        self.gridLayout.addWidget(self.tno_lineEdit, 4, 2, 1, 2)
        self.label_5 = QtWidgets.QLabel(ModelRepairman)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 4, 4, 1, 1)
        self.to_lineEdit = QtWidgets.QLineEdit(ModelRepairman)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.to_lineEdit.sizePolicy().hasHeightForWidth())
        self.to_lineEdit.setSizePolicy(sizePolicy)
        self.to_lineEdit.setMinimumSize(QtCore.QSize(120, 0))
        self.to_lineEdit.setMaximumSize(QtCore.QSize(220, 16777215))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.to_lineEdit.setFont(font)
        self.to_lineEdit.setObjectName("to_lineEdit")
        self.gridLayout.addWidget(self.to_lineEdit, 5, 2, 1, 2)
        self.n_lineEdit = QtWidgets.QLineEdit(ModelRepairman)
        self.n_lineEdit.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.n_lineEdit.sizePolicy().hasHeightForWidth())
        self.n_lineEdit.setSizePolicy(sizePolicy)
        self.n_lineEdit.setMinimumSize(QtCore.QSize(120, 0))
        self.n_lineEdit.setMaximumSize(QtCore.QSize(220, 16777215))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.n_lineEdit.setFont(font)
        self.n_lineEdit.setObjectName("n_lineEdit")
        self.gridLayout.addWidget(self.n_lineEdit, 3, 2, 1, 2)
        self.zi_lineEdit = QtWidgets.QLineEdit(ModelRepairman)
        self.zi_lineEdit.setMinimumSize(QtCore.QSize(120, 0))
        self.zi_lineEdit.setMaximumSize(QtCore.QSize(220, 16777215))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.zi_lineEdit.setFont(font)
        self.zi_lineEdit.setObjectName("zi_lineEdit")
        self.gridLayout.addWidget(self.zi_lineEdit, 6, 2, 1, 2)
        self.c_lineEdit = QtWidgets.QLineEdit(ModelRepairman)
        self.c_lineEdit.setMinimumSize(QtCore.QSize(120, 0))
        self.c_lineEdit.setMaximumSize(QtCore.QSize(220, 16777215))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.c_lineEdit.setFont(font)
        self.c_lineEdit.setObjectName("c_lineEdit")
        self.gridLayout.addWidget(self.c_lineEdit, 2, 2, 1, 2)
        self.z_lineEdit = QtWidgets.QLineEdit(ModelRepairman)
        self.z_lineEdit.setMinimumSize(QtCore.QSize(120, 0))
        self.z_lineEdit.setMaximumSize(QtCore.QSize(220, 16777215))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.z_lineEdit.setFont(font)
        self.z_lineEdit.setObjectName("z_lineEdit")
        self.gridLayout.addWidget(self.z_lineEdit, 7, 2, 1, 2)
        self.precision_lineEdit = QtWidgets.QLineEdit(ModelRepairman)
        self.precision_lineEdit.setMinimumSize(QtCore.QSize(120, 0))
        self.precision_lineEdit.setMaximumSize(QtCore.QSize(220, 16777215))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.precision_lineEdit.setFont(font)
        self.precision_lineEdit.setObjectName("precision_lineEdit")
        self.gridLayout.addWidget(self.precision_lineEdit, 8, 2, 1, 2)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 1, 1, 1)

        self.retranslateUi(ModelRepairman)
        QtCore.QMetaObject.connectSlotsByName(ModelRepairman)
        ModelRepairman.setTabOrder(self.number_variants_lineEdit, self.c_lineEdit)
        ModelRepairman.setTabOrder(self.c_lineEdit, self.n_lineEdit)
        ModelRepairman.setTabOrder(self.n_lineEdit, self.tno_lineEdit)
        ModelRepairman.setTabOrder(self.tno_lineEdit, self.to_lineEdit)
        ModelRepairman.setTabOrder(self.to_lineEdit, self.zi_lineEdit)
        ModelRepairman.setTabOrder(self.zi_lineEdit, self.z_lineEdit)
        ModelRepairman.setTabOrder(self.z_lineEdit, self.precision_lineEdit)
        ModelRepairman.setTabOrder(self.precision_lineEdit, self.calculateButton)
        ModelRepairman.setTabOrder(self.calculateButton, self.tableWidget)

    def retranslateUi(self, ModelRepairman):
        _translate = QtCore.QCoreApplication.translate
        ModelRepairman.setWindowTitle(_translate("ModelRepairman", "Dialog"))
        self.label_12.setText(_translate("ModelRepairman", "руб. / ч"))
        self.number_variants_lineEdit.setText(_translate("ModelRepairman", "3"))
        self.label_14.setText(_translate("ModelRepairman", "Кол-во параметров"))
        self.label_4.setText(_translate("ModelRepairman", "Исходные данные"))
        self.label_7.setText(_translate("ModelRepairman", "Результаты"))
        self.label_8.setText(_translate("ModelRepairman", "Ci"))
        self.label_9.setToolTip(_translate("ModelRepairman", "<html><head/><body><p>Заработная плата специалиста за 1 час</p></body></html>"))
        self.label_9.setText(_translate("ModelRepairman", "Zi"))
        self.N_label.setToolTip(_translate("ModelRepairman", "<html><head/><body><p>Количество компьютеров</p></body></html>"))
        self.N_label.setText(_translate("ModelRepairman", "Ni"))
        self.calculateButton.setText(_translate("ModelRepairman", "Рассчитать"))
        self.label_2.setToolTip(_translate("ModelRepairman", "<html><head/><body><p>Среднее время наработки на отказ одного компьютера</p></body></html>"))
        self.label_2.setText(_translate("ModelRepairman", "tноi"))
        self.label_3.setToolTip(_translate("ModelRepairman", "<html><head/><body><p>Среднее время ремонта одного компьютера</p></body></html>"))
        self.label_3.setText(_translate("ModelRepairman", "tоi"))
        self.label_10.setToolTip(_translate("ModelRepairman", "<html><head/><body><p>Финансовые потери организации от неисправного компьютера за 1 час</p></body></html>"))
        self.label_10.setText(_translate("ModelRepairman", "Z"))
        self.label_6.setText(_translate("ModelRepairman", "ч"))
        self.label_13.setToolTip(_translate("ModelRepairman", "<html><head/><body><p>Количество знаков после запятой. По умолчанию - 5. Максимальное количество - 24</p></body></html>"))
        self.label_13.setText(_translate("ModelRepairman", "Точность"))
        self.label_11.setText(_translate("ModelRepairman", "руб. / ч"))
        self.label.setText(_translate("ModelRepairman", "шт."))
        self.tno_lineEdit.setText(_translate("ModelRepairman", "800, 800, 800"))
        self.label_5.setText(_translate("ModelRepairman", "ч"))
        self.to_lineEdit.setText(_translate("ModelRepairman", "8, 8, 8"))
        self.n_lineEdit.setToolTip(_translate("ModelRepairman", "<html><head/><body><p><br/></p></body></html>"))
        self.n_lineEdit.setWhatsThis(_translate("ModelRepairman", "<html><head/><body><p><br/></p></body></html>"))
        self.n_lineEdit.setText(_translate("ModelRepairman", "100, 100, 100"))
        self.zi_lineEdit.setText(_translate("ModelRepairman", "200, 200, 200"))
        self.c_lineEdit.setText(_translate("ModelRepairman", "1, 2, 3"))
        self.z_lineEdit.setText(_translate("ModelRepairman", "350, 350, 350"))
        self.precision_lineEdit.setText(_translate("ModelRepairman", "5"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ModelRepairman = QtWidgets.QDialog()
    ui = Ui_ModelRepairman()
    ui.setupUi(ModelRepairman)
    ModelRepairman.show()
    sys.exit(app.exec_())

