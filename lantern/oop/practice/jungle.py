from __future__ import annotations

from abc import ABC, abstractmethod
from typing import List


def singleton(cls):
    instances = {}

    def getinstance(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]

    return getinstance


@singleton
class Jungle:
    def __init__(self, predators: List[Predator], herbivorous: List[Herbivorous]):
        self.predators = predators
        self.herbivorous = herbivorous


JUNGLE = Jungle(predators=[], herbivorous=[])


class Animal(ABC):
    def __init__(self, weight, speed):
        self.weight = weight
        self.speed = speed

    @abstractmethod
    def eat(self):
        raise NotImplementedError

    def third_part_of_meat_after_death(self):
        return self.weight / 3


class Predator(Animal):
    def __init__(self, weight, speed, power):
        super().__init__(weight, speed)
        self.power = power

    def __hunt(self):
        for herb in JUNGLE.herbivorous:
            if self.is_herb_a_victim(herb):
                return True
            else:
                for predator in JUNGLE.predators:
                    if self.is_predator_a_victim(predator):
                        return True
        return False

    def speed_of_herb_in_percent(self, herb: Herbivorous):
        return int(herb.speed * 100 / self.speed)

    def is_herb_a_victim(self, herb: Herbivorous):
        return self.power * 3 > herb.weight and self.speed * 1.15 > herb.speed

    def is_predator_a_victim(self, predator: Predator):
        return self.power > predator.power

    def eat(self):
        return self.__hunt()


class Herbivorous(Animal):
    def eat(self):
        pass


if __name__ == "__main__":
    # testing predator's possibility to hunt herbivorous

    simba = Predator(weight=100, speed=100, power=70)
    timon = Herbivorous(weight=10, speed=114)

    JUNGLE.predators.append(simba)
    JUNGLE.herbivorous.append(timon)
    try:
        print(simba.hunt())
    except AttributeError:
        print("Method hunt is hidden")
    # end of testing

    #  testing eat method
    print(simba.eat())

    # test animal of abstract class
    try:
        animal = Animal(weight=5, speed=10)
    except TypeError:
        print("All is OK")
    else:
        print("Something goes wrong. Animal should be abstract")

    # test Singleton
    predators = Jungle()
    herbivorous = Jungle()
    print("\n!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
    print(predators is herbivorous is JUNGLE)
    print(predators)
    print(herbivorous)
    print(JUNGLE)
    # Singleton works:)))

    # testing predator's possibility to hunt other predators
    lion = Predator(weight=250, speed=50, power=70)
    tiger = Predator(weight=300, speed=50, power=80)

    antelope = Herbivorous(weight=120, speed=75)
    buffalo = Herbivorous(weight=850, speed=45)

    JUNGLE.predators.append(lion)
    JUNGLE.predators.append(tiger)

    JUNGLE.herbivorous.append(antelope)
    JUNGLE.herbivorous.append(buffalo)

    print("\nOne another printing block")

    print(JUNGLE.predators)
    print(JUNGLE.herbivorous)

    print(lion.eat())
    # print(tiger.eat())
