function testHough(run_id, event_id)
%% arguments checkout
if nargin < 2
    event_id = 0;
end

if nargin < 1
    run_id = 97;
end
pixel_size = 0.055;

%% loading data
load(['Run' num2str(run_id) '.mat']);
xe = floor(x{event_id+1} / pixel_size);
ye = floor(y{event_id+1} / pixel_size);
n_hits = length(xe);

figure(1)
plot(xe, ye, 'k.')
grid on
title(['Event ' num2str(event_id)])
xlabel('X, mm')
ylabel('Y, mm')

    xy_image = zeros(1);

    for i=1:n_hits
        xy_image(ye(i), xe(i)) = 1;
    end
    figure(2)
imshow(flipud(xy_image))

%% Hough transform
[H,T,R] = hough(xy_image);

figure(3)
imshow(H,[],'XData',T,'YData',R,...
            'InitialMagnification','fit');
xlabel('\theta'), ylabel('\rho');
axis on, axis normal, hold on;

flt = fspecial('average', [11, 11]);
Hf = imfilter(H, flt);

%% Color plot
figure(4)
imagesc(Hf);
colorbar;
xlabel('\theta'), ylabel('\rho');

%% Hough lines
P = houghpeaks(Hf, 5, 'threshold', ceil(0.3*max(Hf(:))));
x = T(P(:,2)); y = R(P(:,1));

x = x - min(T);
y = y - min(R);

figure(4)
hold on
plot(x, y, 's', 'color', 'black');
hold off


%% 
figure(5)
[Tm, Rm] = meshgrid(T, R);
s = surf(Tm, Rm, Hf);
s.EdgeColor = 'None';
view(0, 90);
colorbar;
xlabel('\theta'), ylabel('\rho');
xlim([min(T), max(T)])
ylim([min(R), max(R)])

end



