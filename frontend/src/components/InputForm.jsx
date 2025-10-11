import React, { useState } from "react";

export default function InputForm({ onGenerate }) {
  const [formData, setFormData] = useState({
    age_group: "young",
    gender: "male",
    height_category: "medium",
    weight_category: "normal",
    gymorhome: "gym",
    goal: "weight-loss",
    diet: "vegetarian",
    budget: "medium"
  });

  const handleChange = (e) => {
    setFormData({ ...formData, [e.target.name]: e.target.value });
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    onGenerate(formData);
  };

  return (
    <form onSubmit={handleSubmit}>
      <label>Age Group</label>
      <select name="age_group" value={formData.age_group} onChange={handleChange}>
        <option value="teen">Teen</option>
        <option value="young">Young Adult</option>
        <option value="middle">Middle Age</option>
        <option value="senior">Senior</option>
      </select>

      <label>Gender</label>
      <select name="gender" value={formData.gender} onChange={handleChange}>
        <option value="male">Male</option>
        <option value="female">Female</option>
      </select>

      <label>Height Category</label>
      <select name="height_category" value={formData.height_category} onChange={handleChange}>
        <option value="short">Short</option>
        <option value="medium">Medium</option>
        <option value="tall">Tall</option>
      </select>

      <label>Weight Category</label>
      <select name="weight_category" value={formData.weight_category} onChange={handleChange}>
        <option value="underweight">Underweight</option>
        <option value="normal">Normal</option>
        <option value="overweight">Overweight</option>
        <option value="obese">Obese</option>
      </select>

      <label>Workout Location</label>
      <select name="gymorhome" value={formData.gymorhome} onChange={handleChange}>
        <option value="gym">Gym</option>
        <option value="home">Home</option>
      </select>

      <label>Fitness Goal</label>
      <select name="goal" value={formData.goal} onChange={handleChange}>
        <option value="weight-loss">Weight Loss</option>
        <option value="muscle-gain">Muscle Gain</option>
        <option value="stamina">Stamina</option>
        <option value="flexibility">Flexibility</option>
      </select>

      <label>Diet Preference</label>
      <select name="diet" value={formData.diet} onChange={handleChange}>
        <option value="vegetarian">Vegetarian</option>
        <option value="vegan">Vegan</option>
        <option value="non-vegetarian">Non-Vegetarian</option>
      </select>

      <label>Budget</label>
      <select name="budget" value={formData.budget} onChange={handleChange}>
        <option value="low">Low</option>
        <option value="medium">Medium</option>
        <option value="high">High</option>
      </select>

      <button type="submit" className="btn-submit">Generate Plan</button>
    </form>
  );
}
