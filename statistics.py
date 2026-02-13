
import time
import CFAPI
from pprint import pprint
from pathlib import Path
import json
from datetime import datetime
def general_info

def get_submissions(handle: str, save: bool = False):
  if save:
    if Path("file.json").is_file() is False:
      seen = set()
      submissions = CFAPI.public_submissions(handle)
      json.dump(submissions, open(f"{handle}_submissions.json", "w"), indent = 2)

    submissions = json.load(open(f"{handle}_submissions.json", "r"))
  else:
    submissions = CFAPI.public_submissions(handle)
  return submissions

def recent_solves(handle: str, save: bool = False):
  submissions = get_submissions(handle, save)
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

# shows a heatmap of the number of problems solved by hour and day of the week
def heatmap_weekly(handle: str, save: bool = False):
  submissions = get_submissions(handle, save)
  heatmap_weekly = [[0 for _ in range(24)] for _ in range(7)]
  for sub in submissions:
    if sub['verdict'] != "OK":
      continue
    sub_time = datetime.fromtimestamp(sub['creationTimeSeconds'])
    heatmap_weekly[sub_time.weekday()][sub_time.hour] += 1
  return heatmap_weekly

#shows a heatmap of the number of problems solved every day of every year since the account was created
def heatmap_alltime(handle: str, save: bool = False):

for key, val in recent_solves("Trollbert").items():
  print(f"{key}: {val}")