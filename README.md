# 📈 FNS News Sentiment Analysis

A modular Python project for conducting sentiment and statistical analysis on financial news headlines to explore their relationship with stock price movements. The goal is to extract insights from news data and evaluate its potential to predict stock trends using both NLP and technical analysis techniques.

---

## 🚀 Project Overview

This project is part of the Nova Financial Solutions AI Mastery program. The main objective is to analyze financial news sentiment and correlate it with stock price movements to enhance investment decision-making.

Key tasks:
- Preprocess and analyze news headlines.
- Apply sentiment analysis techniques.
- Perform technical analysis on stock price data using financial indicators.
- Explore correlations between news sentiment and market behavior.

---

## 📂 Project Structure

```

fns-news-sentiment-analysis/
│
├── notebooks/          # Jupyter notebooks for EDA, experimentation
├── src/                # Core logic and reusable modules
├── scripts/            # One-off scripts and utilities
├── data/               # (Excluded) Place raw data files here
├── tests/              # Unit tests
├── .github/            # GitHub workflows (CI/CD)
├── requirements.txt    # Project dependencies
└── README.md           # Project description and instructions

```

---



✅ **Task 1: News Data Exploration**
- Tokenization, lemmatization, stopword removal using `SpaCy` and `NLTK`.
- Exploratory analysis of headline distribution, publisher frequency, and keyword patterns.
- Notebook: [`eda_news_sentiment.ipynb`](notebooks/eda_news_sentiment.ipynb)

## 🛠️ Tasks Completed
1. **Sentiment Analysis** using VADER on financial news headlines.
2. **Stock Return Calculation** using daily closing prices.
3. **Correlation Analysis** between sentiment and returns (same-day & lagged).

---

## 🗂️ Data Setup

The financial news and stock price datasets are large and not stored in the repository. To run the analysis:

1. **Download the data manually** from [Google Drive](https://drive.google.com/drive/u/4/folders/1rsispvTGPjC8pbKS-yYb-6dcJiXTKSAv)
2. **Place the files inside** the `data/` directory:

```

fns-news-sentiment-analysis/
└── data/
├── raw\_analyst\_ratings.csv
└── stock\_prices.csv

````

---

## 🧠 Tech Stack

- **Language:** Python 3.10+
- **Finance Tools (Planned):** `TA-Lib`, `PyNance`, `TextBlob`
- **Visualization:** `matplotlib`, `seaborn`, `plotly`

---

## 🔧 Setup Instructions

1. Clone the repository:
   ```bash
   git clone https://github.com/Selamawit-Alemu/fns-news-sentiment-analysis.git
   cd fns-news-sentiment-analysis
````

2. Create and activate a virtual environment:

   ```bash
   python -m venv venv
   source venv/bin/activate  # or venv\Scripts\activate on Windows
   ```

3. Install the required packages:

   ```bash
   pip install -r requirements.txt
   ```

4. Start exploring notebooks in the `notebooks/` folder.

---

## 📊 Results
- Overall correlation: **0.0108**
- Lagged correlation: **–0.0102**
- Stock-wise correlations:
  | Stock | Correlation |
  |-------|-------------|
  | AAPL  | 0.0453      |
  | AMZN  | –0.0015     |
  | GOOG  | 0.0247      |
  | META  | –0.0106     |
  | MSFT  | 0.0281      |
  | NVDA  | 0.0267      |
  | TSLA  | –0.0158     |
---

## 📬 Contact

**Author:** Selamawit Alemu
**GitHub:** [@Selamawit-Alemu](https://github.com/Selamawit-Alemu)
