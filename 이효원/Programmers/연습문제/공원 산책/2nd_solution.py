def solution(park, routes):
    current_pos_x, current_pos_y = -1, -1
    for y, row in enumerate(park):
        for x, type in enumerate(row):
            if type == "S":
                current_pos_x, current_pos_y = x, y
                break
        if current_pos_x != -1 and current_pos_y != -1:
            break

    dir_vector = {
        "N": (0, -1),
        "S": (0, 1),
        "E": (1, 0),
        "W": (-1, 0)
    }

    for route in routes:
        direction, distance = route.split()
        direction_x, direction_y = dir_vector[direction]
        distance = int(distance)

        temp_x, temp_y = current_pos_x, current_pos_y
        for i in range(distance):
            temp_x += direction_x
            temp_y += direction_y

            if (
                temp_x < 0 or
                temp_x > len(park[0]) - 1 or
                temp_y < 0 or
                temp_y > len(park) - 1
            ):
                break
            elif park[temp_y][temp_x] == "X":
                break
        else:
            current_pos_x, current_pos_y = temp_x, temp_y

    return [current_pos_y, current_pos_x]
