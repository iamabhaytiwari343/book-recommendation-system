import pickle
import streamlit as st
import requests


def recommend():
    user_input = request.form.get('user_input')
    index = np.where(pt.index == user_input)[0][0]
    similar_items = sorted(
        list(enumerate(similarity_scores[index])), key=lambda x: x[1], reverse=True)[1:5]

    data = []
    for i in similar_items:
        item = []
        temp_df = books[books['Book-Title'] == pt.index[i[0]]]
        item.extend(list(temp_df.drop_duplicates(
            'Book-Title')['Book-Title'].values))
        item.extend(list(temp_df.drop_duplicates(
            'Book-Title')['Book-Author'].values))
        item.extend(list(temp_df.drop_duplicates(
            'Book-Title')['Image-URL-M'].values))

        data.append(item)


    print(data)



    return render_template('recommend.html', data=data)




st.header('Book Suggestor')
books = pickle.load(open('../books.pkl', 'rb'))
popular = pickle.load(open('../popular.pkl', 'rb'))
pt = pickle.load(open('../pt.pkl', 'rb'))
similarity = pickle.load(open('../similarity_scores.pkl', 'rb'))

book_list = books['title'].values
selected_movie = st.selectbox(
    "Type or select a movie from the dropdown",
    book_list
)
if st.button('Show Recommendation'):
    recommended_movie_names, recommended_movie_posters = recommend(
        selected_movie)
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.text(recommended_movie_names[0])
        st.image(recommended_movie_posters[0])
    with col2:
        st.text(recommended_movie_names[1])
        st.image(recommended_movie_posters[1])

    with col3:
        st.text(recommended_movie_names[2])
        st.image(recommended_movie_posters[2])
    with col4:
        st.text(recommended_movie_names[3])
        st.image(recommended_movie_posters[3])
    with col5:
        st.text(recommended_movie_names[4])
        st.image(recommended_movie_posters[4])
