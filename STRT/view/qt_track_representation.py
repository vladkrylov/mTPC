from PyQt5 import QtCore, QtWidgets

# global constants
MPL_LEFT_BUTTON = 1
MPL_RIGHT_BUTTON = 3

class TrackRepresentation(QtWidgets.QWidget):
    def __init__(self, track, parent_widget, parent_group_box_layout, canvas):
        super(TrackRepresentation, self).__init__(parent_widget)
        self.track = track
        self.canvas = canvas
        self.line = None
        self.endpoints = None
        
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
        self.canvas.mpl_connect('pick_event', self.onpick)
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
        self.line.set_picker(10)  # possibly wrong, should be called when the line is created, not visibility changed
        self.line.set_visible(True)
        self.canvas.draw()
        self.make_line_sensible()
        return track_changed
    
    def hide_line(self):
        self.track.displayed = False
        if self.line:
            self.line.set_visible(False)
            self.hide_draggable_endpoints()
            self.canvas.draw()
    
    def checked(self, new_state):
        if new_state == QtCore.Qt.Checked:
            self.show_line()
        else:
            self.hide_line()
            
    def onpick(self, click_event):
        if click_event.artist != self.line:
            self.hide_draggable_endpoints()
            return
        self.show_draggable_endpoints()
        
        mouse_button = click_event.mouseevent.button
        if mouse_button == MPL_LEFT_BUTTON:
            pass
        elif mouse_button == MPL_RIGHT_BUTTON:
            pass
        
        return
    
    def show_draggable_endpoints(self):
        if self.endpoints is None:
            x, y = self.track.line
            self.canvas.axes.hold(True)
            self.endpoints = self.canvas.axes.plot(x, y, 'o')[0]
            self.canvas.axes.hold(False)
        self.endpoints.set_visible(True)
        self.canvas.draw()
        
    def hide_draggable_endpoints(self):
        if self.endpoints is not None:
            self.endpoints.set_visible(False)
            self.canvas.draw()
        
    def make_line_sensible(self):
        pass
    
    