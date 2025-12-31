
"""
Docstring for backend.app.api
the task, have the api return a document based on the query input.
'my solution' is to write a query search that returns a particular doc based on the input 'keyword'
"""
from fastapi import FastAPI, Query
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
import os
from pydantic import BaseModel
from dotenv import load_dotenv
import httpx



# load_dotenv()
AI_API_KEY = os.getenv("GOOGLE_GEMINI_API_KEY")


app = FastAPI()

# url that are allowed to make requests
origins = [
        "https://legal-search-doc.vercel.app",
        "http://localhost:5173",
        "http://localhost:5175", 
        
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
                NON-DISCLOSURE AGREEMENT
                Effective Date: 03/02/2026

                This Agreement is entered into between:

                - **PartyA_Name**, of PartyA_Address
                - **PartyB_Name**, of PartyB_Address

                (Collectively referred to as "the Parties".)

                Purpose:
                The Parties acknowledge that, throughout the course of their interaction, certain private, confidential,
                or proprietary information may be exchanged. This agreement exists to ensure such information remains
                protected.

                Confidentiality Obligations:
                1. Any confidential material shared between the Parties shall not be disclosed, copied, or transferred
                to any third party without prior written approval.
                2. Information obtained under this Agreement shall only be used for the intended business purpose.
                3. Both Parties must take reasonable steps to prevent unauthorized access or disclosure.

                Term & Duration:
                This Agreement shall remain valid and enforceable for **three (3) years** from the effective date,
                unless terminated earlier by mutual written consent.

                Signatures:
                ____________________________        ____________________________
                PartyA_Name                         PartyB_Name
                """,
                "date": "03/02/2026"
        },

        "doc2": {
                "title": "Service Agreement",
                "content": """
                SERVICE AGREEMENT
                Date: 8/04/2025

                This Agreement is established between the following parties:

                - **Service Provider:** John Doe  
                - **Client:** Jake Amon  

                Purpose of Agreement:
                The Client is engaging the Service Provider to perform professional services as discussed and agreed
                upon by both parties. The services will be carried out over a working period of **six (6) months**.

                Terms & Conditions:
                1. **Compensation:** The total fee for the services rendered shall be **$50,000**, to be paid upon final
                delivery and acceptance of the completed work.
                2. **Project Duration:** Services are expected to be completed within a period of **three (3) months**
                from the start date, unless otherwise extended by mutual consent.
                3. **Termination Clause:** Either party retains the right to end this Agreement by issuing a formal
                written notice prior to termination.

                Signatures of Agreement:
                _________________________________        _________________________________
                John Doe, Service Provider              Jake Amon, Client
                """,
                "date": "8/04/2025"
        },

        "doc3": {
                "title": "Employment Offer Letter",
                "content": """
                EMPLOYMENT OFFER LETTER
                Date: 12/07/2025

                Dear Josh Athans,

                We are pleased to extend an official offer for the role of **Web Developer** at **Linax**. Your skills
                and experience align with our goals, and we look forward to having you contribute to our team.

                Position & Compensation Details:
                - **Commencement Date:** 20/07/2025
                - **Monthly Salary:** $2,000
                - **Primary Work Location:** California
                - **Employee Benefits:** Paid Time Off (PTO), 401k plan, and other standard company benefits

                Next Steps:
                Kindly review the above details. To indicate your acceptance of this employment offer, please sign
                and date the acknowledgment below.

                Confirmation of Acceptance:
                ___________________________________
                Ada Matthew
                Date: _____________________________
                """,
                "date": "12/07/2025"
        }
}


# Pydantic model for response
class DocumentResponse(BaseModel):
        title: str
        content: str
        summary: str



# # Function to generate summary
# def generate_summary(text: str) -> str:
#         GEMINI_ENDPOINT = "https://generativeai.googleapis.com/v1beta2/models/text-bison-001:generateText"
#         headers = {
#                 "Content-Type": "application/json",
#                 "Authorization": f"Bearer {AI_API_KEY}"
#         }
#         data = {
#         "prompt": f"Summarize this document in a concise paragraph:\n\n{text}",
#         "temperature": 0.5,
#         "maxOutputTokens": 150
#         }

#         with httpx.Client(timeout=30) as client:
#                 response = client.post(GEMINI_ENDPOINT, json=data, headers=headers)
#                 response.raise_for_status()
#                 summary = response.json()["candidates"][0]["content"].strip()
#                 return summary


@app.get('/document/search', response_model=dict)
async def get_document(q:str=Query(..., description="Search text")):
        results = []
        for doc_id, doc in documents.items():
                if q.lower() in doc["title"].lower():
                        # summary = generate_summary(doc["content"])
                        results.append(
                                {
                                "title": doc["title"],
                                "content": doc["content"],
                                # "summary": summary
                                }
                        )
        if results:
                return JSONResponse(content={"matches":results})
        return JSONResponse(content={'matches':[]})