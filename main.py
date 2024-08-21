from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel

app = FastAPI()

class UserRequest(BaseModel):
    cedula: str
    confirm: bool

@app.post("/policy/")
async def accept_policy(request: UserRequest):
    if request.confirm:
        return {"message": "Política aceptada"}
    else:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="No acepta la política")
