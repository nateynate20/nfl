import requests
from bs4 import BeautifulSoup

# Function to scrape NFL schedule data from ESPN
def scrape_nfl_schedule(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Find the element containing schedule data
        schedule_table = soup.find('table', class_='Table Table--align-right')

        nfl_schedule = {}
        current_week = None

        # Iterate through rows of the schedule table
        for row in schedule_table.find_all('tr'):
            cells = row.find_all('td')
            if cells:
                if len(cells) == 1:
                    # This row contains the week header
                    current_week = cells[0].text.strip()
                    nfl_schedule[current_week] = []
                elif len(cells) == 4:
                    # This row contains a game
                    home_team = cells[1].text.strip()
                    away_team = cells[2].text.strip()
                    start_time = cells[3].text.strip()
                    nfl_schedule[current_week].append({
                        'home_team': home_team,
                        'away_team': away_team,
                        'start_time': start_time
                    })
        
        return nfl_schedule
    except requests.exceptions.RequestException as e:
        print(f"Error fetching NFL schedule data: {e}")
        return None

# Function to display NFL schedule with primetime games
def display_primetime_schedule(schedule):
    print("\nPrimetime NFL Schedule:")
    for week, games in schedule.items():
        print(f"{week}:")
        for game in games:
            if is_primetime_game(game['start_time']):
                print(f"{game['home_team']} vs {game['away_team']} ({game['start_time']})")

# Function to check if a game is a primetime game
def is_primetime_game(start_time):
     start_time_lower = start_time.lower()
     return ("sunday" in start_time_lower or "monday" in start_time_lower or "thursday" in start_time_lower) and "est" in start_time_lower and int(start_time_lower.split(":")[0]) >= 20

# Set the current week
current_week = "Week 2"

# URL to ESPN's NFL schedule page
espn_url = "https://www.espn.com/nfl/schedule"

# Scrape NFL schedule data from ESPN
nfl_schedule = scrape_nfl_schedule(espn_url)

if nfl_schedule:
    # Display primetime schedule for the current week
    display_primetime_schedule(nfl_schedule[current_week])
