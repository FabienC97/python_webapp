# This is a centent-based recommender system for movie
This system use cosine similarity to get the closest movies to the movie entered by the user. The result is based on the movies tags (title, overview, genres, keyword, cast and crew combined)

The recommendations are based on a 5000 movies dataset, available here :
https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata
It was generated based on The Movie Database website, we kindly 
we would like to thank the team for providing us with this aggregated data and an API that enables us to retrieve other data, such as the film image, this has enabled us to achieve better visual results.

# Requirements
You need the followings packages to be installed :
- Flask
- pandas
- scikit-learn

# To run the app, write this line in the terminal :
streamlit run app.py

# When opened in a web browser, you just need to enter a movie name to get recommendations !
