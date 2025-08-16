from typing import Any
import httpx
from mcp.server.fastmcp import FastMCP
import os

PORT = os.environ.get("PORT", 1000)
mcp = FastMCP("BOOKKARU",host="0.0.0.0",port=PORT)

@mcp.tool(
    name="get_saad_age",
    description="tell the age of saad",
)
def get_age() -> str:
    """Get the alerts for a given route number."""
    return f"Alerts for route 23"

@mcp.tool(
    name="get_saad_exp",
    description="tell the experience of saad",
)
def get_exp() -> str:
    """Get the experience of saad."""
    return f"Experience of saad is 10 years"


if __name__ == "__main__":
    mcp.run(transport='streamable-http')

