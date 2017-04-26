function events2mat(run_id)
if nargin < 1
    run_id = 0;
end

data_path = '../';
data_files = dir([data_path 'Event*.txt']);
n_events = length(data_files);

x = cell(n_events, 1);
y = cell(n_events, 1);

for i = 1:n_events
    f = data_files(i);
    data = load(fullfile(data_path, f.name));
    
    x(i) = {data(:,1)};
    y(i) = {data(:,2)};
end

out_file = ['Run' num2str(run_id) '.mat'];
save(out_file, 'x', 'y');

end
