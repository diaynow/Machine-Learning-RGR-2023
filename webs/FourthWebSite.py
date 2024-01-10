import streamlit as st
import pickle
import pandas as pd
import numpy as np
import keras



def OutputPrediction(predict):
    if predict == 1:
        st.write("Транзакция является мошеннической.")
    else:
        st.write("Транзакция не является мошеннической.")


def ModelPrediction(type_model, data):
    if type_model == "Обучение с учителем":
        st.subheader("KNN:")
        with open("models/KNN.pickle", "rb") as file:
            knn = pickle.load(file)
        knn_pred = knn.predict(data)[0]
        OutputPrediction(knn_pred)

        st.subheader("Logistic Regression:")
        with open("models/LG.pickle", "rb") as file:
            lg = pickle.load(file)
        lg_pred = lg.predict(data)[0]
        OutputPrediction(lg_pred)

        st.subheader("SVM:")
        with open("models/SVM.pickle", "rb") as file:
            svc = pickle.load(file)
        svc_pred = svc.predict(data)[0]
        OutputPrediction(svc_pred)
    elif type_model == "Обучение без учителя":
        st.subheader("KMeans:")
        with open("models/Kmeans.pickle", "rb") as file:
            kmeans = pickle.load(file)
        kmeans_pred = kmeans.predict(data)[0]
        st.write(kmeans_pred)
    elif type_model == "Ансабль":
        st.subheader("Bagging:")
        with open("models/Bagging.pickle", "rb") as file:
            Bagging = pickle.load(file)
        Bagging_pred = Bagging.predict(data)[0]
        OutputPrediction(Bagging_pred)

        st.subheader("Stacking:")
        with open("models/Stacking.pickle", "rb") as file:
            Stacking = pickle.load(file)
        Stacking_pred = Stacking.predict(data)[0]
        OutputPrediction(Stacking_pred)

        st.subheader("GradientBoosting:")
        with open("models/GradientBoosting.pickle", "rb") as file:
            Gradient = pickle.load(file)
        Gradient_pred = Gradient.predict(data)[0]
        OutputPrediction(Gradient_pred)
    else:
        st.subheader("NN:")
        model_loaded = keras.models.load_model("models/NN.h5")
        NN_pred = np.around(model_loaded.predict(data)[0][0])
        OutputPrediction(NN_pred)


uploadedFile = st.file_uploader("Выберите файл датасет в формате .csv", type="csv")

if uploadedFile is not None:
    data = pd.read_csv(uploadedFile)

    st.header("Предсказание была ли транзакция мошеннической:")

    st.subheader("Введите данные для предсказания:")

    distance_from_home = st.slider(
        "distance_from_home", max_value=58.542735, min_value=0.004874
    )
    distance_from_last_transaction = st.slider(
        "distance_from_last_transaction", max_value=7.944274, min_value=0.000118
    )
    ratio_to_median_purchase_price = st.slider(
        "ratio_to_median_purchase_price", max_value=4.527271, min_value=0.004399
    )
    repeat_retailer = st.select_slider("repeat_retailer", [0, 1])
    used_chip = st.select_slider("used_chip", [0, 1])
    used_pin_number = st.select_slider("used_pin_number", [0, 1])
    online_order = st.select_slider("online_order", [0, 1])

    data = pd.DataFrame(
        {
            "distance_from_home": [distance_from_home],
            "distance_from_last_transaction": [distance_from_last_transaction],
            "ratio_to_median_purchase_price": [ratio_to_median_purchase_price],
            "repeat_retailer": [repeat_retailer],
            "used_chip": [used_chip],
            "used_pin_number": [used_pin_number],
            "online_order": [online_order],
        }
    )

    st.write(data)

    type_model = st.selectbox(
        "Выберите тип модели",
        ["Обучение с учителем", "Обучение без учителя", "Ансабль", "Нейросеть"],
    )

    button_start = st.button("Предсказать")

    if button_start:
        ModelPrediction(type_model, data)
