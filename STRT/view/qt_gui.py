import numpy as np

from PyQt5 import QtCore, QtWidgets
from PyQt5.QtGui import QIntValidator
from mainwindow import Ui_MainWindow
from view.qt_track_representation import TrackRepresentation
from lasso_manager import LassoManager
from tracks_parameters import Ui_DockWidget as analysis_form

class QtGui(Ui_MainWindow):
    def __init__(self):
        super(QtGui, self).__init__()
        self.current_event = None
        self.tracks = []
        self.Houghlines = []
        self.hits_selection_is_on = None
        
    def setupUi(self, MainWindow):
        Ui_MainWindow.setupUi(self, MainWindow)
        self.tracksLayout = self.verticalLayout_6
        self.lasso = LassoManager(self.plotWidget.figure.canvas)
        self.lasso.add_listener(self)
        # analysis form
        self.analysis_widget = QtWidgets.QDockWidget(MainWindow)
        self.analysis_form = analysis_form()
        self.analysis_form.setupUi(self.analysis_widget)
        MainWindow.addDockWidget(QtCore.Qt.BottomDockWidgetArea, self.analysis_widget)
        self.analysis_widget.hide()
        # css
        self.connect_signals_slots()
        
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
        self.action_Hough_transform.triggered.connect(self.show_Hough_transform_canvas)
        self.action_explore_parameters.triggered.connect(self.explore_parameters)
        # 
        self.analysis_form.transfomEventButton.clicked.connect(self.event_Hough_transform_requested)
        self.analysis_form.transformTrackButton.clicked.connect(self.track_Hough_transform_requested)
    
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
#         test_dir_path = "/home/vlad/Program_Files/ilcsoft/marlintpc/workspace/STRT/outdata/Run25"
        test_dir_path = "/home/vlad/Program_Files/ilcsoft/marlintpc/workspace/Run25/raw/session"
        dirname = QtWidgets.QFileDialog.getExistingDirectory(self.centralwidget, "Open Directory", test_dir_path, QtWidgets.QFileDialog.ShowDirsOnly) 
        self.controller.on_load_session(dirname)
        
    def show_Hough_transform_canvas(self):
        self.analysis_widget.show()
    
    def explore_parameters(self):
        self.analysis_widget.show()
        
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
        # 5) synchronize lineedit and slider
        self.sync_nbins_lineedit_slider()
        self.add_tooltip_to_slider(self.trackParamBinningSlider)
        
    def add_tooltip_to_slider(self, sliderWidget):
        sliderWidget.valueChanged.connect(self.track_param_slider_val_changed)
    
    def track_param_slider_val_changed(self, value):
        # taken from here https://stackoverflow.com/questions/31653647/how-to-make-a-tip-to-follow-the-handler-of-slider-with-pyqt
        slider = self.trackParamBinningSlider
        style = slider.style()
        opt = QtWidgets.QStyleOptionSlider()
        slider.initStyleOption(opt)
        rect_handle = style.subControlRect(QtWidgets.QStyle.CC_Slider, opt, QtWidgets.QStyle.SC_SliderHandle, self.analysis_form.parametersMatplotlibToolbar)
        tip_offset = QtCore.QPoint(0, -45)
        pos_local = rect_handle.topLeft() + tip_offset
        pos_global = slider.mapToGlobal(pos_local)
        QtWidgets.QToolTip.showText(pos_global, str(value), slider)
        
    def sync_nbins_lineedit_slider(self):
        self.trackParamBinningLine.returnPressed.connect(self.track_param_lineedit2slider)
        self.trackParamBinningSlider.sliderReleased.connect(self.track_param_slider2lineedit)
        
    def track_param_lineedit2slider(self):
        val = int(self.trackParamBinningLine.text())
        self.trackParamBinningSlider.setValue(val)
        self.set_nbins_in_hist_track_param(val)
        
    def track_param_slider2lineedit(self):
        val = self.trackParamBinningSlider.value()
        self.trackParamBinningLine.setText(str(val))
        self.set_nbins_in_hist_track_param(val)
        
    def update_nbins_slider_lineedit_range(self, minval, maxval):
        self.trackParamBinningLine.setValidator(QIntValidator(minval, maxval))
        self.trackParamBinningSlider.setRange(minval, maxval)
        
    def set_nbins_track_param(self, n_bins):
        self.n_bins_track_param = n_bins
        self.trackParamBinningLine.setText(str(self.n_bins_track_param))
        self.trackParamBinningSlider.setValue(self.n_bins_track_param)
        
    def set_nbins_in_hist_track_param(self, n_bins):
        self.update_track_param_plot(self.track_param_dist, n_bins)
    
    def update_track_param_plot(self, distribution, n_bins=10):
        # filter None values
        self.track_param_dist = filter(lambda x: x is not None, distribution)
        n_entries = len(self.track_param_dist)
        self.update_nbins_slider_lineedit_range(1, 2*n_entries)
#         if not hasattr(self, "n_bins_track_param") or self.n_bins_track_param > n_entries:
        self.set_nbins_track_param(n_bins)
        # plot 
        axes = self.analysis_form.parametersPlotWidget.axes
        if n_entries == 0:
            axes.clear()
            self.analysis_form.parametersPlotWidget.draw()
            return
        counts, bins, _ = axes.hist(self.track_param_dist, self.n_bins_track_param, linewidth=2, histtype='step', stacked=True, fill=False)
        dy = max(counts)*0.05
        axes.set_ylim([-dy, max(counts)+dy])
#         print "n, bins = ", n, bins
        self.analysis_form.parametersPlotWidget.draw()
        
    def track_param_changed(self):
        chosen_param_name = self.get_chosen_track_parameter()
        self.controller.on_track_param_plot_update(chosen_param_name)
    
    def event_Hough_transform_requested(self):
        self.controller.on_event_Hough_transform(self.current_event.id)
        
    def track_Hough_transform_requested(self):
        current_track_repr = self.get_selected_track()
        if current_track_repr is None:
            return
        self.controller.on_track_Hough_transform(self.current_event.id, self.get_selected_track().track.id)
        
    def update_Hough_transform_canvas(self, HT, lines):
        self.analysis_form.HTCanvas.display_Hough_transform(HT)
        self.display_Houghlines(lines)
        
    def display_Houghlines(self, lines):
        self.clear_Houghlines()
        if len(lines) == 0:
            return
        xmin, xmax = self.plotWidget.axes.get_xlim()
        for l in lines:
            rho, theta = l[0]
            x1 = xmin
            x2 = xmax
            y1 = rho + x1*np.tan(theta)
            y2 = rho + x2*np.tan(theta)
            line = self.plotWidget.add_line((x1, x2), (y1, y2), "k")
            self.Houghlines.append(line)
    
    def clear_Houghlines(self):
        if len(self.Houghlines) != 0:
            for l in self.Houghlines:
                l.set_visible(False)
            self.Houghlines = []






    