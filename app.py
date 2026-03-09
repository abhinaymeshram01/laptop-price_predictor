import streamlit as st
import pandas as pd
import joblib

st.set_page_config(page_title="Laptop Price Predictor", page_icon="💻", layout="centered")

st.markdown("""
<style>
/* ── Base ── */
body, [class*="css"] { font-family: 'Trebuchet MS', sans-serif; background: #07070d; color: #e8e6f0; }
#MainMenu, footer, header { visibility: hidden; }
.block-container { padding: 3rem 3rem 5rem; max-width: 900px; }

/* ── Background ── */
.stApp {
  background:
    radial-gradient(ellipse 60% 35% at 10% 0%, rgba(99,60,255,0.18) 0%, transparent 60%),
    radial-gradient(ellipse 45% 35% at 90% 100%, rgba(0,210,180,0.10) 0%, transparent 55%),
    radial-gradient(ellipse 30% 30% at 50% 50%, rgba(255,60,120,0.04) 0%, transparent 60%),
    #07070d; }

/* ── Header ── */
.app-header { margin-bottom: 2.5rem; }
.app-tag { font-family: monospace; font-size: 11px; letter-spacing: 0.28em;
  text-transform: uppercase; color: #00d2b4; margin-bottom: 10px; }
.app-title { font-size: 2.8rem; font-weight: 800; letter-spacing: -0.04em;
  color: #f0eeff; line-height: 1; margin: 0; }
.app-title span { background: linear-gradient(90deg, #633cff, #00d2b4);
  -webkit-background-clip: text; -webkit-text-fill-color: transparent; background-clip: text; }
.app-sub { font-size: 14px; color: rgba(232,230,240,0.4); margin-top: 10px; }

/* ── Divider ── */
hr { border-color: rgba(255,255,255,0.05); margin: 0.8rem 0; }

/* ── Section labels ── */
.section {
  font-family: monospace; font-size: 9px; font-weight: 700;
  letter-spacing: 0.3em; text-transform: uppercase; color: #633cff;
  margin: 2rem 0 1rem; display: flex; align-items: center; gap: 10px; }
.section::after { content: ''; flex: 1; height: 1px; background: rgba(99,60,255,0.2); }

/* ── Widget labels ── */
label[data-testid="stWidgetLabel"] p {
  font-family: monospace !important; font-size: 10px !important;
  letter-spacing: 0.15em !important; text-transform: uppercase !important;
  color: rgba(232,230,240,0.35) !important; }

/* ── Selectbox ── */
div[data-baseweb="select"] > div {
  background: rgba(255,255,255,0.025) !important;
  border: 1px solid rgba(255,255,255,0.08) !important;
  border-radius: 12px !important; color: #e8e6f0 !important;
  font-size: 14px !important; font-weight: 500 !important;
  transition: all 0.2s !important; }
div[data-baseweb="select"] > div:hover {
  border-color: rgba(99,60,255,0.6) !important;
  background: rgba(99,60,255,0.05) !important; }
div[data-baseweb="select"] svg { fill: rgba(232,230,240,0.3); }

/* ── Dropdown menu ── */
div[data-baseweb="popover"] {
  background: #13131e !important;
  border: 1px solid rgba(99,60,255,0.25) !important;
  border-radius: 12px !important;
  box-shadow: 0 20px 60px rgba(0,0,0,0.6) !important; }
li[role="option"] { color: #e8e6f0 !important; border-radius: 8px !important; margin: 2px 6px !important; }
li[role="option"]:hover { background: rgba(99,60,255,0.2) !important; }
li[role="option"][aria-selected="true"] { background: rgba(99,60,255,0.35) !important; color: #fff !important; }

/* ── Slider ── */
div[data-testid="stSlider"] > div > div { background: rgba(255,255,255,0.05) !important; border-radius: 6px; height: 4px !important; }
div[data-testid="stSlider"] > div > div > div:first-child { background: linear-gradient(90deg, #633cff, #00d2b4) !important; border-radius: 6px; }
div[data-testid="stSlider"] [role="slider"] {
  background: #fff !important; border: 3px solid #633cff !important;
  box-shadow: 0 0 14px rgba(99,60,255,0.6), 0 2px 8px rgba(0,0,0,0.4);
  width: 20px !important; height: 20px !important; }
div[data-testid="stSlider"] p { color: rgba(232,230,240,0.4) !important; font-size: 11px !important; }

/* ── Input cards ── */
div[data-testid="stVerticalBlock"] > div[data-testid="stHorizontalBlock"] > div {
  background: rgba(255,255,255,0.018);
  border: 1px solid rgba(255,255,255,0.06);
  border-radius: 14px; padding: 14px 16px;
  transition: border-color 0.2s; }
div[data-testid="stVerticalBlock"] > div[data-testid="stHorizontalBlock"] > div:hover {
  border-color: rgba(99,60,255,0.25); }

/* ── Button ── */
div[data-testid="stButton"] > button {
  width: 100%;
  background: linear-gradient(135deg, #633cff 0%, #4f2ee8 60%, #3d22d4 100%);
  color: #fff; border: none; border-radius: 14px; padding: 18px 0;
  font-size: 14px; font-weight: 800; letter-spacing: 0.14em;
  text-transform: uppercase; margin-top: 1rem;
  box-shadow: 0 0 30px rgba(99,60,255,0.4), 0 4px 20px rgba(0,0,0,0.4);
  transition: all 0.25s; }
div[data-testid="stButton"] > button:hover {
  box-shadow: 0 0 55px rgba(99,60,255,0.7), 0 4px 24px rgba(0,0,0,0.5);
  transform: translateY(-2px); letter-spacing: 0.18em; }
div[data-testid="stButton"] > button:active { transform: translateY(0px); }

/* ── Price result ── */
.price-result {
  background: linear-gradient(135deg, rgba(99,60,255,0.18) 0%, rgba(0,210,180,0.10) 100%);
  border: 1px solid rgba(99,60,255,0.45);
  border-radius: 18px; padding: 2.5rem 2rem;
  text-align: center; margin-top: 1.5rem;
  box-shadow: 0 0 50px rgba(99,60,255,0.15), inset 0 1px 0 rgba(255,255,255,0.07); }
.price-tag { font-family: monospace; font-size: 11px; letter-spacing: 0.3em;
  text-transform: uppercase; color: #00d2b4; margin-bottom: 12px; }
.price-amount { font-size: 4rem; font-weight: 800; letter-spacing: -0.04em;
  color: #f0eeff; line-height: 1; }
.price-symbol { font-size: 2rem; font-weight: 600;
  color: rgba(240,238,255,0.5); vertical-align: super; margin-right: 4px; }

/* ── Column gap ── */
[data-testid="stHorizontalBlock"] { gap: 1rem; }
</style>
""", unsafe_allow_html=True)

@st.cache_resource
def load_model():
    return joblib.load("laptop_price_model.pkl")

model = load_model()

# ── Header ────────────────────────────────────────────────────────────────────
st.markdown("""
<div class="app-header">
  <div class="app-tag">// AI Price Estimation</div>
  <div class="app-title">Laptop<span>IQ</span></div>
  <div class="app-sub">Configure your laptop specs and get an instant price prediction.</div>
</div>
""", unsafe_allow_html=True)
st.divider()

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
with c5: ram_gb       = st.selectbox("RAM (GB)",     [4, 8, 16, 32, 64])
with c6: gpu          = st.selectbox("GPU",          ["Integrated","Intel Iris Xe","AMD Radeon","Apple GPU","NVIDIA RTX 3050","NVIDIA RTX 3060","NVIDIA RTX 4060","NVIDIA RTX 4070"])
c7, c8 = st.columns(2)
with c7: storage_gb   = st.selectbox("Storage (GB)", [128, 256, 512, 1024, 2048])
with c8: storage_type = st.selectbox("Storage Type", ["SSD","NVMe SSD","HDD","eMMC"])

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

if st.button("⚡  Predict Price", use_container_width=True, type="primary"):
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
    st.markdown(f"""
    <div class="price-result">
        <div class="price-tag">Estimated Market Price</div>
        <div class="price-amount"><span class="price-symbol">₹</span>{price:,.0f}</div>
    </div>
    """, unsafe_allow_html=True)
