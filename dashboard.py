# -*- coding: utf-8 -*-
"""dashboard.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1VUemKM5SaId0sDlR13YsJTL0IYFLqJBJ
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st

tiantan_df = pd.read_csv("main_data.csv")

import streamlit as st

# Menempatkan teks di tengah menggunakan HTML
st.markdown("<h2 style='text-align: center;'>Tiantan Air Quality</h2>", unsafe_allow_html=True)


st.subheader('Polutan Udara Terbanyak')

pollutants = ['PM2.5', 'PM10', 'SO2', 'NO2', 'CO', 'O3']

pollutant_counts = tiantan_df[pollutants].mode().iloc[0]
plt.figure(figsize=(10, 4))
pollutant_counts.plot(kind='bar', color='hotpink')
plt.title('Polutan Udara Terbanyak Pada Daerah Tiantan')
plt.xlabel('Polutan Udara')
plt.ylabel('Frekuensi Muncul')
plt.xticks(rotation=35)
st.pyplot(plt)

st.subheader("Polutan Udara Harian dan Tahunan")

col1, col2 = st.columns(2)

with col1:
    tiantan_df['date'] = pd.to_datetime(tiantan_df[['year', 'month', 'day']])

    daily_data = tiantan_df.groupby('date').agg({'PM2.5': 'mean', 'PM10': 'mean', 'SO2': 'mean', 'NO2': 'mean', 'CO': 'mean', 'O3': 'mean'})
    plt.figure(figsize=(10, 8))
    for column in daily_data.columns:
      plt.plot(daily_data.index, daily_data[column], label=column)
    plt.title('Kualitas Udara Harian')
    plt.xlabel('Tanggal')
    plt.ylabel('Nilai Rata-Rata')
    plt.legend()
    st.pyplot(plt)


with col2:
    annual_data = tiantan_df.groupby('year').agg({'PM2.5': 'mean', 'PM10': 'mean', 'SO2': 'mean', 'NO2': 'mean', 'CO': 'mean', 'O3': 'mean'})

    # Visualisasi data tahunan
    plt.figure(figsize=(10, 8))
    for column in annual_data.columns:
      plt.plot(annual_data.index, annual_data[column], label=column)

    plt.title('Kualitas Udara Tahunan')
    plt.xlabel('Tahun')
    plt.ylabel('Nilai Rata-Rata')
    plt.legend()
    st.pyplot(plt)

st.caption('Copyright (c) Shinta 2023')