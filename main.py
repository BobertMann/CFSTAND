import requests
import time
import secrets, string
import hashlib
from sortedcontainers import SortedDict
import pprint
APIkey = "d9a953cd1a6cb9bd00688e07dddc041ed7316e39"
APIsecret = "5177f7f82a88a429ddb4572cd200e7e0bb08e359"

chars = string.ascii_letters + string.digits
rand = ''.join(secrets.choice(chars) for _ in range(6))
rand = '123456'

def contests_from_submissions(submissions):
  contests = []
  for sub in submissions:
    contests.append(sub['contestId'])
  return contests

params = SortedDict({
  "handle" : "MermaidMolester",
  "from" : "1",
  "count" : "1",
  "time" : str(int(time.time())),
  "apiKey" : APIkey,
  # 'contestId' : 566,
})

query = "user.status"
ok = 0
for key, value in params.items():
  query += f"{"?&"[ok]}{key}={value}"
  ok = 1
print(query)



url = f"https://codeforces.com/api/{query}&apiSig={rand}{hashlib.sha512(f'{rand}/{query}#{APIsecret}'.encode()).hexdigest()}"
response = requests.get(url)
print(url)
pprint.pprint(response)
print(response.json()['status'])
if (response.json()['status'] != "OK"):
  print(response.json()['comment'])
  exit()
contestid = response.json()['result'][0]['contestId']
print(response.json()['result'][0]['problem']['name'])
print(contestid)
exit()

url = f"https://codeforces.com/api/contest.standings?contestId={contestid}&showUnofficial=true&handle=TheOnesWhoKnock"
standings = requests.get(url).json()['result']['rows']
# print(standings[0]['party']['teamName'])
for party in standings:
  if 'teamName' in party['party']:
    print(f"{party['rank']} : {party['party']['teamName']}")
    if(party['party']['teamName'] == "TheOnesWhoKnock"):
      break