from collections import namedtuple

__all__ = (
    "CLIENTS",
    "FACILITIES",
    "Client",
    "Facility",
)


Client = namedtuple("Client", ["key", "x", "y"])
Facility = namedtuple("Facility", ["key", "x", "y"])

# UNFACILITATED FACILITY LOCATION PROBLEM
CLIENTS = [
    Client("A", 2, 1),
    Client("B", 3, 2),
    Client("C", 2, 3),
    Client("D", 4, 4),
    Client("E", 3, 5),
    Client("F", 4, 6),
    Client("G", 8, 4),
    Client("H", 9, 5),
    Client("I", 10, 1),
    Client("J", 6, 10),
]
FACILITIES = [
    Facility("X", 4, 1),
    Facility("Y", 8, 3),
    Facility("Z", 3, 7),
]
