from main import Pair, make_Pair

pair = make_Pair(10.5, 3)
if pair:
    pair.display()  # Выводит: Цена: 10.5, Количество: 3
    print("Стоимость:", pair.cost())  # Выводит: Стоимость: 31.5

pair2 = Pair.read()
pair2.display()  # Выводит значения, введенные с клавиатуры
print("Стоимость:", pair2.cost())  # Выводит вычисленную стоимость
