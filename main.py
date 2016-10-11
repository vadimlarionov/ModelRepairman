# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import QApplication, QDialog, QTableWidgetItem, QMessageBox
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
        self.tableWidget.setItem(position, 0, QTableWidgetItem(Utils.to_str(parameter)))
        self.tableWidget.setItem(position, 1, QTableWidgetItem(Utils.to_str(variant_1)))
        self.tableWidget.setItem(position, 2, QTableWidgetItem(Utils.to_str(variant_2)))
        self.tableWidget.setItem(position, 3, QTableWidgetItem(Utils.to_str(variant_3)))

    def calculate(self):
        n = int(self.n_lineEdit.text())
        to = int(self.to_lineEdit.text())
        tno = int(self.tno_lineEdit.text())

        c1 = 2
        c2 = 3
        c3 = 4

        si = 200
        s = 350

        model = ModelRepairman(n, tno, to)

        self.tableWidget.clearContents()
        self.tableWidget.setRowCount(0)

        self.add_row_to_table('Количество ремонтников', 'c = ' + str(c1), 'c = ' + str(c2), 'c = ' + str(c3))
        self.add_row_to_table('P0', model.probability_initial_state(c1),
                              model.probability_initial_state(c2),
                              model.probability_initial_state(c3))
        self.add_row_to_table('Q', model.queue_length(c1),
                              model.queue_length(c2),
                              model.queue_length(c3))
        self.add_row_to_table('L', model.broken_length(c1),
                              model.broken_length(c2),
                              model.broken_length(c3))
        self.add_row_to_table('U = L - Q', model.computers_repair(c1),
                              model.computers_repair(c2),
                              model.computers_repair(c3))
        self.add_row_to_table('ρo = U / C', model.load_factor_specialist(c1),
                              model.load_factor_specialist(c2),
                              model.load_factor_specialist(c3))
        self.add_row_to_table('n = N - L', model.average_broken_computers(c1),
                              model.average_broken_computers(c2),
                              model.average_broken_computers(c3))
        self.add_row_to_table('ρe = n / N', model.load_factor_computer(c1),
                              model.load_factor_computer(c2),
                              model.load_factor_computer(c3))
        self.add_row_to_table('W', model.broken_computer_in_queue_time(c1),
                              model.broken_computer_in_queue_time(c2),
                              model.broken_computer_in_queue_time(c3))
        self.add_row_to_table('Tp', model.broken_computer_time(c1),
                              model.broken_computer_time(c2),
                              model.broken_computer_time(c3))
        self.add_row_to_table('ρe / ρo', model.ratio(c1),
                              model.ratio(c2),
                              model.ratio(c3))
        self.add_row_to_table('Yi', '%.2f' % model.calculate_y(c1, si, s),
                              '%.2f' % model.calculate_y(c2, si, s),
                              '%.2f' % model.calculate_y(c3, si, s))
        self.tableWidget.resizeColumnsToContents()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = ModelRepairmanView()
    window.show()
    sys.exit(app.exec_())
