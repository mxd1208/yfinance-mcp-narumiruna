import os

from mcp.server.transport_security import TransportSecuritySettings
from yfmcp.server import mcp

# Bind to the host/port Manufact expects.
mcp.settings.host = os.environ.get("HOST", "0.0.0.0")
mcp.settings.port = int(os.environ.get("PORT", "8000"))

# Disable DNS-rebinding protection so the platform's proxied Host header is
# accepted (otherwise FastMCP returns HTTP 421 Misdirected Request).
mcp.settings.transport_security = TransportSecuritySettings(
      enable_dns_rebinding_protection=False
)

# ASGI application serving the MCP endpoint at the /mcp path.
app = mcp.streamable_http_app()
