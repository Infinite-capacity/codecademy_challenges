#!/usr/bin/env
premium_ground = 125.0


def get_ground_cost(weight):
    flat_rate = 20.0
    if weight <= 2.0:
        ground_cost = weight * 1.5 + flat_rate
    elif weight <= 6.0:
        ground_cost = weight * 3.0 + flat_rate
    elif weight <= 10.0:
        ground_cost = weight * 4.0 + flat_rate
    else:
        ground_cost = weight * 4.75 + flat_rate
    return ground_cost


def get_drone_cost(weight):
    if weight <= 2.0:
        drone_cost = weight * 4.5
    elif weight <= 6.0:
        drone_cost = weight * 9.0
    elif weight <= 10.0:
        drone_cost = weight * 12.0
    else:
        drone_cost = weight * 14.25
    return drone_cost


def get_cheapest_rate(weight):
    drone = get_drone_cost(weight)
    ground = get_ground_cost(weight)
    if drone < ground and drone < premium_ground:
        return "Drone is the cheapest at: $" + str(drone)
    if ground < drone and ground < premium_ground:
        return "Ground is the cheapest at: $" + str(ground)
    else:
        return "Premium ground is the cheapest at: $" + str(premium_ground)


print(get_cheapest_rate(2))
print(get_cheapest_rate(5))
print(get_cheapest_rate(7))