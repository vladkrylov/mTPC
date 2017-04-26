function set_icon(obj, icon_path, bkg_col)
%% Sets an icon to provided uicontrol object
if nargin < 3
    bkg_col = 205;
end

img = imread(icon_path);
img(img == 0) = bkg_col;
set(obj, 'CData', img);

end
