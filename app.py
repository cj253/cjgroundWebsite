import streamlit as st
from streamlit.components.v1 import html

st.set_page_config(page_title='CJGround - Gorilla Tag Channel', layout='centered')

page_bg = '''
<style>
body {
    background-color: #f0f8ff;
    color: #333333;
    font-family: 'Arial', sans-serif;
}
h1, h2, h3, h4, h5, h6 {
    color: #1e90ff;
}
a {
    color: #1e90ff;
    text-decoration: none;
}
a:hover {
    color: #4682b4;
}
</style>
'''

st.markdown(page_bg, unsafe_allow_html=True)

st.title('Welcome to CJGrounds Website!')


st.header('About Me')
st.write("Hey there! I'm CJGround, and I love playing Gorilla Tag. I create fun and exciting content around the game, sharing gameplay, tips, and hilarious moments!")

st.header('Check Out My YouTube Channel')
st.write("I post videos regularly on my YouTube channel. Make sure to subscribe and join the community!")
st.markdown('[CJGround YouTube Channel](https://www.youtube.com/@cjground)', unsafe_allow_html=True)

st.header('Follow Me on Social Media')
st.write("Stay connected for updates and more content!")
st.markdown('[Twitter](https://twitter.com/) | [Instagram](https://instagram.com/)')

st.header('Contact Me')
st.write("Got questions or just want to chat? Reach out through my social media!")

st.caption("Website created using Streamlit")
