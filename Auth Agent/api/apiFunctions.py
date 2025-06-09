from fastapi import FastAPI

def authlistGET(authAgent):
  output = []
  authlist = authAgent.get_auth_list()
  for i in range(0, len(authlist)):
    output.append({
      "Id": authlist[i][0],
      "External Id": authlist[i][1],
      "Password Hash": authlist[i][2],
      "Salt": authlist[i][3]
    })
  return {"Auth List": output}

def authGET(authAgent, externalId):
  auth = authAgent.get_auth(externalId)
  if (len(auth) > 0):
    output = {
      "Id": auth[0][0],
      "External Id": auth[0][1],
      "Password Hash": auth[0][2],
      "Salt": auth[0][3]
    }
    return output
  else:
    return "Not found"