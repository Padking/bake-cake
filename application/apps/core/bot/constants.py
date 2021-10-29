import aiogram.utils.markdown as fmt


permanent_button_labels = [
    "Собрать торт",
    "Заказать торт",
]

user_status_to_button_labels_for_menu_keyboard = {
    "anonymous": ["Регистрация", *permanent_button_labels],
    "registered": permanent_button_labels,
    "shopper": [*permanent_button_labels, "История заказов"],
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
    "1": "Написать приветственное сообщение",
}
