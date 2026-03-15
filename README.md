# 💻 Laptop Price Prediction (End-to-End Machine Learning Project)

An **end-to-end Machine Learning project** that predicts laptop prices based on hardware specifications such as processor, RAM, GPU, storage, screen size, and other features.

The project covers the **complete ML lifecycle**:
Data Preprocessing → Feature Engineering → Model Training → Model Evaluation → Deployment using **Streamlit**.

The model was trained on a **large dataset of 100,000 laptop records**, enabling accurate price prediction across multiple brands and configurations.

---

# 🚀 Project Overview

Laptop prices vary significantly depending on hardware configuration and brand.

This project builds a **Machine Learning model that estimates laptop prices automatically** based on user-selected specifications.

Users can enter laptop details through an interactive web interface and receive an **instant predicted price**.

---

# 📊 Dataset

- **Total Records:** 100,000 laptops
- **Features:** 18 hardware specifications
- **Target Variable:** Laptop Price

### Key Features Used

| Feature | Description |
|------|------|
| Brand | Laptop manufacturer |
| Processor Brand | Intel / AMD / Apple |
| Processor Name | i3, i5, i7, Ryzen, M1 etc |
| RAM | RAM size in GB |
| Storage | Storage capacity |
| Storage Type | SSD / NVMe / HDD |
| GPU | Graphics processor |
| Screen Size | Display size in inches |
| Resolution | Screen resolution |
| Battery Life | Battery backup |
| Weight | Laptop weight |
| OS | Operating system |
| Touchscreen | Touchscreen availability |
| Backlit Keyboard | Keyboard lighting |
| USB Ports | Number of ports |
| Usage Type | Gaming / Business / Student |
| Warranty | Warranty duration |

---

# ⚙️ Machine Learning Pipeline

The project follows a **production-style ML pipeline**.

### 1️⃣ Data Preprocessing
- Handling missing values
- Encoding categorical variables
- Data cleaning and formatting

### 2️⃣ Feature Engineering
- Resolution split into width and height
- Binary encoding for boolean features
- Feature transformation using pipelines

### 3️⃣ Model Training

Several machine learning models were tested:

- Linear Regression
- Decision Tree
- Random Forest
- Gradient Boosting

### 4️⃣ Model Selection

**Linear Regression performed best on this dataset.**

| Metric | Score |
|------|------|
| R² Score | 0.91 |
| MAE | Low error |
| RMSE | Acceptable variance |

---

# 🖥️ Web Application

The trained model is deployed using **Streamlit**.

Users can configure laptop specifications and instantly receive a predicted price.

### Features

✔ Interactive UI  
✔ Real-time predictions  
✔ User-friendly laptop configuration  
✔ Instant price estimation  

---

# 🛠 Tech Stack

### Programming Language
- Python

### Libraries
- Pandas
- NumPy
- Scikit-learn
- Joblib

### Deployment
- Streamlit

---
