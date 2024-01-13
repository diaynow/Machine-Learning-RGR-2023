import streamlit as st
from PIL import Image
from st_pages import Page, show_pages

show_pages(
    [
        Page("webs/FirstWebSite.py", "Об авторе"),
        Page("webs/SecondWebSite.py", "О датасете"),
        Page("webs/ThirdWebSite.py", "Визуализация датасета"),
        Page("webs/FourthWebSite.py", "Предсказание модели"),
    ]
)

st.title('Расчетно-графическая работа по дисциплине "Машинное обучение"')
st.header("Датасет с мошенническими транзакциями")

st.image(
    Image.open("photo_main.jpeg"),
    width=450,
)
