import streamlit as st
import pandas as pd
import joblib

st.set_page_config(page_title="Laptop Price Predictor", page_icon="💻", layout="centered")

st.markdown("""
<style>
body, [class*="css"] { font-family: 'Trebuchet MS', sans-serif; background: #0f0f13; color: #e8e6f0; }
#MainMenu, footer, header { visibility: hidden; }
.block-container { padding: 2rem 2rem 3rem; max-width: 760px; }
h1 { font-size: 2rem; font-weight: 800; letter-spacing: -0.03em; color: #f0eeff; }
hr { border-color: rgba(255,255,255,0.08); }
label[data-testid="stWidgetLabel"] p { font-family: monospace; font-size: 11px; letter-spacing: 0.12em; text-transform: uppercase; color: rgba(232,230,240,0.5); }
div[data-baseweb="select"] > div { background: rgba(255,255,255,0.04); border: 1px solid rgba(255,255,255,0.10); border-radius: 8px; color: #e8e6f0; font-size: 14px; }
div[data-baseweb="select"] > div:hover { border-color: rgba(99,60,255,0.5); }
div[data-testid="stSlider"] [role="slider"] { background: #633cff; border: 2px solid #a78bfa; }
div[data-testid="stButton"] > button { width: 100%; background: linear-gradient(135deg, #633cff, #4f2ee8); color: #fff; border: none; border-radius: 10px; padding: 14px 0; font-size: 15px; font-weight: 700; letter-spacing: 0.05em; text-transform: uppercase; box-shadow: 0 0 24px rgba(99,60,255,0.3); }
div[data-testid="stButton"] > button:hover { box-shadow: 0 0 40px rgba(99,60,255,0.55); }
div[data-testid="stAlert"] { background: rgba(99,60,255,0.12); border: 1px solid rgba(99,60,255,0.35); border-radius: 12px; font-size: 22px; font-weight: 700; text-align: center; color: #f0eeff; }
</style>
""", unsafe_allow_html=True)

@st.cache_resource
def load_model():
    return joblib.load("laptop_price_model.pkl")

model = load_model()

st.title("💻 Laptop Price Predictor")
st.divider()

brand            = st.selectbox("Brand",            ["Acer","Apple","Asus","Dell","HP","Lenovo","MSI","Razer","Samsung","Toshiba"])
processor_brand  = st.selectbox("Processor Brand",  ["AMD","Apple","Intel","Qualcomm"])
processor_name   = st.selectbox("Processor",        ["Core i3","Core i5","Core i7","Core i9","Ryzen 3","Ryzen 5","Ryzen 7","Ryzen 9","M1","M1 Pro","M2","M2 Pro","M3"])
ram_gb           = st.selectbox("RAM (GB)",         [4, 8, 16, 32, 64])
storage_gb       = st.selectbox("Storage (GB)",     [128, 256, 512, 1024, 2048])
storage_type     = st.selectbox("Storage Type",     ["SSD","NVMe SSD","HDD","eMMC"])
gpu              = st.selectbox("GPU",              ["Integrated","Intel Iris Xe","AMD Radeon","Apple GPU","NVIDIA RTX 3050","NVIDIA RTX 3060","NVIDIA RTX 4060","NVIDIA RTX 4070"])
os               = st.selectbox("Operating System", ["Windows 11","Windows 10","macOS","Linux","Chrome OS"])
usage_type       = st.selectbox("Usage Type",       ["Business","Gaming","Student","Workstation","Casual"])
resolution       = st.selectbox("Resolution",       ["1920x1080","2560x1440","2560x1600","3840x2160","1366x768"])
touchscreen      = st.selectbox("Touchscreen",      ["No","Yes"])
backlit_keyboard = st.selectbox("Backlit Keyboard", ["Yes","No"])
num_usb_ports    = st.selectbox("USB Ports",        [1, 2, 3, 4, 5])
warranty_years   = st.selectbox("Warranty (Years)", [1, 2, 3])
screen_size      = st.slider("Screen Size (inches)", 11.0, 18.0, 15.6, 0.1)
battery_life     = st.slider("Battery Life (hours)",  3.0, 20.0,  8.0, 0.5)
weight_kg        = st.slider("Weight (kg)",           0.8,  4.5,  2.0, 0.1)

st.divider()

if st.button("Predict Price", use_container_width=True, type="primary"):
    res_w, res_h = resolution.split("x")
    input_df = pd.DataFrame([{
        "brand": brand, "processor_brand": processor_brand,
        "processor_name": processor_name, "ram_gb": ram_gb,
        "storage_gb": storage_gb, "storage_type": storage_type,
        "gpu": gpu, "screen_size_inch": screen_size, "os": os,
        "battery_life_hrs": battery_life, "weight_kg": weight_kg,
        "touchscreen": 1 if touchscreen == "Yes" else 0,
        "backlit_keyboard": 1 if backlit_keyboard == "Yes" else 0,
        "num_usb_ports": num_usb_ports, "warranty_years": warranty_years,
        "usage_type": usage_type,
        "resolution_width": int(res_w), "resolution_height": int(res_h),
    }])
    price = max(model.predict(input_df)[0], 5000)
    st.success(f"Estimated Price: ₹{price:,.0f}")
