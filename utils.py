import requests
import time
import secrets, string
import hashlib
from sortedcontainers import SortedDict
import contestclass
import pprint

def public_submissions(handle):
  url = f'https://codeforces.com/api/user.status?handle={handle}'
  response = requests.get(url)
  return response.json()




def submissions_to_contests(submissions):
  class Contest:
  contests = dict()
  for sub in submissions:
    contests[sub['contestId']] = sub
  return list(contests)