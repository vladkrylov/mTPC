# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from axes import PlotCanvas, MatplotlibToolbar

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.plotWidget = PlotCanvas(self.centralwidget)
        self.matplotlibToolbar = MatplotlibToolbar(self.plotWidget, self.centralwidget)
        
        self.matplotlibToolbar.setObjectName("matplotlibToolbar")
        self.verticalLayout.addWidget(self.matplotlibToolbar)
        
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.plotWidget.sizePolicy().hasHeightForWidth())
        self.plotWidget.setSizePolicy(sizePolicy)
        self.plotWidget.setObjectName("plotWidget")
        self.verticalLayout.addWidget(self.plotWidget)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setMinimumSize(QtCore.QSize(120, 50))
        self.widget.setMaximumSize(QtCore.QSize(160, 16777215))
        self.widget.setObjectName("widget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label = QtWidgets.QLabel(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setMinimumSize(QtCore.QSize(20, 0))
        self.label.setObjectName("label")
        self.verticalLayout_3.addWidget(self.label)
        self.scrollArea = QtWidgets.QScrollArea(self.widget)
        self.scrollArea.setMinimumSize(QtCore.QSize(0, 0))
        self.scrollArea.setMaximumSize(QtCore.QSize(8192, 16777215))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 144, 493))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.track1Widget = QtWidgets.QWidget(self.scrollAreaWidgetContents)
        self.track1Widget.setMinimumSize(QtCore.QSize(0, 0))
        self.track1Widget.setMaximumSize(QtCore.QSize(16777215, 30))
        self.track1Widget.setObjectName("track1Widget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.track1Widget)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.track1CheckBox = QtWidgets.QCheckBox(self.track1Widget)
        self.track1CheckBox.setObjectName("track1CheckBox")
        self.horizontalLayout_2.addWidget(self.track1CheckBox)
        self.track1colorLabel = QtWidgets.QLabel(self.track1Widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.track1colorLabel.sizePolicy().hasHeightForWidth())
        self.track1colorLabel.setSizePolicy(sizePolicy)
        self.track1colorLabel.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.track1colorLabel.setObjectName("track1colorLabel")
        self.horizontalLayout_2.addWidget(self.track1colorLabel)
        self.verticalLayout_6.addWidget(self.track1Widget)
        spacerItem = QtWidgets.QSpacerItem(20, 458, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_6.addItem(spacerItem)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout_3.addWidget(self.scrollArea)
        self.horizontalLayout.addWidget(self.widget)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 30))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.toolBar = QtWidgets.QToolBar(MainWindow)
        self.toolBar.setOrientation(QtCore.Qt.Vertical)
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.LeftToolBarArea, self.toolBar)
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)
        self.action_load_event = QtWidgets.QAction(MainWindow)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("view/img/appointment-new.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_load_event.setIcon(icon)
        self.action_load_event.setObjectName("action_load_event")
        self.action_select_new_track = QtWidgets.QAction(MainWindow)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("view/img/insert-link.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_select_new_track.setIcon(icon1)
        self.action_select_new_track.setObjectName("action_select_new_track")
        self.action_delete_track = QtWidgets.QAction(MainWindow)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("view/img/im-kick-user.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_delete_track.setIcon(icon2)
        self.action_delete_track.setObjectName("action_delete_track")
        self.action_add_hits_to_track = QtWidgets.QAction(MainWindow)
        self.action_add_hits_to_track.setEnabled(False)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("view/img/contact-new.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_add_hits_to_track.setIcon(icon3)
        self.action_add_hits_to_track.setObjectName("action_add_hits_to_track")
        self.action_remove_hits = QtWidgets.QAction(MainWindow)
        self.action_remove_hits.setEnabled(False)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("view/img/list-remove.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_remove_hits.setIcon(icon4)
        self.action_remove_hits.setObjectName("action_remove_hits")
        self.action_fit_track = QtWidgets.QAction(MainWindow)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("view/img/graph-2-icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_fit_track.setIcon(icon5)
        self.action_fit_track.setObjectName("action_fit_track")
        self.action_next_event = QtWidgets.QAction(MainWindow)
        self.action_next_event.setEnabled(False)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("view/img/next_event.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_next_event.setIcon(icon6)
        self.action_next_event.setObjectName("action_next_event")
        self.action_previous_event = QtWidgets.QAction(MainWindow)
        self.action_previous_event.setEnabled(False)
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap("view/img/previous_event.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_previous_event.setIcon(icon7)
        self.action_previous_event.setObjectName("action_previous_event")
        self.toolBar.addAction(self.action_load_event)
        self.toolBar.addAction(self.action_previous_event)
        self.toolBar.addAction(self.action_next_event)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.action_delete_track)
        self.toolBar.addAction(self.action_select_new_track)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.action_add_hits_to_track)
        self.toolBar.addAction(self.action_remove_hits)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.action_fit_track)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Tracks:"))
        self.track1CheckBox.setText(_translate("MainWindow", "Track 1"))
        self.track1colorLabel.setText(_translate("MainWindow", "o"))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar"))
        self.action_load_event.setText(_translate("MainWindow", "Load Event"))
        self.action_load_event.setToolTip(_translate("MainWindow", "Load Event"))
        self.action_select_new_track.setText(_translate("MainWindow", "Select new track"))
        self.action_select_new_track.setToolTip(_translate("MainWindow", "Select new track"))
        self.action_delete_track.setText(_translate("MainWindow", "Delete track"))
        self.action_delete_track.setToolTip(_translate("MainWindow", "Delete track"))
        self.action_add_hits_to_track.setText(_translate("MainWindow", "Add hits to track"))
        self.action_add_hits_to_track.setToolTip(_translate("MainWindow", "Add hits to track"))
        self.action_remove_hits.setText(_translate("MainWindow", "Remove hits"))
        self.action_remove_hits.setToolTip(_translate("MainWindow", "Remove hits"))
        self.action_fit_track.setText(_translate("MainWindow", "Fit track"))
        self.action_fit_track.setToolTip(_translate("MainWindow", "Fit track"))
        self.action_next_event.setText(_translate("MainWindow", "Next Event"))
        self.action_next_event.setToolTip(_translate("MainWindow", "Next Event"))
        self.action_previous_event.setText(_translate("MainWindow", "Previous Event"))
        self.action_previous_event.setToolTip(_translate("MainWindow", "Show previous event"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

