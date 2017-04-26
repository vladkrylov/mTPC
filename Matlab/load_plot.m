function load_plot(event_id)
if nargin < 1
    event_id = 0;
end
data_path = '../';
data = load([data_path 'Event' num2str(event_id) '.txt']);

figure()
plot(data(:,1), data(:,2), 'k.')
title(['Event ' num2str(event_id)])
xlabel('X, mm')
ylabel('Y, mm')

end
