import { useState } from 'react'
// import Footer from './components/Footer'
// import NavBar from './components/navbar'
// import Hero from './components/hero'
// import CTA from './components/cta'
import './App.css'
import { BrowserRouter as Router, Routes, Route} from 'react-router-dom';
import LandingPage from './pages/LandingPage'
import Main from './pages/Main'


function App() {
  return (

    <Router>
      <Routes>
        {/* Landing Page (Root URL) */}
        <Route path='/' element={<LandingPage/>} />

        {/* Main App/Dashboard (Different URL) */}
        <Route path='/app/' element={<Main/>}/>

      </Routes>
    </Router>
      // <div className="site-container">
      // </div>
  )
}

export default App;