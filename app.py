import random
import streamlit as st
import database_services as dbs
from yt_extractor import get_info

@st.cache(allow_output_mutation=True)
def get_workouts():
    return dbs.get_all_workouts()

def get_duration_text(duration_s):
    seconds = duration_s % 60
    minutes = int((duration_s/60)%60)
    hours = int(duration_s/ (60*60)%24)
    text = ''
    if hours > 0:
        text += f'{hours:02d}:{minutes:02d}:{seconds:02d}'
    else:
        text += f'{minutes:02d}:{seconds:02d}'
    return text

st.title('WORKOUT APP')

menu_options = ("Today's Workout", "All Workouts", "Add Workout")
selection = st.sidebar.selectbox("Menu", menu_options)

