from datetime import date

import pdfkit
import streamlit as st
from jinja2 import Environment
from jinja2 import FileSystemLoader
from jinja2 import select_autoescape

from shap_app.main import MAIN_DIR

st.set_page_config(layout="centered", page_icon="🎓", page_title="Diploma Generator")
st.title("🎓 Diploma PDF Generator")

st.write(
    "This app shows you how you can use Streamlit to make a PDF generator app "
    "in just a few lines of code!"
)

left, right = st.columns(2)

right.write("Here's the template we'll be using:")

right.image(f"{MAIN_DIR}/template.png", width=300)

env = Environment(loader=FileSystemLoader(MAIN_DIR), autoescape=select_autoescape())
template = env.get_template("template.html")


left.write("Fill in the data:")
form = left.form("template_form")
student = form.text_input("Student name")
course = form.selectbox(
    "Choose course",
    ["Report Generation in Streamlit", "Advanced Cryptography"],
    index=0,
)
grade = form.slider("Grade", 1, 100, 60)
if submit := form.form_submit_button("Generate PDF"):
    html = template.render(
        student=student,
        course=course,
        grade=f"{grade}/100",
        date=date.today().strftime("%B %d, %Y"),
    )

    pdf = pdfkit.from_string(html, False)
    st.balloons()

    right.success("🎉 Your diploma was generated!")
    # st.write(html, unsafe_allow_html=True)
    # st.write("")
    right.download_button(
        "⬇️ Download PDF",
        data=pdf,
        file_name="diploma.pdf",
        mime="application/octet-stream",
    )
