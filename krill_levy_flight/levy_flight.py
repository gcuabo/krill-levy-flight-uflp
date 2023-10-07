from math import gamma
from random import uniform

import numpy as np

from .conf import LEVY_BETA, LEVY_N
from .const import FACILITIES
from .krill import generate_random_solution, verify_solution


def generate_levy_flight_solution(global_best: list) -> dict:
    """Generate random solution from the current global best via levy flight

    Parameters:
        global_best (dict)      : {facility: [clients]}

    Returns:
        dict                    : {facility: [clients]}
    """
    verify_solution(mapping=global_best)

    num = gamma(1 + LEVY_BETA) * np.sin(np.pi * LEVY_BETA / 2)
    den = gamma((1 + LEVY_BETA) / 2) * LEVY_BETA * (2 ** ((LEVY_BETA - 1) / 2))
    σu = (num / den) ** (1 / LEVY_BETA)
    σv = 1
    u = np.random.normal(0, σu, LEVY_N)
    v = np.random.normal(0, σv, LEVY_N)
    S = u / (np.abs(v) ** (1 / LEVY_BETA))
    S = S[0]

    # dictify client positions based on facility
    # {
    #   Client(2,1): 2,
    #   Client(2,1): 0,
    #   ..
    # }
    random_solution = generate_random_solution()
    clients = {}
    for index, (_, facility) in enumerate(random_solution.items()):
        for client in facility:
            clients[client] = index

    client_from_best = {}
    for index, (_, facility) in enumerate(global_best.items()):
        for client in facility:
            client_from_best[client] = index

    # Generate new solution from global best on random walk
    solution = {}
    for index, f in enumerate(FACILITIES):
        solution[index] = {"facility": f, "clients": []}

    # normalize solution
    new_index = None
    for key, index in clients.items():
        while new_index is None or (new_index < 0 or new_index >= len(FACILITIES)):
            new_index = round(
                index + (uniform(0, 1) * (0.1 * S * client_from_best[key]))
            )
        solution[new_index]["clients"].append(key)

    normalized_solution = {}
    for index, soln in solution.items():
        normalized_solution[soln["facility"]] = soln["clients"]

    return normalized_solution
