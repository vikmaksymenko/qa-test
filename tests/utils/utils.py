import time
import json

def current_time_milis() -> int:
    """Returns current time in miliseconds"""

    return int(round(time.time() * 1000))

def load_json(path: str) -> dict:
    """Load json from file"""

    with open(path) as json_file:
        return json.load(json_file)
