from Address import Address
from Mailing import Mailing

to_address = Address ("241020", "г. Брянск", "ул. Красных Партизан ", "27", "28")
from_address = Address ("398006", "г. Липецк", "ул. 3-е Сентября ", "6", "24")
mailing = Mailing(to_address, from_address, "5561", "1748556899")

print(
    f'Отправление {mailing.track} из {mailing.from_address.index}',
    f'{mailing.from_address.city},  { mailing.from_address.street}',
    f'{mailing.from_address.house} - {mailing.from_address.apartment}',
    f'в {mailing.to_address.index}, {mailing.to_address.city}',
    f'{mailing.to_address.street}, {mailing.to_address.house} -{ mailing.to_address.apartment}',
    f'Стоимость {mailing.cost} рублей'
)