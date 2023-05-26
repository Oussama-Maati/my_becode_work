from datetime import datetime, timedelta

def add_gigasecond(datetime):
    lack = 1_000_000_000
    return datetime + timedelta(seconds=lack)

