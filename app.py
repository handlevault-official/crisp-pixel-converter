from io import BytesIO
from PIL import Image
import streamlit as st

# 1. Page Config
st.set_page_config(
    page_title="Pixel Art Crisp Scaler", page_icon="🎨", layout="centered"
)

# 2. Sidebar: Store & Ko-fi Sponsorship
with st.sidebar:
  st.title("🎨 Pixel Art Assets")
  st.write("Mga ready-to-use pixel art packs at background screens para sa iyo!")

  st.markdown("### 🛒 Store & Bundles")
  st.link_button("🎮 Itch.io Store", "https://itch.io")  # Palitan ng link mo
  st.link_button("📦 Gumroad Mega Bundle", "https://gumroad.com")  # Palitan ng link mo

  st.divider()

  st.markdown("### ☕ Support This Tool")
  st.write(
      "100% ad-free! Kung nakatulong ito sa iyo, pwede kang mag-sponsor:"
  )
  st.link_button("💖 Sponsor on Ko-fi", "https://ko-fi.com")  # Palitan ng link mo

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
  # Buksan ang Image gamit ang Pillow
  image = Image.open(uploaded_file)

  col1, col2 = st.columns(2)

  with col1:
    st.subheader("Original Image")
    st.image(image, caption=f"Size: {image.width}x{image.height}px")
    scale_factor = st.selectbox(
        "Pumili ng Scale Multiplier:", [2, 4, 8, 16], index=1
    )

  # Bagong Sukat
  new_size = (image.width * scale_factor, image.height * scale_factor)

  # Nearest-Neighbor scaling para iwas blur at ma-preserve ang transparency
  resized_image = image.resize(new_size, Image.Resampling.NEAREST)

  with col2:
    st.subheader("Crisp Resized Result")
    st.image(
        resized_image, caption=f"New Size: {new_size[0]}x{new_size[1]}px"
    )

  # I-convert ang resized image pabalik sa bytes para sa Download Button
  buffered = BytesIO()
  # Panatilihin ang format (PNG kung may transparency)
  img_format = image.format if image.format else "PNG"
  resized_image.save(buffered, format=img_format)

  st.divider()
  st.download_button(
      label=f"⬇️ Download Scaled Image ({scale_factor}x)",
      data=buffered.getvalue(),
      file_name=f"scaled_{scale_factor}x_{uploaded_file.name}",
      mime=f"image/{img_format.lower()}",
  )
