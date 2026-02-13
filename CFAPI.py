import requests
import time
import secrets, string
import hashlib
from sortedcontainers import SortedDict
import pprint

def public_submissions(handle):
  url = f'https://codeforces.com/api/user.status?handle={handle}'
  response = requests.get(url)
  if (response.json()['status'] != "OK"):
    print(f"In request for user {handle}: {response.json()['comment']}")
    exit()
  return response.json()['result']

full_public_contest_list_cache = None
gym_public_contest_list_cache = None
rounds_public_contest_list_cache = None
def full_public_contest_list():
  if globals()['full_public_contest_list_cache'] is None:
    globals()['full_public_contest_list_cache'] = gym_public_contest_list() + rounds_public_contest_list()
  return globals()['full_public_contest_list_cache']



def gym_public_contest_list():
  url = 'https://codeforces.com/api/contest.list?gym=true'
  response = requests.get(url)
  if (response.json()['status'] != "OK"):
    print(f"In request for gym contest list: {response.json()['comment']}")
    exit()
  if globals()['gym_public_contest_list_cache'] is None:
    globals()['gym_public_contest_list_cache'] = response.json()['result']
  return globals()['gym_public_contest_list_cache']

def rounds_public_contest_list():
  url = 'https://codeforces.com/api/contest.list?gym=false'
  response = requests.get(url)
  if (response.json()['status'] != "OK"):
    print(f"In request for rounds contest list: {response.json()['comment']}")
    exit()
  if globals()['rounds_public_contest_list_cache'] is None:
    globals()['rounds_public_contest_list_cache'] = response.json()['result']
  return globals()['rounds_public_contest_list_cache']


# def submissions_to_contests(submissions, contests : dict((int, str), Contest)):
#   for sub in submissions:
#     ref = contests[(sub['contestId'], sub['author']['']]
#     ref.contestId = sub['contestId']
#     ref.contest_name = sub['contestName']
#     ref.start_time = sub['creationTimeSeconds'] - sub['relativeTimeSeconds']