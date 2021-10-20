'''2. Андре септиянто - Реализовать проект расчета суммарного расхода ткани на производство одежды. Основная сущность (класс) этого проекта — одежда, которая может иметь определенное название.
К типам одежды в этом проекте относятся пальто и костюм. У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма). Это могут быть обычные числа: V и H, соответственно.
Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5), для костюма (2 * H + 0.3). Проверить работу этих методов на реальных данных.
Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке знания: реализовать абстрактные классы для основных классов проекта, проверить на практике работу декоратора @property.'''

from abc import ABC, abstractmethod

from typing import Any


class AbstractClothes(ABC):

    @property
    @abstractmethod
    def tissue_required(self):
        pass

    @property
    @abstractmethod
    def measuring(self):
        pass

    @abstractmethod
    def _calc_tissue_required(self):
        pass


class Clothes(AbstractClothes):
    _clothes = []

    def __init__(self, name: str, measuring: Any):
        self.name = name
        self._measuring = measuring
        self._tissue_required = None

        self._clothes.append(self)

    def _calc_tissue_required(self):
        raise NotImplemented

    @property
    def tissue_required(self) -> float:
        if not self._tissue_required:
            self._calc_tissue_required()

        return self._tissue_required

    @property
    def measuring(self) -> Any:
        return self._measuring

    @measuring.setter
    def measuring(self, measuring: Any):
        self._measuring = measuring
        self._tissue_required = None

    @property
    def total_tissue_required(self):
        return sum([item.tissue_required for item in self._clothes])


class Coat(Clothes):
    def _calc_tissue_required(self):
        self._tissue_required = round(self.measuring / 6.5 + 0.5, 2)

    @property
    def V(self) -> Any:
        return self.measuring

    @V.setter
    def V(self, size: Any):
        self.measuring = size

    def __str__(self):
        return f"Для пошива пальто {self.measuring} размера " \
               f"требуется {self.tissue_required} кв. метров ткани"


class Suit(Clothes):
    def _calc_tissue_required(self):
        self._tissue_required = round(2 * self.measuring * 0.01 + 0.3, 2)

    @property
    def H(self) -> Any:
        return self.measuring

    @H.setter
    def H(self, height: Any):
        self.measuring = height

    def __str__(self):
        return f"Для пошива костюма на рост {self.measuring} см. " \
               f"требуется {self.tissue_required} кв. метров ткани"


if __name__ == '__main__':
    coat = Coat('Пальто от Zara', 5)
    print(coat)
    coat.V = 10
    print(coat)

    suit = Suit('Костюм от H&M', 178)
    print(suit)
    suit.H = 200
    print(suit)

    print(coat.total_tissue_required)
    print(suit.total_tissue_required)
