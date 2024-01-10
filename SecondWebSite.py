import streamlit as st

st.title("Информация о наборе данных")

st.markdown(
    "[Credit Card Fraud](https://www.kaggle.com/datasets/dhanushnarayananr/credit-card-fraud)"
)

st.write("Выбранный мной набор данных содержит информацию о мошенничестве с кридитными картами")

st.header("Описание признаков:")

st.write("1. distance_from_home - расстояние от дома, где произошла транзакция")
st.write("2. distance_from_last_transaction - расстояние от места совершения последней транзакции")
st.write("3. ratio_to_median_purchase_price - отношение стоимости совершенной сделки к медиане покупной цене")
st.write("4. repeat_retailer - транзакция произошла от того же розничного продавца (0,1)")
st.write("5. used_chip - транзакция через чип (кредитную карту) (0,1)")
st.write("6. used_pin_number - транзакция произошла с использованием PIN-кода (0,1)")
st.write("7. online_order - транзакция является онлайн-заказом (0,1)")
st.write("8. fraud - является ли транзакция мошеннической (0,1)")

st.header("Особенности предобработки:")

st.write("1. Дубликаты и пропущенные значения отсуствуют")
st.write("2. Переведены в целочисленный тип данных следующие признаки: fraud, online_order, used_pin_number, used_chip, repeat_retailer")
st.write("3. Удалены выбросы для признаков: distance_from_home, distance_from_last_transaction, ratio_to_median_purchase_price")
st.write("4. Перед обучением устранен дисбаланс классов")
