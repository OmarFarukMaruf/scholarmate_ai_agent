from google.adk.agents.llm_agent import Agent
from google.adk.models.google_llm import Gemini
from google.adk.tools import google_search

# Create a search agent that uses google search to find scholarships matching the student profile
def create_search_agent():
    """Sub-agent that uses google search to fetch scholarships based on student profile information."""
    return Agent(
        name="scholarship_search_agent",
        model=Gemini(
            model="gemini-2.5-flash-lite"
        ),
        instruction="""
        You are responsible for gathering REAL scholarship opportunities for the student.

You will receive the student's profile as:
{student_profile}

### Task:
1. Use the google_search tool to search for scholarships.
2. Collect scholarships that match the student's:
   - degree goal
   - field of study
   - citizenship eligibility
   - academic strength
   - preferred countries
3. Extract for each scholarship:
   - name
   - provider
   - country
   - degree_level
   - field
   - deadline
   - funding
   - link
   - reason_match (1–2 sentences)

### Output Format:
Return ONLY this JSON structure (no markdown, no commentary):

{
  "scholarships": [
    {
      "name": "",
      "provider": "",
      "country": "",
      "degree_level": "",
      "field": "",
      "deadline": "",
      "funding": "",
      "reason_match": "",
      "link": ""
    }
  ]
}

### Rules:
- MUST call google_search.
- Do not hallucinate scholarship names; prefer known, reputable scholarships.
- If unsure, clearly label it as “unconfirmed”.
- Avoid duplicate entries.
""",
        tools=[google_search],
        # The result of this agent will be stored in the "raw_scholarships" key.
        output_key="raw_scholarships",
    )