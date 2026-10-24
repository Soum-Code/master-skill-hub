# azure-maps-search-dotnet

> Azure Maps SDK for .NET. Location-based services including geocoding, routing, rendering, geolocation, and weather. Use for address search, directions, map tiles, IP geolocation, and weather data. Triggers: "Azure Maps", "MapsSearchClient", "MapsRoutingClient", "MapsRenderingClient", "geocoding .NET", "route directions", "map tiles", "geolocation".

| | |
|---|---|
| **ID** | `microsoft/skills:azure-maps-search-dotnet` |
| **Pack** | MLOps / DevOps / Cloud |
| **Kind** | skill |
| **Status** | verified (vetted at pinned commit) |
| **Origin** | [microsoft/skills](https://github.com/microsoft/skills) |
| **License** | MIT |
| **Size** | 506 lines in SKILL.md, 1 file(s) |

## When to use it

- Use for address search, directions, map tiles, IP geolocation, and weather data.

## What it says up front

> Azure Maps SDK for .NET providing location-based services: geocoding, routing, rendering, geolocation, and weather.

## How it is structured

The skill's own section headings, in order:

- Installation
- Environment Variables
- Authentication
  - Subscription Key (Shared Key)
  - Microsoft Entra Token Credential
  - Shared Access Signature (SAS)
- Client Hierarchy
- Core Workflows
  - 1. Geocoding (Address to Coordinates)
  - 2. Batch Geocoding
  - 3. Reverse Geocoding (Coordinates to Address)
  - 4. Get Boundary Polygon
  - 5. Route Directions
  - 6. Route Directions with Options
  - 7. Route Matrix
  - 8. Route Range (Isochrone)
  - 9. Get Map Tiles
  - 10. IP Geolocation
  - 11. Current Weather
- Key Types Reference
  - Search Package
  - Routing Package
  - Rendering Package
  - Common Types
- Best Practices
- Error Handling
- Related SDKs
- Reference Links

## What it bundles

- Just the SKILL.md (instructions only, no scripts).

## Permissions and risk notes

- Declares no pre-approved tools; Claude asks as usual.

## Related skills

- [microsoft/skills:azure-identity-dotnet](microsoft-skills-azure-identity-dotnet.md) - Azure Identity library for .NET. Authentication library for Azure SDK clients using Microsoft Entra ID. Use fo
- [microsoft/skills:azure-eventhub-dotnet](microsoft-skills-azure-eventhub-dotnet.md) - Azure Event Hubs SDK for .NET. Use for high-throughput event streaming: sending events (EventHubProducerClient
- [microsoft/skills:azure-mgmt-apicenter-dotnet](microsoft-skills-azure-mgmt-apicenter-dotnet.md) - Azure API Center SDK for .NET. Centralized API inventory management with governance, versioning, and discovery
- [microsoft/skills:azure-mgmt-apimanagement-dotnet](microsoft-skills-azure-mgmt-apimanagement-dotnet.md) - Azure Resource Manager SDK for API Management in .NET. Use for MANAGEMENT PLANE operations: creating/managing 

## Invoke / install

- Invoke: `/microsoft/skills:azure-maps-search-dotnet`
- Install: `python skills/skill-vetter/scripts/install.py microsoft/skills --path .github/plugins/azure-sdk-dotnet/skills/azure-maps-search-dotnet --commit 2130750147dee0311215099ddf36647ba1e0f006 --expect-tree de9ae652d5a58630e7cc54a7220f2ecac743a61587e3217c3e3114129590f139 --apply`

---
_Generated from the skill's own metadata by [master-skill-hub](https://github.com/Soum-Code/master-skill-hub). Nothing here is hand-written opinion._
