# =====================================================
# PHISHING EMAIL DETECTION MODEL
# Internship Mini Project
# =====================================================

import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report

# -----------------------------------------------------
# Load Dataset
# -----------------------------------------------------

data = pd.read_csv("emails.csv")

# -----------------------------------------------------
# Split Features and Labels
# -----------------------------------------------------

X = data["text"]
y = data["label"]

# -----------------------------------------------------
# Convert Text into Numerical Features
# -----------------------------------------------------

vectorizer = TfidfVectorizer()

X_vectorized = vectorizer.fit_transform(X)

# -----------------------------------------------------
# Train Test Split
# -----------------------------------------------------

X_train, X_test, y_train, y_test = train_test_split(
    X_vectorized,
    y,
    test_size=0.3,
    random_state=42
)

# -----------------------------------------------------
# Train Model
# -----------------------------------------------------

model = MultinomialNB()

model.fit(X_train, y_train)

# -----------------------------------------------------
# Predictions
# -----------------------------------------------------

y_pred = model.predict(X_test)

# -----------------------------------------------------
# Accuracy
# -----------------------------------------------------

accuracy = accuracy_score(y_test, y_pred)

print("\n===================================")
print(" PHISHING EMAIL DETECTION MODEL")
print("===================================")

print(f"\nModel Accuracy : {accuracy * 100:.2f}%")

# -----------------------------------------------------
# Confusion Matrix
# -----------------------------------------------------

print("\nConfusion Matrix:\n")

print(confusion_matrix(y_test, y_pred))

# -----------------------------------------------------
# Classification Report
# -----------------------------------------------------

print("\nClassification Report:\n")

print(classification_report(y_test, y_pred))

# -----------------------------------------------------
# Test Custom Email
# -----------------------------------------------------

print("\n===================================")
print(" Test Your Own Email")
print("===================================")

custom_email = input("\nEnter Email Text : ")

custom_data = vectorizer.transform([custom_email])

prediction = model.predict(custom_data)

print("\nPrediction :", prediction[0])
