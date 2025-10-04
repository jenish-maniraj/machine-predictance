import streamlit as st
import pandas as pd
import numpy as np
import joblib

# Load model and scaler once when app starts
model = joblib.load("model.pkl")
scaler = joblib.load("scaler.pkl")

# Prediction function
def predict_machine_from_12hr_csv(df):
    required_cols = [
        "vibration", "temperature", "usage_hours",
        "rpm", "load_percentage", "last_maintenance_days"
    ]

    if df.shape[0] != 12:
        return "❌ CSV must contain exactly 12 rows (one for each hour)."

    if not all(col in df.columns for col in required_cols):
        return f"❌ CSV is missing required columns: {required_cols}"

    X = df[required_cols]
    X_scaled = scaler.transform(X)
    preds = model.predict(X_scaled)
    failure_votes = np.sum(preds)

    if failure_votes >= 6:
        return f"⚠️ Machine Likely to Fail ({failure_votes}/12 hours abnormal)"
    else:
        return f"✅ Machine is Healthy ({12 - failure_votes}/12 hours normal)"

# Streamlit UI
st.set_page_config(page_title="Machine Health Predictor", layout="centered")
st.title("🛠️ Machine Health Prediction (12-hour Sensor Data)")
st.markdown("Upload a **CSV file** with 12 hourly records of machine data to determine if it's likely to fail.")

# Upload CSV
uploaded_file = st.file_uploader("📂 Upload CSV File", type=["csv"])

# Predict button
if uploaded_file is not None:
    try:
        df = pd.read_csv(uploaded_file)
        st.write("📋 **Data Preview:**")
        st.dataframe(df)

        if st.button("🔍 Predict Machine Health"):
            result = predict_machine_from_12hr_csv(df)
            if "❌" in result:
                st.error(result)
            elif "⚠️" in result:
                st.warning(result)
            else:
                st.success(result)

    except Exception as e:
        st.error(f"❌ Error reading file: {str(e)}")
