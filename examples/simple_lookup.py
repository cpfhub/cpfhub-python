import os
from cpfhub import CPFHub

# Ensure CPFHUB_API_KEY is set in your environment
api_key = os.environ.get("CPFHUB_API_KEY")
client = CPFHub(api_key=api_key)

try:
    result = client.lookup("12345678900")
    print(f"Name: {result.data.name}")
    print(f"Gender: {result.data.gender}")
    print(f"Birth Date: {result.data.birthDate}")
except Exception as e:
    print(f"Error: {e}")
