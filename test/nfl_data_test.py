import requests
from nflapi import NFL

def fetch_nfl_schedule(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.json()
    except
    requests.exceptions.RequestException as e:
    print(f"Error fetching NFL schedule data: {e}")
    return None

def display_primetime_schedule(schedule):
     print("\nPrimetime NFL Schedule:")
     for week, games in schedule.items():
          print(f"{week}:")
          for game in games:
               if is_primetime_game(game["start_time"]):
                    print (f"{game['home_team']} vs {game['away_team']} {game['start_time']}")

def is_primetime_game(start_time):
     start_time_lower = start_time.lower()
     return ("sunday" in start_time_lower or "monday" in start_time_lower or "thursday" in start_time_lower) and "est" in start_time_lower and int(start_time_lower.split(":")[0]) >= 20

current_week = nfl.schedule.current_week()

nfl = NFL(ua="nflapi example script")

nfl_schedule = fetch_nfl_schedule(nfl)

if nfl_schedule :
     display_primetime_schedule(nfl_schedule[current_week])

