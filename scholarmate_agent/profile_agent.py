# collect complete student background interactively, ask follow-up questions and finally output a single clean JSON object
# then use that JSON object to find scholarships
from google.adk.agents.llm_agent import Agent
from google.adk.models.google_llm import Gemini

def create_profile_agent():
    return Agent(
        name="student_profile_agent",
        model=Gemini(
            model="gemini-2.5-flash-lite"
        ),
        description="An agent that collects student profile information interactively.",
        instruction="""
Your job is to collect the student's academic background for scholarship matching.

### Workflow:
1. Ask follow-up questions until you have a complete profile.
2. When the profile is complete, output ONLY a JSON object (no text, no markdown).
3. Use snake_case for all fields.

### Required Fields:
{
  "full_name": "",
  "last_degree": "",
  "study_field": "",
  "cgpa": "",
  "grading_scale": "",
  "ielts_or_toefl": "",
  "work_experience_years": "",
  "citizenship_country": "",
  "current_country": "",
  "target_degree": "",
  "target_field": "",
  "preferred_countries": [],
  "publications_or_projects": "",
  "financial_need": "",
  "graduation_year": ""
}

### Rules:
- If any field is missing, ask a follow-up question.
- When all fields are available, respond with ONLY pure JSON.
- Do NOT include commentary, explanation, or markdown.
- Keep questions short and friendly.
        """,
        output_key="student_profile",
    )