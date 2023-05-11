
# from utilies import sk_util as sk
import pandas as pd
import glob
import matplotlib.pyplot as plt

# Create a list of all CSV files in the current directory
sk_pathFiles = "D:/Projects In Master Degree/2. Second Semester/Deep Learning/Homeworks/Chapter 5/Datasets/"
sk_pathFiles1 = "D:/Projects In Master Degree/2. Second Semester/Deep Learning/Homeworks/Chapter 5/"
# with open("Datasets/Walking.csv", 'r', encoding='utf-16') as f:
#     data_str = f.read().split("\n")
#     data = [row.split(",") for row in data_str]
#     df = pd.DataFrame(data)
#     combined_df = df[0].str.split(r"\t", expand=True)
#     combined_df =  combined_df.iloc[5:]
#     combined_df.columns = ['Time (s)', 'X', 'Y', 'Z', '|V|', 'MAx', 'MAy', 'MAz', 'MAv']
# combined_df["X"]  = pd.to_numeric(combined_df["X"] , errors='coerce')
# combined_df["X"] = combined_df["X"].astype('float')
# combined_df["Y"]  = pd.to_numeric(combined_df["Y"] , errors='coerce')
# combined_df["Y"] = combined_df["Y"].astype('float')
# combined_df["Z"]  = pd.to_numeric(combined_df["Z"] , errors='coerce')
# combined_df["Z"] = combined_df["Z"].astype('float')
# # plt.plot(vertical_acc, '-', color='black', label='Original')
# plt.plot(combined_df["X"], '-', color='blue', label='ACC_X')
# plt.plot(combined_df["Y"], "-", color='red', label='ACC_Y')
# plt.plot(combined_df["Z"], "-", color='green', label='ACC_Z')
# # plt.plot(df["labels"], "-", color='black', label='labels')
# plt.legend()
# plt.title('Data and Labels')
# plt.show()

# # Get list of file names in directory
all_files = glob.glob(f"{sk_pathFiles}*.csv")

# Create an empty list to store dataframes
dfs = []

# Loop through all CSV files and read them into dataframes
for file in all_files:
    # Get the filename from the file path
    filename = file.split('/')[-1]  # Extract the filename from the path
    with open(file, 'r', encoding='utf-16') as f:
        data_str = f.read().split("\n")
        data = [row.split(",") for row in data_str]
        df = pd.DataFrame(data)
        data_set1 = df[0].str.split(r"\t", expand=True)
        data_set1 =  data_set1.iloc[5:]
        data_set1.columns = ['Time (s)', 'X', 'Y', 'Z', '|V|', 'MAx', 'MAy', 'MAz', 'MAv']
        if "Fast Walking.csv" in filename:
            data_set1["labels1"] = 1
        elif "Fast Walking V1.csv" in filename:
            data_set1["labels1"] = 1
        elif "Non Walking V1.csv" in filename:
            data_set1["labels1"] = 2
        elif "Non Walking.csv" in filename:
            data_set1["labels1"] = 2
        elif "Sitting.csv" in filename:
            data_set1["labels1"] = 3
        elif "Sitting V1.csv" in filename:
            data_set1["labels1"] = 3
        elif "Walking.csv" in filename:
            data_set1["labels1"] = 4
        elif "Walking V1.csv" in filename:
            data_set1["labels1"] = 4

        # drop rows with missing or empty values
        data_set1 = data_set1.dropna(how='any', axis=0)
        dfs.append(data_set1)

combined_df = pd.concat(dfs)
# Reset the index of the combined dataframe
combined_df = combined_df.reset_index(drop=True)
combined_df["index"] = range(len(combined_df))

# Save the combined dataframe to a new CSV file
combined_df["X"]  = pd.to_numeric(combined_df["X"] , errors='coerce')
combined_df["X"] = combined_df["X"].astype('float')
combined_df["Y"]  = pd.to_numeric(combined_df["Y"] , errors='coerce')
combined_df["Y"] = combined_df["Y"].astype('float')
combined_df["Z"]  = pd.to_numeric(combined_df["Z"] , errors='coerce')
combined_df["Z"] = combined_df["Z"].astype('float')
combined_df.to_csv(f"{sk_pathFiles1}combined_data.csv", index=False, columns=['index', 'X', 'Y', 'Z', 'labels1'])
print(combined_df)

