from PyQt5 import QtCore, QtWidgets
from mainwindow import Ui_MainWindow
from view.qt_track_representation import TrackRepresentation
from lasso_manager import LassoManager
from tracks_parameters import Ui_DockWidget as analysis_form

class QtGui(Ui_MainWindow):
    def __init__(self):
        super(QtGui, self).__init__()
        self.current_event = None
        self.tracks = []
        self.hits_selection_is_on = None
        
    def setupUi(self, MainWindow):
        Ui_MainWindow.setupUi(self, MainWindow)
        self.tracksLayout = self.verticalLayout_6
        self.connect_signals_slots()
        self.lasso = LassoManager(self.plotWidget.figure.canvas)
        self.lasso.add_listener(self)
        # analysis form
        self.analysis_widget = QtWidgets.QDockWidget(MainWindow)
        self.analysis_form = analysis_form()
        self.analysis_form.setupUi(self.analysis_widget)
        MainWindow.addDockWidget(QtCore.Qt.BottomDockWidgetArea, self.analysis_widget);
        
    def connect_signals_slots(self):
        # matplotlib events
        self.plotWidget.mpl_connect('pick_event', self.on_pick)
        # Qt toolbar actions
        self.action_load_event.triggered.connect(self.load_new_event)
        self.action_previous_event.triggered.connect(self.prev_event)
        self.action_next_event.triggered.connect(self.next_event)
        self.action_select_new_track.triggered.connect(self.add_new_track)
        self.action_add_hits_to_track.triggered.connect(self.add_hits)
        self.action_remove_hits.triggered.connect(self.remove_hits)
        # Qt menu actions
        self.action_save_session.triggered.connect(self.save_session)
        self.action_load_session.triggered.connect(self.load_session)
        self.action_Hough_transform.triggered.connect(self.Hough_transform)
        self.action_explore_parameters.triggered.connect(self.explore_parameters)
    
    def add_listener(self, controller):
        self.controller = controller
        # track parameters list initialization
        self.track_parameters = sorted(self.controller.get_track_parameters())
        self.trackParamsRadioButtons = []
        for p in self.track_parameters:
            self.trackParamsRadioButtons.append(QtWidgets.QRadioButton(self.analysis_form.parameterNames))
            self.trackParamsRadioButtons[-1].setObjectName("%sRadioButton" % p)
            self.trackParamsRadioButtons[-1].setText(p)
            self.analysis_form.verticalLayout.addWidget(self.trackParamsRadioButtons[-1])
        self.trackParamsRadioButtons[0].setChecked(True)
        for rb in self.trackParamsRadioButtons:
            rb.toggled.connect(self.track_param_changed)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.analysis_form.verticalLayout.addItem(spacerItem)
        self.computeParametersButton = QtWidgets.QPushButton(self.analysis_form.parameterNames)
        self.computeParametersButton.setObjectName("computeParametersButton")
        self.computeParametersButton.setText("Recalculate")
        self.analysis_form.verticalLayout.addWidget(self.computeParametersButton)
        self.computeParametersButton.clicked.connect(self.recalculate_track_parameters)
        # finish track parameters list initialization
        self.add_binning_toolbar()
    
    def load_new_event(self):
        test_file_path = "/home/vlad/Program_Files/ilcsoft/marlintpc/workspace/STRT/indata/Run25"
        filenames = QtWidgets.QFileDialog.getOpenFileNames(self.centralwidget, "QFileDialog.getOpenFileNames()", test_file_path, "All Files (*)")
        self.controller.on_load_events(filenames[0])
    
    def update_with_event(self, event, is_first=False, is_last=False):
        self.current_event = event
        points = [(h.x, h.y) for h in event.hits]
        x = map(lambda point: point[0], points)
        y = map(lambda point: point[1], points)
        self.plotWidget.plot(x, y)
        self.handle_events_navigation(is_first, is_last)
        self.update_status_bar(event)
        self.update_track_list(event)
        print "Canvas successfully updated"
        
    def update_track_list(self, event):
        self.clear_track_list()
        for track in event.tracks:
            x = map(lambda ihit: event.hits[ihit].x, track.hit_indices)
            y = map(lambda ihit: event.hits[ihit].y, track.hit_indices)
            self.plotWidget.add_track_hits(x, y, track.color)
            
            t = TrackRepresentation(track, self.scrollAreaWidgetContents, self.tracksLayout, self.plotWidget)
            self.tracks.append(t)
            if t.track.displayed:
                t.show_line()
                t.check_box.setChecked(True)  # TODO check if slot is called here
            else:
                t.hide_line()
                t.check_box.setChecked(False)
        
    def clear_track_list(self):
        n = 0
        while len(self.tracks) != 0:
#             self.tracks.pop()
            del(self.tracks[0])
            
        while self.tracksLayout.count() > n:
            x = self.tracksLayout.itemAt(n)
            if x.widget():
                x.widget().setParent(None)
            else:
                n += 1
    
    def handle_events_navigation(self, is_first, is_last):
        if is_first and is_last:
            self.action_previous_event.setEnabled(False)
            self.action_next_event.setEnabled(False)
        elif is_first:
            self.action_previous_event.setEnabled(False)
            self.action_next_event.setEnabled(True)
        elif is_last:
            self.action_previous_event.setEnabled(True)
            self.action_next_event.setEnabled(False)
        else:
            self.action_next_event.setEnabled(True)
            self.action_previous_event.setEnabled(True)
    
    def update_status_bar(self, event):
        self.statusBar.showMessage(str(event))
    
    def prev_event(self):
        if self.current_event is None:
            return
        self.controller.on_show_previous_event(self.current_event)
    
    def next_event(self):
        if self.current_event is None:
            return
        self.controller.on_show_next_event(self.current_event)
    
    def add_new_track(self):
        if self.current_event is None:
            return
        self.controller.on_add_track(self.current_event.id)
    
    def remove_track(self):
        if self.current_event is None:
            return
        self.controller.on_remove_track(0)
        
    def on_pick(self, mouse_event):
        if len(self.tracks) == 0:
            return
        if mouse_event.artist not in [t.line for t in self.tracks]:
            # some another artist is selected, not track
            return
        
        for t in self.tracks:
            if t.line == mouse_event.artist and not t.is_selected:
                # t was not selected before, but now it is picked
                t.select()
            elif t.line == mouse_event.artist and t.is_selected:
                # t was selected before and now it is picked again, do nothing with it
                pass
            elif t.line != mouse_event.artist and t.is_selected:
                # t was selected before, but now some another track is picked
                t.deselect()
            elif t.line != mouse_event.artist and not t.is_selected:
                # t neither was selected before nor picked now, do nothing with it
                pass
                    
    def add_hits(self):
        if self.action_add_hits_to_track.isChecked():
            if self.action_remove_hits.isChecked():
                self.action_remove_hits.setChecked(False)
            self.select_hits()
        else:
            self.lasso.stop_selection()
    
    def remove_hits(self):
        if self.action_remove_hits.isChecked():
            if self.action_add_hits_to_track.isChecked():
                self.action_add_hits_to_track.setChecked(False)
            self.select_hits()
        else:
            self.lasso.stop_selection()
        
    def select_hits(self):
        print 0
        if self.current_event is None:
            print 1
            return
        t = self.get_selected_track()
        if not t:
            print 2
            return
        print 3
        self.hits_selection_is_on = True
        print 4
        points = [(h.x, h.y) for h in self.current_event.hits]
        print 5
        self.lasso.set_points(self.plotWidget.axes, points)
    
    def get_selected_track(self):
        tracks = [t for t in self.tracks if t.is_selected]
        if len(tracks) != 0:
            return tracks[0]
        return None
    
    def on_hits_selected(self, indices):
        if self.current_event is None:
            return
        t = self.get_selected_track()
        if not t:
            return
        event_id = self.current_event.id
        track_id = t.track.id
        if self.action_add_hits_to_track.isChecked():
            self.controller.on_add_hits(event_id, track_id, indices)
        elif self.action_remove_hits.isChecked():
            self.controller.on_remove_hits(event_id, track_id, indices)
        
    def save_session(self):
        test_dir_path = "/home/vlad/Program_Files/ilcsoft/marlintpc/workspace/STRT/outdata/Run25"
        dirname = QtWidgets.QFileDialog.getExistingDirectory(self.centralwidget, "Open Directory", test_dir_path, QtWidgets.QFileDialog.ShowDirsOnly ) 
        self.controller.on_save_session(dirname)
        
    def load_session(self):
        test_dir_path = "/home/vlad/Program_Files/ilcsoft/marlintpc/workspace/STRT/outdata/Run25"
        dirname = QtWidgets.QFileDialog.getExistingDirectory(self.centralwidget, "Open Directory", test_dir_path, QtWidgets.QFileDialog.ShowDirsOnly) 
        self.controller.on_load_session(dirname)
        
    def Hough_transform(self):
        self.analysis_widget.show()
    
    def explore_parameters(self):
        self.analysis_widget.show()
        par_name = self.get_chosen_track_parameter()
#         self.controller.on_track_param_update(par_name)
        
    def recalculate_track_parameters(self):
        self.controller.on_recalculate_track_parameters()
        self.track_param_changed()
        
    def get_chosen_track_parameter(self):
        if not self.track_parameters:
            return None
        n_widgets = self.analysis_form.verticalLayout.count()
        for i in range(n_widgets):
            w = self.analysis_form.verticalLayout.itemAt(i).widget()
            if isinstance(w, QtWidgets.QRadioButton) and w.isChecked():
                p = w.text()
                p = str(p.replace("&", ""))
                if p in self.track_parameters:
                    return p
        return None
    
    def add_binning_toolbar(self):
        # 1) spacer to separate matplotlib items from custom ones
        self.emptyWidget = QtWidgets.QWidget(self.analysis_form.parametersMatplotlibToolbar)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.emptyWidget.sizePolicy().hasHeightForWidth())
        self.emptyWidget.setSizePolicy(sizePolicy)
        self.emptyWidget.setMinimumSize(QtCore.QSize(10, 0))
        self.emptyWidget.setMaximumSize(QtCore.QSize(10, 16777215))
        self.analysis_form.parametersMatplotlibToolbar.addWidget(self.emptyWidget)
        # 2) label
        self.trackParamBinningLabel = QtWidgets.QLabel(self.analysis_form.parametersMatplotlibToolbar)
        self.label.setObjectName("trackParamBinningLabel")
        self.trackParamBinningLabel.setText("Binning")
        self.analysis_form.parametersMatplotlibToolbar.addWidget(self.trackParamBinningLabel)
        # 3) LineEdit
        self.trackParamBinningLine = QtWidgets.QLineEdit(self.analysis_form.parametersMatplotlibToolbar)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.trackParamBinningLine.sizePolicy().hasHeightForWidth())
        self.trackParamBinningLine.setSizePolicy(sizePolicy)
        self.trackParamBinningLine.setMinimumSize(QtCore.QSize(60, 0))
        self.trackParamBinningLine.setMaximumSize(QtCore.QSize(60, 16777215))
        self.trackParamBinningLine.setObjectName("trackParamBinningLine")
        self.analysis_form.parametersMatplotlibToolbar.addWidget(self.trackParamBinningLine)
        # 4) slider
        self.trackParamBinningSlider = QtWidgets.QSlider(self.analysis_form.parametersMatplotlibToolbar)
        self.trackParamBinningSlider.setMinimumSize(QtCore.QSize(100, 0))
        self.trackParamBinningSlider.setOrientation(QtCore.Qt.Horizontal)
        self.trackParamBinningSlider.setObjectName("trackParamBinningSlider")
        self.analysis_form.parametersMatplotlibToolbar.addWidget(self.trackParamBinningSlider)
        
    def update_track_param_plot(self, distribution):
        # filter None values
        distribution = filter(lambda x: x is not None, distribution)
        axes = self.analysis_form.parametersPlotWidget.axes
        if len(distribution) == 0:
            axes.clear()
            self.analysis_form.parametersPlotWidget.draw()
            return
        counts, bins, _ = axes.hist(distribution, 10, linewidth=2, histtype='step', stacked=True, fill=False)
        dy = max(counts)*0.05
        axes.set_ylim([-dy, max(counts)+dy])
#         print "n, bins = ", n, bins
        self.analysis_form.parametersPlotWidget.draw()
    
    def track_param_changed(self):
        chosen_param_name = self.get_chosen_track_parameter()
        self.controller.on_track_param_plot_update(chosen_param_name)
    
    
    