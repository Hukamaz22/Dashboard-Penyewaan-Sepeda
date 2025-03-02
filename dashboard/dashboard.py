import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sns.set(style='darkgrid')

st.title('Dashboard Penyewaan Sepeda 🚴‍♂️')

df = pd.read_csv('dashboard/main_data.csv')

st.sidebar.header('Filter Data')
selected_season = st.sidebar.selectbox('Pilih Musim:', ['1', '2', '3', '4'], format_func=lambda x: {
    '1': 'Musim Semi',
    '2': 'Musim Panas',
    '3': 'Musim Gugur',
    '4': 'Musim Dingin'
}.get(x))

filtered_data = df[df['season'] == int(selected_season)]

st.subheader('Jumlah Penyewaan Sepeda per Musim')
fig, ax = plt.subplots()
sns.barplot(x='season', y='cnt', data=df, palette='coolwarm', errorbar=None, ax=ax)
ax.set_xticklabels(['Musim Semi', 'Musim Panas', 'Musim Gugur', 'Musim Dingin'])
st.pyplot(fig)

season_colors = {
    '1': '#2E8B57',  
    '2': '#FFD700',  
    '3': '#FF8C00',  
    '4': '#4682B4'   
}

st.subheader('Hubungan antara Suhu dan Penyewaan Sepeda')
fig, ax = plt.subplots()
sns.scatterplot(x='temp', y='cnt', data=filtered_data, color=season_colors[selected_season], ax=ax)
plt.xlabel('Suhu')
plt.ylabel('Jumlah Penyewaan')
st.pyplot(fig)

insight_text = {
    '1': "Pada **Musim Semi**, jumlah penyewaan cukup stabil, tetapi belum setinggi Musim Panas.",
    '2': "Pada **Musim Panas**, jumlah penyewaan sepeda mencapai puncaknya karena cuaca yang lebih mendukung aktivitas luar ruangan.",
    '3': "Pada **Musim Gugur**, jumlah penyewaan mulai menurun seiring dengan penurunan suhu.",
    '4': "Pada **Musim Dingin**, jumlah penyewaan paling sedikit karena kondisi cuaca yang kurang mendukung."
}

st.markdown(f"### 📊 Insight Musim yang Dipilih: {insight_text[selected_season]}")

st.caption('Copyright © Hukamaz Riwanda 2025')
