import streamlit as st
import google.generativeai as genai

# -----------------------------
# Gemini API Configuration
# -----------------------------
genai.configure(api_key="AQ.Ab8RN6Ikp4knRJh51wFVsZNGfAmS-aEgGUNaCDrmtIgZa_QuCg")

model = genai.GenerativeModel("gemini-2.5-flash")

# -----------------------------
# Streamlit Page Configuration
# -----------------------------
st.set_page_config(
    page_title="PyBuddy - AI Python Learning Buddy",
    page_icon="🐍",
    layout="wide"
)
# -----------------------------
# Custom CSS
# -----------------------------
st.markdown("""
<style>

.main{
    background-color:#f8f9fa;
}

h1{
    color:#1f77b4;
    text-align:center;
}

.stButton>button{
    width:100%;
    background:#1f77b4;
    color:white;
    border-radius:10px;
    height:50px;
    font-size:18px;
    font-weight:bold;
}

.stButton>button:hover{
    background:#125ea7;
}

.stTextInput>div>div>input{
    border-radius:10px;
}

.stTextArea textarea{
    border-radius:10px;
}

</style>
""", unsafe_allow_html=True)

# -----------------------------
# Header
# -----------------------------
st.title("🐍 PyBuddy - AI Python Learning Buddy")
st.markdown("""
Welcome to **PyBuddy**, your personal AI tutor for learning Python Programming.

This AI Buddy can help you:
- 📘 Explain Python concepts
- 💡 Give real-life examples
- 📝 Generate quizzes
- ✅ Evaluate your answers
- ❓ Answer any Python question
""")

st.divider()

# -----------------------------
# Sidebar
# -----------------------------
st.sidebar.title("📚 Python Roadmap")

st.sidebar.markdown("""
### Beginner
- Variables
- Data Types
- Operators
- Input & Output

### Intermediate
- Conditions
- Loops
- Functions
- Strings
- Lists
- Tuples
- Dictionaries
- Sets

### Advanced
- OOP
- File Handling
- Exception Handling
- Modules
- NumPy
- Pandas
- Matplotlib
""")

# -----------------------------
# User Input
# -----------------------------
topic = st.text_input(
    "Enter Python Topic",
    placeholder="Example: Loops"
)

activity = st.selectbox(
    "Choose Activity",
    (
        "📘 Explain Concept",
        "💡 Real-Life Example",
        "📝 Generate Quiz",
        "✅ Evaluate My Answer",
        "❓ Ask Anything"
    )
)

student_answer = ""

if activity == "✅ Evaluate My Answer":
    student_answer = st.text_area(
        "Write your answer here"
    )

generate = st.button("🚀 Generate")
# -----------------------------
# Generate AI Response
# -----------------------------
if generate:

    if topic.strip() == "":
        st.warning("⚠ Please enter a Python topic.")
        st.stop()

    if activity == "📘 Explain Concept":

        prompt = f"""
You are an expert Python tutor.

Explain the Python topic '{topic}' for a beginner.

Your explanation should include:

1. Definition
2. Why it is used
3. Syntax
4. Example Program
5. Output
6. Common Mistakes
7. Interview Tip

Use simple English.
"""

    elif activity == "💡 Real-Life Example":

        prompt = f"""
Explain the Python topic '{topic}' using a simple real-life example.

After the example,
explain how it relates to Python.

Keep it beginner friendly.
"""

    elif activity == "📝 Generate Quiz":

        prompt = f"""
Generate a quiz on '{topic}'.

Rules:

Generate exactly 5 MCQs.

Each question should contain

A)

B)

C)

D)

Mention the correct answer after every question.

At the end,

Give score evaluation.

Beginner Friendly.
"""

    elif activity == "✅ Evaluate My Answer":

        if student_answer.strip() == "":
            st.warning("Please enter your answer.")
            st.stop()

        prompt = f"""
You are a Python Trainer.

Topic:

{topic}

Student Answer:

{student_answer}

Evaluate the answer.

Tell whether it is Correct or Incorrect.

Explain mistakes.

Suggest improvements.

Give marks out of 10.
"""

    else:

        prompt = f"""
You are a Python Programming Expert.

Answer this question clearly.

Question:

{topic}

Explain in simple language.
"""

    with st.spinner("🤖 Generating AI Response..."):

        try:

            response = model.generate_content(prompt)

            st.toast("Response Generated Successfully 🎉")

            st.success("Response Generated Successfully")
            st.subheader("📖 AI Response")
            with st.container(border=True):
                st.markdown(response.text)
            st.download_button(
                "📥 Download Response",
                response.text,
                file_name="Python_AI_Response.txt",
                mime="text/plain"
            )

        except Exception as e:

            st.error("Error occurred while generating response.")

            st.exception(e)
