# app.py
from flask import Flask, request, jsonify
from flask_cors import CORS
import pandas as pd
import joblib
import sqlite3
import os
from waitress import serve

app = Flask(__name__)
CORS(app)  # Enable CORS for frontend calls

# ------------------------------
# Load model and dataset
# ------------------------------
model = joblib.load("planner_model.pkl")
df = pd.read_csv("workout_diet_dataset.csv")

# ------------------------------
# Encoding maps
# ------------------------------
age_map = {"teen": 0, "young": 1, "middle": 2, "senior": 3}
gender_map = {"male": 0, "female": 1}
height_map = {"short": 0, "medium": 1, "tall": 2}
weight_map = {"underweight": 0, "normal": 1, "overweight": 2, "obese": 3}
gym_map = {"gym": 0, "home": 1}
goal_map = {"weight-loss": 0, "muscle-gain": 1, "stamina": 2, "flexibility": 3}
budget_map = {"low": 0, "medium": 1, "high": 2}

# ------------------------------
# SQLite DB setup
# ------------------------------
DB_FILE = "fitness_planner.db"

def init_db():
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS user_plans (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            email TEXT,
            age_group TEXT,
            gender TEXT,
            height_category TEXT,
            weight_category TEXT,
            gymorhome TEXT,
            goal TEXT,
            budget TEXT,
            workout_plan TEXT,
            diet_plan TEXT
        )
    """)
    conn.commit()
    conn.close()

init_db()

# ------------------------------
# Generate plan endpoint
# ------------------------------
@app.route("/generate_plan", methods=["POST"])
def generate_plan():
    try:
        data = request.get_json()

        # User info
        name = data.get("name", "")
        email = data.get("email", "")

        # User inputs
        age = data.get("age_group", "young")
        gender = data.get("gender", "male")
        height = data.get("height_category", "medium")
        weight = data.get("weight_category", "normal")
        gymorhome = data.get("gymorhome", "gym")
        goal = data.get("goal", "weight-loss")
        budget = data.get("budget", "medium")

        # Encode inputs
        X_input = pd.DataFrame([[ 
            age_map.get(age, 1),
            gender_map.get(gender, 0),
            height_map.get(height, 1),
            weight_map.get(weight, 1),
            gym_map.get(gymorhome, 0),
            goal_map.get(goal, 0),
            budget_map.get(budget, 1)
        ]], columns=["age_group","gender","height_category","weight_category",
                     "gymorhome","goal","budget"])

        # Predict index
        idx = model.predict(X_input)[0]

        # Retrieve plans
        workout_plan = df.loc[idx, "workout_plan"]
        diet_plan = df.loc[idx, "diet_plan"]

        # Save user + plan to SQLite
        conn = sqlite3.connect(DB_FILE)
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO user_plans
            (name, email, age_group, gender, height_category, weight_category,
             gymorhome, goal, budget, workout_plan, diet_plan)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (
            name, email, age, gender, height, weight,
            gymorhome, goal, budget, workout_plan, diet_plan
        ))
        conn.commit()
        conn.close()

        return jsonify({"workout": workout_plan, "diet": diet_plan})

    except Exception as e:
        return jsonify({"error": str(e)}), 500

# ------------------------------
# Main entry
# ------------------------------
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    print(f"Starting server on port {port}")
    serve(app, host="0.0.0.0", port=port)
