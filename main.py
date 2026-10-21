menu = {
    'понедельник': {
        'салаты': ['Оливье (комплекс)', 'Греческий салат', 'Цезарь'],
        'супы': ['Борщ (комплекс)', 'Суп-лапша', 'Солянка'],
        'вторые': ['Курица-терияки с рисом (комплекс)', 'Плов', 'Горбуша с вареным картофелем'],
        'компоты': ['Яблочный компот (комплекс)', 'Вишневый компот', 'Компот из сухофруктов без сахара']
    },
    'вторник': {
        'салаты': ['Винегрет (комплекс)', 'Морковный салат', 'Свекольный салат'],
        'супы': ['Щи (комплекс)', 'Гороховый суп', 'Куриный суп'],
        'вторые': ['Гречка с гуляшом (комплекс)', 'Картофельное пюре с котлетой "Домашней"', 'Макароны по-флотски'],
        'компоты': ['Грушевый компот (комплекс)', 'Смородиновый компот', 'Напиток Каркаде без сахара']
    },
    'среда': {
        'салаты': ['Сельдь под шубой (комплекс)', 'Салат с фасолью', 'Крабовый салат'],
        'супы': ['Уха (комплекс)', 'Тыквенный крем-суп', 'Харчо'],
        'вторые': ['Тефтели с макаронами (комплекс)', 'Котлета с гречкой по-купечески', 'Удон с курицей'],
        'компоты': ['Абрикосовый компот (комплекс)', 'Ягодный компот', 'Облепиховый компот без сахара']
    },
    'четверг': {
        'салаты': ['Салат Охотничий (комплекс)', 'Салат с тунцом', 'Цезарь'],
        'супы': ['Рассольник (комплекс)', 'Сырный крем-суп', 'Куриный бульон'],
        'вторые': ['Рыбная котлета с рисом (комплекс)', 'Жаркое по-домашнему', 'Паста Карбонара'],
        'компоты': ['Клюквенный морс (комплекс)', 'Яблочный компот', 'Компот из шиповника без сахара']
    },
    'пятница': {
        'салаты': ['Витаминный салат (комплекс)', 'Салат Коул-Слоу', 'Греческий салат'],
        'супы': ['Грибной суп (комплекс)', 'Борщ', 'Томатный суп'],
        'вторые': ['Гуляш с пюре (комплекс)', 'Куриная грудка с овощами', 'Лазанья'],
        'компоты': ['Клубничный компот (комплекс)', 'Персиковый компот', 'Вишневый компот']
    },
    'суббота': {
        'салаты': ['Овощной салат Кубанский (комплекс)', 'Крабовый салат', 'Салат с моцареллой и помидорами'],
        'супы': ['Куриный суп-лапша (комплекс)', 'Солянка', 'Гороховый суп'],
        'вторые': ['Биточки рыбные с булгуром (комплекс)', 'Плов', 'Фунчоза со свининой'],
        'компоты': ['Ягодный компот (комплекс)', 'Компот из сухофруктов без сахара', 'Апельсиновый сок']
    }
}

LACTOSE_DISHES = [
    'Оливье', 'Цезарь', 'Салат Коул-Соул', 
    'Салат с моцареллой и помидорами', 'Солянка', 'Борщ', 'Щи',
    'Картофельное пюре', 'Тыквенный крем-суп', 'Лазанья',
    'Сырный крем-суп', 'Паста Карбонара', 'Гуляш с пюре'
]

PRICES = {
    'салаты': 120,
    'супы': 100,
    'вторые': 200,
    'компоты': 50
}

COMPLEX_FULL_PRICE = 350
COMPLEX_PARTIAL_PRICE = 320


def filter_lactose_dishes(dishes_list, has_intolerance):
    """
    Фильтрует список блюд, исключая те, что содержат лактозу.
    """
    if not has_intolerance:
        return dishes_list

    available_dishes = []

    for dish in dishes_list:
        contains_lactose = False
        for lactose_item in LACTOSE_DISHES:
            if lactose_item in dish:
                contains_lactose = True
                break  

        if not contains_lactose:
            available_dishes.append(dish)

    return available_dishes


print("Добро пожаловать в столовую НИУ ВШЭ!")
print("Сегодня у нас работает система комплексных обедов.")
print()

print("Введите день недели (понедельник, вторник, среда, четверг, пятница, суббота):")
day = ""
while True:
    day_input = input("День: ").strip().lower()

    if day_input in menu:
        day = day_input
        print("Хорошо, смотрим меню на", day)
        break
    else:
        print("Такого дня нет. Введите день с понедельника по субботу.")
print()

print("МЕНЮ НА СЕГОДНЯ")
print("Комплексные обеды:")
print("Полный комплекс (4 блюда) -", COMPLEX_FULL_PRICE, "руб.")
print("Частичный комплекс (3 блюда) -", COMPLEX_PARTIAL_PRICE, "руб.")
print()
print("Цены блюд не из комплекса:")
print("Салаты -", PRICES['салаты'], "руб.")
print("Супы -", PRICES['супы'], "руб.")
print("Вторые блюда -", PRICES['вторые'], "руб.")
print("Компоты -", PRICES['компоты'], "руб.")
print()

print("Есть ли у вас непереносимость лактозы?")
print("Лактоза содержится в молочных продуктах.")
print()
print("1 - Нет, нет непереносимости")
print("2 - Да, есть непереносимость")

has_lactose_intolerance = False
while True:
    choice = input("Ваш ответ: ").strip()

    if choice == '1':
        print("Отлично! Выбираем из всего меню.")
        has_lactose_intolerance = False
        break
    elif choice == '2':
        print("Хорошо, исключим блюда с лактозой.")
        has_lactose_intolerance = True
        break
    else:
        print("Введите 1 или 2.")
print()

print("Теперь выбирайте блюда по категориям.")
print("Блюда с пометкой '(комплекс)' входят в комплексный обед.")
print()

selected_dishes = {
    'салаты': "",
    'супы': "",
    'вторые': "",
    'компоты': ""
}

categories = ['салаты', 'супы', 'вторые', 'компоты']

for category in categories:
    print("Выберите", category + ":")

    dishes = menu[day][category]

    # ИСПОЛЬЗУЕМ ФУНКЦИЮ ДЛЯ ФИЛЬТРАЦИИ БЛЮД
    available_dishes = filter_lactose_dishes(dishes, has_lactose_intolerance)

    current_number = 1
    for dish in available_dishes:
        if "(комплекс)" in dish:
            print(current_number, "-", dish)
        else:
            print(current_number, "-", dish, "(", PRICES[category], "руб.)")

        current_number += 1

    if not available_dishes:
        print("В этой категории нет доступных блюд.")
        selected_dishes[category] = ""
    else:
        while True:
            user_input = input("Номер блюда: ")

            if user_input.isdigit():
                choice = int(user_input)
                if 1 <= choice <= len(available_dishes):
                    selected = available_dishes[choice - 1]
                    selected_dishes[category] = selected
                    print("Выбрано:", selected)
                    break
                else:
                    print("Введите число от 1 до", len(available_dishes))
            else:
                print("Введите число.")
    print()

print("РАСЧЕТ СТОИМОСТИ")
print("Ваш заказ:")

complex_count = 0
selected_count = 0

for category, dish in selected_dishes.items():
    if dish:
        selected_count += 1
        if "(комплекс)" in dish:
            complex_count += 1
            print(dish, "(комплекс)")
        else:
            print(dish, "(", PRICES[category], "руб.)")
print()

if complex_count == 4:
    print("Вы собрали полный комплексный обед!")
    print("Стоимость:", COMPLEX_FULL_PRICE, "руб.")
    total_price = COMPLEX_FULL_PRICE
elif complex_count == 3:
    print("Вы собрали частичный комплексный обед!")
    total_price = COMPLEX_PARTIAL_PRICE
    # Проверяем, было ли выбрано 4-е блюдо не из комплекса
    for category, dish in selected_dishes.items():
        if dish and "(комплекс)" not in dish:
            extra_price = PRICES[category]
            print(f"Дополнительно вне комплекса: {dish} - {extra_price} руб.")
            total_price += extra_price
    print("Итоговая стоимость:", total_price, "руб.")
else:
    # Если в комплексе менее 3 блюд считаем по отдельности
    print("Расчет по отдельности:")
    total_price = 0
    for category, dish in selected_dishes.items():
        if dish:
            price = PRICES[category]
            print(dish, "-", price, "руб.")
            total_price += price

    print("Итого:", total_price, "руб.")
print()

print("ОПЛАТА")
print("К оплате:", total_price, "руб.")
print()
print("Выберите способ оплаты:")
print("1 - Наличными")
print("2 - Картой")
print("3 - QR-код")

while True:
    choice = input("Ваш выбор: ")

    if choice == '1':
        print("Оплата наличными принята.")
        break
    elif choice == '2':
        print("Оплата картой принята.")
        break
    elif choice == '3':
        print("Оплата по QR-коду принята.")
        break
    else:
        print("Введите 1, 2 или 3.")
print()


def save_order(total):
    with open("сумма.txt", 'w', encoding='utf-8') as f:
        f.write(f"Итог: {total} руб.")
    print("Сумма сохранена")


save_order(total_price)

print("Спасибо за покупку!")
print("Приятного аппетита!")
