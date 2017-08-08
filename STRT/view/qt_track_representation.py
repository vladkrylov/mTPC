from PyQt5 import QtCore, QtWidgets

class TrackRepresentation(QtWidgets.QHBoxLayout):
    def __init__(self, track, parent_widget, parent_group_box_layout):
        super(TrackRepresentation, self).__init__()
        self.setObjectName("track%d" % track.id)
        
        self.check_box = QtWidgets.QCheckBox(parent_widget)
        self.check_box.setObjectName("track%dCheckBox" % track.id)
        self.check_box.setText("Track %d" % track.id)
        self.addWidget(self.check_box)
        
        self.labelSymbol = 'o'
        self.colorLabel = QtWidgets.QLabel(parent_widget)
        self.colorLabel.setText(self.labelSymbol)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.colorLabel.sizePolicy().hasHeightForWidth())
        self.colorLabel.setSizePolicy(sizePolicy)
        self.colorLabel.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.colorLabel.setObjectName("track%dColorLabel" % track.id)
        self.addWidget(self.colorLabel)
        
        parent_group_box_layout.addLayout(self)
        
        
        