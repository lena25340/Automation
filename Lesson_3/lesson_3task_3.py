from address import Address
from mailing1 import mailing

to_address = Address("241020", "г. Брянск", "ул. Красных Партизан ", "27", "28")
from_address = Address("398006", "г. Липецк", "ул. 3-е Сентября ", "6", "24")
Mailing = mailing(to_address, from_address, "5561", "1748556899")

print(
    f'Отправление{Mailing.track}из{Mailing.from_address.index}',
    f'{Mailing.from_address.city},{Mailing.from_address.street}',
    f'{Mailing.from_address.house}-{Mailing.from_address.apartment}',
    f'в{Mailing.to_address.index},{Mailing.to_address.city}',
    f'{Mailing.to_address.street},{Mailing.to_address.house}-{Mailing.to_address.apartment}',
    f'Стоимость{Mailing.cost}рублей'
)
