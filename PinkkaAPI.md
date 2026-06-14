# Pinkka API Documentation

## Endpoint
**Base URL:** `https://fmnh-ws-prod3.it.helsinki.fi/pinkka/api/speciescards/`

### Get Species Card
- **Method:** GET
- **URL:** `/speciescards/{speciesId}`
- **Example:** `https://fmnh-ws-prod3.it.helsinki.fi/pinkka/api/speciescards/39802`
- **Response Type:** JSON

### Parameters
| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| speciesId | integer | Yes | Unique species identifier |

### Response Fields
(Once you inspect the JSON, document these — e.g., `name`, `images[]`, `description`, etc.)
| Parameter | Type |
| scientificName | text |
| taxonomy | list |
| images | 

### Notes
- No authentication required
- Get taxonomy tags like: `taxonomy[i][rankName][en]` : `taxonomy[i]`[scientificName]`

