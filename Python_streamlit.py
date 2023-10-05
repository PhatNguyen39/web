import streamlit as st
import requests
from streamlit_lottie import st_lottie


def get_random_joke(joke_api_url):
    response = requests.get(joke_api_url)
    data = response.json()
    return data['setup'], data['punchline']


def load_lottieurl(url):
    r= requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()
def main():
    # Define the URL for the Joke API
    joke_api_url = "https://official-joke-api.appspot.com/jokes/random"

    # Create a Streamlit web app
    st.title("Random Joke Generator")

    # Function to fetch a random joke from the API
    with st.container():
        st.write("---")
        left_column, right_column = st.columns(2)
        with left_column:
    # Button to fetch and display a random joke
            if st.button("Get a Random Joke"):
                setup, punchline = get_random_joke(joke_api_url)
                st.write("**Joke Setup:**", setup)
                st.write("**Joke Punchline:**", punchline)

    # Add some fun graphics or emojis
    # st.image(load_lottieurl("https://lottiefiles.com/animations/cute-bear-dancing-AfMGeP3e3h"), use_column_width=True)

    # A footer with some text
            st.write("Made by Phat Nguyen ❤️")
        with right_column:
            lottie_coding=load_lottieurl("https://lottie.host/be7c3796-3968-434f-b047-97025da2a032/H08KkPEj9y.json")
            st_lottie(lottie_coding, height=300, key="coding")

    # Run the Streamlit app


if __name__ == "__main__":
    main()
