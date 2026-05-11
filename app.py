import streamlit as st
import pickle
import numpy as np
import re

# =========================================================
# Load trained model and TF-IDF vectorizer
# =========================================================
model = pickle.load(open("emotion_model.pkl", "rb"))
tfidf = pickle.load(open("tfidf.pkl", "rb"))

# =========================================================
# Page Configuration
# =========================================================
st.set_page_config(
    page_title="Emotion Detector AI",
    page_icon="💬",
    layout="centered"
)

# =========================================================
# Custom Styling
# =========================================================
st.markdown("""
<style>

.main {
    background-color: #0f172a;
}

h1 {
    text-align: center;
    color: white;
}

.stTextArea textarea {
    font-size: 18px;
    border-radius: 12px;
    border: 2px solid #6366f1;
    background-color: #f8fafc;
}

.stButton button {
    width: 100%;
    background: linear-gradient(90deg, #6366f1, #8b5cf6);
    color: white;
    font-size: 18px;
    border-radius: 10px;
    height: 3em;
    border: none;
}

.stButton button:hover {
    background: linear-gradient(90deg, #4f46e5, #7c3aed);
    color: white;
}

.result-box {
    padding: 20px;
    border-radius: 12px;
    background-color: #111827;
    color: white;
    text-align: center;
    font-size: 24px;
    margin-top: 20px;
}

</style>
""", unsafe_allow_html=True)

# =========================================================
# Title Section
# =========================================================
st.title("💬 Emotion & Sentiment Detection System")

st.markdown("""
<div style='text-align:center; color:gray; font-size:18px;'>
Detect human emotions from text using Machine Learning & NLP
</div>
""", unsafe_allow_html=True)

st.write("")

# =========================================================
# Emotion Labels
# =========================================================
emotion_labels = {
    0: "😠 Angry",
    1: "😨 Fear",
    2: "😊 Joy",
    3: "😍 Love",
    4: "😢 Sad",
    5: "😲 Surprise"
}

# =========================================================
# Text Cleaning Function
# =========================================================
def clean_text(text):
    text = text.lower()
    text = re.sub(r'[^a-zA-Z\s]', '', text)
    return text

# =========================================================
# User Input
# =========================================================
user_input = st.text_area(
    "✍️ Enter your sentence",
    placeholder="Example: I am very excited about my new project!"
)

# =========================================================
# Prediction Button
# =========================================================
if st.button("🔍 Predict Emotion"):

    if user_input.strip() == "":
        st.warning("⚠️ Please enter some text")

    else:

        # Clean text
        cleaned_text = clean_text(user_input)

        # Convert text into numerical vector
        input_vector = tfidf.transform([cleaned_text])

        # Prediction
        prediction = model.predict(input_vector)[0]

        # Probability Scores
        probabilities = model.predict_proba(input_vector)[0]
        confidence = round(np.max(probabilities) * 100, 2)

        # Predicted emotion
        predicted_emotion = emotion_labels.get(prediction, "Unknown")

        # =========================================================
        # Result Display
        # =========================================================
        st.markdown(
            f"""
            <div class="result-box">
                Predicted Emotion <br><br>
                <b>{predicted_emotion}</b><br><br>
                Confidence: {confidence}%
            </div>
            """,
            unsafe_allow_html=True
        )

        # =========================================================
        # Probability Breakdown
        # =========================================================
        st.subheader("📊 Emotion Probability Scores")

        for idx, prob in enumerate(probabilities):
            emotion = emotion_labels.get(idx, "Unknown")
            st.progress(float(prob))
            st.write(f"{emotion}: {round(prob * 100, 2)}%")

        # =========================================================
        # Processed Text (Optional)
        # =========================================================
        with st.expander("🛠️ Cleaned Input Text"):
            st.write(cleaned_text)
