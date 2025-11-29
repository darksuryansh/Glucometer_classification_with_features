import pandas as pd
df = pd.read_csv('breath-data.csv')
def label_breath(x):
    if x < 140:
        return 0
    elif 140 <= x < 200:
        return 1
    else:
        return 2

df['Label'] = df['BGL'].apply(label_breath)
df.drop(columns=['BGL'], inplace=True)
df.to_csv('breath_labels_less.csv', index=False)