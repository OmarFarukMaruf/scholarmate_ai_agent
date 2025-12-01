from google.adk.agents import LlmAgent
from google.adk.models import Gemini
from google.adk.tools.load_memory_tool import load_memory

def create_profile_agent() -> LlmAgent:
    return LlmAgent(
        name="student_profile_agent",
        model=Gemini(model="gemini-2.5-flash-lite"),
        description="Collects and updates student's academic profile.",
        instruction="""
You are the Student Profile Agent.

You MUST:
1. Call `load_memory` first with a query like:
   "previous student profile, academic background, IELTS, preferences".
2. If a profile exists, summarize it to the user and ask for missing/updated info.
3. When the profile is complete, return ONLY JSON, no markdown.

JSON SCHEMA:

{
  "full_name": "",
  "current_level": "bachelor|master|phd|high_school",
  "field_of_study": "",
  "gpa_or_percentage": "",
  "grading_scale": "",
  "university_name": "",
  "country_of_residence": "",
  "citizenship_country": "",
  "english_test_taken": "ielts|toefl|duolingo|none",
  "english_score": "",
  "has_research_experience": true,
  "publications_or_projects": "",
  "work_experience_years": 0,
  "preferred_degree_abroad": "bachelor|master|phd",
  "target_field": "",
  "preferred_countries": [],
  "financial_need": "full_funding|partial_funding|no_need",
  "graduation_year": "",
  "other_constraints": ""
}

Rules:
- Ask follow-up questions for missing/unclear data.
- Final answer: JSON only, no extra text.
""",
        tools=[load_memory],
        output_key="student_profile",
    )