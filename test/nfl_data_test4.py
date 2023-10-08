import requests
from bs4 import BeautifulSoup

# Function to scrape NFL schedule data from pro-football-reference.com
def scrape_nfl_schedule(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')

        nfl_schedule = {}
        current_week = None

        # Find the elements containing schedule data
        schedule_tables = soup.find_all('table', class_='suppress_glossary')
        for table in schedule_tables:
            week_header = table.find_previous('h2')
            if week_header:
                current_week = week_header.text.strip()
                nfl_schedule[current_week] = []

            rows = table.find_all('tr')
            for row in rows[1:]:  # Skip the header row
                columns = row.find_all(['th', 'td'])
                if len(columns) >= 4:
                    home_team = columns[1].text.strip()
                    away_team = columns[2].text.strip()
                    start_time = columns[3].text.strip()
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
    for week, games in schedule.items():
        print(f"{week} Schedule:")
        print("{:<20} {:<20} {:<20}".format("Home Team", "Away Team", "Start Time"))
        for game in games:
            home_team = game['home_team']
            away_team = game['away_team']
            start_time = game['start_time']
            print("{:<20} {:<20} {:<20}".format(home_team, away_team, start_time))
        print()

# Set the current week
current_week = "Week 2"

# URL to pro-football-reference.com's NFL schedule page
pfr_url = "https://www.pro-football-reference.com/years/2023/games.htm"  # Update the URL for the desired year

# Scrape NFL schedule data from pro-football-reference.com
nfl_schedule = scrape_nfl_schedule(pfr_url)

if nfl_schedule:
    # Display primetime schedule for the current week
    display_primetime_schedule(nfl_schedule[current_week])
