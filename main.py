import streamlit as st
import pygame
import time
st.set_page_config(page_title="HAPPY BIRTHDAY", initial_sidebar_state="expanded")

hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            footer {

	visibility: hidden;

	}
footer:after {
	content:'Made by 4S group'; 
	visibility: visible;
	display: block;
	position: relative;
	#background-color: red;
	padding: 5px;
	top: 2px;
}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

st.title("Happy Birthday!")


while True:
    st.balloons()
    time.sleep(.1)

