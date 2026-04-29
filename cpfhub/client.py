import httpx
from typing import Optional, Dict, Any

class CPFHub:
    """
    Official Python SDK for CPFHub.io
    Building the Infrastructure of Trust for Brazil.
    """
    
    BASE_URL = "https://api.cpfhub.io"

    def __init__(self, api_key: str):
        if not api_key:
            raise ValueError("API Key is required. Get yours at https://app.cpfhub.io")
        self.api_key = api_key
        self.client = httpx.Client(
            base_url=self.BASE_URL,
            headers={"x-api-key": self.api_key},
            timeout=10.0
        )

    def lookup(self, cpf: str) -> Dict[str, Any]:
        """
        Lookup Brazilian CPF information.
        Returns name, gender and birth date.
        """
        clean_cpf = "".join(filter(str.isdigit, cpf))
        if len(clean_cpf) != 11:
            raise ValueError("Invalid CPF format. Must have 11 digits.")
            
        response = self.client.get(f"/cpf/{clean_cpf}")
        response.raise_for_status()
        return response.json()

    def get_quota(self) -> Dict[str, Any]:
        """
        Check your remaining credits and plan status.
        """
        # Using the MCP endpoint for quota info as per documentation
        response = self.client.get("/mcp", params={"api_key": self.api_key})
        response.raise_for_status()
        return response.json()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.client.close()
