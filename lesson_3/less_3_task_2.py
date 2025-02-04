from smartphone import Smartphone

catalog_1 = Smartphone("Nokia", "3310", "+79261234567")
catalog_2 = Smartphone("Samsung", "A10", "+79101234567")
catalog_3 = Smartphone("iPhone", "10Pro", "+79161234567")
catalog_4 = Smartphone("HTC", "3589", "+79269638521")
catalog_5 = Smartphone("Honor", "S25", "+79177895864")

catalog = [catalog_1, catalog_2, catalog_3, catalog_4, catalog_5]

for i in range (0, len(catalog)):
    catalog[i].phonePrint()