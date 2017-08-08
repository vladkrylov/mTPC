from PyQt5 import QtCore, QtWidgets

class TrackRepresentation(QtWidgets.QWidget):
    def __init__(self, track, parent_widget, parent_group_box_layout):
        super(TrackRepresentation, self).__init__(parent_widget)
        
        self.setMinimumSize(QtCore.QSize(0, 0))
        self.setMaximumSize(QtCore.QSize(16777215, 30))
        self.setObjectName("track%dWidget" % track.id)
        self.layout = QtWidgets.QHBoxLayout(self)
        self.layout.setObjectName("track%dLayout" % track.id)
        
        self.check_box = QtWidgets.QCheckBox(self)
        self.check_box.setObjectName("track%dCheckBox" % track.id)
        self.check_box.setText("Track %d" % track.id)
        self.check_box.setChecked(True)
        self.layout.addWidget(self.check_box)
        
        self.colorLabel = QtWidgets.QLabel(self)
        self.colorLabel.setStyleSheet("QLabel {color : %s;}" % track.color)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.colorLabel.sizePolicy().hasHeightForWidth())
        self.colorLabel.setSizePolicy(sizePolicy)
        self.colorLabel.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.colorLabel.setObjectName("track%dColorLabel" % track.id)
        self.colorLabel.setText("o")
        self.layout.addWidget(self.colorLabel)
        
        parent_group_box_layout.insertWidget(parent_group_box_layout.count() - 1, self)
        