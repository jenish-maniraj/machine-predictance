# 🛠 Smart Predictive Maintenance System  

## 📌 Overview  
This project is a *Predictive Maintenance Machine Learning system* that analyzes machine sensor data and predicts whether a machine is *Healthy* or *Likely to Fail*.  

The system takes *12-hour sensor readings (CSV input)* from a machine, processes the data, and provides a clear status output.  

The goal is to help industries *reduce downtime, save costs, and improve safety* through early failure detection.  

---

## 🚀 Features  
- ✅ Simulates *realistic sensor data* (vibration, temperature, RPM, load, usage hours, maintenance days).  
- ✅ Uses a *Random Forest Classifier* for prediction.  
- ✅ CSV-based input for easy integration (no complex IoT setup needed).  
- ✅ Interactive *web interface* using *Streamlit / Gradio*.  
- ✅ Predicts based on *12 hours of machine history*, not just one reading.  
- ✅ Handles *noisy and edge-case sensor data*.  

---

## 🔁 Workflow  

1. *Data Simulation / Collection*  
   - Generate synthetic sensor data with realistic noise.  
   - Label machines as Healthy or Failure.  

2. *Preprocessing*  
   - Clean and scale data using StandardScaler.  
   - Train/Test split for evaluation.  

3. *Model Training*  
   - Train Random Forest Classifier.  
   - Save model (model.pkl) and scaler (scaler.pkl) using joblib.  

4. *Prediction*  
   - Input: 12-hour CSV file of machine readings.  
   - Output:  
     - ✅ Healthy if majority readings are normal.  
     - ⚠ Likely to Fail if too many abnormal readings.  

5. *Deployment*  
   - Web interface built using *Streamlit* or *Gradio*.  
   - Can be deployed on Hugging Face Spaces or Streamlit Cloud.  

---

## 📊 Dataset  
- *Synthetic dataset*: 10,000+ samples generated with Gaussian noise.  
- *Features*:  
  - Vibration  
  - Temperature  
  - Usage Hours  
  - RPM  
  - Load Percentage  
  - Last Maintenance Days  
- *Target*: status → 0 = Healthy, 1 = Failure  

---

## ⚙ Tech Stack  
- *Language*: Python  
- *ML Library*: scikit-learn (Random Forest Classifier)  
- *Data Processing*: pandas, numpy  
- *Visualization*: matplotlib, seaborn  
- *Deployment*: Streamlit / Gradio  
- *Model Persistence*: joblib

## Demo link : https://machine-predictance-ske9ewbouksptpblwhgemd.streamlit.app/
## Demo Datasets : https://drive.google.com/drive/folders/1n14DnhtDcoPOOCuOInoZIEPkM6MHARaj?usp=drive_link

---

Authors:
- Jenish Maniraj J C


