import React from "react";
import '../css/navbar.css';
import { CiSearch } from "react-icons/ci";

const NavBar = () => {
    return (
        <nav className="navbar-container">

            <div className="brandLogo">
                <a href="/" className="nav-link-container">
                <img src="/legal_logo.svg" alt="Brand Logo" className="brandLogo"  />
                <p> LegalSearch </p>
                </a>
            </div>

            <ul className="nav-bar">
                <li><a href="/">Home</a></li>
                <li className="search"><a href="/app">< CiSearch/>Search</a></li>
            </ul>
        </nav>
    );
};

export default NavBar;