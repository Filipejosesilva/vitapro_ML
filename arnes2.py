# -*- coding: utf-8 -*-
"""
Created on Mon Dec  5 11:14:29 2022

@author: JSilva
"""

import streamlit as st
import joblib
import numpy as np

model_filename = 'perros.pkl'
loaded_model = joblib.load(model_filename)
print("Modelo Cargado")


st.title('Compra de Arneses y Botas para perros')
st.header("Tienda RED")
st.subheader("Ingrese los datos de su perro")

with st.form(key='diabetes-pred-form'):
    col1, col2 = st.columns(2)
    
    arnes = col1.slider(label='Tamaño del arnés:', min_value=0, max_value=100)
    botas = col2.text_input(label='Tamaño de la Bota:', value = 0)
    submit = st.form_submit_button(label='Check')
    
    arnes = int(arnes)
    inputs = np.array(arnes).reshape(-1, 1)
    predicted_boot_size = loaded_model.predict(inputs)[0]
    #st.write("El modelo estima un tamaño de bota: ",round(predicted_boot_size))
    predicted_boot_size = round(predicted_boot_size)
    
    if int(botas) == predicted_boot_size:
        st.info("La bota es ideal")
    elif int(botas) < predicted_boot_size:
        st.info("La bota es muy pequeña")
    else:
        st.info("La bota es muy grande")
        