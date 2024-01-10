import streamlit as st
from PIL import Image


st.title("Информация об авторе")

st.header('Эксперт Диана Дмитриевна, ФИТ-221.')
st.subheader(
    "Тема: «Разработка Web-приложения (дашборда) для инференса (вывода) моделей ML и анализа данных»"
)

st.image(
    Image.open("photo.jpeg"),
    width=450,
)