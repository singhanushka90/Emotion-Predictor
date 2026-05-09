<!-- 🌈 HERO BANNER -->
<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=0:7c3aed,100:06b6d4&height=200&section=header&text=Emotion%20Detector&fontSize=40&fontColor=ffffff" />
</p>

<h1 align="center">🧠 Emotion Detector</h1>
<h3 align="center"> Emotion & Sentiment Analysis System</h3>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.9+-blue?style=for-the-badge&logo=python" />
  <img src="https://img.shields.io/badge/NLP-TF--IDF-orange?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Machine%20Learning-Emotion%20Analysis-green?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Status-Active-success?style=for-the-badge" />
</p>

<hr/>

<h2>🧠 Overview</h2>

<p>
<b>Emotion Detector</b> is an intelligent NLP-based machine learning system designed to analyze human emotions from text input.
The model predicts emotional states such as:
<b>Anger, Fear, Joy, Love, Sadness, and Surprise.</b>
</p>

<p>
This project demonstrates how Natural Language Processing and Machine Learning can be combined to build emotionally-aware AI systems capable of understanding human sentiment and emotional context.
</p>

<blockquote>
💡 Use Cases: Mental Health Support • AI Chatbots • Social Media Monitoring • Customer Feedback Analysis • Emotion-Aware Applications
</blockquote>

<hr/>

<h2>⚙️ System Pipeline</h2>

<pre>
Text Input
    ↓
Text Cleaning & Preprocessing
    ↓
TF-IDF Vectorization
    ↓
Feature Extraction
    ↓
Machine Learning Model
    ↓
Emotion Prediction
</pre>

<hr/>

<h2>✨ Key Features</h2>

<table>
<tr>
<th>Feature</th>
<th>Description</th>
</tr>

<tr>
<td>🧠 Emotion Classification</td>
<td>Predicts multiple human emotions from text</td>
</tr>

<tr>
<td>⚡ Fast Prediction</td>
<td>Real-time emotion analysis pipeline</td>
</tr>

<tr>
<td>📊 NLP Processing</td>
<td>Text cleaning and feature extraction</td>
</tr>

<tr>
<td>🎯 Multi-Class Detection</td>
<td>Supports 6 different emotions</td>
</tr>

<tr>
<td>🌐 Streamlit Ready</td>
<td>Supports interactive web deployment</td>
</tr>

<tr>
<td>📈 High Accuracy</td>
<td>Optimized ML model for reliable predictions</td>
</tr>

</table>

<hr/>

<h2>🤖 Emotions Supported</h2>

<table>
<tr>
<th>Emotion</th>
<th>Label</th>
</tr>

<tr><td>😡 Anger</td><td>0</td></tr>
<tr><td>😨 Fear</td><td>1</td></tr>
<tr><td>😊 Joy</td><td>2</td></tr>
<tr><td>❤️ Love</td><td>3</td></tr>
<tr><td>😢 Sadness</td><td>4</td></tr>
<tr><td>😲 Surprise</td><td>5</td></tr>

</table>

<hr/>

<h2>⚙️ Technical Implementation</h2>

<ul>
  <li>Text preprocessing using regex cleaning and normalization</li>
  <li>TF-IDF vectorization for feature extraction</li>
  <li>Machine learning classification pipeline</li>
  <li>Label encoding for emotion mapping</li>
  <li>Pickle-based model serialization</li>
  <li>Real-time prediction support</li>
</ul>

<hr/>

<h2>🤖 Models Used</h2>

<table>
<tr>
<th>Model</th>
<th>Purpose</th>
<th>Status</th>
</tr>

<tr>
<td><b>Logistic Regression</b></td>
<td>Primary Emotion Classification</td>
<td>✅ Final Model</td>
</tr>

<tr>
<td><b>Support Vector Classifier (SVC)</b></td>
<td>Performance Comparison</td>
<td>⚡ Experimental</td>
</tr>

</table>

<p>
💡 Logistic Regression achieved strong overall performance with efficient prediction speed.
</p>

<hr/>

<h2>📊 Performance</h2>

<ul>
  <li><b>Accuracy:</b> ~87%</li>
  <li>Balanced multi-class classification</li>
  <li>Efficient TF-IDF based NLP pipeline</li>
  <li>Low prediction latency</li>
</ul>

<hr/>

<h2>📂 Dataset</h2>

<p>
The dataset contains thousands of labeled emotional text samples used for training and evaluation.
</p>

<table>
<tr>
<th>File</th>
<th>Description</th>
</tr>

<tr>
<td>train.txt</td>
<td>Training dataset</td>
</tr>

<tr>
<td>test.txt</td>
<td>Testing dataset</td>
</tr>

<tr>
<td>val.txt</td>
<td>Validation dataset</td>
</tr>

</table>

<p>
<b>Target:</b> Multi-Class Emotion Classification
</p>

<hr/>

<h2>🛠️ Tech Stack</h2>

<p align="center">
  <img src="https://skillicons.dev/icons?i=python,numpy,pandas,sklearn,streamlit" />
</p>

<ul>
  <li>Python</li>
  <li>Pandas & NumPy</li>
  <li>Scikit-learn</li>
  <li>TF-IDF Vectorizer</li>
  <li>Streamlit</li>
</ul>

<hr/>

<h2>📁 Project Structure</h2>

<pre>
Emotion-Detector/
│
├── 📓 emotion_model.ipynb
├── 🌐 app.py
├── 🤖 emotion_model.pkl
├── 🔤 tfidf.pkl
├── 📊 train.txt
├── 📊 test.txt
├── 📊 val.txt
└── 📖 README.md
</pre>

<hr/>

<h2>🚀 Installation</h2>

<pre>
git clone https://github.com/yourusername/Emotion-Detector.git

cd Emotion-Detector

pip install -r requirements.txt
</pre>

<hr/>

<h2>💻 Usage</h2>

<pre>
import pickle

model = pickle.load(open("emotion_model.pkl", "rb"))
tfidf = pickle.load(open("tfidf.pkl", "rb"))

text = ["I am feeling very happy today"]

vector = tfidf.transform(text)

prediction = model.predict(vector)

print(prediction)
</pre>

<hr/>

<h2>📊 Engineering Highlights</h2>

<ul>
  <li>🧠 Multi-class NLP classification system</li>
  <li>⚡ Lightweight and efficient architecture</li>
  <li>📈 Optimized preprocessing workflow</li>
  <li>🌐 Streamlit-ready deployment structure</li>
  <li>🔍 Emotion-aware AI interaction capability</li>
</ul>

<hr/>

<h2>🔮 Future Enhancements</h2>

<table>
<tr>
<th>Feature</th>
<th>Description</th>
</tr>

<tr>
<td>🤖 Deep Learning</td>
<td>LSTM / Transformer-based emotion analysis</td>
</tr>

<tr>
<td>🧠 BERT Integration</td>
<td>Context-aware emotion understanding</td>
</tr>

<tr>
<td>🌐 Cloud Deployment</td>
<td>Live Streamlit web application</td>
</tr>

<tr>
<td>🎤 Voice Emotion Detection</td>
<td>Speech-based emotional analysis</td>
</tr>

<tr>
<td>📱 Mobile Integration</td>
<td>Emotion-aware AI assistant</td>
</tr>

</table>

<hr/>

<h2>👩‍💻 Author</h2>

<p align="center">
  <b>Anushka Singh</b><br/>
  AI Engineer | NLP | Machine Learning
</p>

<hr/>

<h2 align="center">⚡ Final Insight</h2>

<p align="center">
<b>"Building AI systems capable of understanding human emotions through intelligent NLP."</b>
</p>

<hr/>

<p align="center">
⭐ Star this repository if you found it useful!
</p>
