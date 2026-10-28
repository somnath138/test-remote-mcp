import json
import random

from fastmcp import FastMCP

mcp = FastMCP(name="Test Remote Server")


@mcp.tool()
def add(a: float, b: float) -> float:
    """Add two numbers together."""
    return a + b


@mcp.tool()
def random_number(min_value: int = 1, max_value: int = 100) -> int:
    """Return a random integer between min_value and max_value (inclusive)."""
    return random.randint(min_value, max_value)


@mcp.resource("info://server", mime_type="application/json")
def server_info() -> str:
    """Basic information about this server."""
    return json.dumps(
        {
            "name": "Test Remote Server",
            "version": "0.1.0",
            "tools": ["add", "random_number"],
            "author": "Your Name"
        }
    )


if __name__ == "__main__":
    # Streamable HTTP transport: clients connect to http://<host>:8000/mcp
    mcp.run(transport="http", host="0.0.0.0", port=8000)
