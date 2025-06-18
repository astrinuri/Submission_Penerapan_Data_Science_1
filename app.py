import streamlit as st
import pandas as pd
import joblib

# Load model
model = joblib.load("rf_model.joblib")

st.title("Prediksi Attrition Karyawan")

st.markdown("Masukkan informasi berikut untuk memprediksi apakah karyawan akan keluar atau tidak.")

# Form input
with st.form("prediction_form"):
    Age = st.slider("Umur", 18, 60, 30)
    DailyRate = st.number_input("Daily Rate", 100, 1500, 800)
    DistanceFromHome = st.number_input("Jarak dari rumah (km)", 1, 50, 5)
    HourlyRate = st.number_input("Hourly Rate", 10, 100, 50)
    MonthlyIncome = st.number_input("Pendapatan Bulanan", 1000, 50000, 5000)
    MonthlyRate = st.number_input("Monthly Rate", 1000, 30000, 10000)
    OverTime = st.selectbox("Lembur?", ["Yes", "No"])
    PercentSalaryHike = st.slider("Persentase Kenaikan Gaji", 0, 100, 15)
    TotalWorkingYears = st.slider("Total Tahun Bekerja", 0, 40, 10)
    YearsAtCompany = st.slider("Tahun di Perusahaan", 0, 40, 5)
    
    submitted = st.form_submit_button("Prediksi")

# Encoding lembur
def encode_overtime(val):
    return 1 if val == "Yes" else 0

if submitted:
    # Buat dataframe dari input
    input_data = pd.DataFrame([{
        "Age": Age,
        "DailyRate": DailyRate,
        "DistanceFromHome": DistanceFromHome,
        "HourlyRate": HourlyRate,
        "MonthlyIncome": MonthlyIncome,
        "MonthlyRate": MonthlyRate,
        "OverTime": encode_overtime(OverTime),
        "PercentSalaryHike": PercentSalaryHike,
        "TotalWorkingYears": TotalWorkingYears,
        "YearsAtCompany": YearsAtCompany
    }])

    # Prediksi
    prediction = model.predict(input_data)[0]
    proba = model.predict_proba(input_data)[0]

    if prediction == 1:
        st.error(f"Karyawan diprediksi AKAN keluar. (Probabilitas: {proba[1]:.2f})")
    else:
        st.success(f"Karyawan diprediksi TIDAK keluar. (Probabilitas: {proba[0]:.2f})")
