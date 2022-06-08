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

if selection == "All Workouts":
    st.markdown(f"## All Workouts")

    workouts = get_workouts()
    for wo in workouts:
        url = "https://youtu.be/" + wo["video_id"]
        st.text(wo['title'])
        st.text(f"{wo['channel']} - {get_duration_text(wo['duration'])}")

        ok = st.button('Delete Workout', key=wo['video_id'])
        if ok:
            dbs.delete_workout(wo['video_id'])
            st.legacy_caching.clear_cache()
            st.experimental_rerun()

        st.video(url)
    else:
        st.text("No workout videos in database!!")

elif selection=='Add Workout':
    st.markdown(f"## Add workout")

    url = st.text_input("Please enter the video url")
    if url:
        workout_data = get_info(url)
        if workout_data is None:
            st.text("No workout videos!!")
        else:
            st.text(workout_data['title'])
            st.text(workout_data['channel'])
            st.video(url)
            if st.button("Add workout"):
                dbs.insert_workout(workout_data)
                st.text("Added workout!")
                st.legacy_caching.clear_cache()

else:
    st.markdown(f"## Add Workout")

    workouts = get_workouts()
    if not workouts:
        st.text("No workout videos!!")
    else:
        wo = dbs.get_workout_today()

        if not wo:
            # not yet defined
            workouts = get_workouts()
            n = len(workouts)
            idx = random.randint(0, n-1)
            wo = workouts[idx]
            dbs.update_workout_today(wo, insert=True)
        else:
            # first item in list
            wo = wo[0]

        if st.button("Choose Another Workout"):
            workouts = get_workouts()
            n = len(workouts)
            if n > 1:
                idx = random.randint(0, n-1)
                wo_new = workouts[idx]
                while wo_new['video_id'] == wo['video_id']:
                    idx = random.randint(0, n-1)
                    wo_new = workouts[idx]
                wo = wo_new
                dbs.update_workout_today(wo, insert=True)

            
        url = "https://youtu.be/" + wo["video_id"]
        st.text(wo['title'])
        st.text(f"{wo['channel']} - {get_duration_text(wo['duration'])}")
        st.video(url)

