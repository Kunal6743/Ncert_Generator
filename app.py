import streamlit as st
from db_utils import get_chapters, get_chapter_context
from ai_utils import generate_questions
from pdf_utils import generate_pdf
import tempfile
import os


st.set_page_config(page_title="NCERT AI Generator", layout="centered")

st.title("📘 NCERT AI Question Generator")

# ------------------ CLASS ------------------
class_no = st.selectbox(
    "Select Class",
    [8, 9, 10],
    key="class_select"
)

# ------------------ SUBJECT ------------------
subject = st.selectbox(
    "Select Subject",
    ["Science", "Mathematics"],
    key="subject_select"
)

# ------------------ FETCH CHAPTERS (REFRESH SAFE) ------------------
chapters = get_chapters(class_no, subject)

if not chapters:
    st.warning("No chapters found")
    st.stop()

chapter_labels = []
chapter_map = {}

for ch_id, ch_no, ch_name in chapters:
    label = f"Chapter {ch_no} – {ch_name}"
    chapter_labels.append(label)
    chapter_map[label] = ch_id

# ------------------ CHAPTER ------------------
chapter_label = st.selectbox(
    "Select Chapter",
    chapter_labels,
    key="chapter_select"
)

chapter_id = chapter_map[chapter_label]

# ------------------ QUESTIONS COUNT ------------------
total_q = st.number_input(
    "Number of Questions",
    min_value=1,
    max_value=20,
    value=10,
    key="question_count"
)
# ------------------ LONG ANSWER CONTROL ------------------
st.subheader("📊 Question Difficulty Distribution")

easy_q = st.number_input("Easy questions", min_value=0, value=3)
medium_q = st.number_input("Medium questions", min_value=0, value=3)
hard_q = st.number_input("Hard questions", min_value=0, value=2)

total_q = easy_q + medium_q + hard_q



# ------------------ GENERATE ------------------
if st.button("Generate Questions", key="generate_btn"):
    with st.spinner("Generating NCERT questions…"):
        chapter_name, key_topics = get_chapter_context(chapter_id)

        output = generate_questions(
            class_no,
            subject,
            chapter_name,
            key_topics,
            easy_q,
            medium_q,
            hard_q
        )

    st.success("Questions generated successfully!")

    # -------- PDF GENERATION --------
    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp:
        pdf_path = tmp.name

    title = f"Class {class_no} {subject} – {chapter_name}"
    generate_pdf(pdf_path, title, output)

    # -------- DOWNLOAD BUTTON --------
    with open(pdf_path, "rb") as f:
        st.download_button(
            label="📥 Download Questions PDF",
            data=f,
            file_name=f"{chapter_name}.pdf",
            mime="application/pdf"
        )

