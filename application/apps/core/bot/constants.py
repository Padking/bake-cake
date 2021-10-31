import aiogram.utils.markdown as fmt


permanent_button_labels = [
    "Собрать торт",
    "Заказать торт",
]

user_status_to_button_labels_for_menu_keyboard = {
    "anonymous": ["Регистрация"],
    "registered": permanent_button_labels,
    "shopper": [*permanent_button_labels, "История заказов"],
}

scenario_step_to_labels_callback_data = {
    "Регистрация": {
        "Согласен": "Согласен",
        "Не согласен": "Не согласен"
    },
    "Собрать торт": {},
    "Выбор формы": {},
    "Выбор топпинга": {},
    "Выбор ягод": {
        "Без ягод": "Без ягод",
    },
    "Выбор декора": {
        "Без декора": "Без декора",
    },
    "Выбор надписи": {
        "С надписью": "С надписью",
        "Без надписи": "Без надписи",
    },
    "Оставить комментарий": {
        "С комментарием": "С комментарием",
        "Без комментария": "Без комментария",
    },
    "Оставить адрес доставки": {
        "С адресом": "С адресом",  # FIXME
        "Без адреса": "Без адреса",  # FIXME
    },
}

scenario_code_to_scenario_name = {
    "1": "Старт",
    "2": "Регистрация",
    "3": "Собрать торт",
    "4": "Заказать торт",
    "5": "История заказов",
}

layer_template = "{} (+{} ₽)"

# msg_to_add_stuffs_photo = fmt.text(
#     fmt.text('Добавьте фото вещи, нажав на значок 📎,'),
#     fmt.text('без добавления подписи к нему;'),
#     sep='\n'
# )

# commands_available_list = fmt.text(
#     fmt.text(fmt.hbold('Список доступных команд:')),
#     fmt.text(f'• Главное меню (/{constants.BOTS_MENU_CMD})'),
#     fmt.text(f'• Действия с ботом (/{constants.BOTS_START_CMD})'),
#     fmt.text(f'• Добавить вещь (/{constants.BOTS_ADD_STUFF_CMD})'),
#     fmt.text('• Найти вещь ()'),
#     fmt.text('• Обменять вещь ()'),
#     sep='\n'
# )

state_code_to_text_message = {
    "1": "Привет! Я помогу тебе заказать торт на любой вкус.",
    "2": 'Для начала ознакомьтесь с согласием на обработку '
         'персональных данных.\nБез вашего согласия мы не сможем '
         'принять ваш заказ.',
    "3": 'Для дальнейшей работы с ботом нужно указать свой номер телефона.\n'
         'введите его в строку ввода.',
    "4": 'Введите адрес доставки в формате: \n'
         'название улицы,номер дома,номер квартиры'
         'например: Садовая, 7, 23',

    "5": 'Регистрация завершена.\nМожете перейти к заказу торта.',

    "6": 'Выберите количество уровней',
    # "7": 'Количество уровней: {}',
    "7": 'Выберите одну из форм торта',
    "8": 'Выберите один из представленных видов топинга',
    "9": 'Добавьте ягоды по желанию',
    "10": 'Добавьте декор по желанию',
    "11": 'Добавьте надпись к торту по желанию (+ 500).\n'
          'Мы можем разместить на торте любую надпись, '
          'например: «С днем рождения!»\nОтправьте боту желаемую фразу в виде '
          'сообщения или нажмите на кнопку «Без надписи»',
    "12": 'Отправьте следующим сообщением текст надписи',
    "13": 'Добавьте комментарий к заказу.',
    "14": "Хорошо, сделаем такую надпись",
    "15": 'Отправьте следующим сообщением текст комментария',
    "16": 'Так и запишем:)',
}
