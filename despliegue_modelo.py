import streamlit as st
import pandas as pd



# Colocar titulo y logo de la empresa.
col_1, col_2 = st.columns(2)
with col_1:
    st.title('Modelo Clientes con mala practica transaccional')
with col_2:
    st.image('https://files.lafm.com.co/assets/public/2021-12/fallas_en_nequi_1_0.jpg?x.mrRrlrL9raOxVwkN2a2AN.sLsAf2zH')

st.markdown('# ')

left_column, right_column, left_column2,left_column3 = st.columns(4)

with left_column:
    Recency = st.text_input('Recency')
with right_column:
    Frecuency = st.text_input('Frecuency')
with left_column2:
    Monetary = st.text_input('Monetary')
with left_column3:
    top = st.selectbox('top', [0,1])


left_column, right_column, left_column2,left_column3 = st.columns(4)

with left_column:
    high = st.selectbox('high', [0,1])

with right_column:
    medium = st.selectbox('medium', [0,1])

with left_column2:
    low = st.selectbox('low', [0,1])

with left_column3:
    lost = st.selectbox('lost', [0,1])


data={'Recency':Recency,
      'Frequency':Frecuency,
      'Monetary':Monetary,
      '1.Top User':top,
      '2.High value User':high,
      '3.Medium Value User':medium,
      '4.Low Value User':low,
      '5.Lost User':lost}

features= pd.DataFrame(data,index=[0])

#if st.button("RUN"):
#    st.success(KNN.predict(features))
st.button("PREDECIR")