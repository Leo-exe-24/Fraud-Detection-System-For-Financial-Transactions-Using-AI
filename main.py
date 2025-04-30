# Online Payments Fraud Detection

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix

# Seaborn style
sns.set(style="whitegrid")

# Load dataset
data_path = r"C:\Python\Fraud Detection\payment.csv"
data = pd.read_csv(data_path)

# ------------------ Basic Info ------------------
print("First 10 rows of the dataset:")
print(data.head(10))

print("\nLast 10 rows of the dataset:")
print(data.tail(10))

print("\nDataset shape:", data.shape)

print("\nTransaction type counts:")
print(data['type'].value_counts())

# ------------------ Pie Charts ------------------
# Transaction types
type_counts = data['type'].value_counts()
fig1 = px.pie(
    names=type_counts.index,
    values=type_counts.values,
    hole=0.5,
    title="Distribution of Transaction Types"
)
fig1.show()

# Fraud vs Non-Fraud
fraud_counts = data['isFraud'].value_counts()
fraud_labels = ['Not Fraud', 'Fraud']
fig2 = px.pie(
    names=fraud_labels,
    values=fraud_counts.values,
    hole=0.5,
    title="Fraudulent vs Non-Fraudulent Transactions",
    color_discrete_sequence=["green", "red"]
)
fig2.show()

# ------------------ Data Quality ------------------
print("\nMissing values in each column:")
print(data.isnull().sum())

print("\nDataset description:")
print(data.describe())

# ------------------ Visualizations ------------------
# All transactions by type
plt.figure(figsize=(8, 5))
sns.countplot(x='type', data=data)
plt.title("Count of Each Transaction Type")
plt.show()

# Fraudulent transactions by type
plt.figure(figsize=(8, 5))
sns.countplot(x='type', data=data[data['isFraud'] == 1])
plt.title("Fraudulent Transactions by Type")
plt.show()

# Boxplot for fraud amount
plt.figure(figsize=(10, 3))
sns.boxplot(x=data[data['isFraud'] == 1]['amount'])
plt.title("Distribution of Fraudulent Transaction Amounts")
plt.xlabel("Amount")
plt.show()

# Hourly transactions
data['hour'] = (data['step'] - 1) % 24
plt.figure(figsize=(12, 5))
sns.countplot(x='hour', data=data)
plt.title("Transactions by Hour")
plt.xlabel("Hour")
plt.ylabel("Count")
plt.show()

# ------------------ Preprocessing ------------------
# Drop unnecessary columns
columns_to_drop = ['nameOrig', 'nameDest', 'isFlaggedFraud']
data.drop([col for col in columns_to_drop if col in data.columns], axis=1, inplace=True)

# Encode 'type'
label_encoder = LabelEncoder()
data['type'] = label_encoder.fit_transform(data['type'])

# Features and target
X = data.drop('isFraud', axis=1)
y = data['isFraud']

# ------------------ Model Training ------------------
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# ------------------ Evaluation ------------------
y_pred = model.predict(X_test)

print("\nConfusion Matrix:")
print(confusion_matrix(y_test, y_pred))

print("\nClassification Report:")
print(classification_report(y_test, y_pred))

# ------------------ Full Dataset Prediction ------------------
data['Predicted_Fraud'] = model.predict(X)

print("\nSample transactions with predictions:")
print(data[['amount', 'type', 'hour', 'isFraud', 'Predicted_Fraud']].head(10))

# ------------------ Export Results ------------------
output_path = r"C:\Python\Fraud Detection\fraud_predictions.csv"
data.to_csv(output_path, index=False)
print(f"\nPrediction results exported successfully to: {output_path}")
