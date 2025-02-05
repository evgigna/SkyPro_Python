from address import Address
from mailing import Mailing

# Создаем адреса
to_address = Address("123456", "Москва", "Ленина", "10", "5")
from_address = Address("654321", "Санкт-Петербург", "Пушкина", "15", "12")

# Создаем отправление
mailing = Mailing(to_address, from_address, 250, "TRK123456")

# Печатаем информацию об отправлении
print(mailing)
