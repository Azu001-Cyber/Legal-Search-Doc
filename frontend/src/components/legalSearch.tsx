import { useState } from "react";
import { CiSearch } from "react-icons/ci";
import '../css/legalsearch.css'




const LegalSearch = () => {
    
    const [query, setQuery] = useState("");
    const [results, setResult] = useState<[]>([]);

    // const [inputValue, setInputValue] = useState('');

    const handleChange = (event:React.ChangeEvent<HTMLInputElement>) => {
        setQuery(event.target.value);
    }

    const handleSubmit = async (event:React.FormEvent<HTMLFormElement>) => {
        event.preventDefault();
    }

    try {
        const response = await fetch("http://localhost:8000//document/search?q=${query}")
        const data = await response.json();
        setResult(data.matches || []);
    } catch (error) {
        console.error("Error fetching document:", error);
        setResult([]);
    }

    return (
        <div className="container">
            <section className="hero">
                <img src="legal_logo.svg" alt="Brand Logo" className="main-page-logo" />

                <h1>Legal Document Search</h1>
                <p>AI-Powered legal research assistant for intelligent document search and analysis</p>
            </section>

            {/* Input Section */}
            <section className="input-container">

                <form action="" method="get" onSubmit={handleSubmit}>

                    <input type="text" value={query} onChange={handleChange} placeholder="Enter your legal query..."/>

                    <button type="submit" className="lp-btn">
                        <CiSearch />
                        Search
                    </button>
                </form>

            </section>
            {/* Output Section */}
            <section className="output-container">

                <h3>Available Documents</h3>

                <div>
                    {results.length === 0 ? ( 
                    <article>
                        <img src="legal_logo.svg" alt="" className="output-logo" />
                        <p>No Document available yet.</p>
                    </article>
                    ):(
                        results.map((doc) =>(
                            <article key={doc.id}>
                                <img src="legal_logo.svg" alt="" className="output-logo"/>
                                { <h4>{doc.title}</h4> }
                                { <p>{doc.content}</p> }
                            </article>
                        ))
                    )}
                </div>

            </section>

        </div>
    )
};

export default LegalSearch;