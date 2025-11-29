# import pandas as pd
# df = pd.read_csv('reg_labels.csv')
# def label_bgl(x):
#     if x < 140:
#         return 0
#     elif 140 <= x < 200:
#         return 1
#     else:
#         return 2

# df['Label'] = df['BGL'].apply(label_bgl)
# df.drop(columns=['BGL'], inplace=True)
# df.to_csv('Labels.csv', index=False)
import pandas as pd

# Load the CSV files
labels_df = pd.read_csv("Labels.csv")
features_df = pd.read_csv("reg_features_new.csv")

# Combine features and labels (assumes rows are aligned)
combined_df = features_df.copy()
combined_df['Label'] = labels_df['Label']

# Save the combined dataframe to a new CSV (optional)
combined_df.to_csv("combined_dataset_new.csv", index=False)

# Show shape and preview
print("Combined shape:", combined_df.shape)
print(combined_df.head())
