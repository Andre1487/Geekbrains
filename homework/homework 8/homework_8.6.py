"""Андре Септиянто - Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых пользователем данных.
Например, для указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных."""

class AppError(Exception):
    def __init__(self, text):
        self.text = text

    def __str__(self):
        return self.text


class AcceptStorageError(AppError):
    def __init__(self, text):
        self.text = f"can not add Item in storage:\n {text}"


class TransferStorageError(AppError):
    def __init__(self, text):
        self.text = f"Error transfering equipment:\n {text}"


AddStorageError = AcceptStorageError


class ValidateEquipmentError(AppError):
    pass


class Storage:
    def __init__(self):
        self.__storage = []

    def add(self, equipments):
        if not all([isinstance(equipment, OfficeEquipment) for equipment in equipments]):
            raise AddStorageError(f"you are trуin to add in storage non Office Equipment")

        self.__storage.extend(equipments)

    def transfer(self, idx: int, department: str):
        if not isinstance(idx, int):
            raise TransferStorageError(f"unaccessable type'{type(item)}'")

        item: OfficeEquipment = self.__storage[idx]

        if item.department:
            raise TransferStorageError(f" Equipment {item} already linked with department {item.department}")

        item.department = department

    def filter_by(self, **kwargs):
        for id_, item in enumerate(self):
            if all([item.__getattribute__(key) == kwargs[key] for key in kwargs]):
                yield id_, item

    def __getitem__(self, key):
        if not isinstance(key, int):
            raise TypeError

        return self.__storage[key]

    def __delitem__(self, key):
        if not isinstance(key, int):
            raise TypeError

        del self.__storage[key]

    def __iter__(self):
        return self.__storage.__iter__()

    def __str__(self):
        return f"in the storage now {len(self.__storage)} Equipment"


class OfficeEquipment:
    __required_props = ("eq_type", "vendor", "model")

    def __init__(self, eq_type: str = None, vendor: str = "", model: str = ""):
        self.type = eq_type
        self.vendor = vendor
        self.model = model

        self.department = None

    def __setattr__(self, key, value):
        if key in self.__required_props and not value:
            raise AttributeError(f"'{key}' require to has different value with false")

        object.__setattr__(self, key, value)

    def __str__(self):
        return f"{self.type} {self.vendor} {self.model}"

    @staticmethod
    def validate(cnt):
        if not isinstance(cnt, int):
            ValidateEquipmentError(f"'{type(cnt)}'; ammount of instance has to by type 'int'")

    @classmethod
    def create(cls, cnt, **properties):
        cls.validate(cnt)
        return [cls(**properties) for _ in range(cnt)]


class Printer(OfficeEquipment):
    def __init__(self, **kwargs):
        super().__init__(eq_type='Printer', **kwargs)


class Scanner(OfficeEquipment):
    def __init__(self, **kwargs):
        super().__init__(eq_type='Scanner', **kwargs)


class Xerox(OfficeEquipment):
    def __init__(self, **kwargs):
        super().__init__(eq_type='Photocopier', **kwargs)


if __name__ == '__main__':
    storage = Storage()
    storage.add(Printer.create(4, vendor="HP", model="XP-800"))
    storage.add(Scanner.create(3, vendor="Epson", model="3762-FG"))
    storage.add(Xerox.create(6, vendor="Xerox", model="F123"))
    print(storage)

    for idx, itm in storage.filter_by(department=None, vendor="Epson", model="3762-FG"):
        print(f"Reserved {itm} in 'Storage Department'")
        storage.transfer(idx, 'Storage Department')

    for idx, itm in storage.filter_by(department=None):
        print(idx, f"{itm} can't arrange which Department")

    print(storage)
    print("Deleted 1 equipment")
    del storage[0]
    print(storage)
