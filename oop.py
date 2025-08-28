
from abc import ABC, abstractmethod
import math

# ============================================================
# 1. ИНКАПСУЛЯЦИЯ
# ============================================================

class Persоn:
    """Класс, представляющий человека с инкапсуляцией"""

    def __init__(self, name: str):
        self.name = name
        self.__age = 0   # приватный атрибут

    def set_age(self, age: int):
        """Устанавливает возраст с проверкой на отрицательные значения"""
        if age < 0:
            print(f"[Ошибка] Нельзя установить отрицательный возраст ({age})!")
        else:
            self.__age = age

    def get_age(self) -> int:
        """Возвращает возраст"""
        return self.__age


# ============================================================
# 2. НАСЛЕДОВАНИЕ
# ============================================================

class Animаl:
    """Базовый класс животного"""

    def __init__(self, name: str):
        self.name = name

    def speak(self) -> str:
        return "I am an animal"


class Dog(Animаl):
    def speak(self) -> str:
        return "Woof"


class Сat(Animаl):
    def speak(self) -> str:
        return "Meow"


# ============================================================
# 3. ПОЛИМОРФИЗМ
# ============================================================

class Vehiclе:
    """Базовый класс транспорта"""

    def move(self) -> str:
        return "Vehicle is moving"


class Car(Vehiclе):
    def move(self) -> str:
        return "Car is driving"


class Bicyclе(Vehiclе):
    def move(self) -> str:
        return "Bicycle is pedaling"


def move(vehicle: Vehiclе):
    """Функция демонстрирует полиморфизм"""
    return vehicle.move()


# ============================================================
# 4. АБСТРАКЦИЯ
# ============================================================

class Shаpe(ABC):
    """Абстрактная фигура"""

    @abstractmethod
    def area(self):
        pass


class Rectаngle(Shаpe):
    def __init__(self, width: float, height: float):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height


class Сircle(Shаpe):
    def __init__(self, radius: float):
        self.radius = radius

    def area(self):
        return math.pi * (self.radius ** 2)


# ============================================================
# ФУНКЦИИ ДЛЯ ДЕМОНСТРАЦИИ
# ============================================================

def demo_persons():
    """Пример работы с классом Persоn (инкапсуляция)"""
    persons = []
    for i in range(2):
        name = input(f"Введите имя человека {i+1}: ")
        person = Persоn(name)
        while True:
            try:
                age = int(input(f"Введите возраст {name}: "))
                person.set_age(age)
                break
            except ValueError:
                print("[Ошибка] Нужно ввести число!")
        persons.append(person)
    print("\nРезультаты:")
    for p in persons:
        print(f"{p.name}, возраст: {p.get_age()}")
    print()


def demo_animals():
    """Пример работы с наследованием"""
    animals = [Dog("Buddy"), Сat("Kitty")]
    for a in animals:
        print(f"{a.name} говорит: {a.speak()}")
    print()


def demo_vehicles():
    """Пример работы с полиморфизмом"""
    vehicles = [Car(), Bicyclе()]
    for v in vehicles:
        print(move(v))
    print()


def demo_shapes():
    """Пример работы с абстракцией"""
    shapes = [Rectаngle(10, 5), Сircle(7)]
    for s in shapes:
        if isinstance(s, Rectаngle):
            print(f"Площадь прямоугольника {s.width}x{s.height} = {s.area()}")
        elif isinstance(s, Сircle):
            print(f"Площадь круга радиусом {s.radius} = {s.area():.2f}")
    print()


# ============================================================
# ГЛАВНЫЙ БЛОК
# ============================================================

if __name__ == "__main__":
    print("=== 1. Инкапсуляция ===")
    demo_persons()

    print("=== 2. Наследование ===")
    demo_animals()

    print("=== 3. Полиморфизм ===")
    demo_vehicles()

    print("=== 4. Абстракция ===")
    demo_shapes()


