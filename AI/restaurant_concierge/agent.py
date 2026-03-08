"""Restaurant Concierge ADK Agent.

Capabilities:
- Menu search (keyword + semantic via MCP Toolbox) — if Toolbox is available
- Dietary preference tracking (via ToolContext)
- Graceful fallback when Toolbox is offline
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


async def save_dietary_preference(tool_context: ToolContext, preference: str) -> str:
    """Save a dietary preference for the current user.

    Args:
        preference: The dietary preference to save (e.g., "vegetarian", "gluten-free").
    """
    preferences = tool_context.state.get("dietary_preferences", [])
    if preference not in preferences:
        preferences.append(preference)
        tool_context.state["dietary_preferences"] = preferences
    return f"Saved dietary preference: {preference}. Current preferences: {', '.join(preferences)}"


async def get_dietary_preferences(tool_context: ToolContext) -> str:
    """Retrieve all saved dietary preferences for the current user."""
    preferences = tool_context.state.get("dietary_preferences", [])
    if not preferences:
        return "No dietary preferences saved yet."
    return f"Current dietary preferences: {', '.join(preferences)}"


SYSTEM_INSTRUCTION = """You are a friendly and knowledgeable restaurant concierge for "The Cloud Kitchen."

Your capabilities:
- **Menu Search**: Search the menu by category, dietary requirements, or natural language queries.
  Use semantic search for questions like "something light and refreshing."
- **Dietary Preferences**: Remember and apply dietary preferences across the conversation.
  Always check saved preferences when recommending menu items.

Guidelines:
- Be warm and professional, like a real concierge at a fine dining restaurant.
- When recommending menu items, consider the guest's saved dietary preferences.
- For menu searches, use the search tools to find real items from the database — never make up
  menu items.
- If the menu search tools are not available, let the guest know that the menu database is
  currently being updated and offer to help with dietary preferences instead.
- Keep responses concise but informative.
- If a guest mentions a dietary restriction, proactively save it as a preference.
"""

root_agent = LlmAgent(
    model=os.environ.get("ADK_MODEL", "gemini-2.5-flash"),
    name="restaurant_concierge",
    instruction=SYSTEM_INSTRUCTION,
    tools=[
        *toolbox_tools,
        save_dietary_preference,
        get_dietary_preferences,
    ],
)
