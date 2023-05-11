% Read the ARFF file
fileID = fopen('data.arff', 'r');
data = textscan(fileID, '%s', 'Delimiter', '\n');
fclose(fileID);

% Open the output ARFF file for writing
fileID = fopen('out.arff', 'w');

% Write the data lines from the input ARFF file to the output ARFF file
for i = 1:numel(data{1})
    line = data{1}{i};
    fprintf(fileID, '%s\n', line);
end

% Close the file
fclose(fileID);