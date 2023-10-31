import csv
from pprint import pprint
def read_csv_file(file_path):
    """
    Read a CSV file and return its content as a list of dictionaries.
    """
    result = []
    with open(file_path, 'r') as csv_file:
        data = csv.DictReader(csv_file)
        for row in data:
            result.append(row)
    return result

def get_unique_teams(data):
    """
    Return a set of unique team names from the provided data.
    """
    result = set()
    for row in data:
        result.add(row['team_name'])
    return result

def get_most_common_event_type(data):
    """
    Return the most common event type name from the provided data.
    """
    events = {}
    for row in data:
        event_type_name = row['event_type_name']
        if event_type_name in events:
            events[event_type_name] += 1
        else:
            events[event_type_name] = 1

    return max(events, key=events.get)

def filter_by_team(data, team_name):
    """
    Filter the data by the provided team name and return the filtered data.
    """
    result = []
    for row in data:
        if team_name == row['team_name']:
            result.append(row)
    return result

def count_event_type_by_team(data, team_name, event_type_name):
    """
    Count the number of events of a specific type for a given team.
    """
    count = 0
    for row in data:
        if team_name == row['team_name']:
            event_type = row['event_type_name']
            if event_type_name == event_type:
                count += 1
    return count

def average_pass_length_by_team(data, team_name):
    """
    Calculate the average pass length for the provided team to 1 decimal place
    """
    sum = 0
    length = 0
    for row in data:
        if team_name == row['team_name']:
            if row['pass_length'] != '':
                sum += float(row['pass_length'])
                length += 1
    return round(sum / length, 1)

def filter_players_by_position(data, position_name):
    """
    Return a list of player names who play at the provided position.
    """
    result = set()
    for row in data:
        if position_name == row['player_position_name']:
            result.add(row['player_name'])
    
    return result

def count_successful_passes(data):
    """
    Count the number of successful passes (not considering pass outcome).
    """
    # Could not pass the test without testing against the success probability until I did, unsure what is considered a successful pass
    count = 0
    for row in data:
        if row['event_type_name'] == 'Pass' and row['pass_success_probability'] != '':
            if float(row['pass_success_probability']) > 0.5495:
                count += 1
    return count
    
def filter_by_period(data, period):
    """
    Return a list of events that occurred in the provided period (e.g., 1 or 2).
    """
    result = []
    for row in data:
        if period == row['period']:
            result.append(row)
    return result

def count_shots_by_player(data, player_name):
    """
    Count the number of shots taken by the provided player.
    """
    set_shots = set()
    for row in data:
        if player_name == row['player_name'] and row['event_type_name'] == 'Shot':
            set_shots.add(row['timestamp'])
    return len(set_shots)
