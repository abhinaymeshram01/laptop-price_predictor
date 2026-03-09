import streamlit as st
import pandas as pd
import joblib

st.set_page_config(page_title="Laptop Price Predictor", page_icon="💻", layout="centered")

st.markdown("""
<style>
/* ── Base ── */
body, [class*="css"] { font-family: 'Trebuchet MS', sans-serif; background: #0a0a0f; color: #e8e6f0; }
#MainMenu, footer, header { visibility: hidden; }
.block-container { padding: 2.5rem 2.5rem 4rem; max-width: 880px; }

/* ── Background glow ── */
.stApp { background: radial-gradient(ellipse 70% 40% at 15% 5%, rgba(99,60,255,0.12) 0%, transparent 60%),
                      radial-gradient(ellipse 50% 40% at 85% 90%, rgba(0,210,180,0.07) 0%, transparent 55%),
                      #0a0a0f; }

/* ── Title ── */
h1 { font-size: 2.2rem; font-weight: 800; letter-spacing: -0.03em; color: #f0eeff;
     border-bottom: 1px solid rgba(255,255,255,0.07); padding-bottom: 1rem; margin-bottom: 0.5rem; }

/* ── Divider ── */
hr { border-color: rgba(255,255,255,0.06); margin: 1rem 0; }

/* ── Section labels ── */
.section {
  font-family: monospace; font-size: 10px; font-weight: 700;
  letter-spacing: 0.28em; text-transform: uppercase;
  color: #00d2b4; margin: 1.8rem 0 0.8rem;
  display: flex; align-items: center; gap: 8px; }
.section::after { content: ''; flex: 1; height: 1px; background: rgba(0,210,180,0.15); }

/* ── Widget labels ── */
label[data-testid="stWidgetLabel"] p {
  font-family: monospace !important; font-size: 10px !important;
  letter-spacing: 0.14em !important; text-transform: uppercase !important;
  color: rgba(232,230,240,0.4) !important; margin-bottom: 4px; }

/* ── Selectbox ── */
div[data-baseweb="select"] > div {
  background: rgba(255,255,255,0.03) !important;
  border: 1px solid rgba(255,255,255,0.09) !important;
  border-radius: 10px !important; color: #e8e6f0 !important;
  font-size: 14px !important; font-weight: 500 !important;
  transition: border-color 0.2s; }
div[data-baseweb="select"] > div:hover { border-color: rgba(99,60,255,0.55) !important; }
div[data-baseweb="select"] svg { fill: rgba(232,230,240,0.4); }

/* ── Dropdown menu ── */
div[data-baseweb="popover"] { background: #1a1a24 !important; border: 1px solid rgba(255,255,255,0.1) !important; border-radius: 10px !important; }
li[role="option"] { background: transparent !important; color: #e8e6f0 !important; }
li[role="option"]:hover { background: rgba(99,60,255,0.2) !important; }
li[role="option"][aria-selected="true"] { background: rgba(99,60,255,0.3) !important; color: #fff !important; }

/* ── Slider track ── */
div[data-testid="stSlider"] > div > div { background: rgba(255,255,255,0.06) !important; border-radius: 4px; }
div[data-testid="stSlider"] > div > div > div:first-child { background: linear-gradient(90deg, #633cff, #00d2b4) !important; border-radius: 4px; }
div[data-testid="stSlider"] [role="slider"] { background: #fff !important; border: 3px solid #633cff !important; box-shadow: 0 0 10px rgba(99,60,255,0.5); width: 18px !important; height: 18px !important; }
div[data-testid="stSlider"] p { color: rgba(232,230,240,0.5) !important; font-size: 12px !important; }

/* ── Number badge on slider ── */
div[data-testid="stSlider"] [data-testid="stTickBarMin"],
div[data-testid="stSlider"] [data-testid="stTickBarMax"] { color: rgba(232,230,240,0.25) !important; font-size: 10px !important; }

/* ── Button ── */
div[data-testid="stButton"] > button {
  width: 100%; background: linear-gradient(135deg, #633cff 0%, #4f2ee8 100%);
  color: #fff; border: none; border-radius: 12px; padding: 15px 0;
  font-size: 15px; font-weight: 800; letter-spacing: 0.1em;
  text-transform: uppercase; box-shadow: 0 0 28px rgba(99,60,255,0.35);
  margin-top: 0.8rem; transition: all 0.2s; }
div[data-testid="stButton"] > button:hover {
  box-shadow: 0 0 48px rgba(99,60,255,0.65);
  transform: translateY(-1px); }
div[data-testid="stButton"] > button:active { transform: translateY(0); }

/* ── Success result box ── */
div[data-testid="stAlert"] {
  background: linear-gradient(135deg, rgba(99,60,255,0.15), rgba(0,210,180,0.08)) !important;
  border: 1px solid rgba(99,60,255,0.4) !important; border-radius: 14px !important;
  font-size: 26px !important; font-weight: 800 !important;
  text-align: center; color: #f0eeff !important; padding: 1.4rem !important;
  box-shadow: 0 0 32px rgba(99,60,255,0.15); }

/* ── Column gap ── */
[data-testid="stHorizontalBlock"] { gap: 1.2rem; }

/* ── Input container cards ── */
div[data-testid="stVerticalBlock"] > div[data-testid="stHorizontalBlock"] > div {
  background: rgba(255,255,255,0.02);
  border: 1px solid rgba(255,255,255,0.05);
  border-radius: 12px; padding: 12px 14px; }
</style>
""", unsafe_allow_html=True)

@st.cache_resource
def load_model():
    return joblib.load("laptop_price_model.pkl")

model = load_model()

st.title("💻 Laptop Price Predictor")

# ── Identity ──────────────────────────────────────────────────────────────────
st.markdown('<div class="section">01 — Identity</div>', unsafe_allow_html=True)
c1, c2 = st.columns(2)
with c1: brand           = st.selectbox("Brand",            ["Acer","Apple","Asus","Dell","HP","Lenovo","MSI","Razer","Samsung","Toshiba"])
with c2: os              = st.selectbox("Operating System",  ["Windows 11","Windows 10","macOS","Linux","Chrome OS"])

c3, c4 = st.columns(2)
with c3: processor_brand = st.selectbox("Processor Brand",  ["AMD","Apple","Intel","Qualcomm"])
with c4: processor_name  = st.selectbox("Processor",        ["Core i3","Core i5","Core i7","Core i9","Ryzen 3","Ryzen 5","Ryzen 7","Ryzen 9","M1","M1 Pro","M2","M2 Pro","M3"])

# ── Performance ───────────────────────────────────────────────────────────────
st.markdown('<div class="section">02 — Performance</div>', unsafe_allow_html=True)
c5, c6 = st.columns(2)
with c5: ram_gb       = st.selectbox("RAM (GB)",      [4, 8, 16, 32, 64])
with c6: gpu          = st.selectbox("GPU",           ["Integrated","Intel Iris Xe","AMD Radeon","Apple GPU","NVIDIA RTX 3050","NVIDIA RTX 3060","NVIDIA RTX 4060","NVIDIA RTX 4070"])

c7, c8 = st.columns(2)
with c7: storage_gb   = st.selectbox("Storage (GB)",  [128, 256, 512, 1024, 2048])
with c8: storage_type = st.selectbox("Storage Type",  ["SSD","NVMe SSD","HDD","eMMC"])

# ── Physical ──────────────────────────────────────────────────────────────────
st.markdown('<div class="section">03 — Physical</div>', unsafe_allow_html=True)
c9, c10 = st.columns(2)
with c9:  screen_size  = st.slider("Screen Size (inches)", 11.0, 18.0, 15.6, 0.1)
with c10: weight_kg    = st.slider("Weight (kg)",           0.8,  4.5,  2.0, 0.1)

c11, c12 = st.columns(2)
with c11: battery_life = st.slider("Battery Life (hours)",  3.0, 20.0,  8.0, 0.5)
with c12: resolution   = st.selectbox("Resolution",        ["1920x1080","2560x1440","2560x1600","3840x2160","1366x768"])

# ── Extras ────────────────────────────────────────────────────────────────────
st.markdown('<div class="section">04 — Extras</div>', unsafe_allow_html=True)
c13, c14 = st.columns(2)
with c13: touchscreen      = st.selectbox("Touchscreen",      ["No","Yes"])
with c14: backlit_keyboard = st.selectbox("Backlit Keyboard", ["Yes","No"])

c15, c16 = st.columns(2)
with c15: num_usb_ports    = st.selectbox("USB Ports",        [1, 2, 3, 4, 5])
with c16: usage_type       = st.selectbox("Usage Type",       ["Business","Gaming","Student","Workstation","Casual"])

c17, _ = st.columns(2)
with c17: warranty_years   = st.selectbox("Warranty (Years)", [1, 2, 3])

st.divider()

if st.button("⚡ Predict Price", use_container_width=True, type="primary"):
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
    st.success(f"💰  Estimated Price  ·  ₹{price:,.0f}")
