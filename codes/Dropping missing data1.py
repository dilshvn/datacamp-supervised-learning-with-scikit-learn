# Print missing values for each column
print(music_df.isna().sum().sort_values())