from enum import IntEnum

class LogLevel(IntEnum):
    TRACE = 10
    DEBUG = 20
    INFO = 30
    WARNING = 40
    ERROR = 50
    CRITICAL = 60

    @classmethod
    def from_str(cls, level: str) -> "LogLevel":
        return cls[level.upper()]
