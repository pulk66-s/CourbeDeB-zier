from typing import List, Callable
from scipy.special import comb
import matplotlib.pyplot as plt

class Bezier:

    def __bezier_polynomial(self, n: int, i: int) -> Callable[[float], float]:
        return lambda t: comb(n, i) * (t ** i) * (1 - t) ** (n - i)

    def __mul_points(self, scalar: float, point: List[float]) -> List[float]:
        return [scalar * x for x in point]

    def __add_points(self, point1: List[float], point2: List[float]) -> List[float]:
        return [point1[i] + point2[i] for i in range(len(point1))]

    def __active_equation(self, bezier_polynomials: List[Callable[[float], float]], points: List[List[float]], t: float) -> List[float]:
        res: List[float] = [0, 0]
        i: int = 0
        for p in bezier_polynomials:
            res = self.__add_points(res, self.__mul_points(p(t), points[i]))
            i += 1
        return res

    def __get_equation(self, points: List[List[int]]) -> Callable[[float], List[float]]:
        bezier_polynomials: List[Callable[[float], float]] = [self.__bezier_polynomial(self.n, i) for i in range(self.n + 1)]
        lambda_function: Callable[[float], List[float]] = lambda t: self.__active_equation(bezier_polynomials, points, t)
        return lambda_function

    def __init__(self, degree: int, points: List[List[int]]):
        self.n: int = degree
        self.points: List[List[int]] = points
        self.equation: Callable[[float], List[int]] = self.__get_equation(self.points)
        self.bezier_points: List[List[int]] = [self.equation(t / 100) for t in range(0, 101)]
        self.plot_x = [point[0] for point in self.bezier_points] + [i[0] for i in self.points]
        self.plot_y = [point[1] for point in self.bezier_points] + [i[1] for i in self.points]
        self.plot = plt.plot(self.plot_x, self.plot_y)

    def show(self):
        plt.show()