# purpose: filter and rank scholarships returned by the search agent based on student profile
# inputs: raw scholarship and  student profile from profile agent
from google.adk.agents.llm_agent import Agent
from google.adk.models.google_llm import Gemini


def create_ranking_agent():
    """Sub-agent that ranks scholarships based on student profile information.
    It insures only high quality and trustworthy scholarships are returned to the user.
    """
    return Agent(
        name="scholarship_ranking_agent",
        model=Gemini(
            model="gemini-2.5-flash-lite"
        ),
        instruction="""
        You are the ranking engine for the scholarship finder system.

You will receive:
student profile: {student_profile}
raw scholarships: {raw_scholarships}

### Task:
1. Remove:
   - duplicate scholarships
   - fake/unverified or low-trust entries
   - scholarships unrelated to the student's field/degree/country eligibility

2. Rank scholarships using these priorities:
   - Eligibility match (citizenship + target degree)
   - Field of study relevance
   - Funding amount (full > partial)
   - Deadline recency
   - Academic strength requirement

3. Keep 5-7 high-quality scholarships.

### Output Format:
Return ONLY a JSON LIST (no wrapper):
[
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

### Rules:
- No markdown
- No extra explanation
- No hallucinating realistic details
- Keep only meaningful, helpful scholarships
""",
        output_key="ranked_scholarships",
    )
