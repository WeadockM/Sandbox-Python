from database.auth import AuthAgent
from fastapi import FastAPI
from api.apiFunctions import (
  authlistGET,
  authGET
)

authAgent = AuthAgent()
# authAgent.create_table()
# authAgent.create_test_auth()
# authAgent.create_auth('12345', 'TestPassword1!')

app = FastAPI()

@app.get("/authlist")
async def GETauthlist():
  return authlistGET(authAgent)

@app.get("/auth")
async def GETauth(externalId):
  return authGET(authAgent, externalId)
