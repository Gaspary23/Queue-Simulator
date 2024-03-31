from dataclasses import dataclass
from enum import Enum


class EventType(Enum):
    ARRIVAL = 1
    DEPARTURE = 2


@dataclass
class Event:
    event_type: EventType
    time: float
