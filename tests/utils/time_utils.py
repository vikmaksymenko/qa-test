import time

class TimeUtils:
    @staticmethod
    def current_time_milis() -> int:
        """Returns current time in miliseconds"""

        return int(round(time.time() * 1000))
