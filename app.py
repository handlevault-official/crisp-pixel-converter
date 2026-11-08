from io import BytesIO
from PIL import Image
import streamlit as st

# 1. Page Config
st.set_page_config(
    page_title="Pixel Art Crisp Scaler", page_icon="🎨", layout="centered"
)

# 2. Sidebar: Store, Ko-fi Sponsorship & Instructions
with st.sidebar:
  st.title("🎨 Pixel Art Assets")
  st.write("Mga ready-to-use pixel art packs at background screens para sa iyo!")

  st.markdown("### 🛒 Store & Bundles")
  st.link_button("🎮 Itch.io Store", "https://itch.io")
  st.link_button("📦 Gumroad Mega Bundle", "https://gumroad.com")

  st.divider()

  st.markdown("### ☕ Support This Tool")
  st.write("100% ad-free! Kung nakatulong ito, pwede kang mag-sponsor:")
  st.link_button("💖 Sponsor on Ko-fi", "https://ko-fi.com")

  st.divider()

  # Built-in Setup / Usage Instructions sa Code
  with st.expander("📖 How to Use & Setup"):
    st.markdown("""
        **Paano gamitin ang Tool na ito:**
        1. I-upload ang iyong pixel art (PNG, JPG, WebP).
        2. Pumili ng scale multiplier (2x, 4x, 8x, 16x).
        3. I-download ang crisp resized image nang walang blur!
        
        **Local Setup (Bash):**
        ```bash
        git clone <repo-url>
        cd pixel-art-converter
        python -m venv venv
        source venv/Scripts/activate  # o venv/bin/activate
        pip install -r requirements.txt
        streamlit run app.py
        ```
        """)

# 3. Main Content: Converter Utility
st.title("🖼️ Pixel Art Converter & Scaler")
st.write(
    "I-upload ang iyong pixel art para ma-scale nang hindi nagiging blurry"
    " gamit ang **Nearest-Neighbor Filtering**."
)

uploaded_file = st.file_uploader(
    "Mag-upload ng Pixel Art (PNG, JPG, WebP):", type=["png", "jpg", "webp"]
)

if uploaded_file:
  image = Image.open(uploaded_file)

  col1, col2 = st.columns(2)

  with col1:
    st.subheader("Original Image")
    st.image(image, caption=f"Size: {image.width}x{image.height}px")
    scale_factor = st.selectbox(
        "Pumili ng Scale Multiplier:", [2, 4, 8, 16], index=1
    )

  new_size = (image.width * scale_factor, image.height * scale_factor)
  resized_image = image.resize(new_size, Image.Resampling.NEAREST)

  with col2:
    st.subheader("Crisp Resized Result")
    st.image(
        resized_image, caption=f"New Size: {new_size[0]}x{new_size[1]}px"
    )

  buffered = BytesIO()
  img_format = image.format if image.format else "PNG"
  resized_image.save(buffered, format=img_format)

  st.divider()
  st.download_button(
      label=f"⬇️ Download Scaled Image ({scale_factor}x)",
      data=buffered.getvalue(),
      file_name=f"scaled_{scale_factor}x_{uploaded_file.name}",
      mime=f"image/{img_format.lower()}",
  )
    
