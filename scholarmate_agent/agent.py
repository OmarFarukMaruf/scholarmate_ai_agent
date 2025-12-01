from google.adk.agents import LlmAgent
from google.adk.tools.agent_tool import AgentTool
from google.adk.tools.load_memory_tool import load_memory
from google.adk.models import Gemini

# Import sub-agents
from .agents.profile_agent import create_profile_agent
from .agents.search_agent import create_search_agent
from .agents.ranking_agent import create_ranking_agent

# Create sub-agents
profile_agent = create_profile_agent()
search_agent = create_search_agent()
ranking_agent = create_ranking_agent()

# THIS is the root agent ADK needs
root_agent = LlmAgent(
    name="scholarship_root_agent",
    model=Gemini(model="gemini-2.5-flash-lite"),
    description="Root controller for scholarship finder",
    instruction="""
You are the root coordinator agent.
Use the sub-agents to collect profile, search scholarships, and rank them.
""",
    tools=[
        AgentTool(agent=profile_agent),
        AgentTool(agent=search_agent),
        AgentTool(agent=ranking_agent),
        load_memory,
    ],
)