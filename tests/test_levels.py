import unittest

from levels import LEVELS


class LevelPlacementTests(unittest.TestCase):
    def test_build_spots_stay_outside_path(self):
        for level in LEVELS.values():
            path = level["path"]
            path_width = level.get("path_width", 70)
            margin = 12

            for spot in level["build_spots"]:
                self.assertGreaterEqual(
                    self._distance_to_path((spot["x"], spot["y"]), path),
                    path_width / 2 + margin,
                )

    def _distance_to_path(self, point, path):
        px, py = point
        best = float("inf")

        for i in range(len(path) - 1):
            x1, y1 = path[i]
            x2, y2 = path[i + 1]
            dx = x2 - x1
            dy = y2 - y1
            if dx == 0 and dy == 0:
                continue

            t = ((px - x1) * dx + (py - y1) * dy) / (dx * dx + dy * dy)
            t = max(0.0, min(1.0, t))
            cx = x1 + t * dx
            cy = y1 + t * dy
            dist = ((px - cx) ** 2 + (py - cy) ** 2) ** 0.5
            best = min(best, dist)

        return best


if __name__ == "__main__":
    unittest.main()
