import React  from "react";
import "../css/footer.css"

const Footer = () => {
    return (
        <footer className="site-footer">
            <div className="footer-container">

                <div className="footer-brandLogo">
                    <a href="/" className="nav-link-container">
                    <img src="/legal_logo-light.svg" alt="Brand Logo" className="brandLogo-footer"  />
                    <p>LegalSearch</p>
                    </a>
                </div>

                <div className="footer-inner-container">
                    <div className="quotes">
                        <p>Reliable</p>
                        <p>Secure</p>
                        <p>Trustworthy</p>
                    </div>

                    {/* <div className="footer-links">
                        <a href="/about">Privacy</a>
                        <a href="/contact">Terms</a>
                        <a href="/privacy">Contact</a>
                    </div> */}
                </div>

                <hr />
                <p className="signout">&copy; {new Date().getFullYear()} LegalSearch, All rights reserved.</p>
            </div>
        </footer>
    )

}

export default Footer;