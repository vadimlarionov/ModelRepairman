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
        try:
            c = Utils.to_int_list(self.c_lineEdit.text())
            n = Utils.to_int_list(self.n_lineEdit.text())
            tno = Utils.to_int_list(self.tno_lineEdit.text())
            to = Utils.to_int_list(self.to_lineEdit.text())
            zi = Utils.to_int_list(self.zi_lineEdit.text())
            z = Utils.to_int_list(self.z_lineEdit.text())

            if len(c) != 3 or len(n) != 3 or len(tno) != 3 or len(to) != 3:
                print('Fail')
                self.create_error_msg().show()
                return
        except ValueError as e:
            print(e)
            self.create_error_msg().show()
            return

        model_1 = ModelRepairman(n[0], tno[0], to[0], c[0])
        model_2 = ModelRepairman(n[1], tno[1], to[1], c[1])
        model_3 = ModelRepairman(n[2], tno[2], to[2], c[2])

        self.tableWidget.clearContents()
        self.tableWidget.setRowCount(0)

        self.add_row_to_table('Количество ремонтников', 'c = ' + str(c[0]), 'c = ' + str(c[1]),
                              'c = ' + str(c[2]))
        self.add_row_to_table('P0', model_1.probability_initial_state(),
                              model_2.probability_initial_state(),
                              model_3.probability_initial_state())
        self.add_row_to_table('Q', model_1.queue_length(),
                              model_2.queue_length(),
                              model_3.queue_length())
        self.add_row_to_table('L', model_1.broken_length(),
                              model_2.broken_length(),
                              model_3.broken_length())
        self.add_row_to_table('U = L - Q', model_1.computers_repair(),
                              model_2.computers_repair(),
                              model_3.computers_repair())
        self.add_row_to_table('ρo = U / C', model_1.load_factor_specialist(),
                              model_2.load_factor_specialist(),
                              model_3.load_factor_specialist())
        self.add_row_to_table('n = N - L', model_1.average_broken_computers(),
                              model_2.average_broken_computers(),
                              model_3.average_broken_computers())
        self.add_row_to_table('ρe = n / N', model_1.load_factor_computer(),
                              model_2.load_factor_computer(),
                              model_3.load_factor_computer())
        self.add_row_to_table('W', model_1.broken_computer_in_queue_time(),
                              model_2.broken_computer_in_queue_time(),
                              model_3.broken_computer_in_queue_time())
        self.add_row_to_table('Tp', model_1.broken_computer_time(),
                              model_2.broken_computer_time(),
                              model_3.broken_computer_time())

        self.add_row_to_table('Tц', model_1.computer_cycle_time(),
                              model_2.computer_cycle_time(),
                              model_3.computer_cycle_time())

        self.add_row_to_table('ρe / ρo', model_1.ratio(),
                              model_2.ratio(),
                              model_3.ratio())
        self.add_row_to_table('Yi', '%.2f' % model_1.calculate_y(zi[0], z[0]),
                              '%.2f' % model_2.calculate_y(zi[1], z[1]),
                              '%.2f' % model_3.calculate_y(zi[2], z[2]))
        self.tableWidget.resizeColumnsToContents()

    def parse_ci(self):
        c = self.c_lineEdit.text()
        return [int(x) for x in c.split(',')]

    def parse_n(self):
        n = self.n_lineEdit.text()
        return [int(x) for x in n.split(',')]

    def parse_tno(self):
        tno = self.tno_lineEdit.text()
        return [int(x) for x in tno.split(',')]

    def parse_to(self):
        to = self.to_lineEdit.text()
        return [int(x) for x in to.split(',')]

    def create_error_msg(self):
        msg = QMessageBox(self)
        msg.setText("Проверьте входные данные")
        msg.setInformativeText("Необходимо для каждого поля ввода ввести 3 "
                               "числовых значения через запятую")
        msg.setWindowTitle("Внимание")
        return msg

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = ModelRepairmanView()
    window.show()
    sys.exit(app.exec_())
