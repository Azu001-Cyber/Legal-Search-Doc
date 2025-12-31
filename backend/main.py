
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



load_dotenv()
AI_API_KEY = os.getenv("GOOGLE_GEMINI_API_KEY")


app = FastAPI()

# url that are allowed to make requests
origins = [
        "http://localhost:5173",
        "http://localhost:5175", 
        "https://legal-search-doc.vercel.app",
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
                THIS NON-DISCLOSURE AGREEMENT is made on 03/02/2026 between:

                1. PartyA_Name, located at PartyA_Address
                AND
                2. PartyB_Name, located at PartyB_Address

                Both parties agree to keep confidential all shared information including but not limited to
                trade secrets, intellectual property, strategies, and any sensitive data.

                Obligations:
                - Confidential information shall not be shared with third parties.
                - Information must not be used outside the permitted purpose.
                - This agreement remains in force for 3 years.

                Signatures:
                ______________________  ______________________
                PartyA_Name           PartyB_Name
                """,
                "date": "03/02/2026"
        },

        "doc2": {
                "title": "Service Agreement",
                "content": """
                SERVICE AGREEMENT made on 8/04/2025.

                This agreement is between:
                Service Provider: John Doe
                Client: Jake Amon

                Scope of Service:
                - 6 months

                Terms:
                - Payment: $50,000 due upon completion/delivery.
                - Duration: 3 months
                - Termination: Either party may terminate with written notice.

                Signatures:
                ______________________  ______________________
                John Doe        Jake Amon
                """,
                "date": "8/04/2025"
        },

        "doc3": {
                "title": "Employment Offer Letter",
                "content": """
                EMPLOYMENT OFFER LETTER
                Date: 12/07/2025

                Dear Josh Athans,

                We are pleased to offer you the position of Web developer at Linax. 

                Details:
                - Start Date: 20/07/2025
                - Salary: $2,000
                - Work Location: California
                - Benefits: PTO, 401k 

                Please sign below to confirm acceptance of this offer.

                Accepted By:
                ______________________
                Ada matthew
                Date: ________________
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