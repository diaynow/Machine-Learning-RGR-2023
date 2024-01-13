import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import streamlit as st


data = pd.read_csv("card_transdata.csv")

st.title("Визуализация")

st.header("Гистограмма")
columns = ["distance_from_home", "distance_from_last_transaction"]
for column in columns:
    plt.figure(figsize=(8, 6))
    sns.histplot(data[column], bins=100, kde=True)
    plt.title(f"Гистограмма для {column}")
    st.pyplot(plt)

st.header("Ящик с усами")
df_num = data.select_dtypes(include=np.number)
plt.figure(figsize=(20, 10))
for i, column in enumerate(df_num.columns):
    plt.subplot(3, 8, i + 1)
    sns.boxplot(data=df_num, y=column)
    plt.title(column)
plt.tight_layout()
st.pyplot(plt)

st.header("Круговая диаграмма")
plt.figure(figsize=(8, 8))
data["fraud"].value_counts().plot.pie(autopct="%1.1f%%")
plt.title("Fraud")
st.pyplot(plt)

st.header("Тепловая карта")
df_num = data.select_dtypes(include=np.number)
df_corr = df_num.corr()
plt.figure(figsize=(16, 6))
sns.heatmap(df_corr, annot=True)
st.pyplot(plt)
