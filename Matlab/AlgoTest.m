function varargout = AlgoTest(varargin)
% ALGOTEST MATLAB code for AlgoTest.fig
%      ALGOTEST, by itself, creates a new ALGOTEST or raises the existing
%      singleton*.
%
%      H = ALGOTEST returns the handle to a new ALGOTEST or the handle to
%      the existing singleton*.
%
%      ALGOTEST('CALLBACK',hObject,eventData,handles,...) calls the local
%      function named CALLBACK in ALGOTEST.M with the given input arguments.
%
%      ALGOTEST('Property','Value',...) creates a new ALGOTEST or raises the
%      existing singleton*.  Starting from the left, property value pairs are
%      applied to the GUI before AlgoTest_OpeningFcn gets called.  An
%      unrecognized property name or invalid value makes property application
%      stop.  All inputs are passed to AlgoTest_OpeningFcn via varargin.
%
%      *See GUI Options on GUIDE's Tools menu.  Choose "GUI allows only one
%      instance to run (singleton)".
%
% See also: GUIDE, GUIDATA, GUIHANDLES

% Edit the above text to modify the response to help AlgoTest

% Last Modified by GUIDE v2.5 30-Apr-2017 07:05:24

% Begin initialization code - DO NOT EDIT
gui_Singleton = 1;
gui_State = struct('gui_Name',       mfilename, ...
                   'gui_Singleton',  gui_Singleton, ...
                   'gui_OpeningFcn', @AlgoTest_OpeningFcn, ...
                   'gui_OutputFcn',  @AlgoTest_OutputFcn, ...
                   'gui_LayoutFcn',  [] , ...
                   'gui_Callback',   []);
if nargin && ischar(varargin{1})
    gui_State.gui_Callback = str2func(varargin{1});
end

if nargout
    [varargout{1:nargout}] = gui_mainfcn(gui_State, varargin{:});
else
    gui_mainfcn(gui_State, varargin{:});
end
% End initialization code - DO NOT EDIT

% --- Executes just before AlgoTest is made visible.
function AlgoTest_OpeningFcn(hObject, eventdata, handles, varargin)
% This function has no output args, see OutputFcn.
% hObject    handle to figure
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)
% varargin   command line arguments to AlgoTest (see VARARGIN)

% Choose default command line output for AlgoTest
handles.output = hObject;

% Update handles structure
guidata(hObject, handles);

% This sets up the initial plot - only do when we are invisible
% so window can get raised using AlgoTest.
if strcmp(get(hObject,'Visible'),'off')
    plot(rand(5));
end

set(hObject, 'toolbar', 'figure');

setappdata(handles.figure1, 'pixel_size', 0.055);

% UIWAIT makes AlgoTest wait for user response (see UIRESUME)
% uiwait(handles.figure1);


% --- Outputs from this function are returned to the command line.
function varargout = AlgoTest_OutputFcn(hObject, eventdata, handles)
% varargout  cell array for returning output args (see VARARGOUT);
% hObject    handle to figure
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

% Get default command line output from handles structure
varargout{1} = handles.output;

set(hObject,'units','pixel');
set(hObject,'Position',[0 34 1368 676]);

% set_icon(handles.NewEventPushButton, 'img/select_new_track.png');
set_icon(handles.NewEventPushButton, 'img/Properties_32x32.png');
set_icon(handles.AddNewTrackButton, 'img/newtrack_32x32.png');

set_icon(handles.EditTrackButton, 'img/edittrack_32x32.png');
set_icon(handles.StopEditTrackButton, 'img/savetrack_32x32.png');
set_icon(handles.RemoveTrackButton, 'img/delhits_32x32.png');
set_icon(handles.AddHitsToTrackButton, 'img/Add_24x24.png');
set_icon(handles.RemoveHitsFromTrackButton, 'img/Remove_24x24.png');

set_icon(handles.HoughTransformButton, 'img/Forward_32x32.png');
set_icon(handles.SelectHTracksButton, 'img/Presentation_32x32.png');

% --------------------------------------------------------------------
function FileMenu_Callback(hObject, eventdata, handles)
% hObject    handle to FileMenu (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)


% --------------------------------------------------------------------
function OpenMenuItem_Callback(hObject, eventdata, handles)
% hObject    handle to OpenMenuItem (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)
file = uigetfile('*.fig');
if ~isequal(file, 0)
    open(file);
end

% --------------------------------------------------------------------
function PrintMenuItem_Callback(hObject, eventdata, handles)
% hObject    handle to PrintMenuItem (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)
printdlg(handles.figure1)

% --------------------------------------------------------------------
function CloseMenuItem_Callback(hObject, eventdata, handles)
% hObject    handle to CloseMenuItem (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)
selection = questdlg(['Close ' get(handles.figure1,'Name') '?'],...
                     ['Close ' get(handles.figure1,'Name') '...'],...
                     'Yes','No','Yes');
if strcmp(selection,'No')
    return;
end

delete(handles.figure1)

% --- Executes on button press in NewEventPushButton.
function NewEventPushButton_Callback(hObject, eventdata, handles)
% hObject    handle to NewEventPushButton (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)
pixel_size = getappdata(handles.figure1, 'pixel_size');

data_path = '../Event0.txt';
data = load(data_path);
event_id = 0;

setappdata(handles.figure1, 'current_event_id', event_id);
setappdata(handles.figure1, 'x', floor(data(:,1) / pixel_size));
setappdata(handles.figure1, 'y', floor(data(:,2) / pixel_size));

axes(handles.axes1)
x = getappdata(handles.figure1, 'x');
y = getappdata(handles.figure1, 'y');

setappdata(handles.figure1, 'events', struct('id', event_id,...
                                             'xhits', x,...
                                             'yhits', y,...
                                             'zcharge', [],...
                                             'selected_tracks', [],...
                                             'reconstructed_rtacks', []));

plot(x, y, 'k.');
xlabel('x, pixels')
ylabel('y, pixels')

% --- Executes on button press in EditTrackButton.
function EditTrackButton_Callback(hObject, eventdata, handles)
% hObject    handle to EditTrackButton (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)
current_event_id = getappdata(handles.figure1, 'current_event_id');
if isempty(current_event_id)
    errordlg('No hits data loaded','Data not available');
    return;
end
setappdata(handles.figure1, 'edit_track', true);
set(handles.AddHitsToTrackButton, 'Enable', 'on');
set(handles.RemoveHitsFromTrackButton, 'Enable', 'on');

set(handles.NewEventPushButton, 'Enable', 'off');
set(handles.HoughTransformButton, 'Enable', 'off');
set(handles.EditTrackButton, 'Enable', 'off');
set(handles.AddNewTrackButton, 'Enable', 'off');
set(handles.RemoveTrackButton, 'Enable', 'off');


% --- Executes on button press in StopEditTrackButton.
function StopEditTrackButton_Callback(hObject, eventdata, handles)
% hObject    handle to StopEditTrackButton (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)
edit_track = getappdata(handles.figure1, 'edit_track');
if isempty(edit_track) || edit_track == false
    return;
end

setappdata(handles.figure1, 'edit_track', false);

set(handles.AddHitsToTrackButton, 'Enable', 'off');
set(handles.RemoveHitsFromTrackButton, 'Enable', 'off');

set(handles.NewEventPushButton, 'Enable', 'on');
set(handles.HoughTransformButton, 'Enable', 'on');
set(handles.EditTrackButton, 'Enable', 'on');
set(handles.AddNewTrackButton, 'Enable', 'on');
set(handles.RemoveTrackButton, 'Enable', 'on');

% save current track in the corresponding event structure
events = getappdata(handles.figure1, 'events');
current_track = getappdata(handles.figure1, 'current_track');
if isempty(current_track)
    return;
end

for iev = 1:length(events)
    if current_track.event_id == events(iev).id
        events(iev).selected_tracks = [events(iev).selected_tracks current_track];
        setappdata(handles.figure1, 'events', events);
%         rmappdata(handles.figure1, 'current_track');
        break;
    end
end


% --- Executes on button press in AddHitsToTrackButton.
function AddHitsToTrackButton_Callback(hObject, eventdata, handles)
% hObject    handle to AddHitsToTrackButton (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)
events = getappdata(handles.figure1, 'events');
current_event_id = getappdata(handles.figure1, 'current_event_id');
current_track = getappdata(handles.figure1, 'current_track');

for i=1:length(events)
    if current_event_id == events(i).id
        current_event = events(i);
    end
end

% ignore already selected track handles
ignore_list = current_track.plot_handle;
for i=1:length(current_event.selected_tracks)
    ignore_list = [ignore_list current_event.selected_tracks(i).plot_handle];
end

axes(handles.axes1);
[tind,~,~] = selectdata('selectionmode','rect', 'ignore', ignore_list);
current_track.inds = union(current_track.inds, tind);

% display currently selected hits
axes(handles.axes1);
if ~isempty(current_track.plot_handle)
    delete(current_track.plot_handle);
    current_track.plot_handle = [];
%     set(current_track.plot_handle, 'Visible', 'off');
end

hold on
current_track.plot_handle = plot(current_event.xhits(current_track.inds),...
                                 current_event.yhits(current_track.inds),...
                                 'o',...
                                 'MarkerEdgeColor', current_track.color);
hold off
setappdata(handles.figure1, 'current_track', current_track);


% --- Executes on button press in RemoveHitsFromTrackButton.
function RemoveHitsFromTrackButton_Callback(hObject, eventdata, handles)
% hObject    handle to RemoveHitsFromTrackButton (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)
events = getappdata(handles.figure1, 'events');
current_event_id = getappdata(handles.figure1, 'current_event_id');
current_track = getappdata(handles.figure1, 'current_track');

for i=1:length(events)
    if current_event_id == events(i).id
        current_event = events(i);
    end
end

% ignore already selected track handles
ignore_list = current_track.plot_handle;
for i=1:length(current_event.selected_tracks)
    ignore_list = [ignore_list current_event.selected_tracks(i).plot_handle];
end

axes(handles.axes1);
[tind,~,~] = selectdata('selectionmode','rect', 'ignore', ignore_list);
current_track.inds = setdiff(current_track.inds, tind);

% display currently selected hits
axes(handles.axes1);
if ~isempty(current_track.plot_handle)
    delete(current_track.plot_handle);
    current_track.plot_handle = [];
end

hold on
current_track.plot_handle = plot(current_event.xhits(current_track.inds),...
                                 current_event.yhits(current_track.inds),...
                                 'o',...
                                 'MarkerEdgeColor', current_track.color);
hold off
setappdata(handles.figure1, 'current_track', current_track);


% --- Executes on button press in AddNewTrackButton.
function AddNewTrackButton_Callback(hObject, eventdata, handles)
% hObject    handle to AddNewTrackButton (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)
current_event_id = getappdata(handles.figure1, 'current_event_id');
if isempty(current_event_id)
    errordlg('No hits data loaded','Data not available');
    return;
end

event_id = getappdata(handles.figure1, 'current_event_id');
% get current event
events = getappdata(handles.figure1, 'events');
for i=1:length(events)
    if current_event_id == events(i).id
        current_event = events(i);
    end
end

% get list of selected track ids
if isempty(current_event.selected_tracks)
    track_id = 0;
else
    existing_track_ids = zeros(1, length(current_event.selected_tracks));
    for i=1:length(existing_track_ids)
        existing_track_ids(i) = current_event.selected_tracks(i).track_id;
    end
    existing_track_ids = sort(existing_track_ids);

    track_id = existing_track_ids(end)+1;
end

current_track = struct('track_id', track_id,...
                       'event_id', event_id,...
                       'color', nice_color(track_id),...
                       'inds', [],...
                       'plot_handle', []);
setappdata(handles.figure1, 'current_track', current_track);


% --- Executes on button press in RemoveTrackButton.
function RemoveTrackButton_Callback(hObject, eventdata, handles)
% hObject    handle to RemoveTrackButton (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)


% --- Executes on button press in HoughTransformButton.
function HoughTransformButton_Callback(hObject, eventdata, handles)
% hObject    handle to HoughTransformButton (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

x = getappdata(handles.figure1, 'x');
y = getappdata(handles.figure1, 'y');
current_event_id = getappdata(handles.figure1, 'current_event_id');
if isempty(x) || isempty(y)
    errordlg('No hits data loaded','Data not available');
    return;
end

n_hits = length(x);

xy_image = zeros(1);
for i=1:n_hits
    xy_image(y(i), x(i)) = 1;
end

[H,T,R] = hough(xy_image);

axes(handles.axes2)
[Tm, Rm] = meshgrid(T, R);
s = surf(Tm, Rm, H);
s.EdgeColor = 'None';
view(0, 90);
colorbar;
xlabel('\theta, degrees'), ylabel('\rho, pixels');
xlim([min(T), max(T)])
ylim([min(R), max(R)])


% --- Executes on button press in SelectHTracksButton.
function SelectHTracksButton_Callback(hObject, eventdata, handles)
% hObject    handle to SelectHTracksButton (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)



