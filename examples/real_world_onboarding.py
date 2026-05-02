import os
from datetime import datetime
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from cpfhub import CPFHub, CPFHubError

app = FastAPI()

# Initialize CPFHub client
api_key = os.environ.get("CPFHUB_API_KEY")
cpfhub_client = CPFHub(api_key=api_key)

class OnboardingRequest(BaseModel):
    cpf: str

@app.post("/api/onboarding/verify")
async def verify_identity(request: OnboardingRequest):
    try:
        # 1. Lookup identity data using CPFHub
        result = cpfhub_client.lookup(request.cpf)
        identity_data = result.data

        # 2. Perform business logic (e.g., check age)
        current_year = datetime.now().year
        is_adult = identity_data.year <= current_year - 18

        if not is_adult:
            raise HTTPException(status_code=403, detail="User must be 18 or older")

        # 3. Return successful verification
        return {
            "success": True,
            "message": "Identity verified successfully",
            "user": {
                "name": identity_data.name,
                "gender": identity_data.gender,
                "birthDate": identity_data.birthDate
            }
        }

    except CPFHubError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail="Internal server error")

# To run this example:
# uvicorn examples.real_world_onboarding:app --reload
