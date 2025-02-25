import pandas as pd
import os

# creating dataset
data = {"Name": ['Alice', 'Charlie', 'Bob'],
        "Age": [20, 30, 35],
        "City": ['New York', 'Los Angeles', 'Chicago']}

# creating dataframe
df = pd.DataFrame(data)

# # adding new row to df for v2
# new_row_loc = {"Name": "v2", "Age":23, "City": "Delhi"}
# df.loc[len(df.index)] = new_row_loc

# # adding new row to df for v3
# new_row_loc2 = {"Name": "v3", "Age":21, "City": "Noida"}
# df.loc[len(df.index)] = new_row_loc2

# data directory which exist on root level
data_dir = "data"
os.makedirs(data_dir, exist_ok=True)

# define the file path
file_path = os.path.join(data_dir, "sample_data.csv")

# save the data to filepath
df.to_csv(file_path, index=False)

print(f"CSV file saved to {file_path}")