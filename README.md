# 🧠 Next Word Prediction with LSTM and Streamlit

A minimal, elegant NLP web app that predicts the next word in a given sentence using an LSTM model. Built with **TensorFlow**, **Keras**, and **Streamlit**, this app provides real-time predictions with a sleek and responsive UI.

---

 
📁 **Dataset Used**: [Hamlet by Shakespeare](https://www.gutenberg.org/ebooks/1524)



---

## 🛠️ Features

- 📜 Enter a sentence and predict the next word instantly
- 🧠 Trained using an LSTM-based language model on `hamlet.txt`
- 💡 Intelligent padding, preprocessing, and dynamic input handling
- 🌐 Deployed using **Streamlit** for easy access and interactivity
- 🧳 Clean UI with minimal distraction

---

## ⚙️ Tech Stack

- **Frontend**: Streamlit
- **Backend/ML**: TensorFlow, Keras, NumPy, Pickle
- **Preprocessing**: Tokenizer, pad_sequences
- **Model**: LSTM-based language model
- **Deployment**: Streamlit Cloud / Vercel

---

## 📦 Installation

```bash
git clone https://github.com/swasthik-007/NextWordPred.git
cd next-word-lstm
pip install -r requirements.txt
