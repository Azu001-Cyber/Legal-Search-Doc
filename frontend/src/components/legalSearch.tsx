import React, { useState } from "react";
import { CiSearch } from "react-icons/ci";
import '../css/legalsearch.css'


const LegalSearch = () => {
    const [inputValue, setInputValue] = useState('');

    const handleChange = (event:React.ChangeEvent<HTMLInputElement>) => {
        setInputValue(event.target.value);
    }

    const handleSubmit = (event:React.FormEvent<HTMLFormElement>) => {
        event.preventDefault();
    }

    return (
        <div className="container">
            <section className="hero">
                <img src="legal_logo.svg" alt="Brand Logo" className="main-page-logo" />

                <h1>Legal Document Search</h1>
                <p>AI-Powered legal research assistant for intelligent document search and analysis</p>
            </section>

            <section className="input-container">

                <form action="" method="get" onSubmit={handleSubmit}>

                    <input type="text" value={inputValue} onChange={handleChange} placeholder="Enter your legal query..."/>

                    <button type="submit" className="lp-btn">
                        <CiSearch />
                        Search
                    </button>
                </form>

            </section>

            <section className="output-container">

                <h3>Available Documents</h3>

                <div>
                    <article>
                        <img src="legal_logo.svg" alt="" className="output-logo" />
                        <p>No Document available yet.</p>
                    </article>
                </div>

            </section>

        </div>
    )

}

export default LegalSearch;