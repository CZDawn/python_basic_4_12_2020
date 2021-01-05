'''

5. Продолжить работу над четвертым заданием.
Разработать методы, отвечающие за приём оргтехники на склад и
передачу в определенное подразделение компании.
Для хранения данных о наименовании и количестве единиц оргтехники,
а также других данных, можно использовать любую подходящую структуру,
например словарь.

'''

class Warehouse:
    def __init__(self, name: str, volume: int, adress: str, products_types: list):
        self.__name = name
        self.__volume = volume
        self.__adress = adress
        self.products = products_types

class OfficeEquipment:
    def __init__(self, product: dict):
        self.__product = product

    @staticmethod
    def get_equipment(product):
        self.product = product


class Printer(OfficeEquipment):
    def __init__(self, brand: str, model: str, color: bool):
        self.brand = brand
        self.model = model
        self.color = color

    @staticmethod
    def get_printer(equipment_type):
        self.equipment = equipment_type
        brand = input(f'Enter a brand of {self.equipment}:\n>>>')
        model = input(f'Enter a model of {self.equipment}:\n>>>')
        color = input(f'Enter a color mode of {self.equipment} (color - "Yes", black - "No"):\n>>>')
        color = color.lower()
        if color == 'yes':
            color = True
        elif color == 'no':
            color = False
        printer = {'type': self.equipment, 'brand': brand, 'model': model, 'color': color}
        return printer


class Scaner(OfficeEquipment):
    def __init__(self, brand: str, model: str, fax_mode: bool):
        self.brand = brand
        self.model = model
        self.fax_mode = fax_mode

    @staticmethod
    def get_scaner(equipment_type):
        self.equipment = equipment_type
        brand = input(f'Enter a brand of {self.equipment}:\n>>>')
        model = input(f'Enter a model of {self.equipment}:\n>>>')
        fax_mode = input(f'Does it has fax mode? Enter Yes or No:\n>>>')
        fax_mode = fax_mode.lower()
        if fax_mode == 'yes':
            fax_mode = True
        elif fax_mode == 'no':
            fax_mode = False
        scaner = {'type': self.equipment, 'brand': brand, 'model': model, 'fax_mode': fax_mode}
        return scaner

class Copier(OfficeEquipment):
    def __init__(self, brand: str, model: str, color: bool):
        self.brand = brand
        self.model = model
        self.color = color

    @staticmethod
    def get_copier(equipment_type):
        self.equipment = equipment_type
        brand = input(f'Enter a brand of {self.equipment}:\n>>>')
        model = input(f'Enter a model of {self.equipment}:\n>>>')
        color = input(f'Enter a color mode of {self.equipment} (color - "Yes", black - "No"):\n>>>')
        color = color.lower()
        if color == 'yes':
            color = True
        elif color == 'no':
            color = False
        copier = {'type': self.equipment, 'brand': brand, 'model': model, 'color': color}
        return copier

equipment_type = input('Enter a type of office equipment (printer, scaner, copier):\n>>>')
equipment_type = equipment_type.lower()

def get_equipment(equipment_type):
    equipments = {
            'Printers': {'quantity': 0, 'items': []},
            'Scaners': {'quantity': 0, 'items': []},
            'Copiers': {'quantity': 0, 'items': []}
    }
    get_equipment = {}
    if equipment_type == 'printer':
        get_equipment = Printer.get_printer(equipment_type)
    elif equipment_type == 'scaner':
        get_equipment = Scaner.get_scaner(equipment_type)
    elif equipment_type == 'copier':
        get_equipment = Copier.get_copier(equipment_type)



