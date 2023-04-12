import pandas as pd

#read the data
complete_df = pd.read_csv("~/PyProject/rotten_tomatoes_movies.csv")

#select relevant columns
selected_columns = ['movie_title', 'movie_info', 'genres', 'directors', 'actors', 'original_release_date', 'tomatometer_rating']
processed_df = complete_df[selected_columns]

# Convert the original_release_date column to datetime format and extract the year
processed_df.loc[:, 'original_release_date'] = pd.to_datetime(processed_df['original_release_date']).dt.year
print(processed_df.head())