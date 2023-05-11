% Read the CSV file
data = readmatrix('combined_data.csv');

% Define attribute names and types
attributeNames = {'index', 'X', 'Y', 'Z'};
attributeTypes = {'numeric', 'numeric', 'numeric', 'numeric'};
labelName = 'class';
labelValues = [1, 2, 3, 4]; % Mapping for class labels
classTypes = {'Fast Walking', 'Non Walking', 'Sitting', 'Walking'};

% Open the ARFF file for writing
fileID = fopen('data.arff', 'w');

% Write the header information
fprintf(fileID, '@relation Data\n\n');

% Write attribute declarations
for i = 1:numel(attributeNames)
    fprintf(fileID, '@attribute %s %s\n', attributeNames{i}, attributeTypes{i});
end

% Write class declarations
fprintf(fileID, '@attribute %s {%s}\n\n', labelName, strjoin(cellstr(num2str(labelValues)), ','));

% Write the data instances
fprintf(fileID, '@data\n');
for i = 1:size(data, 1)
    fprintf(fileID, '%d,%f,%f,%f,%d\n', data(i, :));
end

% Close the file
fclose(fileID);
