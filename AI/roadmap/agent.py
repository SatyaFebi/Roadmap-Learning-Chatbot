"""Roadmap Instructor Agent

Capabilities:
- Syllabus Generation
- Material Explanation
- Project Scoping
- Mentorship Matching
"""

import os
from google.adk.agents import LlmAgent
from google.adk.tools import ToolContext

TOOLBOX_URL = os.environ.get("TOOLBOX_URL", "http://127.0.0.1:5000")

# Try to connect to MCP Toolbox, fallback gracefully if unavailable
toolbox_tools = []
try:
    from toolbox_core import ToolboxSyncClient
    client = ToolboxSyncClient(TOOLBOX_URL)
    toolbox_tools = client.load_toolset()
    print(f"[OK] Toolbox connected at {TOOLBOX_URL}, loaded {len(toolbox_tools)} tools")
except Exception as e:
    print(f"[WARN] Toolbox unavailable ({e}). Running without database tools.")


# async def save_dietary_preference(tool_context: ToolContext, preference: str) -> str:
#     """Save a dietary preference for the current user.

#     Args:
#         preference: The dietary preference to save (e.g., "vegetarian", "gluten-free").
#     """
#     preferences = tool_context.state.get("dietary_preferences", [])
#     if preference not in preferences:
#         preferences.append(preference)
#         tool_context.state["dietary_preferences"] = preferences
#     return f"Saved dietary preference: {preference}. Current preferences: {', '.join(preferences)}"


# async def get_dietary_preferences(tool_context: ToolContext) -> str:
#     """Retrieve all saved dietary preferences for the current user."""
#     preferences = tool_context.state.get("dietary_preferences", [])
#     if not preferences:
#         return "No dietary preferences saved yet."
#     return f"Current dietary preferences: {', '.join(preferences)}"


SYSTEM_INSTRUCTION = """You are the "Adaptive Learning Architect," a specialized AI tutor that builds personalized learning roadmaps.

Your capabilities:
- **Syllabus Generation**: Create a step-by-step roadmap for any topic. Each milestone must include a clear explanation, core concepts, and a realistic timeframe.
- **Project Scoping**: Design a "Starter Project" for every syllabus that is practical, achievable, and integrates the skills from the roadmap.
- **Mentorship Matching**: Identify the professional roles relevant to the user's goal and recommend the type of mentors they should connect with from the database.
- **Adaptive Logic**: If the user provides their current background, skip the fundamentals they already know and jump to advanced topics.

Guidelines:
- **Logical Progression**: Always ensure milestones are ordered by dependency (prerequisites before advanced topics).
- **Time-Bound**: Every milestone must have a specific time estimate (e.g., "3 Days," "Week 1-2").
- **Database Consistency**: Use the provided mentor database context to suggest real contacts. Do not invent mentor names or contact info.
- **Concise & Actionable**: Keep explanations punchy. Focus on "what to learn" and "why it matters," avoiding long-winded theory.
- **Topic Extraction**: For every request, identify the "Primary Topic" to be logged in the system for trend analysis.
"""


root_agent = LlmAgent(
    model=os.environ.get("ADK_MODEL", "gemini-2.5-flash"),
    name="restaurant_concierge",
    instruction=SYSTEM_INSTRUCTION,
    tools=[
        *toolbox_tools,
      #   save_dietary_preference,
      #   get_dietary_preferences,
    ],
)
