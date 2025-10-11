import pandas as pd
import random

# -----------------------------
# Feature options
# -----------------------------
age_groups = ["teen", "young", "middle", "senior"]
genders = ["male", "female"]
height_categories = ["short", "medium", "tall"]
weight_categories = ["underweight", "normal", "overweight", "obese"]
gym_home = ["gym", "home"]
goals = ["weight-loss", "muscle-gain", "stamina", "flexibility"]
budgets = ["low", "medium", "high"]
diet_types = ["vegetarian", "vegan", "non-vegetarian"]

# -----------------------------
# Workout templates per goal
# -----------------------------
workouts_gym = {
    "weight-loss": ["Treadmill HIIT", "Cross Trainer", "Rowing Machine", "Battle Ropes", "Spinning"],
    "muscle-gain": ["Squat Rack", "Bench Press", "Deadlift", "Pull-up Bar", "Leg Press"],
    "stamina": ["Elliptical", "Jump Rope", "Circuit Training", "Stair Climber", "HIIT Treadmill"],
    "flexibility": ["Yoga Machines", "Pilates Machines", "Stretching", "Balance Boards", "Core Machines"]
}

workouts_home = {
    "weight-loss": ["Jumping Jacks", "Burpees", "Mountain Climbers", "High Knees", "Bodyweight Circuit"],
    "muscle-gain": ["Push-ups", "Pull-ups", "Squats", "Lunges", "Resistance Bands"],
    "stamina": ["Jump Rope", "HIIT Cardio", "Burpees", "Running in Place", "Bodyweight Circuit"],
    "flexibility": ["Yoga Flow", "Stretching", "Pilates Mat", "Balance Exercises", "Mobility Drills"]
}

# -----------------------------
# Diet templates per goal & type
# -----------------------------
diet_base = {
    "vegetarian": {
        "weight-loss": ["Oats + Skim Milk + Banana", "Vegetable Salad + Quinoa", "Fruit + Nuts", "Lentil Soup + Veggies"],
        "muscle-gain": ["Paneer + Brown Rice", "Chickpeas + Quinoa", "Nuts + Smoothie", "Tofu Stir Fry + Veggies"],
        "stamina": ["Smoothie + Oats", "Vegetable Wraps + Rice", "Fruit + Nuts", "Vegetable Soup + Bread"],
        "flexibility": ["Oatmeal + Soy Milk", "Salads + Tofu", "Fruit + Yogurt", "Veg Stir Fry + Rice"]
    },
    "vegan": {
        "weight-loss": ["Oatmeal + Almond Milk", "Lentil Salad + Veg", "Fruit + Nuts", "Tofu Soup + Veggies"],
        "muscle-gain": ["Tofu + Quinoa", "Chickpeas + Brown Rice", "Nuts + Smoothie", "Tempeh Stir Fry + Veggies"],
        "stamina": ["Smoothie Bowl", "Veg Wrap + Rice", "Fruit + Nuts", "Veggie Soup + Bread"],
        "flexibility": ["Oatmeal + Soy Milk", "Salads + Tofu", "Fruit + Almond Yogurt", "Veg Stir Fry + Rice"]
    },
    "non-vegetarian": {
        "weight-loss": ["Eggs + Oats + Milk", "Chicken + Rice + Veg", "Protein Shake + Nuts", "Fish + Sweet Potato"],
        "muscle-gain": ["Chicken Breast + Brown Rice", "Eggs + Quinoa", "Protein Shake + Nuts", "Fish Stir Fry + Veggies"],
        "stamina": ["Egg Omelette + Toast", "Grilled Chicken + Rice", "Fruit + Nuts", "Fish Soup + Veggies"],
        "flexibility": ["Eggs + Oats", "Chicken Salad + Quinoa", "Protein Shake + Nuts", "Fish + Veg Stir Fry"]
    }
}

# -----------------------------
# Helper functions for realistic choices
# -----------------------------
def realistic_goal(age, weight):
    if age in ["teen", "young"]:
        return random.choices(goals, weights=[0.3,0.3,0.3,0.1])[0]
    elif age == "middle":
        return random.choices(goals, weights=[0.3,0.3,0.2,0.2])[0]
    else:  # senior
        return random.choices(goals, weights=[0.4,0.1,0.2,0.3])[0]

def realistic_gym_home(budget):
    if budget == "high":
        return random.choices(gym_home, weights=[0.7,0.3])[0]
    elif budget == "medium":
        return random.choices(gym_home, weights=[0.5,0.5])[0]
    else:
        return random.choices(gym_home, weights=[0.3,0.7])[0]

def realistic_diet(goal, diet_type):
    diet_list = diet_base[diet_type][goal]
    # Randomly shuffle for each user to make it less repetitive
    return random.sample(diet_list * 2, 7)  # 7 meals a week

def realistic_workout(goal, gym_or_home):
    workouts_list = workouts_gym[goal] if gym_or_home == "gym" else workouts_home[goal]
    return random.sample(workouts_list * 2, 7)  # 7 days a week

# -----------------------------
# Generate dataset
# -----------------------------
rows = 30000
data = []

for _ in range(rows):
    age = random.choice(age_groups)
    gender = random.choice(genders)
    height = random.choice(height_categories)
    weight = random.choice(weight_categories)
    budget = random.choice(budgets)
    
    goal = realistic_goal(age, weight)
    gym_or_home = realistic_gym_home(budget)
    diet_type = random.choice(diet_types)
    
    # Workout plan
    workouts_list = realistic_workout(goal, gym_or_home)
    weekly_workout = "; ".join([f"{day}: {workouts_list[i]}" for i, day in enumerate(["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"])])
    
    # Diet plan
    diet_list = realistic_diet(goal, diet_type)
    weekly_diet = "; ".join([f"{meal}: {diet_list[i]}" for i, meal in enumerate(["Breakfast","Lunch","Snacks","Dinner","Breakfast2","Lunch2","Snacks2"])])
    
    data.append([age, gender, height, weight, gym_or_home, goal, budget, diet_type, weekly_workout, weekly_diet])

# -----------------------------
# Save CSV
# -----------------------------
df = pd.DataFrame(data, columns=["age_group","gender","height_category","weight_category",
                                 "gymorhome","goal","budget","diet_type","workout_plan","diet_plan"])
df.to_csv("workout_diet_dataset_realistic.csv", index=False)
print("✅ Realistic dataset generated with 30,000 rows!")
