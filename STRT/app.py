import unittest

from PyQt5 import QtWidgets
from view import Ui_MainWindow

from ptests import *

if __name__ == "__main__":
#     import sys
#     app = QtWidgets.QApplication(sys.argv)
#     MainWindow = QtWidgets.QMainWindow()
#     ui = Ui_MainWindow()
#     ui.setupUi(MainWindow)
#     MainWindow.show()
#     sys.exit(app.exec_())

    # Tests
    suites = []
#     suite = unittest.TestLoader().loadTestsFromTestCase(TestControllerModelInterface)
    suites.append(unittest.TestLoader().loadTestsFromTestCase(TestModelAPI))
    for suite in suites:
        unittest.TextTestRunner(verbosity=2).run(suite)


