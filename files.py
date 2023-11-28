import  streamlit as st
import pandas as pd

st.subheader('Loading the CSV file')
df = st.file_uploader('Upload the CSV file :', type = ['csv','xlsx ','png','jpg'])

st.subheader('Dealing with image')
img_file = st.file_uploader("Upload the Image file : ", type = ['png', 'jpeg'])
if img_file is not None:
    st.image(img_file)

st.subheader('Working with Videos')
video_File = st.file_uploader('Upload the Video file :',type=['mkv','mp4'])
if video_File is not None:
    st.video(video_File,start_time=0)

st.subheader('Working with Audio files')
audio_File = st.file_uploader('Upload the Video file :',type=['wav','mp3'])
if audio_File is not None:
    st.audio(audio_File.read())

#st.subheader('loading the CSV file')
#df = pd.read_csv('')
 #if df is not None:
     # df.head()
