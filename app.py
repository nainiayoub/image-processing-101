import streamlit as st
from multiapp import Multiapp
from pages import home, filtering, compression

app = Multiapp()

app.add_app("Home", home.app)
app.add_app("Image Filtering", filtering.app)
app.add_app("Image Compression", compression.app)



app.run()