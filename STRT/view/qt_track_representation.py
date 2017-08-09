from PyQt5 import QtCore, QtWidgets

class TrackRepresentation(QtWidgets.QWidget):
    def __init__(self, track, parent_widget, parent_group_box_layout, canvas):
        super(TrackRepresentation, self).__init__(parent_widget)
        self.track = track
        self.canvas = canvas
        self.line = None
        
        self.setMinimumSize(QtCore.QSize(0, 0))
        self.setMaximumSize(QtCore.QSize(16777215, 30))
        self.setObjectName("track%dWidget" % self.track.id)
        self.layout = QtWidgets.QHBoxLayout(self)
        self.layout.setObjectName("track%dLayout" % self.track.id)
        
        self.check_box = QtWidgets.QCheckBox(self)
        self.check_box.setObjectName("track%dCheckBox" % self.track.id)
        self.check_box.setText("Track %d" % self.track.id)
        self.check_box.setChecked(True)
        self.layout.addWidget(self.check_box)
        
        self.colorLabel = QtWidgets.QLabel(self)
        self.colorLabel.setStyleSheet("QLabel {color : %s;}" % self.track.color)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.colorLabel.sizePolicy().hasHeightForWidth())
        self.colorLabel.setSizePolicy(sizePolicy)
        self.colorLabel.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.colorLabel.setObjectName("track%dColorLabel" % self.track.id)
        self.colorLabel.setText("o")
        self.layout.addWidget(self.colorLabel)
        
        parent_group_box_layout.insertWidget(parent_group_box_layout.count() - 1, self)
        
        self.connect_signals_slots()
        
    def connect_signals_slots(self):
        self.check_box.stateChanged.connect(self.checked)
    
    def show_line(self):
        self.track.displayed = True
        track_changed = False
        if not self.track.has_line():
            self.track.set_random_line(self.canvas.axes.get_xlim(), self.canvas.axes.get_ylim())
            track_changed = True
            self.line = self.canvas.add_line(self.track)
        elif self.line is None:
            self.line = self.canvas.add_line(self.track)
        self.line.set_visible(True)
        self.canvas.draw()
        self.make_line_sensible()
        return track_changed
    
    def hide_line(self):
        self.track.displayed = False
        if self.line:
            self.line.set_visible(False)
            self.canvas.draw()
    
    def checked(self, new_state):
        if new_state == QtCore.Qt.Checked:
            self.show_line()
        else:
            self.hide_line()
            
    def make_line_sensible(self):
        pass
    
    