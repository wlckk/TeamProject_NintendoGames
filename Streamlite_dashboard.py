import streamlit as st
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates


#Streamlite
st.set_page_config(
    page_title="Project 3 - Video Games Analysis",
    page_icon=":smiley:",
    layout="wide",
)

dash = st.sidebar.radio(
    "What dashboard do you want to see ?",
    ('What happened to games?','Clash and platforms', 'Tips for your game'))
if dash == "what happened to games?"
if dash == 'Tips for your game'
    