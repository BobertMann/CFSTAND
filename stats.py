
import time
import CFAPI
from pprint import pprint
from pathlib import Path
import json
from datetime import datetime

def get_submissions(handle: str, save: bool = False, force_save: bool = False):
  if save:
    if Path(f"user_data/{handle}/{handle}_submissions.json").is_file() is False or force_save:
      seen = set()
      submissions = CFAPI.public_submissions(handle)
      Path(f"user_data/{handle}").mkdir(parents=True, exist_ok=True)
      json.dump(submissions, open(f"user_data/{handle}/{handle}_submissions.json", "w"), indent = 2)
    submissions = json.load(open(f"user_data/{handle}/{handle}_submissions.json", "r"))
  else:
    submissions = CFAPI.public_submissions(handle)
  return submissions

def recent_solves(handle: str, save: bool = False, upsolve_only: bool = False, force_save: bool = False):
  submissions = get_submissions(handle, save, force_save)
  sysdate = datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S')
  cur_time = datetime.fromtimestamp(time.time())
  today = 0
  this_week = 0
  last_month = 0
  last_year = 0
  all_time = 0
  all_time = 0
  #for sub in json:
  print(sysdate)
  seen = set()
  for sub in reversed(submissions):
    if sub['verdict'] != "OK" or (sub['contestId'], sub['problem']['index']) in seen:
      continue
    if upsolve_only and sub['author']['participantType'] == "CONTESTANT":
      continue
    seen.add((sub['contestId'], sub['problem']['index']))
    problem_date = datetime.fromtimestamp(sub['creationTimeSeconds']).strftime('%Y-%m-%d %H:%M:%S')
    sub_time = datetime.fromtimestamp(sub['creationTimeSeconds'])
    delt = (cur_time - sub_time).days
    if problem_date == sysdate:
      today += 1
    if delt < 7:
      this_week += 1
    if delt < 30:
      last_month += 1
    if delt < 365:
      last_year += 1
    all_time += 1
  return {'today': today, 'this_week': this_week, 'last_month': last_month, 'last_year': last_year, 'all_time': all_time}

# returns a matrix of the number of problems solved by hour and day of the week
def heatmap_weekly(handle: str, save: bool = False, upsolve_only: bool = False, force_save: bool = False):
  submissions = get_submissions(handle, save, force_save)
  heatmap_weekly = [[0 for _ in range(24)] for _ in range(7)]
  for sub in submissions:
    if sub['verdict'] != "OK":
      continue
    if upsolve_only and sub['author']['participantType'] == "CONTESTANT":
      continue
    sub_time = datetime.fromtimestamp(sub['creationTimeSeconds'])
    heatmap_weekly[sub_time.weekday()][sub_time.hour] += 1
  return heatmap_weekly

# returns a dictionary of the number of problems solved every day of every year since the account was created
def heatmap_alltime(handle: str, save: bool = False, upsolve_only: bool = False, force_save: bool = False):
  submissions = get_submissions(handle, save, force_save)
  heatmap_alltime = {}
  for sub in submissions:
    if sub['verdict'] != "OK":
      continue
    sub_time = datetime.fromtimestamp(sub['creationTimeSeconds'])
    date_str = sub_time.strftime('%Y-%m-%d')
    if date_str not in heatmap_alltime:
      heatmap_alltime[date_str] = 0
    heatmap_alltime[date_str] += 1
  return heatmap_alltime

# returns a dictionary of the number of verdicts of each type (OK, WRONG_ANSWER, TIME_LIMIT_EXCEEDED, etc.)
def verdict_counts(handle: str, save: bool = False, upsolve_only: bool = False, force_save: bool = False):
  submissions = get_submissions(handle, save, force_save)
  verdict_counts = {}
  for sub in submissions:
    if upsolve_only and sub['author']['participantType'] == "CONTESTANT":
      continue
    verdict = sub['verdict']
    if verdict not in verdict_counts:
      verdict_counts[verdict] = 0
    verdict_counts[verdict] += 1
  return verdict_counts

# returns a dictionary of the number of problems solved in each programming language
def language_counts(handle: str, save: bool = False, upsolve_only: bool = False, force_save: bool = False):
  submissions = get_submissions(handle, save, force_save)
  language_counts = {}
  for sub in submissions:
    if upsolve_only and sub['author']['participantType'] == "CONTESTANT":
      continue
    language = sub['programmingLanguage']
    if language not in language_counts:
      language_counts[language] = 0
    language_counts[language] += 1
  return language_counts

#returns a dictionary of the number of problems solved with each tag
def tag_counts(handle: str, save: bool = False, upsolve_only: bool = False, force_save: bool = False):
  submissions = get_submissions(handle, save, force_save)
  tag_counts = {}
  for sub in submissions:
    if sub['verdict'] != 'OK':
      continue
    if sub['author']['participantType'] == 'CONTESTANT' and upsolve_only:
      continue
    for tag in sub['problem']['tags']:
      if tag not in tag_counts:
        tag_counts[tag] = 0
      tag_counts[tag] += 1


# returns data for each handle the user had in the past
def user_info(handle: str):
  return CFAPI.user_info(handle)
