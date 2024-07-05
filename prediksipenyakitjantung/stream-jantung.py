import pickle 
import numpy as np 
import streamlit as st 

#load save model
model = pickle.load(open('penyakit_jantung.sav','rb'))
#judul web
st.title('Prediksi Penyakit Jantung')

col1, col2, col3 = st.columns(3)

with col1:
    age = st.text_input('Umur')
with col2:
    sex = st.text_input('Jenis Kelamin')
with col3:
    cp = st.text_input('Jenis Nyeri Dada')
with col1:
    trestbps = st.text_input('Tekanan Darah')
with col2:
    chol = st.text_input('Kandungan Kolestrol')
with col3:
    fbs = st.text_input('Gula Darah Puasa')
with col1:
    restecg = st.text_input('Hasil Elektrokardiografi')
with col2:
    thalach = st.text_input('Denyut Jantung Maksimal')
with col3:
    exang = st.text_input('Induksi Angina')
with col1:
    oldpeak = st.text_input('Tingkat Depresi')
with col2:
    slope = st.text_input('Grafik Klinis')
with col3:
    ca = st.text_input('Nilai CA')
with col1:
    thal = st.text_input('Nilai Thal')


#code for prediction
heart_diagnosis = ''

##membuat tombol prediksi
if st.button('Hasil Prediksi Penyakit Jantung'):
    inputs = [float(age), float(sex), float(cp), float(trestbps), float(chol), float(fbs),
              float(restecg), float(thalach), float(exang), float(oldpeak), float(slope),
              float(ca), float(thal)]
    heart_prediction = model.predict([inputs])
    
    if (heart_prediction[0] == 1):
        heart_diagnosis = 'Pasien Terkena Penyakit Jantung'
    else: 
        heart_diagnosis = 'Pasien Tidak Terkena Penyakit Jantung'
st.success(heart_diagnosis)
