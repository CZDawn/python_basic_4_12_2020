'''

4. Начните работу над проектом «Склад оргтехники».
Создайте класс, описывающий склад.
А также класс «Оргтехника», который будет базовым для классов-наследников.
Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
В базовом классе определить параметры, общие для приведенных типов.
В классах-наследниках реализовать параметры,
уникальные для каждого типа оргтехники.

'''

class Warehouse:
    def __init__(self, name: str, volume: int, adress: str, products_types: list):
        self.name = name
        self.volume = volume
        self.adress = adress
        self.products = products_types

class OfficeEquipment:
    def __init__(self, type_of_product: str, quantity_of_type: int, provider: str, recipient: str, delivery_date: str, shipment_date: str):
        self.type = type_of_product
        self.quantity = quantity_of_product
        self.provider = provider
        self.recipient = recipient
        self.delivery = delivery_date
        self.shipment = shipment_date

class Printer(OfficeEquipment):
    def __init__(self, brand: str, model: str, produce_year: int, manufacturer: str, color: bool):
        self.brand = brand
        self.model = model
        self.year = produce_year
        self.manufacturer = manufacturer
        self.color = color

class Scaner(OfficeEquipment):
    def __init__(self, brand: str, model: str, produce_year: int, manufacturer: str, fax_mode: bool):
        self.brand = brand
        self.model = model
        self.year = produce_year
        self.manufacturer = manufacturer
        self.fax_mode = fax_mode

class Copier(OfficeEquipment):
    def __init__(self, brand: str, model: str, produce_year: int, manufacturer: str, color: bool):
        self.brand = brand
        self.model = model
        self.year = produce_year
        self.manufacturer = manufacturer
        self.color = color
