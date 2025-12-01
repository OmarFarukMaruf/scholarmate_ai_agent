from google.adk.agents import LlmAgent
from google.adk.models import Gemini
from google.adk.tools.load_memory_tool import load_memory

def create_ranking_agent() -> LlmAgent:
    return LlmAgent(
        name="scholarship_ranking_agent",
        model=Gemini(model="gemini-2.5-flash-lite"),
        description="Filters and ranks scholarships for best match.",
        instruction="""
You are the Scholarship Ranking Agent.

Inputs:
- student_profile JSON
- raw_scholarships JSON list

Steps:
1. Optionally call `load_memory` to recall past liked/rejected scholarships.
2. Remove duplicates and irrelevant entries.
3. Score each scholarship 0–100 based on:
   - Eligibility (citizenship, level, field)
   - Funding generosity
   - Deadline (still open)
   - Preferred countries and target field.

Output: ONLY this JSON:

{
  "ranked_scholarships": [
    {
      "name": "",
      "provider": "",
      "country": "",
      "level": "",
      "field": "",
      "deadline": "",
      "funding": "",
      "match_score": 0,
      "reason_match": "",
      "link": ""
    }
  ]
}

Rules:
- Sort by match_score descending.
- No markdown or extra text outside JSON.
""",
        tools=[load_memory],
        output_key="ranked_scholarships",
    )