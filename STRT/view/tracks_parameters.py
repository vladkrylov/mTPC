# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'tracks_parameters.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from axes import TrackParametersCanvas, MatplotlibToolbar

class Ui_DockWidget(object):
    def setupUi(self, DockWidget):
        DockWidget.setObjectName("DockWidget")
        DockWidget.resize(616, 651)
        DockWidget.setFloating(False)
        DockWidget.setAllowedAreas(QtCore.Qt.AllDockWidgetAreas)
        self.dockWidgetContents = QtWidgets.QWidget()
        self.dockWidgetContents.setObjectName("dockWidgetContents")
        self.gridLayout = QtWidgets.QGridLayout(self.dockWidgetContents)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.tabWidget = QtWidgets.QTabWidget(self.dockWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy)
        self.tabWidget.setTabPosition(QtWidgets.QTabWidget.North)
        self.tabWidget.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.tabWidget.setElideMode(QtCore.Qt.ElideNone)
        self.tabWidget.setDocumentMode(False)
        self.tabWidget.setTabsClosable(False)
        self.tabWidget.setMovable(False)
        self.tabWidget.setObjectName("tabWidget")
        self.parametersWidgetPage = QtWidgets.QWidget()
        self.parametersWidgetPage.setObjectName("parametersWidgetPage")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.parametersWidgetPage)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.parametersPlotWidget = TrackParametersCanvas(self.parametersWidgetPage)
        self.parametersMatplotlibToolbar = MatplotlibToolbar(self.parametersPlotWidget, self.parametersWidgetPage)
        
        self.parametersMatplotlibToolbar.setObjectName("parametersMatplotlibToolbar")
        self.verticalLayout_2.addWidget(self.parametersMatplotlibToolbar)
        
        self.parametersPlotWidget.setObjectName("parametersPlotWidget")
        self.verticalLayout_2.addWidget(self.parametersPlotWidget)
        self.gridLayout_2.addLayout(self.verticalLayout_2, 0, 0, 1, 1)
        self.tabWidget.addTab(self.parametersWidgetPage, "")
        self.HoughWidgetPage = QtWidgets.QWidget()
        self.HoughWidgetPage.setObjectName("HoughWidgetPage")
        self.tabWidget.addTab(self.HoughWidgetPage, "")
        self.horizontalLayout.addWidget(self.tabWidget)
        self.parameterNames = QtWidgets.QGroupBox(self.dockWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.parameterNames.sizePolicy().hasHeightForWidth())
        self.parameterNames.setSizePolicy(sizePolicy)
        self.parameterNames.setMinimumSize(QtCore.QSize(100, 0))
        self.parameterNames.setMaximumSize(QtCore.QSize(200, 16777215))
        self.parameterNames.setObjectName("parameterNames")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.parameterNames)
        self.verticalLayout.setObjectName("verticalLayout")
        self.paramRadioButton1 = QtWidgets.QRadioButton(self.parameterNames)
        self.paramRadioButton1.setChecked(True)
        self.paramRadioButton1.setObjectName("paramRadioButton1")
        self.verticalLayout.addWidget(self.paramRadioButton1)
        self.paramRadioButton2 = QtWidgets.QRadioButton(self.parameterNames)
        self.paramRadioButton2.setObjectName("paramRadioButton2")
        self.verticalLayout.addWidget(self.paramRadioButton2)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.computeParametersButton = QtWidgets.QPushButton(self.parameterNames)
        self.computeParametersButton.setObjectName("computeParametersButton")
        self.verticalLayout.addWidget(self.computeParametersButton)
        self.horizontalLayout.addWidget(self.parameterNames)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        DockWidget.setWidget(self.dockWidgetContents)

        self.retranslateUi(DockWidget)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(DockWidget)

    def retranslateUi(self, DockWidget):
        _translate = QtCore.QCoreApplication.translate
        DockWidget.setWindowTitle(_translate("DockWidget", "A&nalysis"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.parametersWidgetPage), _translate("DockWidget", "Track parameters"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.HoughWidgetPage), _translate("DockWidget", "Hough transform"))
        self.parameterNames.setTitle(_translate("DockWidget", "Track parameters"))
        self.paramRadioButton1.setText(_translate("DockWidget", "Para&meter name"))
        self.paramRadioButton2.setText(_translate("DockWidget", "Another parameter"))
        self.computeParametersButton.setText(_translate("DockWidget", "Recalculate"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    DockWidget = QtWidgets.QDockWidget()
    ui = Ui_DockWidget()
    ui.setupUi(DockWidget)
    DockWidget.show()
    sys.exit(app.exec_())

