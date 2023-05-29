import pickle
import streamlit as st
import streamlit.components.v1 as components #to be able to add html code
import requests

st.set_page_config(layout="wide")

def get_img(movie_id):
    #We retrieve the corresponding image thanks to an API at themoviedb.org
    #More info : https://developer.themoviedb.org/docs
    url = "https://api.themoviedb.org/3/movie/{}?api_key=fe7a3ee55b7792cd4c28d15ae6b75374".format(movie_id)
    data = requests.get(url)
    data = data.json()
    img_path = data['poster_path']
    full_path = "https://image.tmdb.org/t/p/w500/" + img_path
    return full_path

def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    recommended_movie_names = []
    recommended_movie_posters = []
    for i in distances[1:11]:
        # fetch the movie poster
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movie_posters.append(get_img(movie_id))
        recommended_movie_names.append(movies.iloc[i[0]].title)

    return recommended_movie_names,recommended_movie_posters


st.header(':yellow[Searching for a good movie to watch ?]')
st.subheader('Choose a movie and get recommendations based on it !')
st.markdown("")
movies = pickle.load(open('movie_list.pkl','rb'))
similarity = pickle.load(open('similarity.pkl','rb'))

movie_list = movies['title'].values
selected_movie = st.selectbox(
    "Type or select a movie from the dropdown menu",
    movie_list
)

if st.button('Inspire me'):
    st.markdown("")
    st.subheader('Recommended Movies :')
    st.markdown("")
    recommended_movie_names,recommended_movie_posters = recommend(selected_movie)
    col1, col2, col3, col4, col5 = st.columns(5)
    st.markdown("")
    col6, col7, col8, col9, col10 = st.columns(5)
    with col1:
        st.image(recommended_movie_posters[0])
    with col2:
        st.image(recommended_movie_posters[1])
    with col3:
        st.image(recommended_movie_posters[2])
    with col4:
        st.image(recommended_movie_posters[3])
    with col5:
        st.image(recommended_movie_posters[4])
    with col6:
        st.image(recommended_movie_posters[5])
    with col7:
        st.image(recommended_movie_posters[6])
    with col8:
        st.image(recommended_movie_posters[7])
    with col9:
        st.image(recommended_movie_posters[8])
    with col10:
        st.image(recommended_movie_posters[9])
    
    





