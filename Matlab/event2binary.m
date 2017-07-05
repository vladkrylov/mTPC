function event2binary(txt_event_file)
if nargin < 1
    txt_event_file = '../Event6.txt';
end

pixel_size = 0.055;
data = load(txt_event_file);
x = floor(data(:,1) / pixel_size);
y = floor(data(:,2) / pixel_size);

n = 2000;
m = 2000;

im = zeros(n,m);
for i=1:length(x)
    im(n - y(i), x(i)) = 1;
end
im = im2bw(im);
imshow(im)
imwrite(im, 'binEvent6.tif')

end