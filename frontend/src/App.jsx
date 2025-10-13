import React, { useState } from "react";
import Navbar from "./components/Navbar";
import InputForm from "./components/InputForm";
import PlanCard from "./components/PlanCard";

export default function App() {
  const [plan, setPlan] = useState(null);
  const [showForm, setShowForm] = useState(false);
  const [loading, setLoading] = useState(false);
  const [showUserForm, setShowUserForm] = useState(true);
  const [user, setUser] = useState({ name: "", email: "" });

  // Handle user info submission
  const handleUserSubmit = (e) => {
    e.preventDefault();
    if (user.name && user.email) {
      setShowUserForm(false);
      setShowForm(true);
    }
  };

  const handleGenerate = async (formData) => {
    setLoading(true);
    try {
      const res = await fetch(`${process.env.REACT_APP_BACKEND_URL}/generate_plan`, {
  method: "POST",
  headers: { "Content-Type": "application/json" },
  body: JSON.stringify(formData),
});


      if (!res.ok) throw new Error(`HTTP error! Status: ${res.status}`);
      const data = await res.json();
      setPlan(data);
      setShowForm(false);
      document.getElementById("plans")?.scrollIntoView({ behavior: "smooth" });
    } catch (error) {
      console.error(error);
      alert("Failed to generate plan. Check backend.");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="min-h-screen bg-gray-50">
      <Navbar />

      {/* Hero Section */}
      <section className="hero relative text-center py-20 px-4 bg-gradient-to-r from-blue-500 to-purple-600 min-h-[80vh] flex flex-col justify-center items-center">
        <h1 className="text-4xl md:text-5xl font-extrabold mb-6 text-white">
          Achieve Your Fitness Goals with AI
        </h1>
        <p className="text-lg md:text-xl text-white mb-8 max-w-xl">
          Personalized Workout & Diet Plans tailored to your goal, budget, and lifestyle
        </p>

        {showUserForm && (
          <div className="bg-white rounded-3xl shadow-2xl p-10 max-w-lg w-full transform hover:scale-105 transition-transform">
            <h2 className="text-2xl font-bold text-gray-800 mb-6 text-center">
              Let's Get Started
            </h2>
            <form onSubmit={handleUserSubmit} className="flex flex-col gap-5">
              <input
                type="text"
                placeholder="Your Name"
                value={user.name}
                onChange={(e) => setUser({ ...user, name: e.target.value })}
                className="border border-gray-300 rounded-xl px-5 py-3 focus:outline-none focus:ring-2 focus:ring-blue-500 text-lg"
                required
              />
              <input
                type="email"
                placeholder="Email ID"
                value={user.email}
                onChange={(e) => setUser({ ...user, email: e.target.value })}
                className="border border-gray-300 rounded-xl px-5 py-3 focus:outline-none focus:ring-2 focus:ring-blue-500 text-lg"
                required
              />
              <button
                type="submit"
                className="bg-blue-600 text-white font-bold py-3 rounded-full shadow-lg hover:bg-blue-700 transition-colors text-lg"
              >
                Continue
              </button>
            </form>
          </div>
        )}

        {!showUserForm && !showForm && (
          <button
            className="bg-white text-blue-600 font-bold py-3 px-8 rounded-full shadow-lg hover:scale-105 transition-transform text-lg"
            onClick={() => setShowForm(true)}
          >
            Start Planning
          </button>
        )}

        {/* Background circles */}
        <div className="absolute w-48 h-48 bg-yellow-300 rounded-full top-0 right-10 opacity-40 -z-10"></div>
        <div className="absolute w-64 h-64 bg-red-400 rounded-full bottom-0 left-10 opacity-30 -z-10"></div>
      </section>

      {/* Input Form */}
      {showForm && (
        <section id="form" className="form-container py-8">
          <InputForm onGenerate={handleGenerate} />
        </section>
      )}

      {/* Loading Spinner */}
      {loading && (
        <div className="spinner-container flex justify-center items-center py-20">
          <div className="spinner w-16 h-16 border-4 border-blue-300 border-t-blue-600 rounded-full animate-spin"></div>
        </div>
      )}

      {/* Plan Cards */}
      {plan && !loading && (
        <section
          id="plans"
          className="plans-container grid grid-cols-1 md:grid-cols-2 gap-6 px-4 md:px-20 py-10"
        >
          <PlanCard title="Workout Plan" content={plan.workout} type="workout" />
          <PlanCard title="Diet Plan" content={plan.diet} type="diet" />
        </section>
      )}

      {/* Footer */}
      <footer className="bg-gray-800 text-gray-200 text-center py-6 mt-10">
        <p>© 2025 AI Fitness Planner. All rights reserved.</p>
        <p>Built with ❤️ using React & Flask</p>
      </footer>
    </div>
  );
}

