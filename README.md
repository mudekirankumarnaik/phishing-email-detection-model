# Phishing Email Detection Model

A beginner-friendly Machine Learning cybersecurity project developed using Python and Scikit-learn to detect phishing emails.

This project analyzes email text content and classifies emails as either:

- Phishing
- Safe

The model is trained using a dataset of phishing and legitimate emails.

---

# Features

- Train machine learning model on email dataset
- Extract email text features using TF-IDF
- Detect phishing and legitimate emails
- Display model accuracy
- Generate confusion matrix
- Predict custom email messages

---

# Technologies Used

- Python
- Pandas
- Scikit-learn

---

# Machine Learning Concepts Used

- Text Classification
- TF-IDF Vectorization
- Naive Bayes Algorithm
- Train-Test Split
- Confusion Matrix

---

# Project Structure

```bash
phishing-email-detection-model/
│
├── phishing_detector.py
├── emails.csv
├── requirements.txt
└── README.md
```

---

# Dataset Format

Example dataset:

```csv
text,label
"Congratulations! You won a free iPhone",phishing
"Meeting scheduled tomorrow",safe
"Verify your bank account immediately",phishing
"Project report attached",safe
```

---

# Installation

Install required libraries:

```bash
pip install -r requirements.txt
```

---

# Run the Project

```bash
python phishing_detector.py
```

---

# Example Output

```text
===================================
 PHISHING EMAIL DETECTION MODEL
===================================

Model Accuracy : 100.00%

Confusion Matrix:

[[1 0]
 [0 1]]

Enter Email Text :
"Click here to verify your bank account"

Prediction : phishing
```

---

# Expected Outcome

The model successfully classifies emails as phishing or safe using machine learning techniques and textual feature analysis.

---

# Applications

- Email Security
- Spam Detection
- Cybersecurity Awareness
- Phishing Detection Systems

---

# Future Improvements

- Larger email datasets
- Deep Learning integration
- GUI interface
- Real-time email scanning
- URL analysis
- Web deployment using Flask

---

# Disclaimer

This project is developed for educational and authorized cybersecurity learning purposes only.

---

# Author

M. Kiran Kumar Naik

Cybersecurity & Python Enthusiast
