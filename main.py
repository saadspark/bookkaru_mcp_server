from typing import Any
import httpx
from mcp.server.fastmcp import FastMCP
import os

PORT = os.environ.get("PORT", 1000)
mcp = FastMCP("BOOKKARU",host="0.0.0.0",port=PORT)

@mcp.tool(
    name="get_saad_age",
    description="get saad age",
)
def get_age(route_number: str) -> str:
    """Get the alerts for a given route number."""
    return f"Alerts for route {route_number}"


if __name__ == "__main__":
    mcp.run(transport='streamable-http')

