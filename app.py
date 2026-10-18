import streamlit as st

menu = {
    'понедельник': {
        'салаты': ['Оливье (комплекс)', 'Греческий салат', 'Цезарь'],
        'супы': ['Борщ (комплекс)', 'Суп-лапша', 'Солянка'],
        'вторые': ['Курица-терияки с рисом (комплекс)', 'Плов', 'Горбуша с вареным картофелем'],
        'компоты': ['Яблочный (комплекс)', 'Вишневый компот', 'Компот из сухофруктов']
    },
    'вторник': {
        'салаты': ['Винегрет (комплекс)', 'Морковный салат', 'Свекольный салат'],
        'супы': ['Щи (комплекс)', 'Гороховый суп', 'Куриный суп'],
        'вторые': ['Гречка с гуляшом (комплекс)', 'Картофельное пюре с котлетой "Домашней"', 'Макароны по-флотски'],
        'компоты': ['Грушевый (комплекс)', 'Смородиновый компот', 'Компот мультифрукт']
    },
    'среда': {
        'салаты': ['Сельдь под шубой (комплекс)', 'Салат с фасолью', 'Крабовый салат'],
        'супы': ['Уха (комплекс)', 'Тыквенный крем-суп', 'Харчо'],
        'вторые': ['Тефтели с макаронами (комплекс)', 'Котлета с гречкой по-купечески', 'Удон с курицей'],
        'компоты': ['Абрикосовый (комплекс)', 'Ягодный компот', 'Облепиховый компот']
    },
    'четверг': {
        'салаты': ['Салат Охотничий (комплекс)', 'Салат с тунцом', 'Цезарь'],
        'супы': ['Рассольник (комплекс)', 'Сырный крем-суп', 'Куриный бульон'],
        'вторые': ['Рыбная котлета с рисом (комплекс)', 'Жаркое по-домашнему', 'Паста Карбонара'],
        'компоты': ['Клюквенный морс (комплекс)', 'Яблочный компот', 'Компот из шиповника']
    },
    'пятница': {
        'салаты': ['Витаминный салат (комплекс)', 'Салат Коул-Слоу', 'Греческий салат'],
        'супы': ['Грибной суп (комплекс)', 'Борщ', 'Томатный суп'],
        'вторые': ['Гуляш с пюре (комплекс)', 'Куриная грудка с овощами', 'Лазанья'],
        'компоты': ['Клубничный (комплекс)', 'Персиковый компот', 'Вишневый компот']
    },
    'суббота': {
        'салаты': ['Овощной салат Кубанский (комплекс)', 'Крабовый салат', 'Салат с моцареллой и помидорами'],
        'супы': ['Куриный суп-лапша (комплекс)', 'Солянка', 'Гороховый суп'],
        'вторые': ['Биточки рыбные с булгуром (комплекс)', 'Плов', 'Фунчоза со свининой'],
        'компоты': ['Ягодный (комплекс)', 'Компот из сухофруктов', 'Апельсиновый напиток']
    }
}

LACTOSE_DISHES = [
    'Оливье', 'Цезарь', 'Солянка', 'Борщ', 'Щи',
    'Картофельное пюре', 'Тыквенный крем-суп', 'Лазанья',
    'Сырный крем-суп', 'Паста Карбонара', 'Гуляш с пюре',
    'Салат с моцареллой и помидорами'
]

PRICES = {
    'салаты': 120,
    'супы': 100,
    'вторые': 200,
    'компоты': 50
}

COMPLEX_FULL_PRICE = 350
COMPLEX_PARTIAL_PRICE = 320


# ФУНКЦИЯ ДЛЯ ФИЛЬТРАЦИИ БЛЮД ПО ЛАКТОЗЕ
def filter_lactose_dishes(dishes_list, has_intolerance):
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


st.title("Добро пожаловать в столовую НИУ ВШЭ!")
st.write("Сегодня у нас работает система комплексных обедов.")

st.subheader("МЕНЮ НА СЕГОДНЯ")
st.write("Комплексные обеды:")
st.write("Полный комплекс (4 блюда) -", COMPLEX_FULL_PRICE, "руб.")
st.write("Частичный комплекс (3 блюда) -", COMPLEX_PARTIAL_PRICE, "руб.")

st.write("Цены блюд не из комплекса:")
st.write("Салаты -", PRICES['салаты'], "руб.")
st.write("Супы -", PRICES['супы'], "руб.")
st.write("Вторые блюда -", PRICES['вторые'], "руб.")
st.write("Компоты -", PRICES['компоты'], "руб.")

days_list = ['понедельник', 'вторник', 'среда', 'четверг', 'пятница', 'суббота']
day = st.selectbox("Выберите день недели:", days_list)

st.write("Есть ли у вас непереносимость лактозы? (Лактоза содержится в молочных продуктах)")
lactose_choice = st.radio(
    "Ваш ответ:",
    ["1 - Нет, нет непереносимости", "2 - Да, есть непереносимость"]
)

if lactose_choice == "2 - Да, есть непереносимость":
    has_lactose_intolerance = True
else:
    has_lactose_intolerance = False

st.subheader("Выбор блюд по категориям")
st.write("Блюда с пометкой '(комплекс)' входят в комплексный обед.")

selected_dishes = {
    'салаты': "",
    'супы': "",
    'вторые': "",
    'компоты': ""
}

categories = ['салаты', 'супы', 'вторые', 'компоты']

for category in categories:
    dishes = menu[day][category]
    available_dishes = filter_lactose_dishes(dishes, has_lactose_intolerance)

    if not available_dishes:
        st.write("В этой категории нет доступных блюд.")
        selected_dishes[category] = ""
    else:
        selected = st.selectbox("Выберите " + category + ":", available_dishes)
        selected_dishes[category] = selected

st.subheader("РАСЧЕТ СТОИМОСТИ")
st.write("Ваш заказ:")

complex_count = 0
selected_count = 0

for category, dish in selected_dishes.items():
    if dish:
        selected_count += 1
        if "(комплекс)" in dish:
            complex_count += 1
            st.write(dish)
        else:
            st.write(dish, "(", PRICES[category], "руб.)")

if complex_count == 4:
    st.write("Вы собрали полный комплексный обед!")
    total_price = COMPLEX_FULL_PRICE
    st.write("Стоимость:", total_price, "руб.")
elif complex_count == 3:
    st.write("Вы собрали частичный комплексный обед!")
    total_price = COMPLEX_PARTIAL_PRICE
    for category, dish in selected_dishes.items():
        if dish and "(комплекс)" not in dish:
            extra_price = PRICES[category]
            st.write("Дополнительно вне комплекса:", dish, "-", extra_price, "руб.")
            total_price += extra_price
    st.write("Итоговая стоимость:", total_price, "руб.")
else:
    st.write("Расчет по отдельности:")
    total_price = 0
    for category, dish in selected_dishes.items():
        if dish:
            price = PRICES[category]
            st.write(dish, "-", price, "руб.")
            total_price += price
    st.write("Итого:", total_price, "руб.")

st.subheader("ОПЛАТА")
st.write("К оплате:", total_price, "руб.")

payment_choice = st.radio(
    "Выберите способ оплаты:",
    ["1 - Наличными", "2 - Картой", "3 - QR-код"]
)


def save_order(total):
    with open("сумма.txt", 'w', encoding='utf-8') as f:
        f.write(f"Итог: {total} руб.")


if st.button("Оплатить"):
    if payment_choice == "1 - Наличными":
        st.write("Оплата наличными принята.")
    elif payment_choice == "2 - Картой":
        st.write("Оплата картой принята.")
    elif payment_choice == "3 - QR-код":
        st.write("Оплата по QR-коду принята.")

    save_order(total_price)
    st.write("Сумма сохранена в файл сумма.txt")
    st.write("Спасибо за покупку! Приятного аппетита!")
