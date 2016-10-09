import sys
from PyQt5.QtWidgets import QApplication, QDialog
from ui_modelrepairman import Ui_ModelRepairman


class ModelRepairman(QDialog, Ui_ModelRepairman):

    def __init__(self):
        super(ModelRepairman, self).__init__()
        self.setupUi(self)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = ModelRepairman()
    window.show()
    sys.exit(app.exec_())
