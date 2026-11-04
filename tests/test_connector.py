import json
import sys
import threading
import urllib.request
from http.server import HTTPServer
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "connector"))
sys.path.insert(0, str(ROOT / "connector" / "api"))
import mcp_handler as H  # noqa: E402
from mcp import handler  # noqa: E402


def rpc(method, params=None, mid=1):
    return H.handle({"jsonrpc": "2.0", "id": mid, "method": method, "params": params or {}})


def test_initialize_and_tools_list():
    r = rpc("initialize", {"protocolVersion": "2025-03-26"})
    assert r["result"]["protocolVersion"] == "2025-03-26" and r["result"]["serverInfo"]["name"] == "master-skill-hub"
    names = [t["name"] for t in rpc("tools/list")["result"]["tools"]]
    assert names == ["search_skills", "get_skill", "list_packs"]
    assert all(t["annotations"]["readOnlyHint"] for t in rpc("tools/list")["result"]["tools"])


def test_search_matches_local_router():
    r = rpc("tools/call", {"name": "search_skills", "arguments": {"query": "review this NDA from a vendor", "top": 2}})
    out = json.loads(r["result"]["content"][0]["text"])
    assert out["results"][0]["id"].startswith("legal:")


def test_get_skill_and_unknown_and_bad_method():
    ok = rpc("tools/call", {"name": "get_skill", "arguments": {"id": "skill-hub:skill-vetter"}})
    assert "skill-vetter" in ok["result"]["content"][0]["text"]
    assert rpc("tools/call", {"name": "get_skill", "arguments": {"id": "nope"}})["result"]["isError"] is True
    assert rpc("nope")["error"]["code"] == -32601


def test_notifications_get_no_response_and_garbage_is_rejected():
    assert H.handle({"jsonrpc": "2.0", "method": "notifications/initialized"}) is None
    assert H.handle_body(b"not json")[0] == 400
    assert H.handle_body(b"x" * (70 * 1024))[0] == 413
    assert H.handle_body(b'{"jsonrpc":"2.0","method":"notifications/initialized"}')[0] == 202


def test_http_roundtrip():
    srv = HTTPServer(("127.0.0.1", 0), handler)
    t = threading.Thread(target=srv.serve_forever, daemon=True)
    t.start()
    try:
        url = f"http://127.0.0.1:{srv.server_port}/api/mcp"
        req = urllib.request.Request(url, data=json.dumps({"jsonrpc": "2.0", "id": 7, "method": "tools/list"}).encode(),
                                     headers={"Content-Type": "application/json"})
        with urllib.request.urlopen(req, timeout=5) as r:
            assert r.status == 200 and json.loads(r.read())["id"] == 7
        try:
            urllib.request.urlopen(url, timeout=5)
            assert False, "GET must be rejected"
        except urllib.error.HTTPError as e:
            assert e.code == 405
    finally:
        srv.shutdown()
