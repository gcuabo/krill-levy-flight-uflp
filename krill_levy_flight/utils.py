from .const import Client, Facility

__all__ = (
    "assert_are_coordinates",
    "distance_of_coordinates",
)


def assert_are_coordinates(client_or_facility: list) -> None:
    """Assert that the list of coordinates are valid

    Parameters:
        client_or_facility (list)       : List of coordinates

    Raises:
        AssertionError                  : If any conditions are not met
    """
    assert isinstance(client_or_facility, list)
    assert all(
        [
            isinstance(client, tuple) and client.x and client.y
            for client in client_or_facility
        ]
    )


def distance_of_coordinates(
    coord_1: Client | Facility, coord_2: Client | Facility
) -> None:
    """Calculates the distance between two coordinates

    Parameters:
        coord_1 (tuple)                 : (x, y)
        coord_2 (tuple)                 : (x, y)
    """
    assert_are_coordinates([coord_1, coord_2])
    return (((coord_1.x - coord_2.x) ** 2) + ((coord_1.y - coord_2.y) ** 2)) ** 0.5
