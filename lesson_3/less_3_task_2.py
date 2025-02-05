from smartphone import Smartphone

catalog = [
    Smartphone("Nokia", "3310", "+79261234567"),
    Smartphone("Samsung", "A10", "+79101234567"),
    Smartphone("iPhone", "10Pro", "+79161234567"),
    Smartphone("HTC", "3589", "+79269638521"),
    Smartphone("Honor", "S25", "+79177895864")
    ]

for phone in catalog:
    phone.phone_Print()