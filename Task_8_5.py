class StorageError(Exception):
    def __init__(self, text):
        self.text = text

    def __str__(self):
        return self.text


class AddStorageError(StorageError):
    def __init__(self, text):
        self.text = f"Unable to add item to stock: \n {text}"


class TransferStorageError(StorageError):
    def __init__(self, text):
        self.text = f"Transfer of equipment is not possible: \n {text}"


class Storage:
    def __init__(self):
        self.__storage = []

    def add(self, item: "OfficeEquipment"):
        if not isinstance(item, OfficeEquipment):
            raise AddStorageError(f"{item} not item")

        self.__storage.append(item)

    def transfer(self, idx: int, department: str):
        if not isinstance(idx, int):
            raise TransferStorageError(f"Incorrect type '{type(item)}'")

        item: OfficeEquipment = self.__storage[idx]

        if item.department:
            raise TransferStorageError(f"The equipment {item} is already assigned to the department {item.department}")

        item.department = department

    def filter_by(self, **kwargs):
        for idx, item in enumerate(self):
            a: OfficeEquipment = item
            if all([a.__getattribute__(key) == kwargs[key] for key in kwargs]):
                yield idx, item

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
        return f"In stock {len(self.__storage)} devices"


class OfficeEquipment:
    def __init__(
            self,
            eq_type: str,
            vendor: str,
            model: str,
    ):
        self.type = eq_type
        self.vendor = vendor
        self.model = model

        self.department = None

    def __getattribute__(self, name):
        return object.__getattribute__(self, name)

    def __str__(self):
        return f"{self.type} {self.vendor} {self.model}"


class Printer(OfficeEquipment):
    def __init__(self, *args):
        super().__init__('printer', *args)


class Scanner(OfficeEquipment):
    def __init__(self, *args):
        super().__init__('scanner', *args)


class Xerox(OfficeEquipment):
    def __init__(self, *args):
        super().__init__('samsung', *args)


if __name__ == '__main__':
    storage = Storage()
    storage.add(Printer("Samsung", "MF-4070D"))
    storage.add(Scanner("Xerox", "FD2030"))
    storage.add(Xerox("Cannon", "G123"))
    print(storage)

    last_idx = None
    for idx, itm in storage.filter_by(department=None):
        print(idx, itm)
        last_idx = idx

    print("Transfer one device")
    storage.transfer(last_idx, 'IT department')

    for idx, itm in storage.filter_by(department=None):
        print(idx, itm)

    print(storage)
    print("Delete one device")
    del storage[last_idx]
    print(storage)