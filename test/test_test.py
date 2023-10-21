from ohmysportsfeedspy import MySportsFeeds

# Create an instance of MySportsFeeds with your API credentials
msf = MySportsFeeds(version="2.1", verbose=True)
msf.authenticate("natedogg1", "wizkids5!")

# Define the season and format
season = "2023-2024-regular"
output_format = "json"

# Get NFL game schedule data
data = msf.msf_get_data(league="nfl", season=season, feed="seasonal_games", format=output_format)

# Process and work with the data as needed
# For example, you can save it to a CSV file:
import json
with open("nfl_game_schedule.json", "w") as json_file:
    json.dump(data, json_file, indent=4)

print("NFL game schedule data retrieved and saved to 'nfl_game_schedule.json'.")
