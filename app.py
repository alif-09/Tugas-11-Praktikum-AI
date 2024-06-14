import streamlit as st
import numpy as np
from dominant_colors import get_dominant_colors
from PIL import Image

st.title("Ekstraksi 5 Warna Dominan dari Gambar")

uploaded_files = st.file_uploader("Pilih gambar", type=["jpg", "jpeg", "png"], accept_multiple_files=True)

if uploaded_files:
    st.write(f"Jumlah gambar yang diunggah: {len(uploaded_files)}")

    for index, uploaded_file in enumerate(uploaded_files):
        image = Image.open(uploaded_file)
        st.image(image, caption=f"Gambar {index+1}", use_column_width=True)
        
        colors = get_dominant_colors(uploaded_file, num_colors=5)
        
        st.write("5 Warna Dominan:")

        image_width = image.width

        color_html = []
        for i, color in enumerate(colors):
            rgb_str = f"RGB {color}"

            box_size = min(image_width // 2, 115.3) 

            color_html.append(
                f"<div style='position: relative; display: inline-block; width: {box_size}px; height: {box_size}px; margin: 10px; "
                f"background-color: rgb({color[0]}, {color[1]}, {color[2]}); border: 1px solid #ccc; padding: 5px;'"
                f" title=' RGB: {color}'"
                f" onclick='navigator.clipboard.writeText(\"RGB: {color}\")';"
                f" onmouseover='this.querySelector(\".copy-icon\").style.opacity = 1;' onmouseout='this.querySelector(\".copy-icon\").style.opacity = 0;'>"
                f"</span>"
                f"</div>"
            )

        # Join color boxes into a single HTML string
        color_display = ''.join(color_html)

        # Add horizontal rule and spacing between images
        if index < len(uploaded_files) - 1:
            st.markdown("<hr style='margin: 30px 0;'>", unsafe_allow_html=True)

        # Display the image followed by the color boxes
        st.markdown(f"<div style='margin-bottom: 30px;'><div style='display: inline-block; margin-right: 20px;'>{color_display}</div></div>", unsafe_allow_html=True)
