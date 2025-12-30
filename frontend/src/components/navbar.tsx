
import '../css/navbar.css';
import { CiSearch } from "react-icons/ci";
import { Link } from 'react-router-dom';


// import Container from 'react-bootstrap/Container';
// import Nav from 'react-bootstrap/Nav';
// import Navbar from 'react-bootstrap/Navbar';


const NavBar = () => {
    return (
        // <Navbar expand='lg' className="navbar-container">
        //     <Container>
        //         <Navbar.Brand>
        //             <Link to={"/"} className="nav-link-container">
        //                 <img src="/legal_logo.svg" alt="Brand Logo" className="brandLogo"  />
        //                 <p> LegalSearch </p>
        //             </Link>
        //         </Navbar.Brand>

        //         <Navbar.Toggle aria-controls='basic-navbar-nav'/>

        //         <Navbar.Collapse id='basic-navbar-nav'>
        //             <Nav className='me-auto'>
        //                 <Nav.Link href='/'>Home</Nav.Link>
        //                 <Nav.Link href='/app' className='search'><CiSearch/>Search</Nav.Link>
        //             </Nav>
        //         </Navbar.Collapse>
        //     </Container>

        // </Navbar>
        <nav className="navbar-container">

            <div className="brandLogo">
                <Link to={"/"} className="nav-link-container">
                <img src="/legal_logo.svg" alt="Brand Logo" className="brandLogo"  />
                <p> LegalSearch </p>
                </Link>
            </div>

            <ul className="nav-bar">
                <li><Link to={"/"}>Home</Link></li>
                <li className="search"><Link to={"/app"}><CiSearch/>Search</Link></li>
            </ul>
        </nav>
    );
};

export default NavBar;