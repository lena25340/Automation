from smartphone1 import Smartphone

catalog = [Smartphone("Apple", "14 pro", "+79501357194"),
           Smartphone("Xiaomi", "Xiaomi12", "+79546284751"),
           Smartphone("TECNO", "SPARK GO", "+79942458648"),
           Smartphone("Samsung", "Galaxxy S23", "+79564587327"),
           Smartphone("POCO", "M6", "+79804582657")]

for i in catalog:
    i.brandmodelnumber()