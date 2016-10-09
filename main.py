# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import QApplication, QDialog, QTableWidgetItem
from ui_modelrepairman import Ui_ModelRepairman
from model_repairman import ModelRepairman
from utils import Utils


class ModelRepairmanView(QDialog, Ui_ModelRepairman):

    def __init__(self):
        super(ModelRepairmanView, self).__init__()
        self.setupUi(self)
        self.calculateButton.clicked.connect(self.calculate)
        self.calculateButton.click()

    def add_row_to_table(self, parameter, variant_1, variant_2, variant_3):
        position = self.tableWidget.rowCount()
        self.tableWidget.insertRow(position)
        self.tableWidget.setItem(position, 0, QTableWidgetItem(parameter))
        self.tableWidget.setItem(position, 1, QTableWidgetItem(variant_1))
        self.tableWidget.setItem(position, 2, QTableWidgetItem(str(variant_2)))
        self.tableWidget.setItem(position, 3, QTableWidgetItem(str(variant_3)))

    def calculate(self):
        n = int(self.n_lineEdit.text())
        to = int(self.to_lineEdit.text())
        tno = int(self.tno_lineEdit.text())

        c1 = 1
        c2 = 2
        c3 = 3

        model_repairman = ModelRepairman(n, tno, to)
        self.add_row_to_table('Количество ремонтников', 'c = ' + str(c1), 'c = ' + str(c2), 'c = ' + str(c3))
        self.add_row_to_table('P0', Utils.to_str(model_repairman.probability_initial_state(1)),
                              Utils.to_str(model_repairman.probability_initial_state(2)),
                              Utils.to_str(model_repairman.probability_initial_state(3)))
        self.add_row_to_table('Q', Utils.to_str(model_repairman.queue_length(1)),
                              Utils.to_str(model_repairman.queue_length(2)),
                              Utils.to_str(model_repairman.queue_length(3)))
        self.add_row_to_table('L', Utils.to_str(model_repairman.broken_length(1)),
                              Utils.to_str(model_repairman.broken_length(2)),
                              Utils.to_str(model_repairman.broken_length(3)))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = ModelRepairmanView()
    window.show()
    sys.exit(app.exec_())
