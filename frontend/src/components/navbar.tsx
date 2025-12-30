
import '../css/navbar.css';
import { CiSearch } from "react-icons/ci";
import { Link } from 'react-router-dom';

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
                <li><Link to={"/"}>Home</Link></li>
                <li className="search"><Link to={"/app"}><CiSearch/>Search</Link></li>
            </ul>
        </nav>
    );
};

export default NavBar;