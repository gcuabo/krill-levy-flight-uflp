import numpy as np

from .conf import KRILL_MAX_ITER, KRILL_NUM_KRILL
from .const import CLIENTS, FACILITIES
from .krill import (distance_of_coordinates, fitness, generate_random_solution,
                    get_facility_of_client)
from .levy_flight import generate_levy_flight_solution
from .logger import logger

__all__ = ("run_krill_algo",)


def run_krill_algo() -> tuple:
    """Run krill-herd algorithm

    Returns:
        tuple       : (best_solution, best_fitness)
    """
    # Initialize krill positions randomly in the solution space
    krill_positions = [generate_random_solution() for _ in range(KRILL_NUM_KRILL)]

    # # Initialize krill fitness values
    krill_fitness = [fitness(krill) for krill in krill_positions]

    logger.info(f"Iteration : Best Fitness = {min(krill_fitness)}")

    # Main loop
    for iteration in range(KRILL_MAX_ITER):
        for i in range(KRILL_NUM_KRILL):
            # Attraction movement
            attractor = krill_positions[np.argmin(krill_fitness)]  # returns dictionary

            new_krill = {}
            for facility in FACILITIES:
                new_krill[facility] = []
            random_value = np.random.random()
            for client in CLIENTS:
                current_krill_client_facility = get_facility_of_client(
                    krill_positions[i], client
                )
                attractor_krill_client_facility = get_facility_of_client(
                    attractor, client
                )
                movement = random_value * (
                    (
                        # distance between attractor_krill_client_facility and attractor
                        distance_of_coordinates(current_krill_client_facility, client)
                    )
                    - (
                        # distance between current_krill_client_facility and attractor
                        distance_of_coordinates(attractor_krill_client_facility, client)
                    )
                )
                repulsion = max(
                    distance_of_coordinates(
                        get_facility_of_client(krill, client), client
                    )
                    for index, krill in enumerate(krill_positions)
                    if index != i
                ) - distance_of_coordinates(current_krill_client_facility, client)

                # Find facility nearest to this movement
                distance_to_facilities = [
                    distance_of_coordinates(facility, client) for facility in FACILITIES
                ]
                new_facility = FACILITIES[
                    np.argmin(
                        [
                            np.abs(
                                distance_to_facilities[facility_index]
                                - (movement + repulsion)
                            )
                            for facility_index, _ in enumerate(FACILITIES)
                        ]
                    )
                ]
                new_krill[new_facility].append(client)

            krill_positions[i] = new_krill
            krill_fitness[i] = fitness(new_krill)

            # Update attractor position based on the best krill
            global_best = np.argmin(krill_fitness)
            new_krill = generate_levy_flight_solution(krill_positions[global_best])

            if global_best > fitness(new_krill):
                krill_positions[i] = new_krill
                krill_fitness[i] = fitness(new_krill)

        logger.info(f"Iteration {iteration+1}: Best Fitness = {min(krill_fitness)}")

    # Print the final result
    best_solution = krill_positions[np.argmin(krill_fitness)]
    best_fitness = min(krill_fitness)

    logger.info(f"Optimal Solution: {best_solution}")
    logger.info(f"Optimal Fitness: {best_fitness}")

    return best_solution, best_fitness
