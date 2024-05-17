import streamlit as st
from PIL import Image
import base64

st.set_page_config(
    page_title="Trang Chủ",
    page_icon="🏠",
)

# Function to get the base64 of the image
def get_base64(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

# Path to your background image
img_path = 'images/background2.jpg'

# Inject CSS with background image and styling for content box and headings
bg_img = get_base64(img_path)
st.markdown(
    f"""
    <style>
    .stApp {{
        background-image: url("data:image/jpg;base64,{bg_img}");
        background-size: cover;
        color: white;
    }}
    .content-box {{
        background: rgba(0, 0, 0, 0.4); /* Lighter semi-transparent black */
        padding: 20px;
        border-radius: 10px;
        margin: 20px;
        max-width: 800px;
        margin-left: auto;
        margin-right: auto;
    }}
    h3 {{
        color: #FFFFFF; /* Bright white color for h3 */
    }}
    a {{
        color: #1E90FF; /* Optional: Adjust link color */
        text-decoration: none;
    }}
    a:hover {{
        text-decoration: underline;
    }}
    </style>
    """,
    unsafe_allow_html=True
)

# Content within the box
st.markdown(
    """
    <div class="content-box">
        <h3>Website Xử Lý Ảnh Số</h3>
        <ul>
            <li>Thực hiện bởi: Nguyễn Trung Phiên và Hoàng Mai Hiếu</li>
            <li>Giảng viên hướng dẫn: ThS. Trần Tiến Đức</li>
            <li>Lớp Xử Lý Ảnh Số nhóm 01: DIPR430685_23_1_01</li>
        </ul>
    </div>
    """,
    unsafe_allow_html=True
)

st.markdown(
    """
    <div class="content-box">
        <h3>Thông tin liên hệ</h3>
        <ul>
            <li>Facebook: <a href="https://www.facebook.com/phien.phassphachss">Nguyễn Trung Phiên</a> hoặc <a href="https://www.facebook.com/tuilahiuu">Hoàng Mai Hiếu</a></li>
            <li>Email: 21110593@student.hcmute.edu.vn hoặc 21110448@student.hcmute.edu.vn</li>
            <li>Lấy source code tại <a href="https://github.com/quangnghia1110/XuLyAnhSo.git">đây</a></li>
        </ul>
    </div>
    """,
    unsafe_allow_html=True
)

st.markdown(
    """
    <div class="content-box">
        <h3>Video giới thiệu về Website</h3>
        <a href="#">Video giới thiệu website Xử Lý Ảnh Số</a>
    </div>
    """,
    unsafe_allow_html=True
)
