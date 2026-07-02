import math


def generate_build_spots(path, path_width=70, spot_size=24, margin=12):
    spots = []
    for index in range(len(path) - 1):
        x1, y1 = path[index]
        x2, y2 = path[index + 1]

        dx = x2 - x1
        dy = y2 - y1
        length = max(math.hypot(dx, dy), 1.0)
        nx = -dy / length
        ny = dx / length

        side = 1 if index % 2 == 0 else -1
        distance = path_width / 2 + margin + spot_size / 2
        mid_x = (x1 + x2) / 2
        mid_y = (y1 + y2) / 2

        x = mid_x + nx * distance * side
        y = mid_y + ny * distance * side

        spots.append({"x": int(round(x)), "y": int(round(y)), "size": spot_size})

    return spots


LEVELS = {
    "default": {
        "name": "River Bend",
        "path": [
            (0, 0),
            (220, 0),
            (220, 260),
            (620, 260),
            (620, 620),
            (1000, 620),
        ],
        "path_width": 70,
        "build_spots": generate_build_spots(
            [
                (0, 0),
                (220, 0),
                (220, 260),
                (620, 260),
                (620, 620),
                (1000, 620),
            ],
            path_width=70,
        ),
    },
    "zigzag": {
        "name": "Zigzag",
        "path": [
            (0, 120),
            (180, 120),
            (180, 360),
            (520, 360),
            (520, 650),
            (1000, 650),
        ],
        "path_width": 70,
        "build_spots": generate_build_spots(
            [
                (0, 120),
                (180, 120),
                (180, 360),
                (520, 360),
                (520, 650),
                (1000, 650),
            ],
            path_width=70,
        ),
    },
}
