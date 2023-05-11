import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("combined_data.csv")
print(df.info())

# plt.plot(vertical_acc, '-', color='black', label='Original')
plt.plot(df["X"], '-', color='blue', label='ACC_X')
plt.plot(df["Y"], "-", color='red', label='ACC_Y')
plt.plot(df["Z"], "-", color='green', label='ACC_Z')
plt.plot(df["labels1"], "-", color='black', label='labels')
plt.legend()
plt.title('Data and Labels')
# plt.show()


import pandas as pd
# from scipy.io import arff
import arff

# Read the CSV file
data = pd.read_csv('combined_data.csv')

# Define the attribute names and types
attribute_names = ['index', 'X', 'Y', 'Z']
class_types = ['Fast Walking', 'Non Walking', 'Sitting', 'Walking']

# Add the 'labels' column to the DataFrame
data['labels'] = data['labels1'].map({1: 'Fast Walking', 2: 'Non Walking', 3: 'Sitting', 4: 'Walking'})

# Drop the 'class' column
data = data.drop('labels1', axis=1)


# Convert DataFrame to ARFF format
data_arff = arff.dumps(data.values.tolist(), relation='acceleration_data', names=attribute_names)

# Insert the class types as a separate attribute in the ARFF header
data_arff = data_arff.replace("@data", f"@attribute classes {{{', '.join(class_types)}}}\n\n@data")

# Write ARFF data to a file
with open('out.arff', 'w') as f:
    f.write(data_arff)