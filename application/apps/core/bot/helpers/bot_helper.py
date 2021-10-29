from aiogram.types import ReplyKeyboardMarkup

from ..constants import (
    user_status_to_button_labels_for_menu_keyboard,
)


def get_keyboard(user_status,
                 b_labels=user_status_to_button_labels_for_menu_keyboard,
                 buttons=None) -> ReplyKeyboardMarkup:

    buttons = buttons or []
    labels = b_labels[user_status]

    keyboard = ReplyKeyboardMarkup(one_time_keyboard=True, row_width=2)
    keyboard.add(*labels)

    return keyboard


# def get_inline_keyboard(buttons_labels=buttons_labels_for_assements_keyboard,
#                         buttons=None):

#     buttons = buttons or []
#     keyboard = types.InlineKeyboardMarkup()

#     buttons = [types.InlineKeyboardButton(text=btn_label, callback_data=btn_c_data)
#                for btn_label, btn_c_data in buttons_labels.items()]

#     keyboard.add(*buttons)

#     return keyboard
