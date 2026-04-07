import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
import joblib

# ---------------- LOAD DATA ----------------
data = pd.read_csv("greenhouse_data_labeled.csv")

# ---------------- CLEAN DATA ----------------
data = data.dropna()
data = data[(data["temp"] > 5) & (data["humidity"] >= 0) & (data["gas"] >= 0)]

# ---------------- FEATURES ----------------
X = data[["temp", "humidity", "gas", "intrusion"]]

# ---------------- TARGET ----------------
y = data["label"].astype(str).str.strip().str.lower()

# ---------------- SPLIT ----------------
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

# ---------------- MODEL ----------------
model = RandomForestClassifier(
    n_estimators=200,
    random_state=42
)

model.fit(X_train, y_train)

# ---------------- TEST ----------------
y_pred = model.predict(X_test)

print("========== RESULTS ==========")
print("Accuracy:", accuracy_score(y_test, y_pred))
print("\nClassification Report:\n")
print(classification_report(y_test, y_pred))

print("Confusion Matrix:")
print(confusion_matrix(y_test, y_pred))

# ---------------- FEATURE IMPORTANCE ----------------
importance = pd.DataFrame({
    "Feature": X.columns,
    "Importance": model.feature_importances_
}).sort_values(by="Importance", ascending=False)

print("\nFeature Importance:")
print(importance)

# ---------------- SAVE MODEL ----------------
joblib.dump(model, "greenhouse_model.pkl")
print("\nModel saved as greenhouse_model.pkl")