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

project_scenario_to_labels_callback_data = {
    "Регистрация": {
        "Согласен": "Согласен",
        "Не согласен": "Не согласен"
    },
}

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
    "4": 'Введите адрес доставки в формате \n'
         'название улицы, номер дома, номер квартиры',
    "5": 'Регистрация завершена.\nМожете перейти к заказу торта.',
}
