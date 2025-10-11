import React, { useState } from "react";

export default function Navbar() {
  const [menuOpen, setMenuOpen] = useState(false);

  return (
    <nav className="navbar">
      <h1>AI Fitness</h1>

      <ul className={`nav-links ${menuOpen ? "open" : ""}`}>
        <li><a href="#form">Start</a></li>
        <li><a href="#plans">Plans</a></li>
        <li><a href="#footer">Contact</a></li>
      </ul>

      <div className="hamburger" onClick={() => setMenuOpen(!menuOpen)}>
        <div className={`bar1 ${menuOpen ? "change" : ""}`}></div>
        <div className={`bar2 ${menuOpen ? "change" : ""}`}></div>
        <div className={`bar3 ${menuOpen ? "change" : ""}`}></div>
      </div>
    </nav>
  );
}
