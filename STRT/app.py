import unittest

from PyQt5 import QtWidgets
from view import Ui_MainWindow

from ptests import TestControllerModelInterface

if __name__ == "__main__":
#     import sys
#     app = QtWidgets.QApplication(sys.argv)
#     MainWindow = QtWidgets.QMainWindow()
#     ui = Ui_MainWindow()
#     ui.setupUi(MainWindow)
#     MainWindow.show()
#     sys.exit(app.exec_())

    # Tests
    suite = unittest.TestLoader().loadTestsFromTestCase(TestControllerModelInterface)
    unittest.TextTestRunner(verbosity=2).run(suite)


