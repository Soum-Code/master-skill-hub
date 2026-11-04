"""Local dev server: python connector/serve.py [port]"""
import os
import sys
from http.server import HTTPServer

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "api"))
from mcp import handler  # noqa: E402

if __name__ == "__main__":
    port = int(sys.argv[1]) if len(sys.argv) > 1 else 8787
    print(f"MCP connector on http://127.0.0.1:{port}/api/mcp")
    HTTPServer(("127.0.0.1", port), handler).serve_forever()
