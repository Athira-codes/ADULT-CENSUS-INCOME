import streamlit as st
import pickle
from PIL import Image
import time


def app():
    st.title(":blue[Adult income prediction]")
    agree = st.checkbox('I agree the terms and conditions of this app')
    if agree:
      image=Image.open("cash.gif")
      st.image(image,width=800)
      key1 = st.slider('age', 0, 100, 5)
      edu_num =st.number_input("years of education",value=None)
      ma= st.selectbox(
          "marital.status",
          ('Married-civ-spouse', 'Divorced', 'Never-married', 'Separated', 'Widowed', 'Married-spouse-absent', 'Married-AF-spouse'),
         index=None,
          placeholder="Select your marital status...",
      )
      st.write(':red[You selected:]', ma)
      if (ma=='Divorced'):
         ma=0
      elif(ma=='Married-AF-spouse'):
          ma=1
      elif(ma=='Married-civ-spouse'):
          ma = 2
      elif(ma=='Married-spouse-absent'):
          ma=3
      elif(ma=='Never-married'):
          ma=4
      elif(ma=='Separated'):
          ma=5
      elif(ma=='Widowed'):
          ma=6
      rel = st.selectbox(
          "relationship",
          ('Not-in-family', 'Unmarried', 'Own-child', 'Other-relative','Husband', 'Wife'),
          index=None,
          placeholder="Select your relaionship status...",
      )
      if (rel=='Husband'):
         rel=0
      elif (rel == 'Not-in-family'):
         rel = 1
      elif(rel=='Other-relative'):
          rel= 2
      elif(rel=='Own-child'):
          rel= 3
      elif(rel=='Unmarried'):
          rel=4
      elif(rel=='Wife'):
          rel=5
      gender=st.radio('sex',['Male','Female'])
      if gender=='Male':
          sex=1
      else:
          sex=0
      cap= st.text_input('capital gain', 'type here')
      loss=st.text_input('capital loss','Type here')
      work=st.text_input('hours per week','Type here')
      features=[key1,edu_num,ma,rel,sex,cap,loss,work]
      model=pickle.load(open('model3.sav','rb'))
      scaler=pickle.load(open('scaler4.sav','rb'))
      pred=st.button(':green[CHECK INCOME]')
      if pred:

          progress_text = "Operation in progress. Please wait."
          my_bar = st.progress(0, text=progress_text)

          for percent_complete in range(100):
              time.sleep(0.01)
              my_bar.progress(percent_complete + 1, text=progress_text)
          time.sleep(1)
          my_bar.empty()
          st.button("RERUN")
          prediction=model.predict(scaler.transform([features]))
          if prediction == 0:
              st.write("**:blue[income is less than or equal to 50k :dollar:]**")
              time.sleep(4)
          else:
              st.write("**:blue[income is greater than 50k :dollar:]**")
              time.sleep(4)
