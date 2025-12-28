import React from "react";
import { PiArrowRightLight } from "react-icons/pi";
import { Link } from 'react-router-dom';
import "../css/cta.css";

const CTA = () => {
    return (
        <section className="cta-section">
            <div className="cta-card">
                
                <div className="cta-text">
                    <h2>Ready to Transform Your Legal Research?</h2>
                    <p>
                        Join thousands of legal professionals who trust LegalSearch for faster, more
                        accurate document discovery.
                    </p>
                </div>

                <Link to="/app" className="cta-btn">
                    Get Started <PiArrowRightLight />
                </Link>
            </div>
        </section>
    )
}
export default CTA;