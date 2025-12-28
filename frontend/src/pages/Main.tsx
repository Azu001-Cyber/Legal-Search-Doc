import React from "react";
import LegalSearch from "../components/legalSearch";
import NavBar from "../components/navbar";
import Footer from "../components/Footer";



export default function Main(){
    return (
        // Main app components
        <div className="site-container">
            <NavBar/>
            <LegalSearch/>
            <Footer/>
        </div>
    )

    
}