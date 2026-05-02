# cpfhub: Python SDK for CPFHub.io

**Official Python SDK for [CPFHub.io](https://cpfhub.io) — Brazilian CPF Lookup API**

> Official Python SDK for CPFHub.io. Retrieve identity data from a Brazilian CPF number.

[![PyPI version](https://img.shields.io/pypi/v/cpfhub)](https://pypi.org/project/cpfhub/)
[![Python](https://img.shields.io/pypi/pyversions/cpfhub)](https://pypi.org/project/cpfhub/)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)

---

## What is CPFHub.io?

CPFHub.io is a REST API that returns name, gender, and date of birth from any Brazilian CPF number — in ~300ms, with 99.9% uptime, and full LGPD compliance.

**10M+ CPFs queried · 1,300+ active companies · 99.9% uptime**

---

## Why use the CPFHub.io Python SDK?

This SDK is designed to offer a fluid and efficient integration of the CPFHub.io API into Python projects, focusing on Developer Experience (DX) and compatibility with AI Agents.

### 1. Optimized Developer Experience (DX)

*   **Fast Integration**: Easily incorporate CPF lookups into your Python scripts and applications.
*   **API Abstraction**: Automatically handles headers, JSON parsing, and error handling, allowing you to focus on business logic.

### 2. Native Compatibility with AI Agents

To facilitate integration with AI agents and LLMs, this SDK and the CPFHub.io API offer:

*   **OpenAPI Specification**: The official API specification is available at [cpfhub-openapi](https://github.com/cpfhub/cpfhub-openapi), allowing agents to automatically understand its structure and typed schemas.
*   **Tool Descriptions**: The API is easily representable as "tool descriptions" for LLMs, facilitating invocation in agent frameworks.
*   **Native MCP Server**: CPFHub.io offers an MCP server that exposes the API directly to AI agents (Claude, Cursor, Windsurf), complementing its use in Python development environments.

---

## Installation

```bash
pip install cpfhub
```

---

## Quick Start

```python
from cpfhub import CPFHub

client = CPFHub(api_key="YOUR_API_KEY")

result = client.lookup("00000000000")

print(result.name)       # "Fulano de Tal"
print(result.gender)     # "M"
print(result.birth_date) # "15/06/1990"
```

Get your free API key at [app.cpfhub.io](https://app.cpfhub.io) — no credit card required.

---

## Async Support

```python
import asyncio
from cpfhub import AsyncCPFHub

async def main():
    client = AsyncCPFHub(api_key="YOUR_API_KEY")
    result = await client.lookup("00000000000")
    print(result.name)

asyncio.run(main())
```

---

## API Reference

### `CPFHub(api_key, timeout=10, base_url=None)`

| Parameter | Type | Required | Default | Description |
|-----------|------|----------|---------|-------------|
| `api_key` | `str` | Yes | — | Your CPFHub API key |
| `timeout` | `int` | No | `10` | Request timeout in seconds |
| `base_url` | `str` | No | `https://api.cpfhub.io` | API base URL |

### `client.lookup(cpf: str) -> CPFResult`

Looks up a CPF and returns the associated data.

Accepts CPF with or without formatting (`000.000.000-00` or `00000000000`).

#### `CPFResult` attributes

| Attribute | Type | Description |
|-----------|------|-------------|
| `cpf` | `str` | CPF number (digits only) |
| `name` | `str` | Full name — `"Fulano de Tal"` |
| `name_upper` | `str` | Full name in uppercase |
| `gender` | `str` | `"M"` or `"F"` |
| `birth_date` | `str` | Date of birth — `"DD/MM/YYYY"` |
| `day` | `int` | Birth day |
| `month` | `int` | Birth month |
| `year` | `int` | Birth year |

---

## Error Handling

```python
from cpfhub import CPFHub, CPFHubError

client = CPFHub(api_key="YOUR_API_KEY")

try:
    result = client.lookup("00000000000")
    print(result.name)
except CPFHubError as e:
    print(f"Error {e.status_code}: {e.message}")
    # 400 — Invalid CPF format
    # 401 — Invalid or missing API key
    # 404 — CPF not found
    # 429 — Rate limit exceeded
    # 500 — Server error
    # 503 — Service temporarily unavailable
```

---

## Examples

Check the `examples/` directory for sample usage:

*   [simple_lookup.py](examples/simple_lookup.py)
*   [real_world_onboarding.py](examples/real_world_onboarding.py)

### requests (sync)

```python
from cpfhub import CPFHub

client = CPFHub(api_key="YOUR_API_KEY", timeout=5)
result = client.lookup("00000000000")
print(result.name)
```

### httpx (async)

```python
import asyncio
from cpfhub import AsyncCPFHub

async def verify_cpf(cpf: str):
    client = AsyncCPFHub(api_key="YOUR_API_KEY")
    return await client.lookup(cpf)

asyncio.run(verify_cpf("00000000000"))
print(result.name)
```

### FastAPI

```python
from fastapi import FastAPI
from cpfhub import AsyncCPFHub

app = FastAPI()
client = AsyncCPFHub(api_key="YOUR_API_KEY")

@app.get("/cpf/{cpf}")
async def lookup_cpf(cpf: str):
    result = await client.lookup(cpf)
    return {"name": result.name, "gender": result.gender}
```

### Django

```python
# views.py
from django.http import JsonResponse
from cpfhub import CPFHub

client = CPFHub(api_key="YOUR_API_KEY")

def lookup_cpf(request, cpf):
    result = client.lookup(cpf)
    return JsonResponse({"name": result.name, "gender": result.gender})
```

---

## Rate Limits

| Plan | Limit |
|---|---|
| Free | 1 request every 2 seconds · 50 requests/month |
| Pro | 1 request per second · 1,000 requests/month |
| Corporate | Custom |

The SDK automatically retries on `429` with exponential backoff (up to 3 attempts).

---

## Plans & Pricing

| Plan | Price | Included | Extra |
|------|-------|----------|-------|
| **Free** | R$ 0/month | 50 lookups | — |
| **Pro** | R$ 149/month | 1,000 lookups | R$ 0,15/lookup |
| **Corporate** | Custom | Custom | Custom |

[View full pricing at cpfhub.io →](https://cpfhub.io#pricing)

---

## Requirements

- Python 3.8+
- `requests` (sync) or `httpx` (async) — installed automatically

---

## Links

- [Documentation](https://cpfhub.io/documentacao)
- [Dashboard](https://app.cpfhub.io)
- [Status Page](https://app.cpfhub.io/status)
- [Pricing](https://cpfhub.io#pricing)
- [LGPD Compliance](https://cpfhub.io/lgpd)
- [OpenAPI Specification](https://github.com/cpfhub/cpfhub-openapi/blob/main/openapi.yaml)

---

## License

MIT © [CPFHub.io](https://cpfhub.io)
