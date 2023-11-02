# These methods do time-based calculations.
# Jira stores time spans as seconds, and these
# convert the seconds into more readable formats
# (i.e. number of years, months, days, hours, minutes)

def get_time_estimate_in_seconds(issue):
    """Strips time estimate from issue object, or
       0 if not present in metadata

    Args:
        issue (object): Issue object from Jira API

    Returns:
        string or 0: formatted time estimate in seconds, if available
    """
    fields = issue["fields"]
    timetracking = fields["timetracking"]
    if "originalEstimateSeconds" in timetracking:
        return f"{timetracking['originalEstimateSeconds']:.2f}"
    return 0


def get_time_remaining_in_seconds(issue):
    """Strips time remaining from issue object, or
       0 if not present in metadata

    Args:
        issue (object): Issue object from Jira API

    Returns:
        string or 0: formatted time remaining in seconds, if available
    """
    fields = issue["fields"]
    timetracking = fields["timetracking"]
    if "remainingEstimateSeconds" in timetracking:
        return f"{timetracking['remainingEstimateSeconds']:.2f}"
    return 0

def get_man_seconds(issue):
    """Strips man seconds from issue object timetracking, or
       0 if not present in metadata

    Args:
        issue (object): Issue object from Jira API

    Returns:
        string or 0: formatted man seconds, if available
    """
    fields = issue["fields"]
    timetracking = fields["timetracking"]
    if "timeSpentSeconds" in timetracking:
        return timetracking["timeSpentSeconds"]
    return 0

# Based on 8-hour day
def convert_seconds_to_days(timespan_in_seconds):
    """Calculates how many 8-hour workdays are in the given timespan (seconds)

    Args:
        timespan_in_seconds (int): Number of seconds from Jira API timetracking

    Returns:
        number: timespan in days
    """
    if isinstance(timespan_in_seconds, str):
        try:
            timespan_in_seconds = float(timespan_in_seconds)
        except ValueError:
            return 0
    return timespan_in_seconds/(8*3600)

def timestring_to_seconds(timestring):
    """Parses a string that may have a week (w), day (d),
       hours (h), min (m), and/or seconds (s) component,
       and calculates the resulting number of seconds 
    Args:
        timestring (string): Jira description of timespan, with
                             w/d/h/m/s components

    Returns:
        number/int: combined calclation of seconds from timespan components
    """
    if isinstance(timestring, int):
        return timestring
    if isinstance(timestring, float):
        return timestring
    parts = timestring.split(' ')
    total_time = 0
    for part in parts:
        if part[-1].isalpha():
            unit = part[-1]
            number = part[:-1]
            if unit == 's':
                total_time += int(number)
            elif unit == 'm':
                total_time += int(number)*60
            elif unit == 'h':
                total_time += int(number)*60*60
            elif unit == 'd':
                total_time += int(number)*60*60*8
            elif unit == 'w':
                total_time += int(number)*60*60*40
        else:
            if len(parts) == 1:
                return float(parts[0])
    return total_time
