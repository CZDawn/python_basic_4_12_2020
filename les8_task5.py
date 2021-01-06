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

    @staticmethod
    def get_item(product: dict):
        pass

    @staticmethod
    def issue_item(product: dict):
        pass

class OfficeEquipment:
    def __init__(self, product: dict):
        self.__product = product

    @staticmethod
    def get_equipment():
        equipments = {
                'Printers': {'quantity': 0, 'items': []},
                'Scaners': {'quantity': 0, 'items': []},
                'Copiers': {'quantity': 0, 'items': []}
        }
        total_equipments = 0
        while True:
            equipment_type = input('Enter a type of office equipment (printer, scaner, copier):\n>>>')
            equipment_type = equipment_type.lower()
            get_equipment = {}
            if equipment_type == 'printer':
                get_equipment = Printer.get_printer(equipment_type)
                equipments['Printers']['quantity'] += 1
                equipments['Printers']['items'].append(get_equipment)
            elif equipment_type == 'scaner':
                get_equipment = Scaner.get_scaner(equipment_type)
                equipments['Scaners']['quantity'] += 1
                equipments['Scaners']['items'].append(get_equipment)
            elif equipment_type == 'copier':
                get_equipment = Copier.get_copier(equipment_type)
                equipments['Copier']['quantity'] += 1
                equipments['Copier']['quantity'].append(get_equipment)
            user_answer = input('Do you want to continue? Yes or No:\n>>>')
            user_answer = user_answer.lower()
            if user_answer == 'yes':
                total_equipments += 1
                continue
            else:
                print(f'You have added {total_equipments} office equipments on warehouse.')
                break
        return equipments


class Printer(OfficeEquipment):
    def __init__(self, brand: str, model: str, color: bool):
        self.brand = brand
        self.model = model
        self.color = color

    @staticmethod
    def get_printer(equipment):
        brand = input(f'Enter a brand of {equipment}:\n>>>')
        model = input(f'Enter a model of {equipment}:\n>>>')
        color = input(f'Enter a color mode of {equipment} (color - "Yes", black - "No"):\n>>>')
        color = color.lower()
        if color == 'yes':
            color = True
        elif color == 'no':
            color = False
        printer = {'type': equipment, 'brand': brand, 'model': model, 'color': color}
        return printer


class Scaner(OfficeEquipment):
    def __init__(self, brand: str, model: str, fax_mode: bool):
        self.brand = brand
        self.model = model
        self.fax_mode = fax_mode

    @staticmethod
    def get_scaner(equipment):
        brand = input(f'Enter a brand of {equipment}:\n>>>')
        model = input(f'Enter a model of {equipment}:\n>>>')
        fax_mode = input(f'Does it has fax mode? Enter Yes or No:\n>>>')
        fax_mode = fax_mode.lower()
        if fax_mode == 'yes':
            fax_mode = True
        elif fax_mode == 'no':
            fax_mode = False
        scaner = {'type': equipment, 'brand': brand, 'model': model, 'fax_mode': fax_mode}
        return scaner

class Copier(OfficeEquipment):
    def __init__(self, brand: str, model: str, color: bool):
        self.brand = brand
        self.model = model
        self.color = color

    @staticmethod
    def get_copier(equipment):
        brand = input(f'Enter a brand of {equipment}:\n>>>')
        model = input(f'Enter a model of {equipment}:\n>>>')
        color = input(f'Enter a color mode of {equipment} (color - "Yes", black - "No"):\n>>>')
        color = color.lower()
        if color == 'yes':
            color = True
        elif color == 'no':
            color = False
        copier = {'type': equipment, 'brand': brand, 'model': model, 'color': color}
        return copier

office_equipment = OfficeEquipment.get_equipment()
print(office_equipment)

