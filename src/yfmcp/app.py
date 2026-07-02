import os

from yfmcp.server import mcp

# Bind to the host/port Manufact expects. FastMCP reads these settings when
# constructing the streamable-http app.
mcp.settings.host = os.environ.get("HOST", "0.0.0.0")
mcp.settings.port = int(os.environ.get("PORT", "8000"))

# ASGI application serving the MCP endpoint at the /mcp path.
app = mcp.streamable_http_app()
