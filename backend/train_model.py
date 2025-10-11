# train_model.py
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
import joblib

# -------------------------
# 1️⃣ Load dataset
# -------------------------
df = pd.read_csv("workout_diet_dataset.csv")

# -------------------------
# 2️⃣ Encode categorical features
# -------------------------
age_map = {"teen": 0, "young": 1, "middle": 2, "senior": 3}
gender_map = {"male": 0, "female": 1}
height_map = {"short": 0, "medium": 1, "tall": 2}
weight_map = {"underweight": 0, "normal": 1, "overweight": 2, "obese": 3}
gym_map = {"gym": 0, "home": 1}
goal_map = {"weight-loss": 0, "muscle-gain": 1, "stamina": 2, "flexibility": 3}
budget_map = {"low": 0, "medium": 1, "high": 2}

df["age_group"] = df["age_group"].map(age_map)
df["gender"] = df["gender"].map(gender_map)
df["height_category"] = df["height_category"].map(height_map)
df["weight_category"] = df["weight_category"].map(weight_map)
df["gymorhome"] = df["gymorhome"].map(gym_map)
df["goal"] = df["goal"].map(goal_map)
df["budget"] = df["budget"].map(budget_map)

# -------------------------
# 3️⃣ Features & target
# -------------------------
X = df[["age_group","gender","height_category","weight_category",
        "gymorhome","goal","budget"]]

# Use row index as "label" to retrieve plan later
y = df.index

# -------------------------
# 4️⃣ Train-test split
# -------------------------
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# -------------------------
# 5️⃣ Train model (lightweight)
# -------------------------
clf = DecisionTreeClassifier(max_depth=12, random_state=42)
clf.fit(X_train, y_train)

# -------------------------
# 6️⃣ Save model
# -------------------------
joblib.dump(clf, "planner_model.pkl")

# -------------------------
# 7️⃣ Print accuracy
# -------------------------
train_acc = clf.score(X_train, y_train)
test_acc = clf.score(X_test, y_test)

print("✅ Model trained and saved as 'planner_model.pkl'")
print(f"Training Accuracy: {train_acc:.2f}")
print(f"Test Accuracy: {test_acc:.2f}")
