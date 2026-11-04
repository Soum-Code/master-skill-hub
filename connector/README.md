# Optional connector (MCP server)

A small read-only server so claude.ai (custom connector) or any MCP client can query the live hub registry. It reuses the router's own ranking code, so results match `route.py`.

- Tools: `search_skills`, `get_skill`, `list_packs`. Read-only, no secrets, no outbound calls.
- Transport: stateless Streamable HTTP, `POST /api/mcp`.
- Not deployed by default. Deploying publishes an endpoint, so it is your call.

## Run locally

```bash
python connector/serve.py 8787
curl -s localhost:8787/api/mcp -H 'content-type: application/json' \
  -d '{"jsonrpc":"2.0","id":1,"method":"tools/call","params":{"name":"search_skills","arguments":{"query":"review an NDA"}}}'
```

## Deploy on Vercel

```bash
python connector/bundle.py     # copies route.py + registry.json next to the function
cd connector
vercel deploy --prod
```

`vercel.json` ships the bundled router script and registry with the function. Then in claude.ai: **Settings, Connectors, Add custom connector**, URL `https://<your-project>.vercel.app/api/mcp`.

The bundled registry is a snapshot from the last build; redeploy (or add a deploy hook to the weekly workflow) to refresh it.
