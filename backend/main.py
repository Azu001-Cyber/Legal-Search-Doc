
"""
Docstring for backend.app.api
the task, have the api return a document based on the query input.
'my solution' is to write a query search that returns a particular doc based on the input 'keyword'
"""
from fastapi import FastAPI, Query
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# url that are allowed to make requests
origins = [
        "http://localhost:5173",
        "https://legal-search-doc.vercel.app/"
]

app.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
)

"""
The Following document mockup was made with AI
"""
documents = {
        "doc1": {
                "title": "Non-Disclosure Agreement (NDA)",
                "content": """
                THIS NON-DISCLOSURE AGREEMENT is made on {date} between:

                1. {PartyA_Name}, located at {PartyA_Address}
                AND
                2. {PartyB_Name}, located at {PartyB_Address}

                Both parties agree to keep confidential all shared information including but not limited to
                trade secrets, intellectual property, strategies, and any sensitive data.

                Obligations:
                - Confidential information shall not be shared with third parties.
                - Information must not be used outside the permitted purpose.
                - This agreement remains in force for {Duration} years.

                Signatures:
                ______________________  ______________________
                {PartyA_Name}           {PartyB_Name}
                """,
                "date": "{date}"
        },

        "doc2": {
                "title": "Service Agreement",
                "content": """
                SERVICE AGREEMENT made on {date}.

                This agreement is between:
                Service Provider: {Provider_Name}
                Client: {Client_Name}

                Scope of Service:
                - {Services_Description}

                Terms:
                - Payment: {Payment_Amount} due upon completion/delivery.
                - Duration: {Contract_Duration}
                - Termination: Either party may terminate with written notice.

                Signatures:
                ______________________  ______________________
                {Provider_Name}         {Client_Name}
                """,
                "date": "{date}"
        },

        "doc3": {
                "title": "Employment Offer Letter",
                "content": """
                EMPLOYMENT OFFER LETTER
                Date: {date}

                Dear {Employee_Name},

                We are pleased to offer you the position of {Job_Title} at {Company_Name}.

                Details:
                - Start Date: {Start_Date}
                - Salary: {Salary}
                - Work Location: {Location}
                - Benefits: {Benefits}

                Please sign below to confirm acceptance of this offer.

                Accepted By:
                ______________________
                {Employee_Name}
                Date: ________________
                """,
                "date": "{date}"
        }
}


@app.get('/document/search')
async def get_document(q:str=Query(..., description="Search text")):
        results = []
        for doc_id, doc in documents.items():
                if q.lower() in doc["content"].lower():
                    results.append({"id":doc_id, **doc})
        if results:
                return JSONResponse(content={"matches":results})
        return JSONResponse(content={'matches':[]})