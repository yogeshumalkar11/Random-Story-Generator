import streamlit as st
from story import generate_story

st.set_page_config(page_title='Bedtime Stories', page_icon=None,
                   layout="wide", initial_sidebar_state="auto", menu_items=None)
st.title("AI generated Bedtime Stories")
st.sidebar.title("Customize Your Story")
name = st.sidebar.text_input("Enter a name:")
genre = st.sidebar.selectbox("Select a Genre:", ('Action', 'Adventure', 'Comedy',
                             'Drama', 'Fantasy', 'Horror', 'Mystery', 'Romance', 'Sci-Fi', 'Thriller', 'Western'))


if st.sidebar.button("Generate New Story"):
    story = generate_story(name, genre)
    st.write(story['story'].strip())
else:
    st.write("Click the button to generate the story.")
