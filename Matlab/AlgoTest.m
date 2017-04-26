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

% Last Modified by GUIDE v2.5 26-Apr-2017 01:47:04

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

set(hObject, 'toolbar', 'figure')

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
set_icon(handles.SelectNewTrackButton, 'img/Add_32x32.png');
set_icon(handles.RemoveTrackButton, 'img/Delete_32x32.png');
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


% --- Executes on selection change in popupmenu1.
function popupmenu1_Callback(hObject, eventdata, handles)
% hObject    handle to popupmenu1 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

% Hints: contents = get(hObject,'String') returns popupmenu1 contents as cell array
%        contents{get(hObject,'Value')} returns selected item from popupmenu1


% --- Executes during object creation, after setting all properties.
function popupmenu1_CreateFcn(hObject, eventdata, handles)
% hObject    handle to popupmenu1 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: popupmenu controls usually have a white background on Windows.
%       See ISPC and COMPUTER.
if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
     set(hObject,'BackgroundColor','white');
end

set(hObject, 'String', {'plot(rand(5))', 'plot(sin(1:0.01:25))', 'bar(1:.5:10)', 'plot(membrane)', 'surf(peaks)'});


% --- Executes on button press in NewEventPushButton.
function NewEventPushButton_Callback(hObject, eventdata, handles)
% hObject    handle to NewEventPushButton (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)
pixel_size = getappdata(handles.figure1, 'pixel_size');

data_path = '../Event0.txt';
data = load(data_path);

setappdata(handles.figure1, 'current_event_id', 0);
setappdata(handles.figure1, 'x', floor(data(:,1) / pixel_size));
setappdata(handles.figure1, 'y', floor(data(:,2) / pixel_size));

axes(handles.axes1)
x = getappdata(handles.figure1, 'x');
y = getappdata(handles.figure1, 'y');
plot(x, y, 'k.');
xlabel('x, pixels')
ylabel('y, pixels')

% --- Executes on button press in SelectNewTrackButton.
function SelectNewTrackButton_Callback(hObject, eventdata, handles)
% hObject    handle to SelectNewTrackButton (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)
current_event_id = getappdata(handles.figure1, 'current_event_id');
if isempty(current_event_id)
    errordlg('No hits data loaded','Data not available');
    return;
end
    
selected_tracks = getappdata(handles.figure1, 'selected_tracks');
if isempty(selected_tracks)
    selected_tracks = {};
end

setappdata(handles.figure1, 'selected_tracks', selected_tracks)




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
