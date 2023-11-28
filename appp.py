import  streamlit as st
st.title('title-> Hello Geeks , welcome to Geeks for Geeks ')
st.header('header-> GFG')
st.subheader('subheader -> GFG')
st.text('text-> hello ji ramm ram sareyanu')

st.markdown('#hi')
st.markdown('##hi')
st.markdown('###hi')
st.markdown('####hi')

st.success('SUCCESS')
st.info('INFORMATION')
st.warning('! WARNING')
st.error('ERROR !n')
st.exception(ZeroDivisionError('Div not possible'))
st.help(ZeroDivisionError('not zero'))

st.write('1+2+3')
st.write(6)

st.code('x=10\n''for i in range(1,10)\n''print(i)\n')


st.checkbox('Male')
st.checkbox('Female')
if(st.checkbox('Adult')):
    st.write('You! are an adult!')


radioButton = st.radio('Select your Gender:',('Male','Female','Other'))
if(radioButton=='Male'):
  st.write('You! are Male')
elif(radioButton=='Female'):
  st.write('You! are Female')
else:
   st.write('You! are Other')


st.subheader('Select Box')
selectBox = st.selectbox('Data Science: ',['Machine Learning ','Computer Vision',
                             'Natural Language Processing','Data Analytics',
                             'Deep Learning'])
st.write('You have selected : ', selectBox )

##multiselectbox
st.subheader('Multiselectbox')
multiSelBox = st.multiselect('Data Science: ',['Machine Learning ','Computer Vision',
                             'Natural Language Processing','Data Analytics',
                             'Deep Learning'])
st.write('You have selected : ', multiSelBox)

st.subheader('BUTTON')
st.button('click me')

st.subheader('SLIDER')
vol=st.slider('Set your volume:',0,100,step=5)
st.write('volume :',vol)

st.subheader('INPUT FROM USER')
username = st.text_input('Enter your username: ')
password = st.text_input('Enter your password: ', type='password')

st.subheader('TEXT AREA')
textArea = st.text_area('write your bio in 20 words :',height =20)
st.write(textArea)

st.subheader('Input Number')
st.number_input('Select Your Age')

st.subheader('Input Date')
st.date_input('date')

st.subheader('Input Time')
st.time_input('Time')
