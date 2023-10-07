from random import choice

from .const import CLIENTS, FACILITIES, Client, Facility
from .utils import distance_of_coordinates


def generate_random_solution() -> dict:
    """Generate random solution

    Returns:
        dict                : {facility: [clients]}
    """
    solution = {}
    for f in FACILITIES:
        solution[f] = []

    for client in CLIENTS:
        assign_to_facility = choice(FACILITIES)
        if assign_to_facility in solution:
            solution[assign_to_facility].append(client)
        else:
            solution[assign_to_facility] = [client]
    return solution


def verify_solution(mapping: dict):
    """Verify solution

    Parameters:
        mapping (dict)      : {facility: [clients]}

    Raises:
        AssertionError      : If any conditions are not met
    """
    assert isinstance(mapping, dict)
    assert len(mapping) == len(FACILITIES)
    assert all([isinstance(facility, Facility) for facility in mapping.keys()])
    assert all([facility in mapping.keys() for facility in FACILITIES])

    assert all([isinstance(clients_list, list) for clients_list in mapping.values()])
    all_clients = []
    for client_list in mapping.values():
        assert all([isinstance(client, Client) for client in client_list])
        all_clients.extend(client_list)
    assert len(all_clients) == len(CLIENTS)
    assert [client in client_list for client in CLIENTS]


def fitness(mapping: dict) -> float:
    """Calculate fitness of a solution

    Define the objective function to be optimized
    (you need to replace this with your own function)

    Parameters:
        mapping (dict)      : {facility: [clients]}

    Returns:
        float               : fitness value
    """
    verify_solution(mapping=mapping)
    _fitness = 0

    for facility, clients in mapping.items():
        for client in clients:
            _fitness += distance_of_coordinates(
                facility,
                client,
            )
    return _fitness


def get_facility_of_client(krill: dict, client: Client) -> Facility:
    """Get facility of client from a given solution (krill)

    Parameters:
        krill (dict)        : {facility: [clients]}
        client (Client)     : client

    Returns:
        Facility            : facility of client
    """
    for facility in krill:
        facility_clients = [client.key for client in krill[facility]]
        if client.key in facility_clients:
            return facility
    raise Exception("Client not found in any facility")
