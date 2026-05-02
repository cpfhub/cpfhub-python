# cpfhub: Python SDK for CPFHub.io

🇺🇸 **English** | [🇧🇷 Português](#português)

**Official Python SDK for [CPFHub.io](https://cpfhub.io) — Brazilian CPF Lookup API**

[![PyPI version](https://img.shields.io/pypi/v/cpfhub)](https://pypi.org/project/cpfhub/)
[![Python](https://img.shields.io/pypi/pyversions/cpfhub)](https://pypi.org/project/cpfhub/)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)

---

## What is CPFHub.io?

CPFHub.io is a REST API that returns name, gender, and date of birth from any Brazilian CPF number — in ~300ms, with 99.9% uptime, and full LGPD compliance.

**10M+ CPFs queried · 1,300+ active companies · 99.9% uptime**

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

## curl Example

```bash
curl -X GET "https://api.cpfhub.io/cpf/12345678909" \
  -H "x-api-key: YOUR_API_KEY"
```

**Response:**

```json
{
  "success": true,
  "data": {
    "cpf": "12345678909",
    "name": "Fulano de Tal",
    "nameUpper": "FULANO DE TAL",
    "gender": "M",
    "birthDate": "15/06/1990",
    "day": 15,
    "month": 6,
    "year": 1990
  }
}
```

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

Looks up a CPF and returns the associated identity data.

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

- [simple_lookup.py](examples/simple_lookup.py)
- [real_world_onboarding.py](examples/real_world_onboarding.py)

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

result = asyncio.run(verify_cpf("00000000000"))
print(result.name)
```

### FastAPI

```python
from fastapi import FastAPI
from cpfhub import AsyncCPFHub

app = FastAPI()
client = AsyncCPFHub(api_key="YOUR_API_KEY")

@app.get("/cpf/{cpf}")
async def get_person_by_cpf(cpf: str):
    result = await client.lookup(cpf)
    return {"name": result.name, "gender": result.gender}
```

### Django

```python
# views.py
from django.http import JsonResponse
from cpfhub import CPFHub

client = CPFHub(api_key="YOUR_API_KEY")

def get_person_by_cpf(request, cpf):
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
- [MCP Server (AI Agents)](https://github.com/cpfhub/cpfhub-mcp)

---

## License

MIT © [CPFHub.io](https://cpfhub.io)

---

# Português

[🇺🇸 English](#cpfhub-python-sdk-for-cpfhubio) | 🇧🇷 **Português**

**SDK Python oficial para [CPFHub.io](https://cpfhub.io) — API de Consulta de CPF Brasileiro**

---

## O que é o CPFHub.io?

O CPFHub.io é uma API REST que retorna nome, gênero e data de nascimento de qualquer CPF brasileiro — em ~300ms, com 99,9% de uptime e total conformidade com a LGPD.

**10M+ CPFs consultados · 1.300+ empresas ativas · 99,9% uptime**

---

## Instalação

```bash
pip install cpfhub
```

---

## Início Rápido

```python
from cpfhub import CPFHub

client = CPFHub(api_key="SUA_CHAVE_DE_API")

result = client.lookup("00000000000")

print(result.name)       # "Fulano de Tal"
print(result.gender)     # "M"
print(result.birth_date) # "15/06/1990"
```

Obtenha sua chave de API gratuita em [app.cpfhub.io](https://app.cpfhub.io) — sem cartão de crédito.

---

## Exemplo curl

```bash
curl -X GET "https://api.cpfhub.io/cpf/12345678909" \
  -H "x-api-key: SUA_CHAVE_DE_API"
```

**Resposta:**

```json
{
  "success": true,
  "data": {
    "cpf": "12345678909",
    "name": "Fulano de Tal",
    "nameUpper": "FULANO DE TAL",
    "gender": "M",
    "birthDate": "15/06/1990",
    "day": 15,
    "month": 6,
    "year": 1990
  }
}
```

---

## Suporte a Async

```python
import asyncio
from cpfhub import AsyncCPFHub

async def main():
    client = AsyncCPFHub(api_key="SUA_CHAVE_DE_API")
    result = await client.lookup("00000000000")
    print(result.name)

asyncio.run(main())
```

---

## Referência da API

### `CPFHub(api_key, timeout=10, base_url=None)`

| Parâmetro | Tipo | Obrigatório | Padrão | Descrição |
|-----------|------|-------------|--------|-----------|
| `api_key` | `str` | Sim | — | Sua chave de API do CPFHub |
| `timeout` | `int` | Não | `10` | Timeout da requisição em segundos |
| `base_url` | `str` | Não | `https://api.cpfhub.io` | URL base da API |

### `client.lookup(cpf: str) -> CPFResult`

Consulta um CPF e retorna os dados de identidade associados.

Aceita CPF com ou sem formatação (`000.000.000-00` ou `00000000000`).

#### Atributos de `CPFResult`

| Atributo | Tipo | Descrição |
|----------|------|-----------|
| `cpf` | `str` | CPF (apenas dígitos) |
| `name` | `str` | Nome completo — `"Fulano de Tal"` |
| `name_upper` | `str` | Nome completo em maiúsculas |
| `gender` | `str` | `"M"` ou `"F"` |
| `birth_date` | `str` | Data de nascimento — `"DD/MM/YYYY"` |
| `day` | `int` | Dia de nascimento |
| `month` | `int` | Mês de nascimento |
| `year` | `int` | Ano de nascimento |

---

## Tratamento de Erros

```python
from cpfhub import CPFHub, CPFHubError

client = CPFHub(api_key="SUA_CHAVE_DE_API")

try:
    result = client.lookup("00000000000")
    print(result.name)
except CPFHubError as e:
    print(f"Erro {e.status_code}: {e.message}")
    # 400 — Formato de CPF inválido
    # 401 — Chave de API inválida ou ausente
    # 404 — CPF não encontrado
    # 429 — Limite de requisições excedido
    # 500 — Erro no servidor
    # 503 — Serviço temporariamente indisponível
```

---

## Exemplos

Veja o diretório `examples/` para exemplos de uso:

- [simple_lookup.py](examples/simple_lookup.py)
- [real_world_onboarding.py](examples/real_world_onboarding.py)

### requests (síncrono)

```python
from cpfhub import CPFHub

client = CPFHub(api_key="SUA_CHAVE_DE_API", timeout=5)
result = client.lookup("00000000000")
print(result.name)
```

### httpx (assíncrono)

```python
import asyncio
from cpfhub import AsyncCPFHub

async def verify_cpf(cpf: str):
    client = AsyncCPFHub(api_key="SUA_CHAVE_DE_API")
    return await client.lookup(cpf)

result = asyncio.run(verify_cpf("00000000000"))
print(result.name)
```

### FastAPI

```python
from fastapi import FastAPI
from cpfhub import AsyncCPFHub

app = FastAPI()
client = AsyncCPFHub(api_key="SUA_CHAVE_DE_API")

@app.get("/cpf/{cpf}")
async def get_person_by_cpf(cpf: str):
    result = await client.lookup(cpf)
    return {"name": result.name, "gender": result.gender}
```

### Django

```python
# views.py
from django.http import JsonResponse
from cpfhub import CPFHub

client = CPFHub(api_key="SUA_CHAVE_DE_API")

def get_person_by_cpf(request, cpf):
    result = client.lookup(cpf)
    return JsonResponse({"name": result.name, "gender": result.gender})
```

---

## Limites de Requisição

| Plano | Limite |
|---|---|
| Gratuito | 1 requisição a cada 2 segundos · 50 requisições/mês |
| Pro | 1 requisição por segundo · 1.000 requisições/mês |
| Corporativo | Personalizado |

O SDK faz retry automático no erro `429` com backoff exponencial (até 3 tentativas).

---

## Planos e Preços

| Plano | Preço | Incluído | Extra |
|-------|-------|----------|-------|
| **Gratuito** | R$ 0/mês | 50 consultas | — |
| **Pro** | R$ 149/mês | 1.000 consultas | R$ 0,15/consulta |
| **Corporativo** | Personalizado | Personalizado | Personalizado |

[Ver preços completos em cpfhub.io →](https://cpfhub.io#pricing)

---

## Requisitos

- Python 3.8+
- `requests` (síncrono) ou `httpx` (assíncrono) — instalados automaticamente

---

## Links

- [Documentação](https://cpfhub.io/documentacao)
- [Dashboard](https://app.cpfhub.io)
- [Página de Status](https://app.cpfhub.io/status)
- [Preços](https://cpfhub.io#pricing)
- [Conformidade LGPD](https://cpfhub.io/lgpd)
- [Especificação OpenAPI](https://github.com/cpfhub/cpfhub-openapi/blob/main/openapi.yaml)
- [Servidor MCP (Agentes de IA)](https://github.com/cpfhub/cpfhub-mcp)

---

## Licença

MIT © [CPFHub.io](https://cpfhub.io)
