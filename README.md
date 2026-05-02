# cpfhub: SDK Python para Consulta de CPF (AI-Native)

**Official Python SDK for [CPFHub.io](https://cpfhub.io) — Brazilian CPF Lookup API**

> SDK oficial Python para a [CPFHub.io](https://cpfhub.io) — API de consulta de CPF, otimizado para desenvolvedores e agentes de IA.

[![PyPI version](https://img.shields.io/pypi/v/cpfhub)](https://pypi.org/project/cpfhub/)
[![Python](https://img.shields.io/pypi/pyversions/cpfhub)](https://pypi.org/project/cpfhub/)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)

---

## O que é CPFHub.io?

CPFHub.io é uma API REST que retorna nome, gênero e data de nascimento a partir de qualquer CPF brasileiro — em ~300ms, com 99.9% de uptime, e total conformidade com a LGPD.

> CPFHub.io é uma API REST que retorna nome, gênero e data de nascimento a partir de qualquer CPF brasileiro — em ~300ms, com 99,9% de uptime e total conformidade com a LGPD.

**10M+ CPFs consultados · 1.300+ empresas ativas · 99.9% uptime**

---

## Por que usar o SDK Python do CPFHub.io?

Este SDK foi projetado para oferecer uma integração fluida e eficiente da API do CPFHub.io em projetos Python, com foco em Developer Experience (DX) e compatibilidade com Agentes de IA.

### 1. Developer Experience (DX) Otimizada

*   **Integração Rápida**: Facilita a incorporação de consultas de CPF em seus scripts e aplicações Python.
*   **Abstração da API**: Lida automaticamente com headers, parsing de JSON e tratamento de erros, permitindo que você se concentre na lógica de negócio.

### 2. Compatibilidade Nativa com Agentes de IA

Para facilitar a integração com agentes de IA e LLMs, este SDK e a API do CPFHub.io oferecem:

*   **OpenAPI Specification**: Um arquivo `openapi.yaml` está disponível para descrever a API, permitindo que agentes entendam automaticamente sua estrutura e schemas tipados.
*   **Tool Descriptions**: A API é facilmente representável como "tool descriptions" para LLMs, facilitando a invocação em frameworks de agentes.
*   **MCP Server Nativo**: O CPFHub.io oferece um servidor MCP que expõe a API diretamente para agentes de IA (Claude, Cursor, Windsurf), complementando o uso em ambientes de desenvolvimento Python.

---

## Installation / Instalação

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

> Obtenha sua chave gratuita em [app.cpfhub.io](https://app.cpfhub.io) — sem cartão de crédito.

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

## Rate Limits / Limites de Requisição

| Plan / Plano | Limit / Limite |
|---|---|
| Free / Grátis | 1 request every 2 seconds · 50 requests/month |
| Pro | 1 request per second · 1,000 requests/month |
| Corporate / Corporativo | Custom / Personalizado |

The SDK automatically retries on `429` with exponential backoff (up to 3 attempts).

> O SDK faz retry automático em `429` com backoff exponencial (até 3 tentativas).

---

## Plans & Pricing / Planos e Preços

| Plan | Price | Included | Extra |
|------|-------|----------|-------|
| **Free** | R$ 0/month | 50 lookups | — |
| **Pro** | R$ 149/month | 1,000 lookups | R$ 0,15/lookup |
| **Corporate** | Custom | Custom | Custom |

[View full pricing at cpfhub.io →](https://cpfhub.io#pricing)

---

## Requirements / Requisitos

- Python 3.8+
- `requests` (sync) or `httpx` (async) — installed automatically

---

## Links

- [Documentation / Documentação](https://cpfhub.io/documentacao)
- [Dashboard / Painel](https://app.cpfhub.io)
- [Status Page](https://app.cpfhub.io/status)
- [Pricing / Preços](https://cpfhub.io#pricing)
- [LGPD Compliance](https://cpfhub.io/lgpd)
- [OpenAPI Specification](openapi.yaml)

---

## License / Licença

MIT © [CPFHub.io](https://cpfhub.io)
