from nfl_data_py import nfl

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

# Initialize NFLData
nfl_data = nfl()

try:
    # Fetch NFL schedule data
    nfl_schedule = nfl_data.get_schedule()

    if nfl_schedule:
        # Display primetime schedule for the current week
        display_primetime_schedule(nfl_schedule[current_week])

except Exception as e:
    print(f"Error fetching NFL schedule data: {e}")
