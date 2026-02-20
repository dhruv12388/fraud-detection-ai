import pandas as pd
from xgboost import XGBClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
import joblib
import os

# 1. Load the data
print("📂 Loading data...")
df = pd.read_csv('data/transactions.csv')

# 2. Prepare Features (X) and Target (y)
X = df[['amount', 'hour']]
y = df['is_fraud']

# 3. Split into Training (80%) and Testing (20%) data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 4. Initialize the AI (XGBoost)
# We use 'scale_pos_weight' because fraud is rare (only 1% of data)
model = XGBClassifier(scale_pos_weight=1000)

print("🧠 Training the AI Brain... please wait.")
model.fit(X_train, y_train)

# 5. Check how smart the AI is
y_pred = model.predict(X_test)
print("\n📊 Model Performance Report:")
print(classification_report(y_test, y_pred))

# 6. Save the Brain so we can use it later
if not os.path.exists('models'):
    os.makedirs('models')

joblib.dump(model, 'models/fraud_model.pkl')
print("\n✅ Phase 4 Complete! Model saved in 'models/fraud_model.pkl'")