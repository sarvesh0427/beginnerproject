import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
import joblib

# 1. Load Data
df = pd.read_csv('dataset/playtennis.csv')

# 2. Preprocessing: Fill missing values with the most common value (mode)
for col in df.columns:
    df[col] = df[col].fillna(df[col].mode()[0])

# 3. Encoding: Convert text (e.g., 'Sunny') to numbers (e.g., 2)
encoders = {}
for col in df.columns:
    le = LabelEncoder()
    df[col] = le.fit_transform(df[col])
    encoders[col] = le

# 4. Train the Model
X = df.drop('PlayTennis', axis=1)
y = df['PlayTennis']
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X, y)

# 5. Save Model and Encoders for use in the Backend
joblib.dump(model, 'models/tennis_model.joblib')
joblib.dump(encoders, 'models/encoders.joblib')
print("Model and Encoders saved successfully!")