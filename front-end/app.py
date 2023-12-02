import streamlit as st
import requests

st.title('Sayı Toplama Uygulaması')
num1 = st.number_input('Birinci Sayı', min_value=0, max_value=100, value=0)
num2 = st.number_input('İkinci Sayı', min_value=0, max_value=100, value=0)

if st.button('Topla'):
    response = requests.post("http://backend:5000/add", json={"num1": num1, "num2": num2})
    if response.status_code == 200:
        result = response.json()['result']
        st.success(f"Sonuç: {result}")
    else:
        st.error("Bir hata oluştu.")
