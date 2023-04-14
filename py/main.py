import sys
from typing import List
from Bezier3 import Bezier3
from Bezier2 import Bezier2
from Bezier import Bezier

def get_points_from_file(file_name: str) -> List[List[int]]:
    points = []
    with open(file_name, "r") as file:
        lines = file.readlines()
        for line in lines:
            points.append(line.strip().split(","))
    points = [[int(x) for x in point] for point in points]
    return points

def get_file_name() -> str:
    if len(sys.argv) > 1:
        return sys.argv[1]
    return "../coords/simpleCurve3"

def main():
    file_to_open: str       = get_file_name()
    points: List[List[int]] = get_points_from_file(file_name=file_to_open)
    bezier_degree: int      = len(points) - 1
    bezier = None
    bezier_class = {
        3: Bezier3,
        2: Bezier2
    }

    print("points: ", points)
    if bezier_degree in bezier_class:
        bezier = bezier_class[bezier_degree](points=points)
    else:
        bezier = Bezier(points=points, degree=bezier_degree)
    bezier.show()

if __name__ == "__main__":
    main()
