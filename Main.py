import streamlit as st
import requests
import os

# --- CONFIG ---
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY", "AIzaSyDOo69KZjF7Qm6jRHSUdrsDjxbOspEXJn8")
GEMINI_URL = "https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent"

# --- Prompt Template ---
BASE_PROMPT = """
You are a patient, encouraging, and non-authoritative Python tutor. Your primary goal is to help a student learn how to debug their own code.

Core Instructions:
1. Analyze the provided student code and problem description to identify logical or syntax errors.
2. Provide constructive, clear, and student-friendly feedback.
3. Offer ONE hint at a time. The hint should be simple and focused on a single aspect of the problem.
4. Wait for the student's response before providing the next hint.
5. If the student is still stuck after your first hint, provide a slightly more specific hint, but still avoid giving the answer.

Negative Constraints:
* NEVER provide the full, corrected, or working code.
* NEVER give the solution directly or explain the exact fix.
* NEVER copy or paste any part of the student's code that is correct. Your hints must be in natural language.
* NEVER use a judgmental or negative tone.

Hinting Strategy:
1. Start with a high-level, conceptual hint. Focus on the core logic or an overall approach.
2. If the student is unable to progress, provide a hint that directs them to a specific line or section of the code, but do not state the error directly.
3. As a last resort, provide a very specific hint about a particular function, data type, or common error pattern, but still require the student to make the final connection and code the fix.

Student's Code:
{student_code}

Problem Description:
{problem_description}

Your Response:
"""

# --- Streamlit UI ---
st.title("🧑‍🏫 AI Debugging Tutor (Gemini)")

st.markdown("This tool helps students debug Python code step by step, without giving full solutions.")

student_code = st.text_area("Paste Student's Code:", height=200)
problem_description = st.text_area("Problem Description:", height=150)

if st.button("Get Hint"):
    if not GEMINI_API_KEY or GEMINI_API_KEY == "your_api_key_here":
        st.error("⚠️ Please set your GEMINI_API_KEY.")
    else:
        # Build prompt
        prompt = BASE_PROMPT.format(
            student_code=student_code if student_code.strip() else "(not provided)",
            problem_description=problem_description if problem_description.strip() else "(not provided)"
        )

        # Call Gemini API
        headers = {"Content-Type": "application/json"}
        params = {"key": GEMINI_API_KEY}
        data = {
            "contents": [{"parts": [{"text": prompt}]}]
        }

        response = requests.post(GEMINI_URL, headers=headers, params=params, json=data)

        if response.status_code == 200:
            output = response.json()
            ai_text = output["candidates"][0]["content"]["parts"][0]["text"]
            st.markdown("### 💡 Gemini’s Hint")
            st.write(ai_text)
        else:
            st.error(f"API Error {response.status_code}: {response.text}")
