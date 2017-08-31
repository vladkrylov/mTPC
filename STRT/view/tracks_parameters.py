# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'tracks_parameters.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from axes import TrackParametersCanvas, HoughTransformCanvas, MatplotlibToolbar

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
        self.parameterNames = QtWidgets.QGroupBox(self.parametersWidgetPage)
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
        self.gridLayout_2.addWidget(self.parameterNames, 0, 1, 1, 1)
        self.tabWidget.addTab(self.parametersWidgetPage, "")
        self.HoughWidgetPage = QtWidgets.QWidget()
        self.HoughWidgetPage.setObjectName("HoughWidgetPage")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.HoughWidgetPage)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.HTCanvas = HoughTransformCanvas(self.HoughWidgetPage)
        self.HTMatplotlibToolbar = MatplotlibToolbar(self.HTCanvas, self.HoughWidgetPage)
        
        self.HTMatplotlibToolbar.setObjectName("HTMatplotlibToolbar")
        self.verticalLayout_4.addWidget(self.HTMatplotlibToolbar)
        
        self.HTCanvas.setObjectName("HTCanvas")
        self.verticalLayout_4.addWidget(self.HTCanvas)
        self.gridLayout_3.addLayout(self.verticalLayout_4, 0, 0, 1, 1)
        self.HTActionsGroup = QtWidgets.QGroupBox(self.HoughWidgetPage)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.HTActionsGroup.sizePolicy().hasHeightForWidth())
        self.HTActionsGroup.setSizePolicy(sizePolicy)
        self.HTActionsGroup.setMinimumSize(QtCore.QSize(100, 0))
        self.HTActionsGroup.setMaximumSize(QtCore.QSize(200, 16777215))
        self.HTActionsGroup.setObjectName("HTActionsGroup")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.HTActionsGroup)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.transfomEventButton = QtWidgets.QPushButton(self.HTActionsGroup)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.transfomEventButton.sizePolicy().hasHeightForWidth())
        self.transfomEventButton.setSizePolicy(sizePolicy)
        self.transfomEventButton.setObjectName("transfomEventButton")
        self.verticalLayout_3.addWidget(self.transfomEventButton)
        spacerItem = QtWidgets.QSpacerItem(20, 473, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem)
        self.gridLayout_3.addWidget(self.HTActionsGroup, 0, 1, 1, 1)
        self.tabWidget.addTab(self.HoughWidgetPage, "")
        self.horizontalLayout.addWidget(self.tabWidget)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        DockWidget.setWidget(self.dockWidgetContents)

        self.retranslateUi(DockWidget)
        self.tabWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(DockWidget)

    def retranslateUi(self, DockWidget):
        _translate = QtCore.QCoreApplication.translate
        DockWidget.setWindowTitle(_translate("DockWidget", "A&nalysis"))
        self.parameterNames.setTitle(_translate("DockWidget", "Track parameters"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.parametersWidgetPage), _translate("DockWidget", "Track parameters"))
        self.HTActionsGroup.setTitle(_translate("DockWidget", "Actions"))
        self.transfomEventButton.setText(_translate("DockWidget", "Transform Event"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.HoughWidgetPage), _translate("DockWidget", "Hough transform"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    DockWidget = QtWidgets.QDockWidget()
    ui = Ui_DockWidget()
    ui.setupUi(DockWidget)
    DockWidget.show()
    sys.exit(app.exec_())

