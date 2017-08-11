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
        self.cid_point_pick = None
        self.cid_point_move = None
        self.cid_point_release = None
        
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
        self.line.set_picker(5)  # possibly wrong, should be called when the line is created, not visibility changed
        self.line.set_visible(True)
        self.canvas.draw()
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
        print("=== From track %d: %s was picked ===" % (self.track.id, click_event.artist))
        print "event.artist = %s" % str(click_event.artist)
        print "self.line = %s" % str(self.line)
        print "self.endpoints = "
        if self.endpoints is not None:
            for p in self.endpoints:
                print("    %s") % str(p)
        print("=================\n")
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
            self.endpoints = [self.canvas.axes.plot(x[i], y[i], 'o', picker=5)[0] for i in range(len(x))]
            self.canvas.axes.hold(False)
            self.cid_point_pick = self.canvas.mpl_connect('pick_event', self.on_point_pick)
        for p in self.endpoints:
            p.set_visible(True)
        self.canvas.draw()
        
    def hide_draggable_endpoints(self):
        if self.endpoints is not None:
            for p in self.endpoints:
                p.set_visible(False)
            self.canvas.draw()
        
    def on_point_pick(self, mouse_event):
        if mouse_event.artist not in self.endpoints:
            return
        self.im_moving = mouse_event.artist
        # multiple calls here, don't know why
        # set None flags to avoid many connection on point pick
        # TODO fix this!
        if self.cid_point_release is None:
            self.cid_point_release = self.canvas.mpl_connect('button_release_event', self.on_point_release)
        if self.cid_point_move is None:
            self.cid_point_move = self.canvas.mpl_connect('motion_notify_event', self.on_point_drag)
        
    def on_point_drag(self, mouse_event):
        if self.im_moving is None:
            return
        print("=== dragging ===")
        x, y = mouse_event.xdata, mouse_event.ydata
        self.im_moving.set_position(x, y)
        self.canvas.draw()
        
    def on_point_release(self, mouse_event):
        self.im_moving = None
        # TODO as well, fix None flags
        self.canvas.mpl_disconnect(self.cid_point_move)
        self.cid_point_move = None
        self.canvas.mpl_disconnect(self.cid_point_release)
        self.cid_point_release = None
        
#         print("self.im_moving = %s") % self.im_moving
#         for p in self.endpoints:
#             print("    %s") % str(p)
#         print("=================\n")
#         if self.im_moving not in self.endpoints:
#             return
#         
#         new_track_xs = self.track.line[0]
#         new_track_ys = self.track.line[1]
#         x, y = mouse_event.xdata, mouse_event.ydata
#         
#         i = self.endpoints.index(self.im_moving)
#         new_track_xs[i] = x
#         new_track_ys[i] = y
#     
#         self.track.set_line(new_track_xs, new_track_ys)
#         self.update_endpoints()

#     def show_draggable_endpoints(self):
#         if self.endpoints is None:
#             self.cid_point_pick = self.canvas.mpl_connect('pick_event', self.on_point_pick)
#             
#         # clear existing endpoint if any
#         self.hide_draggable_endpoints()
#         # create points plot
#         x, y = self.track.line
#         self.canvas.axes.hold(True)
#         self.endpoints = [self.canvas.axes.plot(x[i], y[i], 'o', picker=5)[0] for i in range(len(x))]
#         self.canvas.axes.hold(False)
#             
#         for p in self.endpoints:
#             p.set_visible(True)
#         self.canvas.draw()
#     
#     def hide_draggable_endpoints(self):
#         if self.endpoints is not None:
#             for p in self.endpoints:
#                 p.set_visible(False)
#             self.canvas.draw()
#     
#     def on_point_pick(self, mouse_event):
#         if mouse_event.artist not in self.endpoints:
#             return
#         self.im_moving = mouse_event.artist
#         # multiple calls here, don't know why
#         # set None flags to avoid many connection on point pick
#         # TODO fix this!
#         if self.cid_point_release is None:
#             self.cid_point_release = self.canvas.mpl_connect('button_release_event', self.on_point_release)
#         if self.cid_point_move is None:
#             self.cid_point_move = self.canvas.mpl_connect('motion_notify_event', self.on_point_drag)
#         
#     def on_point_release(self, mouse_event):
#         self.im_moving = None
#         # TODO as well, fix None flags
#         self.canvas.mpl_disconnect(self.cid_point_move)
#         self.cid_point_move = None
#         self.canvas.mpl_disconnect(self.cid_point_release)
#         self.cid_point_release = None
#         
#     def on_point_drag(self, mouse_event):
#         print("=== dragging ===")
#         print("self.im_moving = %s") % self.im_moving
#         for p in self.endpoints:
#             print("    %s") % str(p)
#         print("=================\n")
#         if self.im_moving not in self.endpoints:
#             return
#         
#         new_track_xs = self.track.line[0]
#         new_track_ys = self.track.line[1]
#         x, y = mouse_event.xdata, mouse_event.ydata
#         
#         i = self.endpoints.index(self.im_moving)
#         new_track_xs[i] = x
#         new_track_ys[i] = y
#     
#         self.track.set_line(new_track_xs, new_track_ys)
#         self.update_endpoints()
#         
#     def update_endpoints(self):
#         x, y = self.track.line
#         self.canvas.axes.hold(True)
#         self.endpoints = [self.canvas.axes.plot(x[i], y[i], 'o', picker=5)[0] for i in range(len(x))]
#         self.canvas.axes.hold(False)
#         
        
    
    