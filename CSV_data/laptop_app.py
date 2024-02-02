import streamlit as st
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split

limited_df = pd.read_csv(r"CSV_data\clean_data.csv", encoding='latin-1')

x = limited_df.drop('Price_euros', axis=1).drop('Unnamed: 0', axis=1)
print(x.columns)
y = limited_df['Price_euros']

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.15, random_state=42)

scaler = StandardScaler()
x_train_scaled = scaler.fit_transform(x_train)
x_test_scaled = scaler.transform(x_test)

forest = RandomForestRegressor()
forest.fit(x_train_scaled, y_train)

st.title('Laptop Price Estimator')

st.sidebar.header('Input Laptop Specifications')
windows = st.sidebar.slider('Windows', 0, 1, 0)
linux = st.sidebar.slider('Linux', 0, 1, 0)
no_os = st.sidebar.slider('No OS', 0, 1, 0)
msi = st.sidebar.slider('MSI', 0, 1, 0)
amd_cpu = st.sidebar.slider('AMD CPU', 0, 1, 1)
intel_cpu = st.sidebar.slider('Intel CPU', 0, 1, 1)
intel_gpu = st.sidebar.slider('Intel GPU', 0, 1, 1)
amd_gpu = st.sidebar.slider('AMD GPU', 0, 1, 0)
acer = st.sidebar.slider('Acer', 0, 1, 0)
weight = st.sidebar.slider('Weight', 1.37, 1.83, 1.37)
razer = st.sidebar.slider('Razer', 0, 1, 0)
workstation = st.sidebar.slider('Workstation', 0, 1, 0)
ultrabook = st.sidebar.slider('Ultrabook', 0, 1, 0)
nvidia_gpu = st.sidebar.slider('Nvidia GPU', 0, 1, 0)
gaming = st.sidebar.slider('Gaming', 0, 1, 0)
cpu_frequency = st.sidebar.slider('CPU Frequency (GHz)', 1.8, 3.1, 2.3)
notebook = st.sidebar.slider('Notebook', 0, 1, 0)
screen_height = st.sidebar.slider('Screen Height (Pixels)', 900, 1800, 1600)
screen_width = st.sidebar.slider('Screen Width (Pixels)', 1440, 2880, 2560)
ram = st.sidebar.slider('Ram (GB)', 8, 16, 8)


user_input = pd.DataFrame({
    'Windows': [windows],
    'Linux': [linux],
    'No OS': [no_os],
    'MSI': [msi],
    'AMD CPU': [amd_cpu],
    'Intel CPU': [intel_cpu],
    'Intel GPU': [intel_gpu],
    'AMD GPU': [amd_gpu],
    'Acer': [acer],
    'Weight': [weight],
    'Razer': [razer],
    'Workstation': [workstation],
    'Ultrabook': [ultrabook],
    'Nvidia GPU': [nvidia_gpu],
    'Gaming': [gaming],
    'CPU Frequency': [cpu_frequency],
    'Notebook': [notebook],
    'Screen Height (Pixels)': [screen_height],
    'Screen Width (Pixels)': [screen_width],
    'Ram (GB)': [ram]
})

user_input.columns = x.columns

user_input_scaled = scaler.transform(user_input)

predicted_price = forest.predict(user_input_scaled)

st.write(f'Estimated Laptop Price: {predicted_price[0]:.2f} euros')

st.header('Categorization')
os_category = st.selectbox('Select OS Category', ['Windows', 'Linux', 'No OS'])

type_category = st.selectbox('Select Type Category', ['MSI', 'Acer', 'Razer', 'Other'])

company_category = st.selectbox('Select Company Category', ['AMD', 'Intel', 'Nvidia', 'Other'])

st.write(f'Selected OS Category: {os_category}')
st.write(f'Selected Type Category: {type_category}')
st.write(f'Selected Company Category: {company_category}')
