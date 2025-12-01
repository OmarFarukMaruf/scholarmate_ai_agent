# scholarmate_ai_agent
The AI Scholarship Finder Agent is an autonomous agent that collects a student’s academic background, performs real-time web search, identifies globally available scholarships. The project is built using Google’s Agent Development Kit (ADK) in Python, and follows a modular AI agent architecture.

# Core Components

**Orchestration Layer (Agent Brain)**
Controls the entire workflow:
• Collect student data
• Search scholarships
• Filter & match
• Save memory for future queries

**Tools (Agent Hands)**
• Profile Building Tool
• Scholarship Search Tool
• Match Tool (LLM Re-Ranker)

# Demo — What the Agent Does

**1️⃣ Input: Student profile**

The student enters:
• Nationality
• Degree goal (BSc/MSc/PhD)
• Field of study
• GPA/CGPA
• IELTS/TOEFL scores
• Work experience
• Publications & projects

**2️⃣ Processing: Agent reasoning loop**
• Agent searches the dataset
• Filters based on hard rules
• Sends promising matches to LLM for deeper reasoning
• Produces JSON output with scores and explanations

**3️⃣ Output: Ranked scholarship list**

Each item includes:
• Scholarship name
• Funding type
• Eligibility explanation
• Score (0–100)
• Why You Fit bullets
• Required documents
• Keywords for the CV

This demo showcases a fully autonomous workflow

# The Build — Tools & Technologies
Languages & Frameworks
• Python
• Google Agent Development Kit (ADK)
• Google Gemini / LLM APIs

Data
• A curated CSV of global scholarships (DAAD, Chevening, Erasmus Mundus, Fulbright, MEXT, etc.).
• Student profile data stored as structured JSON.

Outputs
• Ranked opportunities
• Reasoning explanations
• Memory logs
