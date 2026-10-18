import streamlit as st

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
        'компоты': ['Абрикосовый компот(комплекс)', 'Ягодный компот', 'Облепиховый морс без сахара']
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
        'компоты': ['Клубничный компот (комплекс)', 'Персиковый компот', 'Вишневый компот']
    },
    'суббота': {
        'салаты': ['Овощной салат Кубанский (комплекс)', 'Крабовый салат', 'Салат с моцареллой и помидорами'],
        'супы': ['Куриный суп-лапша (комплекс)', 'Солянка', 'Гороховый суп'],
        'вторые': ['Биточки рыбные с булгуром (комплекс)', 'Плов', 'Фунчоза со свининой'],
        'компоты': ['Ягодный компот (комплекс)', 'Компот из сухофруктов', 'Апельсиновый сок']
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


# Фильтрация блюд по лактозе
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


# Интерфейс страницы
st.set_page_config(page_title="Столовая НИУ ВШЭ", page_icon="🍽️")

st.title("🍽️ Добро пожаловать в столовую НИУ ВШЭ!")
st.write("Сегодня у нас работает система комплексных обедов.")

# Блок с ценами
st.subheader("📋 Прайс-лист")
col1, col2 = st.columns(2)
with col1:
    st.markdown("**Комплексные обеды:**")
    st.write(f"• Полный комплекс (4 блюда) — **{COMPLEX_FULL_PRICE} руб.**")
    st.write(f"• Частичный комплекс (3 блюда) — **{COMPLEX_PARTIAL_PRICE} руб.**")
with col2:
    st.markdown("**Блюда не из комплекса:**")
    st.write(f"• Салаты — **{PRICES['салаты']} руб.**")
    st.write(f"• Супы — **{PRICES['супы']} руб.**")
    st.write(f"• Вторые блюда — **{PRICES['вторые']} руб.**")
    st.write(f"• Компоты — **{PRICES['компоты']} руб.**")

st.divider()

# Выбор дня недели и лактозы
day = st.selectbox(
    "Выберите день недели:",
    options=list(menu.keys()),
    format_func=lambda x: x.capitalize()
)

has_lactose_intolerance = st.radio(
    "Есть ли у вас непереносимость лактозы? (Лактоза содержится в молочных продуктах)",
    options=[False, True],
    format_func=lambda x: "2 - Да, есть непереносимость (исключить молочное)" if x else "1 - Нет, нет непереносимости"
)

st.divider()
st.subheader(f"🍴 Меню на {day}")
st.caption("Блюда с пометкой '(комплекс)' входят в комплексный обед.")

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
        st.warning(f"В категории «{category}» нет доступных блюд без лактозы.")
        selected_dishes[category] = ""
    else:
        # Формируем красивый список для выбора с ценами
        display_options = []
        for dish in available_dishes:
            if "(комплекс)" in dish:
                display_options.append(dish)
            else:
                display_options.append(f"{dish} ({PRICES[category]} руб.)")

        chosen_index = st.selectbox(
            f"Выберите ({category}):",
            options=range(len(available_dishes)),
            format_func=lambda i, opts=display_options: f"{i + 1} - {opts[i]}",
            key=f"{day}_{category}"
        )
        selected_dishes[category] = available_dishes[chosen_index]

# Расчет стоимости
st.divider()
st.subheader("🧾 РАСЧЕТ СТОИМОСТИ")
st.markdown("**Ваш заказ:**")

complex_count = 0
selected_count = 0

for category, dish in selected_dishes.items():
    if dish:
        selected_count += 1
        if "(комплекс)" in dish:
            complex_count += 1
            st.write(f"• {dish}")
        else:
            st.write(f"• {dish} ({PRICES[category]} руб.)")

total_price = 0

if complex_count == 4:
    st.success(f"Вы собрали полный комплексный обед! Стоимость: **{COMPLEX_FULL_PRICE} руб.**")
    total_price = COMPLEX_FULL_PRICE
elif complex_count == 3:
    st.info("Вы собрали частичный комплексный обед!")
    total_price = COMPLEX_PARTIAL_PRICE
    for category, dish in selected_dishes.items():
        if dish and "(комплекс)" not in dish:
            extra_price = PRICES[category]
            st.write(f"*Дополнительно вне комплекса:* {dish} — {extra_price} руб.")
            total_price += extra_price
    st.success(f"Итоговая стоимость: **{total_price} руб.**")
else:
    st.warning("Расчет по отдельности (в комплексе меньше 3 блюд):")
    for category, dish in selected_dishes.items():
        if dish:
            price = PRICES[category]
            total_price += price
    st.success(f"Итого к оплате: **{total_price} руб.**")

# Оплата
st.divider()
st.subheader("💳 ОПЛАТА")
st.write(f"К оплате: **{total_price} руб.**")

payment_method = st.radio(
    "Выберите способ оплаты:",
    ["1 - Наличными", "2 - Картой", "3 - QR-код"]
)

if st.button("✅ Оплатить заказ"):
    if "1" in payment_method:
        st.success("Оплата наличными принята.")
    elif "2" in payment_method:
        st.success("Оплата картой принята.")
    else:
        st.success("Оплата по QR-коду принята.")

    st.write("**Спасибо за покупку! Приятного аппетита!**")
    st.balloons()

    # Сохранение чека в файл и кнопка для скачивания на устройство пользователя
    receipt_text = f"Итог: {total_price} руб."
    with open("сумма.txt", 'w', encoding='utf-8') as f:
        f.write(receipt_text)

    st.download_button(
        label="📥 Скачать сохраненный чек (сумма.txt)",
        data=receipt_text,
        file_name="сумма.txt",
        mime="text/plain"
    )
