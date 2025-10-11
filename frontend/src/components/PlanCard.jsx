import React from "react";
import { MdRestaurant, MdFitnessCenter } from "react-icons/md";

export default function PlanCard({ title, content, type }) {
  // Parse backend content
  const parsePlan = (planStr) => {
    const planObj = {};
    planStr.split(";").forEach((item) => {
      const [key, val] = item.split(":");
      if (key && val) {
        const cleanKey = key.trim().replace(/[0-9]/g, ""); // remove numbers
        if (!planObj[cleanKey]) {
          planObj[cleanKey] = val.trim(); // only first occurrence
        }
      }
    });
    return planObj;
  };

  const plan = parsePlan(content);

  if (type === "diet") {
    const meals = Object.keys(plan);
    const mealColors = {
      Breakfast: "#fde68a", // yellow
      Lunch: "#bbf7d0",     // green
      Snacks: "#fbcfe8",    // pink
      Dinner: "#c7d2fe"     // purple
    };

    return (
      <div className="plan-card">
        <h2 className="text-2xl font-bold mb-4 flex items-center gap-2 text-green-600">
          <MdRestaurant size={28} /> {title}
        </h2>
        <table className="min-w-full text-center border-collapse shadow-lg rounded-lg">
          <tbody>
            {meals.map((meal) => (
              <tr key={meal} style={{ backgroundColor: mealColors[meal] || "#f3f4f6" }}>
                <td className="px-4 py-2 font-semibold border">{meal}</td>
                <td className="px-4 py-2 border">{plan[meal]}</td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    );
  }

  // Workout Plan Table
  const days = Object.keys(plan);
  const workoutColors = ["#dbeafe", "#bfdbfe", "#93c5fd", "#60a5fa", "#3b82f6", "#2563eb", "#1e40af"];

  return (
    <div className="plan-card">
      <h2 className="text-2xl font-bold mb-4 flex items-center gap-2 text-blue-600">
        <MdFitnessCenter size={28} /> {title}
      </h2>
      <table className="min-w-full border-collapse text-center shadow-lg rounded-lg">
        <thead>
          <tr>
            {days.map((day, idx) => (
              <th
                key={day}
                className="px-4 py-2 border text-white"
                style={{ backgroundColor: workoutColors[idx % workoutColors.length] }}
              >
                {day}
              </th>
            ))}
          </tr>
        </thead>
        <tbody>
          <tr>
            {days.map((day, idx) => (
              <td
                key={day}
                className="px-4 py-2 border font-semibold"
                style={{ backgroundColor: workoutColors[idx % workoutColors.length] + "aa" }}
              >
                {plan[day]}
              </td>
            ))}
          </tr>
        </tbody>
      </table>
    </div>
  );
}
