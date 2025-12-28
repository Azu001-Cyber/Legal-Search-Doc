import React from "react";
import Hero from "../components/hero";
import NavBar from "../components/navbar";
import Footer from "../components/Footer";
import CTA from "../components/cta";

export default function LandingPage(){
    return (
        <div>
            <NavBar/>
            <main className="site-container">
                <Hero/>
                <CTA/>
            </main>
            <Footer/>
        </div>
    )
}