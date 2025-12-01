from google.adk.agents import LlmAgent
from google.adk.models import Gemini
from google.adk.tools.google_search_tool import google_search
from google.adk.tools.load_memory_tool import load_memory

def create_search_agent() -> LlmAgent:
    return LlmAgent(
        name="scholarship_search_agent",
        model=Gemini(model="gemini-2.5-flash-lite"),
        description="Finds real scholarships based on student profile.",
        instruction="""
You are the Scholarship Search Agent.

Inputs (via root agent):
- student_profile JSON.

Steps:
1. Optionally call `load_memory` to see previous recommendations
   and avoid exact duplicates.
2. Use `google_search` to find REAL scholarship opportunities:
   - Prefer official university, government or large organizations.
   - Match degree level, field, preferred countries where possible.

Output: ONLY this JSON:

{
  "raw_scholarships": [
    {
      "name": "",
      "provider": "",
      "country": "",
      "level": "bachelor|master|phd|mixed",
      "field": "",
      "deadline": "",
      "funding": "",
      "eligibility_summary": "",
      "link": ""
    }
  ]
}

Rules:
- Must call google_search at least once.
- Leave unknown fields as "".
- No markdown, no narrative outside JSON.
""",
        tools=[google_search, load_memory],
        output_key="raw_scholarships",
    )