import streamlit as st
import pickle

# Load model and vectorizer
model = pickle.load(open("emotion_model.pkl", "rb"))
tfidf = pickle.load(open("tfidf.pkl", "rb"))

# Page config
st.set_page_config(page_title="Emotion Detector", layout="centered")

# Title

st.title("💬 Emotion and Sentiment Detection App")
st.markdown("""
<style>
    .stTextArea textarea {
        font-size: 18px;
    }
    .stButton button {
        background-color: #ff4b4b;
        color: white;
        font-size: 16px;
    }
</style>
""", unsafe_allow_html=True)
st.write("Enter a sentence and detect the emotion")

# Input box
user_input = st.text_area("Enter your text here:")


emotion_labels = {
    4: "😢 Sad",
    2: "😊 Joy",
    0: "😠 Angry",
    1: "😨 Fear",
    3: "😍 Love",
    5: "😲 Surprise"
}

# Button
if st.button("Predict Emotion"):
    if user_input.strip() == "":
        st.warning("⚠️ Please enter some text")
    else:
        # Transform input
        input_vector = tfidf.transform([user_input])

        # Prediction
        prediction = model.predict(input_vector)[0]

        # Output
        st.success(f"Predicted Emotion: {emotion_labels.get(prediction, 'Unknown')}")
