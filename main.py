# -*- coding: utf-8 -*-

import sys
from PyQt5 import QtCore
from PyQt5.QtWidgets import QApplication, QDialog, QTableWidgetItem, QMessageBox
from ui_modelrepairman import Ui_ModelRepairman
from model_repairman import ModelRepairman
from utils import Utils


class ModelRepairmanView(QDialog, Ui_ModelRepairman):

    def __init__(self):
        super(ModelRepairmanView, self).__init__()
        self.setupUi(self)
        self.calculateButton.clicked.connect(self.calculate)
        self.calculate()

    def create_table_headers(self, number_variants):
        self.tableWidget.setColumnCount(number_variants + 1)
        self.tableWidget.setHorizontalHeaderItem(0, QTableWidgetItem('Параметр'))
        for x in range(1, number_variants + 1):
            self.tableWidget.setHorizontalHeaderItem(x, QTableWidgetItem('Вариант ' + str(x)))

    def add_row_to_table(self, parameter, *args):
        row = self.tableWidget.rowCount()
        self.tableWidget.insertRow(row)
        self.tableWidget.setItem(row, 0, QTableWidgetItem(Utils.to_str(parameter)))
        column = 1
        for x in args:
            self.tableWidget.setItem(row, column, QTableWidgetItem(Utils.to_str(x)))
            column += 1

    def calculate(self):
        try:
            number_variants = int(self.number_variants_spinBox.text())

            c = Utils.to_int_list(self.c_lineEdit.text())
            n = Utils.to_int_list(self.n_lineEdit.text())
            tno = Utils.to_int_list(self.tno_lineEdit.text())
            to = Utils.to_int_list(self.to_lineEdit.text())
            zi = Utils.to_int_list(self.zi_lineEdit.text())
            z = Utils.to_int_list(self.z_lineEdit.text())

            if not Utils.args_is_equals_len(c, n, tno, to, zi, z, size=number_variants):
                print('Parameters size is not equals')
                self.create_error_msg().show()
                return
        except ValueError as e:
            print(e)
            self.create_error_msg().show()
            return

        Utils.set_precision(self.precision_lineEdit.text())

        models = []
        for i in range(number_variants):
            models.append(ModelRepairman(n[i], tno[i], to[i], c[i], zi[i], z[i]))

        self.create_table_headers(number_variants)
        self.tableWidget.clearContents()
        self.tableWidget.setRowCount(0)

        self.add_row_to_table('Количество ремонтников', *['c = ' + str(x) for x in c])
        self.add_row_to_table('P0', *[model.probability_initial_state() for model in models])
        self.add_row_to_table('Q', *[model.queue_length() for model in models])
        self.add_row_to_table('L', *[model.broken_length() for model in models])
        self.add_row_to_table('U = L - Q', *[model.computers_repair() for model in models])
        self.add_row_to_table('ρo = U / C', *[model.load_factor_specialist() for model in models])
        self.add_row_to_table('n = N - L', *[model.average_broken_computers() for model in models])
        self.add_row_to_table('ρe = n / N', *[model.load_factor_computer() for model in models])
        self.add_row_to_table('W', *[model.broken_computer_in_queue_time() for model in models])
        self.add_row_to_table('Tр', *[model.broken_computer_time() for model in models])
        self.add_row_to_table('Tц = Tр + tно', *[model.computer_cycle_time() for model in models])
        self.add_row_to_table('ρe / ρo', *[model.ratio() for model in models])
        self.add_row_to_table('Yi', *[model.calculate_y() for model in models])

        self.tableWidget.resizeColumnsToContents()

    def create_error_msg(self):
        msg = QMessageBox(self)
        msg.setText('<font size=6>Проверьте входные данные</font>')
        msg.setInformativeText('<font size=5>Необходимо для каждого поля ввода ввести '
                               'целочисленные значения через запятую. '
                               'Количество значений должно совпадать со значением в '
                               'поле "Кол-во вариантов"</font>')
        msg.setWindowTitle('Внимание')
        return msg

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = ModelRepairmanView()
    window.setWindowFlags(window.windowFlags() | QtCore.Qt.WindowMinimizeButtonHint |
                          QtCore.Qt.WindowMaximizeButtonHint)
    window.show()
    sys.exit(app.exec_())
