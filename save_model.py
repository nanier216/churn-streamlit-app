import os
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import pickle

# Local path to the dataset CSV
data_path = os.path.join('data', 'telco_customer_churn.csv')

df = pd.read_csv(data_path)

# Basic preprocessing
df = df.dropna()  # Drop missing values for simplicity

# Convert 'TotalCharges' to numeric (some values might be spaces)
df['TotalCharges'] = pd.to_numeric(df['TotalCharges'], errors='coerce')
df = df.dropna(subset=['TotalCharges'])

# Encode target variable: 'Churn' -> 1 (Yes), 0 (No)
df['Churn'] = df['Churn'].map({'Yes': 1, 'No': 0})

# Select features and target
# For simplicity, use only numerical columns
feature_cols = ['tenure', 'MonthlyCharges', 'TotalCharges']
X = df[feature_cols]
y = df['Churn']

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train Random Forest Classifier
model = RandomForestClassifier(random_state=42)
model.fit(X_train, y_train)

# Evaluate on test set
y_pred = model.predict(X_test)
acc = accuracy_score(y_test, y_pred)
print(f"Test Accuracy: {acc:.4f}")

# Save the model
model_path = os.path.join('model', 'churn_model.pkl')
with open(model_path, 'wb') as f:
    pickle.dump(model, f)

print(f"Model saved to {model_path}")
