# Brand Voice Consistency Analyzer

Analyze the consistency of your brand's written communications (blog posts, emails, social media, etc.) using NLP metrics and embeddings.

## Features

- Upload or paste multiple text samples
- Analyze average sentence length, readability, sentiment, passive voice, and formality
- Detect outlier samples and measure overall consistency
- Downloadable CSV report and interactive visualizations

## Installation

### 1. **Clone the repository**

```bash
git clone https://github.com/yourusername/brand_voice_analyzer.git
cd brand_voice_analyzer
```

### 2. **Set up a virtual environment**

```bash
python3.11 -m venv venv
# Activate (Windows)
venv\Scripts\activate
# Activate (macOS/Linux)
source venv/bin/activate
```

### 3. **Install dependencies**

```bash
pip install --upgrade pip
pip install -r requirements.txt
python -m spacy download en_core_web_sm
python -m textblob.download_corpora
```

### 4. **Run the Streamlit app**

```bash
streamlit run app.py
```

---

## 📝 Usage

- **Upload `.txt` files** (one sample per file) or **paste text samples** directly in the app.
- The app will analyze each sample and display:
  - A metrics table (with outliers highlighted)
  - Consistency scores
  - Visualizations for style and sentiment
- **Download the full report** as a CSV for further analysis.

---

## 📊 Metrics Explained

- **Average Sentence Length:**  
  Average number of words per sentence.
- **Readability Score:**  
  Flesch Reading Ease score (higher = easier to read).
- **Sentiment Polarity:**  
  Ranges from -1 (negative) to 1 (positive).
- **Passive Voice %:**  
  Percentage of sentences in passive voice.
- **Formality Score:**  
  Heuristic based on sentence length and vocabulary complexity.
- **Consistency Score:**  
  Measures how similar all samples are in style/tone using sentence embeddings.

---

## 🛠️ Tech Stack

- [Streamlit](https://streamlit.io/) for the interactive UI
- [spaCy](https://spacy.io/) for NLP and passive voice detection
- [TextBlob](https://textblob.readthedocs.io/) for sentiment analysis
- [textstat](https://pypi.org/project/textstat/) for readability
- [SentenceTransformers](https://www.sbert.net/) for embeddings
- [Pandas](https://pandas.pydata.org/) for data handling

---

## 🤝 Contributing

Pull requests are welcome! For major changes, please open an issue first to discuss what you would like to change.

## 🙋 FAQ

**Q: What should my `.txt` files contain?**  
A: Each `.txt` file should contain a single text sample (e.g., one blog post, email, or social media post).

**Q: Can I use this for languages other than English?**  
A: The current models and metrics are optimized for English.

**Q: I see an error or blank page!**  
A: Make sure all dependencies are installed, your virtual environment is activated, and you are running Python 3.10 or 3.11.

