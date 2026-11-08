import io
from PIL import Image
import streamlit as st

# Page configuration
st.set_page_config(
    page_title="Pixel Art Crisp Scaler - Arcade Edition",
    page_icon="🕹️",
    layout="wide",
)

# Custom Retro Arcade CSS Styling
st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Press+Start+2P&family=VT323&display=swap');

    .stApp {
        background-color: #0d0f18;
        color: #c9d1d9;
        font-family: 'VT323', monospace;
        font-size: 22px;
    }

    h1, h2, h3 {
        font-family: 'Press Start 2P', cursive !important;
        color: #ff007f !important;
        text-shadow: 2px 2px #00ffcc;
    }

    [data-testid="stSidebar"] {
        background-color: #161b22;
        border-right: 3px solid #ff007f;
    }

    .stButton>button, .stLinkButton>a {
        background-color: #ff007f !important;
        color: white !important;
        font-family: 'Press Start 2P', cursive !important;
        font-size: 10px !important;
        border: 2px solid #00ffcc !important;
        border-radius: 0px !important;
        box-shadow: 3px 3px #00ffcc;
    }
    .stButton>button:hover, .stLinkButton>a:hover {
        background-color: #00ffcc !important;
        color: #0d0f18 !important;
    }
    </style>
""",
    unsafe_allow_html=True,
)

# Sidebar: Store, Ko-fi Sponsorship & Instructions
with st.sidebar:
  st.markdown("### 🕹️ PIXEL ARCADE")
  st.write("100% Crisp Scaling para sa iyong indie game assets!")

  st.divider()

  st.markdown("### 🛒 STORE & BUNDLES")
  st.link_button("🎮 Itch.io Store", "https://itch.io")
  st.link_button("📦 Gumroad Mega Pack", "https://gumroad.com")

  st.divider()

  st.markdown("### ☕ SUPPORT")
  st.link_button("💖 Sponsor on Ko-fi", "https://ko-fi.com/handlevault")

# Main Interface
st.markdown("## 🎨 PIXEL ART CRISP SCALER")
st.write(
    "I-upload ang iyong pixel art para sa nearest-neighbor scaling nang"
    " walang blur."
)

uploaded_file = st.file_uploader(
    "Mag-upload ng Pixel Art (PNG, JPG)", type=["png", "jpg", "jpeg", "webp"]
)

if uploaded_file is not None:
  image = Image.open(uploaded_file)

  col1, col2 = st.columns(2)

  with col1:
    st.markdown("### 📷 ORIGINAL")
    st.image(image, caption=f"Size: {image.size[0]}x{image.size[1]}px")

  # Scale controls
  scale_factor = st.selectbox(
      "SCALE MULTIPLIER", [2, 4, 8, 16], index=1, format_func=lambda x: f"{x}X"
  )

  new_width = image.size[0] * scale_factor
  new_height = image.size[1] * scale_factor

  # Nearest Neighbor Scaling (Secret sauce para hindi lumabo)
  scaled_image = image.resize(
      (new_width, new_height), resample=Image.Resampling.NEAREST
  )

  with col2:
    st.markdown("### ⚡ CRISP SCALED RESULT")
    st.image(scaled_image, caption=f"New Size: {new_width}x{new_height}px")

  # Download button
  buf = io.BytesIO()
  scaled_image.save(buf, format="PNG")
  byte_im = buf.getvalue()

  st.download_button(
      label="⬇️ DOWNLOAD SCALED PNG",
      data=byte_im,
      file_name=f"pixel_scaled_{scale_factor}x.png",
      mime="image/png",
  )
