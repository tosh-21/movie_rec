def filter_movies(processed_df, **kwargs):
    """
    Filters the processed dataframe based on the user's search criteria.
    
    Parameters:
    processed_df (pandas.DataFrame): Processed dataframe containing movie data
    **kwargs: variable keyword arguments containing user's search criteria
    
    Returns:
    filtered_df (pandas.DataFrame): Dataframe containing filtered movie data based on user's search criteria
    """
    # Create an empty boolean mask
    mask = pd.Series([True] * len(processed_df), index=processed_df.index)
    
    # Iterate over the keyword arguments passed in and update the boolean mask accordingly
    for key, value in kwargs.items():
        if key == 'title':
            mask = mask & processed_df['movie_title'].str.contains(value, case=False)
        elif key == 'genres':
            mask = mask & processed_df['genres'].str.contains(value, case=False)
        elif key == 'directors':
            mask = mask & processed_df['directors'].str.contains(value, case=False)
        elif key == 'actors':
            mask = mask & processed_df['actors'].str.contains(value, case=False)
        elif key == 'release_date_min':
            mask = mask & (processed_df['original_release_date'] >= int(value))
        elif key == 'release_date_max':
            mask = mask & (processed_df['original_release_date'] <= int(value))
        elif key == 'tomatometer_min':
            mask = mask & (processed_df['tomatometer_rating'] >= int(value))
        elif key == 'tomatometer_max':
            mask = mask & (processed_df['tomatometer_rating'] <= int(value))
    
    # Filter the dataframe based on the boolean mask and return it
    filtered_df = processed_df[mask]
    return filtered_df
