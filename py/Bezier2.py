from typing import List, Callable
from scipy.special import comb
import matplotlib.pyplot as plt

class Bezier2:

    def __bezier2_polynomial(self, i: int) -> Callable[[float], float]:
        return lambda t: comb(2, i) * (t ** i) * (1 - t) ** (2 - i)

    def __mul_points(self, scalar: float, point: List[float]) -> List[float]:
        return [scalar * x for x in point]

    def __add_points(self, point1: List[float], point2: List[float]) -> List[float]:
        return [point1[i] + point2[i] for i in range(len(point1))]

    def __get_equation(self, points: List[List[int]]) -> Callable[[float], List[float]]:
        B0: Callable[[float], float] = self.__bezier2_polynomial(0)
        B1: Callable[[float], float] = self.__bezier2_polynomial(1)
        B2: Callable[[float], float] = self.__bezier2_polynomial(2)

        return lambda t: self.__add_points(
            self.__add_points(
                self.__mul_points(B0(t), points[0]),
                self.__mul_points(B1(t), points[1])
            ),
            self.__mul_points(B2(t), points[2])
        )

    def __init__(self, points: List[List[int]]):
        self.points: List[List[int]] = points
        self.equation: Callable[[float], List[int]] = self.__get_equation(self.points)
        self.bezier_points: List[List[int]] = [self.equation(t / 100) for t in range(0, 101)]
        self.plot_x = [point[0] for point in self.bezier_points] + [i[0] for i in self.points]
        self.plot_y = [point[1] for point in self.bezier_points] + [i[1] for i in self.points]
        self.plot = plt.plot(self.plot_x, self.plot_y)

    def show(self):
        plt.show()