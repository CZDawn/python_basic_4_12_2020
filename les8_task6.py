'''

6. Продолжить работу над пятым заданием.
Реализуйте механизм валидации вводимых пользователем данных.
Например, для указания количества принтеров, отправленных на склад,
нельзя использовать строковый тип данных.

'''

class Warehouse:
    def __init__(self, name: str, volume: int,
                 adress: str, products_types: list):
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
    def get_equipment(equipments: dict):
        total_equipments = 0
        while True:
            equipment_type = input(
                'Enter a type of office equipment'
                '(printer, scaner, copier):\n>>>'
            )
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
                equipments['Copiers']['quantity'] += 1
                equipments['Copiers']['items'].append(get_equipment)
            total_equipments += 1
            user_answer = input('Do you want to continue? Yes or No:\n>>>')
            user_answer = user_answer.lower()
            if user_answer == 'yes':
                continue
            else:
                print(
                    f'You have added {total_equipments}'
                    f'office equipments on warehouse.'
                )
                break
        return equipments

    @staticmethod
    def issue_equipment(equipments: dict):
        equipment_type =  input(
            'Enter a type of equipment which you want to issue:\n>>>'
        )
        equipment_brand = input(
            'Enter a brand of equipment which you want to issue:\n>>>'
        )
        equipment_model = input(
            'Enter a model of equipment which you want to issue:\n>>>'
        )

        equipment_mode_title = ''
        if equipment_type == 'printer' or equipment_type == 'copier':
            equipment_mode_title = 'color'
        elif equipment_type == 'scaner':
            equipment_mode_title = 'fax_mode'

        equipment_mode = input(
            f'Enter a color or fax mode of {equipment_type}'
            f'(color or fax - "Yes", black or no fax - "No"):\n>>>'
        )
        equipment_mode = equipment_mode.lower()
        if equipment_mode == 'yes':
            equipment_mode = True
        elif equipment_mode == 'no':
            equipment_mode = False

        recipient = input('Enter a recipient of equipment:\n>>>')
        # forms caracters to find the product wich send to recepient
        itm_caracters = {
            'type': equipment_type,
            'brand': equipment_brand,
            'model': equipment_model,
            equipment_mode_title: equipment_mode
        }
        equip_key = equipment_type.capitalize() + 's'
        equipments[equip_key]['quantity'] -= 1
        item_pos_index = equipments[equip_key]['items'].index(itm_caracters)
        item_for_send = equipments[equip_key]['items'].pop(item_pos_index)
        send_dict = {recipient: item_for_send}
        return send_dict


class Printer(OfficeEquipment):
    def __init__(self, brand: str, model: str, color: bool):
        self.brand = brand
        self.model = model
        self.color = color

    @staticmethod
    def get_printer(equipment):
        brand = input(f'Enter a brand of {equipment}:\n>>>')
        model = input(f'Enter a model of {equipment}:\n>>>')
        color = input(
            f'Enter a color mode of {equipment}'
            f'(color - "Yes", black - "No"):\n>>>'
        )
        color = color.lower()
        if color == 'yes':
            color = True
        elif color == 'no':
            color = False
        printer = {
            'type': equipment,
            'brand': brand,
            'model': model,
            'color': color
        }
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
        scaner = {
            'type': equipment,
            'brand': brand,
            'model': model,
            'fax_mode': fax_mode
        }
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
        color = input(
            f'Enter a color mode of {equipment}'
            f'(color - "Yes", black - "No"):\n>>>'
        )
        color = color.lower()
        if color == 'yes':
            color = True
        elif color == 'no':
            color = False
        copier = {
            'type': equipment,
            'brand': brand,
            'model': model,
            'color': color
        }
        return copier

office_equipments = {
    'Printers': {'quantity': 0, 'items': []},
    'Scaners': {'quantity': 0, 'items': []},
    'Copiers': {'quantity': 0, 'items': []}
}
office_equipment_add = OfficeEquipment.get_equipment(office_equipments)
print(office_equipments)
office_equipment_issue = OfficeEquipment.issue_equipment(office_equipments)
print(office_equipment_issue)
print(office_equipments)

