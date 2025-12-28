import React from "react";
import { CiSearch } from "react-icons/ci";
import { Link } from 'react-router-dom';
import "../css/hero.css";



const Hero = () => {
    return (
        <section className="hero-section">
            <div className="hero-card">

                <div className="hero-text">
                    <h1>
                        Find Legal Documents <br />
                        <span>In Seconds</span>
                    </h1>
                    <p>
                        Search through millions of legal
                        documents, case law, and statues
                        with our intelligent search engine.Built for legal professional who value
                        precision and speed.
                    </p>
                </div>

                <Link to="/app" className="lp-btn">
                    <CiSearch /> Start Searching
                </Link>
            </div>

        </section>
    )
}

export default Hero;