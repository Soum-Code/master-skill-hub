"""Vercel Python entry point: POST /api/mcp  (also usable as a plain WSGI-less http.server handler)."""
import json
import os
import sys
from http.server import BaseHTTPRequestHandler

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from mcp_handler import handle_body  # noqa: E402


class handler(BaseHTTPRequestHandler):
    def _send(self, status: int, body) -> None:
        raw = b"" if body is None else json.dumps(body, ensure_ascii=False).encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(raw)))
        self.send_header("Cache-Control", "no-store")
        self.send_header("Access-Control-Allow-Origin", "*")
        self.end_headers()
        if raw:
            self.wfile.write(raw)

    def do_POST(self):
        length = int(self.headers.get("Content-Length") or 0)
        if length > 64 * 1024:
            return self._send(413, {"error": "request too large"})
        status, body = handle_body(self.rfile.read(length))
        self._send(status, body)

    def do_GET(self):  # no server-initiated stream: this server is stateless
        self._send(405, {"error": "use POST with a JSON-RPC body"})

    def do_OPTIONS(self):
        self.send_response(204)
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Access-Control-Allow-Methods", "POST, OPTIONS")
        self.send_header("Access-Control-Allow-Headers", "Content-Type, Mcp-Protocol-Version, Mcp-Session-Id")
        self.end_headers()

    def log_message(self, *a):  # keep logs free of request data
        pass
