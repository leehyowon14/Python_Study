def get_east_barrier(pos, barrier_pos_list):
    distance = sorted([
        item[0] - pos[0]
        for item in barrier_pos_list
        if item[1] == pos[1] and item[0] - pos[0] > 0
    ])
    if len(distance) == 0:
        return [0, 0]
    return [distance[0], 0]


def get_west_barrier(pos, barrier_pos_list):
    distance = sorted([
        item[0] - pos[0]
        for item in barrier_pos_list
        if item[1] == pos[1] and item[0] - pos[0] < 0
    ], reverse=True)
    if len(distance) == 0:
        return [0, 0]
    return [distance[0], 0]


def get_south_barrier(pos, barrier_pos_list):
    distance = sorted([
        item[1] - pos[1]
        for item in barrier_pos_list
        if item[0] == pos[0] and item[1] - pos[1] > 0
    ])
    if len(distance) == 0:
        return [0, 0]
    return [0, distance[0]]


def get_north_barrier(pos, barrier_pos_list):
    distance = sorted([
        item[1] - pos[1]
        for item in barrier_pos_list
        if item[0] == pos[0] and item[1] - pos[1] > 0
    ], reverse=True)
    if len(distance) == 0:
        return [0, 0]
    return [0, distance[0]]


get_closest_barrier_relative_pos = {
    "E": get_east_barrier,
    "W": get_west_barrier,
    "S": get_south_barrier,
    "N": get_north_barrier
}


def move(pos, size, route, barrier_pos_list):
    route = route.split(' ')
    route[1] = int(route[1])
    barrier_relative_pos = get_closest_barrier_relative_pos[route[0]](
        pos, barrier_pos_list)
    is_column = 0 if barrier_relative_pos[0] != 0 else 1
    distance = abs(barrier_relative_pos[is_column])
    if distance > route[1]:
        if (
            pos[is_column] + route[is_column] > size[is_column] or
            distance < route[1]
        ):
            return pos
    if is_column:
        return [pos[0] + route[1], pos[1]]
    else:
        return [pos[0], pos[1] + route[1]]


def solution(park, routes):
    current_pos = []
    barrier_pos_list = []
    size = [len(park[0]), len(park)]
    for y, items in enumerate(park):
        for x, letter in enumerate(items):
            if letter == "O":
                continue
            elif letter == "X":
                barrier_pos_list.append([x, y])
            else:
                current_pos = [x, y]

    for route in routes:
        current_pos = move(current_pos, size, route, barrier_pos_list)
    return current_pos
