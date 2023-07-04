# Задание 2. Список объектов

# 1. Создайте файл `smartphone.py`.
# 2. В файле объявите класс `Smartphone`.
# 3. Объявите в классе конструктор.

# Конструктор должен принимать на вход следующие параметры:
# - марка телефона,
# - модель телефона,
# - абонентский номер (”+79…”).

# 1. Создайте файл `lesson_3_task_2.py`.
# 2. В файле объявите переменную `catalog`.
# 3. Переменная хранит в себе список (`[]`).
# 4. Наполните список пятью разными экземплярами класса `Smartphone`.
# 5. Напишите цикл, который печатает весь каталог (список) в формате `<марка> - <модель>. <номер телефона>`.


from smartphone import Smartphone


catalog_1 = Smartphone('nokia', '3310', '+79161234567')
catalog_2 = Smartphone('samsung', 'galaxy', '+79261234568')
catalog_3 = Smartphone('iphone', '10', '+79991234568')
catalog_4 = Smartphone('htc', 'vive', '+79554568489')
catalog_5 = Smartphone('honor', 'x5', '+79012023030')

catalog = [catalog_1, catalog_2, catalog_3, catalog_4, catalog_5]

for i in range(0, 5):
    print(catalog[i])