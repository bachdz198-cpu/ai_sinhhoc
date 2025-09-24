import streamlit as st
import subprocess

st.set_page_config(page_title="AI Sinh học", page_icon="🧬")
st.title("🤖 Chatbot AI Sinh học (THPT + Nâng cao)")
st.write("Bạn có thể gõ lệnh như khi chạy trên Python console.")

# Ô nhập lệnh
command = st.text_input("Nhập lệnh (ví dụ: python chatbot.py) hoặc câu hỏi:")

if st.button("Chạy"):
    if command.strip() != "":
        try:
            # Gọi lại file chatbot.py, truyền input
            result = subprocess.run(
                ["python", "chatbot.py"],
                capture_output=True, text=True, input=command
            )
            st.text_area("Kết quả:", result.stdout + result.stderr, height=300)
        except Exception as e:
            st.error(str(e))
