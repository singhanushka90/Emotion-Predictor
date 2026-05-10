<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=0:6d28d9,50:7c3aed,100:06b6d4&height=220&section=header&text=Emotion%20Detector%20AI&fontSize=42&fontColor=ffffff&fontAlignY=38&desc=Text-Based%20Emotion%20%26%20Sentiment%20Intelligence%20System&descAlignY=58&descSize=16&animation=fadeIn" />
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.9+-3776AB?style=for-the-badge&logo=python&logoColor=white" />
  <img src="https://img.shields.io/badge/Scikit--Learn-ML%20Pipeline-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white" />
  <img src="https://img.shields.io/badge/NLP-TF--IDF%20%7C%20Bigrams-06b6d4?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Accuracy-89%25-22c55e?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Status-Active-success?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Streamlit-Deployable-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white" />
</p>

<br/>

---

## 🧠 What Is This?

**Emotion Detector** is an NLP-powered Machine Learning system that reads a piece of text and identifies the human emotion behind it — whether someone is joyful, angry, fearful, in love, sad, or surprised.

Built with a clean ML pipeline using **TF-IDF vectorization** and **Logistic Regression**, this project achieves **~89% accuracy** on a multi-class emotion classification task across **6 emotional categories**.

> 💡 **Real-World Use Cases:**
> Mental Health Monitoring • AI-Powered Chatbots • Social Media Sentiment Analysis • Customer Feedback Systems • Emotion-Aware AI Assistants

---

## 🎯 Emotions Detected

| Emoji | Emotion | Encoded Label |
|-------|---------|--------------|
| 😡 | **Anger** | `0` |
| 😨 | **Fear** | `1` |
| 😊 | **Joy** | `2` |
| ❤️ | **Love** | `3` |
| 😢 | **Sadness** | `4` |
| 😲 | **Surprise** | `5` |


Raw Text Input
↓
Lowercasing + Regex Cleaning  (remove special chars, numbers)
↓
TF-IDF Vectorization          (10,000 features, unigrams + bigrams)
↓
stop_words='english'          (noise reduction)
min_df=2, max_df=0.9          (filter rare & too-common words)
↓
Logistic Regression           (max_iter=2000)
↓
Emotion Prediction  →  Pickle Serialization
---

## ⚙️ ML Pipeline
