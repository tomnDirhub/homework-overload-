class House:
    def __init__(self, name, qt_of_floors):
        self.name = name
        self.qt_of_floors = qt_of_floors

    def go_to(self, new_floor):
        if new_floor > self.qt_of_floors or new_floor < 1:
            print("Введенного этажа не существует")
        else:
            print("Этажи, пройденные вами:")
            for i in range(1, new_floor + 1):
                print(i)

    def __len__(self):
        return self.qt_of_floors

    def __str__(self):
        return f"Название: \"{self.name}\", количество этажей: {self.qt_of_floors}"

    def __lt__(self, other):
        return self.qt_of_floors < other.qt_of_floors

    def __gt__(self, other):
        return self.qt_of_floors > other.qt_of_floors

    def __eq__(self, other):
        return self.qt_of_floors == other.qt_of_floors

    def __le__(self, other):
        return self.qt_of_floors <= other.qt_of_floors

    def __ge__(self, other):
        return self.qt_of_floors >= other.qt_of_floors

    def __ne__(self, other):
        return self.qt_of_floors != other.qt_of_floors

    def __add__(self, value):
        self.qt_of_floors += value
        return self

    def __iadd__(self, value):
        self.qt_of_floors += value
        return self

    def __radd__(self, value):
        self.qt_of_floors += value
        return self

libr = House("Библиотека", 13)
coll = House("Колледж", 3)

print(libr)
print(libr + 2)
print(libr.qt_of_floors)

print(libr < coll)
print(libr == coll)
print(libr > coll)



coll += 12
print(coll.qt_of_floors)

print(libr.qt_of_floors)
print(libr <= coll)
print(libr == coll)
print(libr >= coll)